import streamlit as st
import google.generativeai as genai

# Configure the Generative AI API key
genai.configure(api_key="AIzaSyD1uX9EStt8b7w7wlkM66v9j0DdGUPzS0o")
llm = genai.GenerativeModel("models/gemini-1.5-flash")

# Configure Streamlit app
st.set_page_config(
    page_title="SmartCode Review",
    page_icon="🧠",
    layout="wide",
)

# Path to your image (update it accordingly)
image_path = r"C:\Users\HP\OneDrive\Pictures\inoopng.png"

# Display the logo with a specified width
st.image(image_path, width=400)

# Header Section
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #0288D1;  # Changed the title color to a more modern blue
        font-weight: bold;
        text-align: center;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #555555;
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #888888;
        margin-top: 50px;
    }
    </style>
    <div>
        <p class="main-title">SmartCode Review 🤖</p>
        <p class="sub-title">AI-powered code analysis for optimization and bug fixes</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar Content
st.sidebar.header("SmartCode Reviewer 🤖")
st.sidebar.markdown(
    """
    - 💻 **Supported Languages:** Python, Java, C, C++, JS, SQL
    - 🧠 **Bug Detection:** AI identifies issues in your code and offers suggestions
    - ✨ **Optimize Your Code:** Get instant fixes and improvement tips
    """
)

# Sidebar Image
st.sidebar.image(r"C:\Users\HP\OneDrive\Pictures\codereview logo.png", width=300)

# Language Selection
language = st.selectbox("👆 Select a Programming Language", ["Python", "Java", "C", "C++", "JS", "SQL"])
st.markdown(f"🙇 Paste or write your {language} code below:")
code_input = st.text_area("🧑‍💻 Enter your code 📝:", height=200, placeholder="Paste or type your code here...")

# Function to Process Code and Get Review
def analyze_code(language: str, code: str) -> str:
    """
    Function to send the code for AI review and get suggestions.
    :param language: The programming language of the code.
    :param code: The code to analyze.
    :return: Response containing review and fixes.
    """
    try:
        prompt = f"Review the following {language} code. Identify bugs, suggest improvements, and provide optimized code:\n\n{code}"
        chat_bot = llm.start_chat(history=[])
        response = chat_bot.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error during analysis: {e}"

# Submit Button and Display Results
if st.button("👾 Submit Code for Review"):
    if not code_input.strip():
        st.error("Please enter some code before submitting.")
    else:
        with st.spinner("Analyzing your code...🧐"):
            response_text = analyze_code(language, code_input)
            if response_text.startswith("⚠️"):
                st.error(response_text)
            else:
                st.markdown("### Code Review Results:")
                st.write(response_text)

# Footer Section
st.markdown(
    """
    <div class="footer">
        <hr>
        <p>Powered by Streamlit and Google's Gemini AI for code analysis</p>
    </div>
    """,
    unsafe_allow_html=True,
)
