# Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()

# Function to read data from text file
def read_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data

# Function to get Gemini response from the provided data
def get_gemini_response(question, data):
    lines = data.split("\n")
    for line in lines:
        if question.lower() in line.lower():
            return line
    return "No response found in the provided text file."

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Read data from text file
file_path = "text.txt"  # Update with the path to your text file
data = read_data(file_path)

# User input and button
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

# If submit button is clicked
if submit_button and input_text:
    response = get_gemini_response(input_text, data)
    
    # Display response
    st.subheader("The Response is")
    st.write(response)

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state.get('chat_history', []):
    st.write("{}: {}".format(role, text))
