import warnings
import time
import os 
import base64

warnings.filterwarnings('ignore')
import streamlit as st
from PIL import Image

from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
client = OpenAI(os.environ["OPENAI_API_KEY"])

def add_background_image(image_file):
  with open(image_file, "rb") as image_file:
     encoded_string = base64.b64encode(image_file.read())
  st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
  
def generate_test_cases(requirement):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant capable of generating software test cases."},
        {"role": "user", "content": requirement}
      ]
    )
    return response.choices[0].message.content
  add_background_image('bgi.png') 


