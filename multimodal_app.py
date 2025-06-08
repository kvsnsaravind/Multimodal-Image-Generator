import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = API_KEY)

st.title("Multimodal Image Generation")

user_input = st.text_input("Enter a prompt for image generation:")

if st.button("Generate Image"):
    if not user_input:
        st.warning("Please enter a prompt.")
    else:
        try:
            with st.spinner("Generating image..."):
                response = client.models.generate_content(
                model="gemini-2.0-flash-exp-image-generation",
                contents=user_input,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'])
                )
            
            st.subheader("Generated Image:")
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    st.write(part.text)
                elif part.inline_data is not None:
                    image = Image.open(BytesIO((part.inline_data.data)))
                    st.image(image)
        except Exception as e:
            st.error("An error occurred while generating the image.")

