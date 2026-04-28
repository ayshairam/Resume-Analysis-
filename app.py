import streamlit as st
import requests
import re

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer")
st.caption("Powered by Local AI (Ollama - Llama3)")

# -----------------------------
# FUNCTION TO CALL OLLAMA
# -----------------------------
def get_response(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"⚠️ Error: {response.status_code}"

    except requests.exceptions.ConnectionError:
        return "❌ Ollama not running. Run this in terminal: `ollama run llama3`"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# -----------------------------
# USER INPUT
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area("📌 Paste your Resume", height=300)

with col2:
    job_role = st.text_input("🎯 Job Role (e.g., Data Scientist)")

# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("Analyze Resume"):

    if not resume_text or not job_role:
        st.warning("⚠️ Please fill all fields")

    else:
        prompt = f"""
        You are an expert HR recruiter.

        Analyze the resume for the role: {job_role}

        Return STRICTLY in this format:

        Score: <number>/100

        Strengths:
        - point 1
        - point 2

        Weaknesses:
        - point 1
        - point 2

        Missing Skills:
        - point 1
        - point 2

        Suggestions:
        - point 1
        - point 2

        Resume:
        {resume_text}
        """

        with st.spinner("Analyzing... ⏳"):
            result = get_response(prompt)

        # -----------------------------
        # SCORE EXTRACTION
        # -----------------------------
        match = re.search(r"(\d+)/100", result)
        score = int(match.group(1)) if match else 0

        # -----------------------------
        # DISPLAY
        # -----------------------------
        st.success("✅ Analysis Complete")

        st.subheader("📊 Match Score")
        st.progress(score)
        st.write(f"### {score}/100")

        st.markdown("## 📌 Detailed Feedback")
        st.markdown(result)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Built using Streamlit + Ollama (Local LLM)")