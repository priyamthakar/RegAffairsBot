import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def main():
    st.set_page_config(page_title="Regulatory Affairs Specialist by Priyam", page_icon="🤖", layout="wide")
    st.title("RegAffairsBot 🤖")
    st.write("I am a Regulatory Affairs Specialist. I can help you with regulatory compliance, quality assurance, and product development. Ask me anything!")
    st.caption("Created by Priyam Thakar")
    st.caption("Disclaimer: This tool is intended for informational purposes only. It is not a substitute for professional advice.")

    st.sidebar.title("About")
    st.sidebar.info("This is a chatbot powered by OpenAI's GPT-4 model. It is designed to provide information on regulatory affairs, quality assurance, and product development. Please use it responsibly.")

    with st.sidebar:
        st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        st.markdown("[Priyam's LinkedIn](https://www.linkedin.com/in/priyam-thakar)")
        st.markdown("[Priyam's GitHub](https://github.com/priyamthakar)")
        st.markdown("[Contact Priyam via email](mailto:priyamthakar1@gmail.com)")

    # Check if the API key has been provided
    if "openai_api_key" not in st.session_state:
        with st.form(key="api_key_form"):
            openai_api_key = st.text_input("Enter your OpenAI API Key", type="password", key="chatbot_api_key")
            submit = st.form_submit_button("Submit")
            if submit:
                st.session_state.openai_api_key = openai_api_key
                st.success("API key accepted. You can now access the chatbot.")
            else:
                st.warning("Please enter your OpenAI API key to access the chatbot.")
                return

    # Initialize the OpenAI client
    client = OpenAI(api_key=st.session_state.openai_api_key)

    def interact_with_assistant(prompt):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a top-tier Regulatory Affairs Specialist."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("I am happy to help:", key="user_input")
    if user_input:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate and append assistant response
        assistant_response = interact_with_assistant(user_input)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        # Display assistant response
        st.write("Assistant:", assistant_response)

    if st.button("Clear Chat"):
        st.session_state.messages.clear()

if __name__ == "__main__":
    main()