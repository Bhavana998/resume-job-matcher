import streamlit as st
from utils import extract_text_from_pdf, clean_text, calculate_match, skill_match

st.set_page_config(page_title="Resume Job Matcher", layout="centered")

st.title("📄 Resume–Job Match Analyzer")

st.write("Upload your resume and paste job description to get match percentage.")

# Upload resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("Paste Job Description Here")

if st.button("Analyze Match"):
    if resume_file is None or job_description.strip() == "":
        st.error("Please upload resume and enter job description.")
    else:
        # Extract and clean text
        resume_text = extract_text_from_pdf(resume_file)
        resume_text = clean_text(resume_text)
        job_text = clean_text(job_description)

        # Calculate match
        match_percentage = calculate_match(resume_text, job_text)
        skills_found = skill_match(resume_text)

        st.success(f"✅ Match Percentage: {match_percentage}%")

        st.subheader("🛠 Skills Found in Resume")
        if skills_found:
            st.write(", ".join(skills_found))
        else:
            st.write("No matching skills found.")