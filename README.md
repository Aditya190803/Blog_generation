# Blog Writer

Blog Writer is a Streamlit-based web application that generates blog using the Gemini LLM API. Users can input a topic and specify the content length to generate relevant content in English.

## Features

- Generate content based on a user-provided topic
- Specify the desired length of the generated content
- Display the generated content in a user-friendly interface

## Prerequisites

- Python 3.7 or higher
- A Google Generative AI API key

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/aditya190803/blog-generation.git
    cd blog-generation
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your Google Generative AI API key**:
    - Create a file named `.streamlit/secrets.toml` in the root directory of your project:
    ```sh
    mkdir -p .streamlit
    nano .streamlit/secrets.toml  # You can use any text editor to create this file
    ```
    - Add your API key to the `secrets.toml` file:
    ```toml
    [secrets]
    GOOGLE_API_KEY = "your-google-api-key"
    ```

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

2. **Open your web browser** and navigate to `http://localhost:8501` to access the application.

3. **Generate content**:
    - Enter a topic in the text input box.
    - Specify the desired content length (in words).
    - Click the "Generate Content" button to generate and display the content.

## Troubleshooting

- Ensure that your API key is correct and has the necessary permissions.
- Make sure you have a stable internet connection to interact with the Google Generative AI API.

