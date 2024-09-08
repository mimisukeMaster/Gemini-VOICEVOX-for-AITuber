"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ['API_KEY'])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
    history=[
    ]
)

prompt = "音楽理論におけるコード表記についてdim sus augの違いを教えて"
response = chat_session.send_message(prompt + "。ただし、回答は話しかけるような文体にして、記号(マークアップ用も含む)や改行を使わないで下さい。句点・読点は例外的にOKです。")

print(response.text)
