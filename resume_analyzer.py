import json
import re
from pathlib import Path


def read_resume(file_path):
    return file_path.read_text(encoding="utf-8")


def extract_resume_data(text):
    name = re.search(r"Name:\s*(.*)", text).group(1).strip()
    email = re.search(r"Email:\s*(.*)", text).group(1).strip()

    skills_text = re.search(r"Skills:\s*(.*)", text).group(1)
    skills = [s.strip().lower() for s in skills_text.split(",")]

    experience = int(re.search(r"Experience:\s*(\d+)", text).group(1))

    return {
        "name": name,
        "email": email,
        "skills": skills,
        "experience": experience
    }


def load_job_requirements(path):
    return json.loads(path.read_text(encoding="utf-8"))


def calculate_match_score(candidate, job):
    required_skills = job["required_skills"]
    min_exp = job["minimum_experience"]

    matched = list(set(candidate["skills"]) & set(required_skills))

    skill_score = (len(matched) / len(required_skills)) * 70
    exp_score = 30 if candidate["experience"] >= min_exp else 10

    total_score = round(skill_score + exp_score, 2)

    return total_score, matched


def generate_recommendation(score):
    if score >= 75:
        return "Strong Hire"
    elif score >= 50:
        return "Consider"
    else:
        return "Reject"


def analyze_all_resumes():
    resumes_folder = Path("resumes")
    reports_folder = Path("analysis_reports")
    job_file = Path("job_requirements.json")

    job = load_job_requirements(job_file)

    for resume_file in resumes_folder.iterdir():
        if resume_file.suffix != ".txt":
            continue

        text = read_resume(resume_file)
        candidate = extract_resume_data(text)

        score, matched_skills = calculate_match_score(candidate, job)
        recommendation = generate_recommendation(score)

        report = {
            "candidate_name": candidate["name"],
            "email": candidate["email"],
            "matched_skills": matched_skills,
            "total_experience": candidate["experience"],
            "match_score": score,
            "recommendation": recommendation
        }

        output_file = reports_folder / f"{candidate['name'].replace(' ', '_')}_report.json"
        output_file.write_text(json.dumps(report, indent=4))

        print(f"Processed: {candidate['name']}")


if __name__ == "__main__":
    analyze_all_resumes()
    print("\nAll resumes analyzed successfully ✅")
