import os
import base64
import streamlit as st
from io import BytesIO
from PIL import Image
import ollama
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="Vision Model Analyzer", layout="centered")
st.title("🔍 Vision Model Analyzer")
st.write("Upload an image to analyze it using a vision model.")

def vision_model_selection():
    available_models = ollama.list()
    vision_families = {'mllama', 'clip'} 
    vision_model_names = [
        model['model']
        for model in available_models['models']
        if any(family in model['details']['families'] for family in vision_families)
    ]
    vision_model_names.insert(0, "") 
    if vision_model_names[1:]:
        selected_model = st.selectbox("Choose a vision model:", vision_model_names)
    else:
        st.warning("No vision models found.")
        selected_model = ""
    return selected_model

def process_and_analyze_image(pil_image, extension, model):
    try:
        ext = extension.replace('.', '').upper()
        format = "JPEG" if ext == "JPG" else ext
        buffered = BytesIO()
        pil_image.save(buffered, format=format)
        image_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        user_input = st.text_input("Ask your query about the image:", key="vision_query")

        if user_input:
            with st.spinner("Analyzing image..."):
                system_prompt = """
                    You are a highly skilled AI vision model specialized in analyzing various types of images from various types of domains
                    Your task is to:
                    - Accurately describe the visible images
                    - Mention features like structure, orientation and more
                    - Use concise, clear, and professional language
                    - Avoid guessing or hallucinating details not clearly visible
                """
                llm = OllamaLLM(model=model, system_prompt=system_prompt)
                image_context = llm.bind(images=[image_b64])
                response = image_context.invoke(user_input)
                st.markdown("### 📋 Response")
                st.write(response)
    except Exception as e:
        st.error(f"Error during image analysis: {e}")

uploaded_file = st.file_uploader(
    "Upload an image (jpg, jpeg, png, tiff):",
    type=["jpg", "jpeg", "png", "tiff"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    model = vision_model_selection()
    if model:
        process_and_analyze_image(image, os.path.splitext(uploaded_file.name)[1], model)
    else:
        st.warning("Please select a vision model to continue.")
