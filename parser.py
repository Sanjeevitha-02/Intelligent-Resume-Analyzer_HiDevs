import re


def parse_resume(text):
    """Extract name, email, skills, and experience from resume text.

    Returns a dict with keys: name, email, skills, experience_years.
    Handles missing/malformed fields gracefully.
    """
    if not text or not text.strip():
        return {
            "name": None,
            "email": None,
            "skills": [],
            "experience_years": 0
        }

    data = {}

    # Email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    data['email'] = email_match.group() if email_match else None

    # Name — assume first non-empty line is the name
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    data['name'] = lines[0] if lines else None

    # Skills — look for a "Skills:" section
    skills_match = re.search(r'Skills:(.*)', text, re.IGNORECASE)
    if skills_match:
        skills_line = skills_match.group(1)
        data['skills'] = [s.strip() for s in skills_line.split(',') if s.strip()]
    else:
        data['skills'] = []

    # Experience — look for "X years"
    exp_match = re.search(r'(\d+)\+?\s*years?', text, re.IGNORECASE)
    data['experience_years'] = int(exp_match.group(1)) if exp_match else 0

    return data