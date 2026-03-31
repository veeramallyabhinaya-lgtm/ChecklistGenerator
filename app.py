import streamlit as st
from openai import OpenAI
import json

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI-Powered Regulatory Checklist Generator")

st.write("Generate submission checklists using AI")

submission_type = st.text_input("Submission Type (e.g., NDA)")
region = st.text_input("Region (e.g., US FDA)")

if st.button("Generate Checklist"):
    prompt = f"""
Generate a structured checklist for {submission_type} submission in {region}.

IMPORTANT:
- Return ONLY valid JSON
- Do NOT include markdown or backticks
- Do NOT include explanations

Format:
{{
  "Module 1": {{
    "documents": [],
    "validation_checks": [],
    "risks": []
  }}
}}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

output = response.output[0].content[0].text

# Remove markdown formatting
clean_output = output.replace("```json", "").replace("```", "").strip()

try:
    parsed = json.loads(clean_output)
    st.json(parsed)
except:
    st.write("Raw Output:")
    st.write(clean_output)
