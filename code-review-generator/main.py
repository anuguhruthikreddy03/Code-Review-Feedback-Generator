import json
import streamlit as st

from streamlit_ace import st_ace

from parser import CodeReview
from prompt import prompt
from model import llm

from langchain_core.output_parsers import PydanticOutputParser

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="AI Code Review Generator",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------

st.title("💻 AI Code Review Feedback Generator")

st.markdown("Analyze code quality using Generative AI")

# -----------------------------------
# Language Selection
# -----------------------------------

language = st.selectbox(
    "Select Programming Language",
    [
        "python",
        "java",
        "javascript",
        "c",
        "cpp",
        "html",
        "css"
    ]
)

# -----------------------------------
# Theme Selection
# -----------------------------------

theme = st.radio(
    "Choose Theme",
    ["light", "dark"]
)

# -----------------------------------
# Code Editor
# -----------------------------------

code_input = st_ace(
    placeholder="Paste your code here...",
    language=language,
    theme="monokai" if theme == "dark" else "github",
    height=300
)

# -----------------------------------
# Parser
# -----------------------------------

parser = PydanticOutputParser(
    pydantic_object=CodeReview
)

# -----------------------------------
# Review Button
# -----------------------------------

if st.button("Review Code"):

    if code_input.strip() == "":
        st.warning("Please enter code")

    else:

        with st.spinner("Reviewing Code..."):

            final_prompt = prompt.format(
                code=code_input,
                language=language,
                format_instructions=parser.get_format_instructions()
            )

            try:
                response = llm.invoke(final_prompt)
                result = parser.parse(response.content)
                result_dict = result.model_dump()  # not .dict()
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.stop()

        # -----------------------------------
        # Output
        # -----------------------------------

        st.success("Code Review Completed")

        st.subheader("Review Result")

        st.json(result_dict)

        # -----------------------------------
        # JSON Output
        # -----------------------------------

        json_output = json.dumps(
            result_dict,
            indent=4
        )

        st.code(json_output, language="json")

        # -----------------------------------
        # Download Button
        # -----------------------------------

        st.download_button(
            label="Download Review Report",
            data=json_output,
            file_name="code_review_report.json",
            mime="application/json"
        )