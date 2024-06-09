import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def generate_content(topics, content_length):
    # Generate content using the Gemini LLM API
    model = genai.GenerativeModel('gemini-1.5-pro')
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
    st.title('Gemini Blog Assistant')

    topics = st.text_input('Enter a topic:')
    content_length = st.number_input('Enter the content length (words):', min_value=1)

    if st.button('Generate Content'):
        if not topics:
            st.warning("Please enter a topic.")
        else:
            generated_content = generate_content(topics, content_length)
            st.subheader('Generated Content:')
            st.markdown(generated_content, unsafe_allow_html=True)  # Display the generated content as markdown

if __name__ == '__main__':
    main()
