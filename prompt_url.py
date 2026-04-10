import os
import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

# 1. Load environment variables
load_dotenv()

# 2. UI Setup
st.set_page_config(page_title="Research Tool", page_icon="🔬")
st.header("Research Tool")
paper_input = st.selectbox("select the paper name :",["attention is all you need", "Diffusion model beat GANs on image synthesis"])
style_input = st.selectbox("Select explanation style:", ["Beginner-friendly", "technical", "code-oriented", "mathematical"])
length_input = st.selectbox("Select response length:", ["Short (1-2 paragraphs)", "Medium (3-4 paragraphs)", "Long(5+ paragraphs)"])

# 3. Model Initialization
# It's often better to wrap this in a function or cache it, 
# but for a simple script, initializing here is fine.
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    # Adding a timeout and temperature is usually helpful
    timeout=300 
)
model = ChatHuggingFace(llm=llm)
template = PromptTemplate(
        template="Explain the paper '{paper_input}' in a {style_input} style with a {length_input} response.",
        input_variables=["paper_input", "style_input", "length_input"]
)
# 4. Execution Logic
if st.button("Submit"):
                formatted_prompt =  template.format(
                        paper_input=paper_input,
                        style_input=style_input, 
                        length_input=length_input
                        )
                with st.spinner("genrating explanation......"):
                        try:
                                result = model.invoke(formatted_prompt)
                                st.subheader("Result:")
                                st.write(result.content)
                        except Exception as e:
                                st.error(f"An error occurred: {e}")
           



    