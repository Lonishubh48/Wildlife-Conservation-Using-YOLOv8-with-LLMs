import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np
from gtts import gTTS
import os
import google.generativeai as genai
import base64

# Configure the API key
genai.configure(api_key="Your google Api key")

# Load the trained model
model = YOLO("trainedweight.pt")

# Set the background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/667205/pexels-photo-667205.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        color: white; /* Change text color to white for better visibility */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title
st.title("YOLO-Powered Wildlife Recognition!")
st.write("Upload an image, and the model will detect animals.")

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image using OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Run prediction
    results = model.predict(image, imgsz=640)

    # Draw bounding boxes and labels on the image
    detected_classes = []
    for result in results:
        boxes = result.boxes.xyxy.numpy()
        confidence = result.boxes.conf.numpy()
        class_ids = result.boxes.cls.numpy()

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box)
            label = f"{model.names[int(class_ids[i])]} {confidence[i]:.2f}"
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            detected_classes.append(int(class_ids[i]))

    # Display the image with detections
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Processed Image', use_container_width=True)

    # Print detected classes
    unique_classes = set(detected_classes)
    st.write("Detected classes:")

    detected_text = ""
    for class_id in unique_classes:
        class_name = model.names[class_id]
        st.write(f"**{class_name}**")
        detected_text += f"{class_name}, "

    # Generate speech
    if detected_text:
        detected_text = detected_text.rstrip(", ")  # Remove trailing comma
        tts = gTTS(text=f"Detected animals are: {detected_text}", lang='en')
        audio_file = "detected_animals.mp3"
        tts.save(audio_file)

        # Provide a link to download the audio
        st.audio(audio_file, format='audio/mp3')

    # Use Gemini Pro to enhance the description with image data
    def generate_enhanced_description(text, image_bytes):
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = (
            f"You are an expert in wildlife conservation. Based on the detected animals in the image, "
            f"provide a brief description of each animal, including its characteristics, habitat, and behavior. "
            f"Additionally, briefly describe how to conserve each species in one or two sentences.\n\n"
            f"Here are the detected animals: {text}.\n\n"
            f"For each animal, include:\n"
            f"1. A brief description.\n"
            f"2. Its role in the ecosystem.\n"
            f"3. Threats it faces.\n"
            f"4. A brief conservation strategy (1-2 sentences).\n\n"
            f"Please provide the information in a structured format."
        )
        image_data = base64.b64encode(image_bytes).decode('utf-8')
        prompt += f"\nImage data (base64): {image_data}"
        response = model.generate_content(prompt)
        return response.text

    enhanced_description = generate_enhanced_description(detected_text, file_bytes)
    st.write(enhanced_description)

    # Generate speech output
    tts = gTTS(text=enhanced_description, lang='en')
    audio_file = "enhanced_description.mp3"
    tts.save(audio_file)

    # Provide a link to download the audio
    st.audio(audio_file, format='audio/mp3')


# Animal conservation information
st.subheader("Why Animal Conservation Matters")
st.markdown("""
- **Biodiversity**: Protecting animals ensures the survival of diverse species, which is vital for ecosystem balance.
- **Ecological Health**: Animals play key roles in their ecosystems, such as pollination, seed dispersal, and maintaining food chains- **Cultural Significance**: Many cultures have deep connections with wildlife, and conservation helps preserve these cultural heritages.
- **Economic Benefits**: Wildlife tourism and sustainable practices can provide economic benefits to local communities.
- **Climate Regulation**: Healthy animal populations contribute to climate regulation and can help mitigate the effects of climate change.
""")
