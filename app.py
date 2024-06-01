import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Function to get response from LLaMA model
def getLLamaresponse(input_text, no_words, blog_style):
    # Initialize the GROQ chat model
    groq_api_key = os.getenv('GROQ_API_KEY')
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192", temperature=0.35)
    
    # Define the prompt template
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """
    prompt_text = template.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
    
    # Generate the response from the LLaMA model
    try:
        response = llm.generate(messages=[{'role': 'system', 'content': prompt_text}])
    except TypeError as e:
        st.error(f"TypeError: {e}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

    return response

# Streamlit configuration
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

# Get user input
input_text = st.text_input("Enter the Blog Topic")
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

# Button to generate the blog
submit = st.button("Generate")

# Display the generated blog
if submit:
    if input_text and no_words.isdigit():
        no_words = int(no_words)  # Convert to integer
        response = getLLamaresponse(input_text, no_words, blog_style)
        if response:
            st.write(response)
    else:
        st.error("Please enter a valid topic and number of words.")
