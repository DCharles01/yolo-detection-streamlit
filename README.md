# YOLO Object Detection Application

This application utilizes the YOLO (You Only Look Once) object detection model to detect objects in images. The application is built using Streamlit for the frontend and Flask for the backend API. Users can upload images, and the application will return the image with detected objects highlighted.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Without Docker](#without-docker)
  - [With Docker](#with-docker)
- [Usage](#usage)
- [Customization](#customization)
- [Makefile Commands](#makefile-commands)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Upload an image and view the uploaded image in the application.
- Detect objects in the image using the YOLO model.
- Display the processed image with bounding boxes around detected objects.
- Download the processed image.

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Flask
- **Object Detection**: OpenCV with YOLO
- **Containerization**: Docker (optional)

## Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- Docker (optional, if you want to run it in a container)
- Make (optional, if you want to use the Makefile)

## Installation

### Without Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/DCharles01/yolo-detection-streamlit
   cd yolo-detection-streamlit
   ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have the YOLO model files (`yolov3.cfg`, `yolov3.weights`, `yolov3.txt`) in the project directory.

5. Start the Flask API:
   Navigate to the Flask API directory (if applicable) and run:

    ```bash
    python app.py
    ```

6. Start the Streamlit app:
   In a new terminal window, run:

    ```bash
    streamlit run streamlit_app.py
    ```

7. Open your browser and navigate to [http://localhost:8501](http://localhost:8501).

### With Docker

1. Build the Docker image and start the application:

    You can use the provided Makefile for convenience. Run the following command to build and start the application:

    ```bash
    make up-build
    ```

2. Alternatively, if you want to start the application without rebuilding the image, run:

    ```bash
    make up
    ```

3. To stop the application, run:

    ```bash
    make down
    ```

4. Open your browser and navigate to [http://localhost:8501](http://localhost:8501).

## Usage

1. Upload an image by clicking on the "Choose an image..." button.
2. Click on the "Detect Objects" button to start the detection process.
3. The processed image will be displayed with bounding boxes around detected objects.
4. Use the "Download Processed Image" button to save the processed image.

## Customization

You can adjust the confidence threshold and non-maximum suppression threshold in the Streamlit app using sliders. These values are sent to the API with each detection request.

## Makefile Commands

The following commands are available in the provided Makefile:

- **Build and start the application**:

    ```bash
    make up-build
    ```

- **Start the application without rebuilding**:

    ```bash
    make up
    ```

- **Stop the application**:

    ```bash
    make down
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- YOLO (You Only Look Once)
- OpenCV
- Streamlit
- Flask
