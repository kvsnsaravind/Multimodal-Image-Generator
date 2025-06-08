# Multimodal-Image-Generator
Gemini AI Image Generator: Create AI-Powered Images from Text Prompts

# 🎨 Gemini AI Image Generator

A Streamlit-powered web app that generates AI images using Google's Gemini 2.0 Flash model. Just enter a text prompt and watch the model generate a relevant image and optional description instantly.

---

## 🚀 Features

- Text-to-Image generation via Gemini API
- Multi-modal output: view both AI-generated text and images
- User-friendly UI built with Streamlit
- Spinner and error handling for smooth UX
---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Generative AI (Gemini) API
- Pillow (for image rendering)
- `dotenv` for API key security

---
## Install dependencies

```
pip install -r requirements.txt
```
---

## Set up environment variables

Create a .env file in the project root.
Add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```
---

### ▶️ Usage
Run the Streamlit app:
```
streamlit run app.py
```
Then, open your browser and go to http://localhost:8501.

Enter a prompt like:
"A futuristic city at sunset with flying cars"

Click Generate Image and enjoy the AI magic!

---

### 📄 License
This project is open-source under the MIT License.

### 🤝 Acknowledgments
Google Gemini API

Streamlit

