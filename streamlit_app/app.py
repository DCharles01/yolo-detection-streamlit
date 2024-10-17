import streamlit as st
import requests
from PIL import Image
import io

# Streamlit app layout
st.title("YOLO Object Detection")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Add sliders for Confidence and NMS Thresholds
conf_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.2, 0.01)
nms_threshold = st.slider("NMS Threshold", 0.0, 1.0, 0.4, 0.01)

# If an image is uploaded
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert the image to bytes to send via API
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()
    
    # Call the Flask API when user clicks the "Detect Objects" button
    if st.button("Detect Objects"):
        # Define the API endpoint
        api_url = "http://yolo-api:80/detect"
        
        # Make a POST request to Flask API, including threshold values
        files = {'image': ('image.jpg', img_bytes, 'image/jpeg')}
        data = {'conf_threshold': conf_threshold, 'nms_threshold': nms_threshold}
        
        response = requests.post(api_url, files=files, data=data)
        
        if response.status_code == 200:
            # Convert response content back to image
            img_with_boxes = Image.open(io.BytesIO(response.content))
            
            # Display the output image with bounding boxes
            st.image(img_with_boxes, caption="Processed Image", use_column_width=True)
            
            # Provide a download button
            st.download_button(
                label="Download Processed Image",
                data=response.content,
                file_name="object_detection_output.jpg",
                mime="image/jpeg"
            )
        else:
            st.error("Error: Could not process the image")
