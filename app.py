import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI-Powered Regulatory Checklist Generator")

st.write("Generate submission checklists using AI")

submission_type = st.text_input("Submission Type (e.g., NDA)")
region = st.text_input("Region (e.g., US FDA)")

if st.button("Generate Checklist"):
    prompt = f"""
    Generate a structured checklist for {submission_type} submission in {region}.
    
    Include:
    - Module-wise checklist
    - Required documents
    - Validation checks
    - Risks
    
    Return JSON format.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    output = response.output[0].content[0].text

    st.json(output)
