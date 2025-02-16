import streamlit as st
import google.generativeai as genai
# Setting the API Key
with open("key.txt", "r") as file:
    genai.configure(api_key = file.read().strip())
# System instruction for AI
system_prompt = """You are a Python code reviewer. You should review the code,
identify errors, provide improvements, and provide feedback on potential bugs
along with suggestions for fixes. You should accept only Python code as input.
Response structure should be like this: 1.error identification 2.Code optimization 3.Fixed code"""
# Initialize Gemini AI
gemini = genai.GenerativeModel(
    model_name="models/gemini-2.0-flash-exp",
    system_instruction=system_prompt
)
# Streamlit UI
st.title("Python Code Reviewer")
st.write("Enter your Python code")
# Text input for user
user_prompt = st.text_area("Code:", height=200)
# Button to review code
if st.button("Review"):
    if user_prompt.strip():
        with st.spinner("Reviewing your code..."):
            response = gemini.generate_content(user_prompt, stream=True)
        # Display the Review
        st.subheader("Review:")
        for chunk in response:
            st.write(chunk.text)
    else:
        st.warning("Kindly provide a Python code snippet before proceeding")