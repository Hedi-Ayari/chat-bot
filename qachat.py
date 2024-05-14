import streamlit as st

# Function to read data from a file
def read_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data

# Function to get response from data
def get_gemini_response(question, data):
    # Search for the question in the provided data
    for index, line in enumerate(data):
        if question.lower() in line.lower():
            # Assuming question on first line, answer on second
            response_lines = data[index + 1:]
            # Remove empty lines and comments from the response
            response = [line.strip() for line in response_lines if line.strip() and not line.strip().startswith("#")]
            return response
    return "No response found for the question in the provided text file."
# Initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# File path containing responses
file_path = "text.txt"

# Read data from the file
data = read_data(file_path)

# Debug print to check the data read from the file
st.write("Data from file:", data)

# User input
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

# Respond to user input
if submit_button and input_text:
    response = get_gemini_response(input_text, data)
    
    # Debug print to check the response
    st.write("Response:", response)
    
    # Add user query and response to session state chat history
    st.subheader("The Response is")
    st.write(response)
    st.session_state['chat_history'].append(("You", input_text))
    st.session_state['chat_history'].append(("Bot", response))

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state.get('chat_history', []):
    st.write(f"{role}: {text}")
