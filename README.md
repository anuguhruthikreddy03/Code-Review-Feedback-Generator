# Code Review Feedback Generator

An AI-powered application that analyzes code snippets and generates structured feedback about code quality, issues, and improvement suggestions using Generative AI.

---

## Project Overview

Software development teams rely heavily on code reviews to maintain code quality. However, manual reviews can be time-consuming and depend on reviewer availability and expertise.

This project provides an automated AI-based code review assistant that:
- Accepts a code snippet as input
- Analyzes the code without executing it
- Detects syntax and readability issues
- Suggests improvements
- Generates a structured review response

The system is designed for educational purposes, beginner developers, and early-stage software development workflows.

---

## Features

- AI-powered code review
- Detects formatting and syntax issues
- Provides improvement suggestions
- Generates code quality ratings
- Summarizes review feedback
- Simple Streamlit-based user interface
- Logging support for tracking requests and responses

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI/LLM
- Google Gemini API / Generative AI

### Libraries Used
- streamlit
- google-generativeai
- logging
- json
- os

---

## Project Structure

```bash
code-review-generator/
│
├── app.py                # Streamlit frontend
├── chatbot.py            # AI review logic
├── chatbot.log           # Log file
├── requirements.txt      # Dependencies
├── README.md             # Project documentation

## Clone the Repository

```bash
git clone https://github.com/your-username/code-review-generator.git
```

---

## Navigate to Project Folder

```bash
cd code-review-generator
```

---

## Create Virtual Environment (Optional)

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

## Advantages

- Saves developer time
- Improves code quality
- Beginner-friendly
- Fast automated reviews
- Easy to use interface

---

## Limitations

- Does not execute code
- Limited contextual understanding
- Depends on AI model quality
- May miss advanced logical errors

---

## Conclusion

The Code Review Feedback Generator helps developers quickly analyze and improve code quality using Generative AI. It provides structured feedback, practical suggestions, and an easy-to-use interface, making it useful for students, beginners, and development teams.

---

## Author

**Hruthik**
