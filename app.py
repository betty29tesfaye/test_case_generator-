import warnings
import time
import os 
import base64

warnings.filterwarnings('ignore')
import streamlit as st
from PIL import Image

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
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
  
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

chat_model = ChatOpenAI()
template = """
Return all the test cases of the following requirement
 
{test_requirement}
"""

prompt = PromptTemplate(
    input_variables=['test_requirement'],
    template=template
)
chain = LLMChain(
    llm=chat_model,
    prompt=prompt,
    verbose=True
)
add_background_image('bgi.png') 
st.markdown(f'<span style="background-color:#DFF2FF;color:#0F52BA;font-family:book-antiqua;font-size:24px;">AI App For Generating Test Cases</span>', unsafe_allow_html=True)
test_requirement = st.text_input("Hi there, Please enter the requirement of your test cases. Enter a statement similar to :The system shall allow users to edit the email body")
if test_requirement:
   st.write(chain.run(test_requirement))


