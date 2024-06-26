import streamlit as st
import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Cache the generative model initialization
@st.cache_resource
def get_model():
    return genai.GenerativeModel('gemini-1.5-pro')

# Cache the generated content based on the input parameters
@st.cache_data
def generate_content(topics, content_length):
    model = get_model()
    prompt = f"Generate content related to {topics} with a length of {content_length} words in English."
    
    try:
        response = model.generate_content(prompt)
        # Ensure the response has parts and the first part has text
        if response.parts and len(response.parts) > 0 and hasattr(response.parts[0], 'text'):
            generated_content = response.parts[0].text
        else:
            generated_content = "Error: No content generated or response format unexpected."
    except Exception as e:
        generated_content = f"Error: {str(e)}"
    
    return generated_content

def main():
    st.title('Blog Writer')

    topics = st.text_input('Enter a topic:')
    content_length = st.number_input('Enter the content length (words):', min_value=1)

    if st.button('Generate Content'):
        if not topics:
            st.warning("Please enter a topic.")
        else:
            generated_content = generate_content(topics, content_length)
            st.subheader('Generated Content:')
            st.markdown(generated_content, unsafe_allow_html=True)  # Display the generated content as markdown
            
            # Convert generated content to markdown and offer download
            markdown_content = f"# {topics}\n\n{generated_content}"
            st.download_button(
                label="Download Markdown",
                data=markdown_content,
                file_name="generated_blog.md",
                mime="text/markdown"
            )

if __name__ == '__main__':
    main()
