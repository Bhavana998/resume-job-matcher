# 📄 Resume Job Matcher

An AI-powered web application that analyzes and matches resumes with job descriptions using Natural Language Processing (NLP) techniques.

### 🔗 Live App:
👉 https://bhavana998-resume-job-matcher-app-ncmlai.streamlit.app/

### 🚀 Project Overview

Resume Job Matcher helps candidates evaluate how well their resume aligns with a job description.

The system:

Extracts text from uploaded resumes (PDF/TXT)

Processes and cleans the text

Applies NLP techniques

Computes similarity score between resume and job description

Displays a match percentage

This project demonstrates practical implementation of:

Text preprocessing

Feature extraction (TF-IDF)

Cosine similarity

Web deployment using Streamlit

### 🧠 Tech Stack

Python

Streamlit – Frontend & Deployment

Scikit-learn – TF-IDF & Cosine Similarity

NLTK – Text preprocessing

PyPDF2 – PDF text extraction

Pandas & NumPy

### ✨ Features

### 📄 Upload Resume (PDF / TXT)

### 📝 Paste Job Description

### 🔍 Automatic Text Cleaning & Processing

### 📊 Match Score Calculation

### 🌐 Deployed Web Application

###⚡ Lightweight and Fast

### 🏗 How It Works

Resume text is extracted.

Both resume and job description are preprocessed:

Lowercasing

Stopword removal

Tokenization

TF-IDF Vectorization is applied.

Cosine Similarity calculates the match score.

Result is displayed as percentage.

### 📂 Project Structure
resume-job-matcher/
│
├── app.py                 # Streamlit frontend
├── src/
│   ├── matcher.py         # Matching logic
│   ├── preprocessing.py   # Text cleaning
│
├── requirements.txt
└── README.md

### 🛠 Installation (Run Locally)

Clone the repository:

git clone https://github.com/Bhavana998/resume-job-matcher.git
cd resume-job-matcher


Create virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py


App will open at:

http://localhost:8501

### 🌍 Deployment

This application is deployed using Streamlit Cloud.

Live URL:
### https://bhavana998-resume-job-matcher-app-ncmlai.streamlit.app/

### 📊 Example Use Case

If a job description requires:

Python

Machine Learning

NLP

Data Analysis

The app compares these skills with resume content and provides a match score like:

Match Score: 78%

### 🔮 Future Improvements

Highlight missing skills

Skill extraction visualization

Sentence Transformer embeddings (BERT)

Resume feedback suggestions

Downloadable match report

ATS compatibility scoring

### 👩‍💻 Author

Setty Bhavana
B.Tech – Information Technology
Aspiring AI/ML Engineer

GitHub: https://github.com/Bhavana998

### ⭐ If You Like This Project

Give it a ⭐ on GitHub!
