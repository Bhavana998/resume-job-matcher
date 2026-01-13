import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def calculate_match(resume_text, job_text):
    resume_words = set(resume_text.split())
    job_words = set(job_text.split())

    if len(job_words) == 0:
        return 0

    matched = resume_words.intersection(job_words)
    score = (len(matched) / len(job_words)) * 100
    return round(score, 2)


def skill_match(text):
    skills = [
        "python", "machine learning", "deep learning", "sql",
        "data analysis", "pandas", "numpy", "streamlit",
        "tensorflow", "pytorch", "opencv"
    ]
    found = [skill for skill in skills if skill in text.lower()]
    return found