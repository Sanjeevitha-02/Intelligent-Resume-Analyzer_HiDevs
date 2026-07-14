import json
import os

from parser import parse_resume
from matcher import calculate_match_score
from report_generator import generate_summary_report
from resume_data import sample_resumes


def load_resumes_from_folder(folder_path):
    """Read all .txt files in a folder and return their contents as a list."""
    resumes = []
    if not os.path.isdir(folder_path):
        print(f"Folder not found: {folder_path}")
        return resumes

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    resumes.append(f.read())
            except Exception as e:
                print(f"Could not read {filename}: {e}")
    return resumes


def load_job_requirements(filepath):
    """Load job requirements from a JSON file. Falls back to defaults on failure."""
    default = {"skills": [], "min_experience": 0}
    if not os.path.isfile(filepath):
        print(f"Job requirements file not found: {filepath}. Using defaults.")
        return default
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filepath}: {e}. Using defaults.")
        return default


def analyze_resumes(resumes, requirements):
    """Parse and score a list of resume text blocks. Returns list of results."""
    results = []
    for resume_text in resumes:
        try:
            candidate = parse_resume(resume_text)
            score = calculate_match_score(candidate, requirements)
            results.append({"candidate": candidate, "score": score})
        except Exception as e:
            print(f"Error processing a resume: {e}")
            continue
    return results


if __name__ == "__main__":
    resumes = load_resumes_from_folder("resumes")

    if not resumes:
        print("No resumes found in 'resumes' folder, using sample data instead.")
        resumes = sample_resumes

    requirements = load_job_requirements("job_requirements.json")

    results = analyze_resumes(resumes, requirements)

    report = generate_summary_report(results)
    print(report)

    with open("result.json", "w") as f:
        json.dump(results, f, indent=2)