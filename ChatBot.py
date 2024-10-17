import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer
import torch

# Load the BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()

# Function to generate a response
def generate_response(user_input):
    # Encode the user input and generate a response
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    
    # Generate a response
    response_ids = model.generate(input_ids, max_length=200, num_beams=5, early_stopping=True)
    
    # Decode the response
    bot_response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    
    return bot_response

# Streamlit application
st.title("AI Chatbot")
st.write("Ask me any question about Artificial Intelligence!")

# Input box for user question
user_input = st.text_input("You: ")

if st.button("Send"):
    if user_input:
        bot_response = generate_response(user_input)
        st.write(f"Chatbot: {bot_response}")
    else:
        st.write("Please enter a question.")
