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
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#chat_model = ChatOpenAI()
llmtouse = OpenAI()
template = """
Return all the test cases of the following requirement
 
{system_requirement}
"""

prompt = PromptTemplate(
    input_variables=['system_requirement'],
    template=template
)
chain = LLMChain(
    llm=llmtouse,
    prompt=prompt,
    verbose=True
)
add_background_image('bgi.png') 
st.markdown(f'<span style="background-color:#DFF2FF;color:#0F52BA;font-family:book-antiqua;font-size:24px;">AI App For Generating Test Cases</span>', unsafe_allow_html=True)
st.markdown(f'<p style="background-color:#b3cee5;color:#414C6B;">Hi there to get test cases, please enter a statement requirement similar to: The system shall allow users to edit the email body</p>', unsafe_allow_html=True) 
system_requirement = st.text_input("") 
if system_requirement:
   with st.spinner('Generating The TestCases'):
      st.write(chain.run(system_requirement))


