import streamlit as st
from PIL import Image
import yaml
from ultralytics import YOLO
import cv2
import os  # Import the 'os' module
import tempfile

# Set the title of the Streamlit app
st.title("YOLOv8 Object Detection with Streamlit")

# Add a sidebar for user inputs
st.sidebar.header("Configuration")

# Load custom YAML file
@st.cache_data
def load_yaml(file_path):
    """
    Loads a YAML file.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The content of the YAML file as a dictionary.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Path to your custom YAML file
yaml_path = 'yolov8s-swin.yaml'
try:
    yaml_content = load_yaml(yaml_path)
    class_names = yaml_content.get('names', [])
    st.sidebar.success(f"Successfully loaded {len(class_names)} class names from {yaml_path}")
except Exception as e:
    st.sidebar.error(f"Error loading YAML file: {e}")
    class_names = []

# Load the YOLOv8 model
@st.cache_resource
def load_model(model_path):
    """
    Loads the YOLOv8 model from the specified path.

    Args:
        model_path (str): The path to the model weights file.

    Returns:
        YOLO: The loaded YOLOv8 model.
    """
    try:
        model = YOLO(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model_path = 'best.pt'
model = load_model(model_path)

if model:
    st.sidebar.success("YOLOv8 model loaded successfully.")
else:
    st.sidebar.error("Failed to load YOLOv8 model. Please check the model path.")

# Confidence threshold slider
confidence_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.25, 0.05)

# Input type selection
input_type = st.radio("Select Input Type", ('Image', 'Video', 'Live Feed'))

if input_type == 'Image':
    # File uploader for image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open and display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform object detection
        if st.button("Detect Objects"):
            with st.spinner("Processing..."):
                # Perform prediction
                results = model.predict(image, conf=confidence_threshold)
                
                # Draw bounding boxes on the image
                annotated_image = results[0].plot()

                # Display the annotated image
                st.image(annotated_image, caption="Annotated Image", use_column_width=True)

                # Display detected class names
                if len(results[0].boxes) > 0:
                    detected_classes = []
                    for c in results[0].boxes.cls:
                        class_index = int(c)
                        if 0 <= class_index < len(class_names): # Check if the index is valid
                            detected_classes.append(class_names[class_index])
                        else:
                            print(f"Warning: Class index {class_index} is out of range.")
                            # Handle the out-of-range index appropriately, e.g., skip it, assign a default name, etc.
                            detected_classes.append("Unknown") # Example: use "Unknown" for out-of-range indices

                    st.write("Detected Objects:")
                    st.write(list(set(detected_classes)))
                else:
                    st.write("No objects detected.")

elif input_type == 'Video':
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        video_path = tfile.name

        if st.button("Detect Objects in Video"):
            with st.spinner("Processing video..."):
                try:
                    cap = cv2.VideoCapture(video_path)
                    st_frame = st.empty()

                    while cap.isOpened():
                        ret, frame = cap.read()
                        if not ret:
                            break
                        
                        # Perform prediction
                        results = model.predict(frame, conf=confidence_threshold)
                        annotated_frame = results[0].plot()

                        # Display the annotated frame
                        st_frame.image(annotated_frame, channels="BGR", use_column_width=True)

                    cap.release()
                    st.success("Video processing complete.")
                except Exception as e:
                    st.error(f"An error occurred during video processing: {e}")
                finally:
                    # Clean up the temporary file
                    os.remove(video_path)

elif input_type == 'Live Feed':
    # Use OpenCV to capture the live video feed
    cap = cv2.VideoCapture(1)  # 0 represents the default camera

    if not cap.isOpened():
        st.error("Could not open video stream")
    else:
        st_frame = st.empty()  # Create an empty placeholder for the video frame

        while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("End of frame")
                break

            # Perform object detection
            results = model.predict(frame, conf=confidence_threshold)
            annotated_frame = results[0].plot()

            # Display the annotated frame in Streamlit
            st_frame.image(annotated_frame, channels="BGR", use_column_width=True)

        # Release the video capture object
        cap.release()