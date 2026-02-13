# Intelligent Resume Analyzer

## 📌 Overview
The Intelligent Resume Analyzer is a Python-based HR Tech application that automates resume screening.  
It parses resumes, extracts key candidate information, matches skills against job requirements, calculates a match score (0–100), and generates structured hiring reports.

This project demonstrates:
- Python programming
- Text processing using Regular Expressions
- Data extraction algorithms
- JSON file handling
- Matching algorithms

---

## 🚀 Features

✔ Extracts candidate details:
- Name
- Email
- Skills
- Experience

✔ Loads job requirements from JSON  
✔ Calculates match score (0–100)  
✔ Generates hiring recommendation  
✔ Saves detailed analysis reports  
✔ Handles missing files and invalid formats  
✔ Modular and clean code structure  

---

## 🧠 Scoring Logic

The match score is calculated as:

- **Skills Match → 70%**
- **Experience Match → 30%**

### Recommendation Rules:

- **75+ → Strong Hire**
- **50–74 → Consider**
- **Below 50 → Reject**

---

## 📂 Project Structure

