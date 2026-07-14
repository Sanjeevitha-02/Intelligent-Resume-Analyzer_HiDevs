def calculate_match_score(candidate_data, job_requirements):
    """Compare candidate skills/experience to job requirements. Returns 0-100."""
    if not candidate_data or not job_requirements:
        return 0.0

    required_skills = set(s.lower() for s in job_requirements.get('skills', []))
    candidate_skills = set(s.lower() for s in candidate_data.get('skills', []))

    if required_skills:
        skill_overlap = len(required_skills & candidate_skills) / len(required_skills)
    else:
        skill_overlap = 0

    required_exp = job_requirements.get('min_experience', 0)
    candidate_exp = candidate_data.get('experience_years', 0)
    exp_score = min(candidate_exp / required_exp, 1) if required_exp else 1

    # Weight: 70% skills, 30% experience
    final_score = (skill_overlap * 0.7 + exp_score * 0.3) * 100
    return round(final_score, 2)