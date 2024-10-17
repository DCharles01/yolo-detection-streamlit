from flask import Flask, request, send_file
import cv2
import numpy as np
import io
from PIL import Image

app = Flask(__name__)

# Load YOLO model and classes
yolo_config = 'yolov3.cfg'
yolo_weights = 'yolov3.weights'
yolo_classes = 'yolov3.txt'

net = cv2.dnn.readNet(yolo_weights, yolo_config)

with open(yolo_classes, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

# Function to get the output layer names
def get_output_layers(net):
    layer_names = net.getLayerNames()
    return [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Function to draw bounding box
def draw_bounding_box(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    color = COLORS[class_id]
    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
    cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

@app.route('/detect', methods=['POST'])
def detect_objects():
    if 'image' not in request.files:
        return "No image provided", 400
    
    # Read the image file
    file = request.files['image']
    image_stream = io.BytesIO(file.read())
    image = np.array(Image.open(image_stream))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV

    # Prepare the image for YOLO
    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392
    blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    
    # Run forward pass and get output layers
    outs = net.forward(get_output_layers(net))
    
    # Process detections
    class_ids = []
    confidences = []
    boxes = []
    
    # Get thresholds from the request
    conf_threshold = float(request.form.get('conf_threshold', 0.2))  # Default to 0.2 if not provided
    nms_threshold = float(request.form.get('nms_threshold', 0.4))    # Default to 0.4 if not provided

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            draw_bounding_box(image, class_ids[i], confidences[i], round(x), round(y), round(x + w), round(y + h))

    # Convert image back to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Convert the image back to byte stream for sending as a response
    _, img_encoded = cv2.imencode('.jpg', image_rgb)
    return send_file(io.BytesIO(img_encoded.tobytes()), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
