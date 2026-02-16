import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import streamlit as st
from utils.llm_client import HuggingFaceClient
from utils.debugging_helper import build_debugging_prompt
def main():
    st.set_page_config(
        page_title="AI Debugging Assistant",
        page_icon= "👨‍🏫",
        layout = "centered"
    )

    st.title("👨‍🏫 AI Debugging Assistant")
    st.write("Describe your coding issue, and I will help you debug it!")

    user_input =st.text_area(
        label="Enter your code or error log below:",
        height=200,
        placeholder="Example:\nprint('Hello World')"
    )

    if st.button("🔍 Debug code"):
        if not user_input.strip():
            st.warning("Please enter your code or error log to proceed.")
            return
        with st.spinner("Analyzing your code.."):
            try:
                prompt = build_debugging_prompt(user_input)
                client = HuggingFaceClient()
                response = client.ask(prompt)

                st.markdown("---")
                st.subheader("🧠 debugging result")
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occured: {str(e)}")

if __name__ =="__main__":
    main()