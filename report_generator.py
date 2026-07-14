def generate_report(candidate_data, score):
    """Build a readable hiring report for one candidate."""
    lines = []
    lines.append(f"Candidate: {candidate_data.get('name') or 'Unknown'}")
    lines.append(f"Email: {candidate_data.get('email') or 'N/A'}")
    skills = candidate_data.get('skills', [])
    lines.append(f"Skills: {', '.join(skills) if skills else 'None listed'}")
    lines.append(f"Experience: {candidate_data.get('experience_years', 0)} years")
    lines.append(f"Match Score: {score}/100")

    if score >= 75:
        recommendation = "Strong match — recommend interview"
    elif score >= 50:
        recommendation = "Moderate match — consider for interview"
    else:
        recommendation = "Weak match — likely not a fit"

    lines.append(f"Recommendation: {recommendation}")
    return "\n".join(lines)


def generate_summary_report(results):
    """Build a combined report for multiple candidates, sorted by score."""
    sorted_results = sorted(results, key=lambda r: r['score'], reverse=True)
    sections = []
    for r in sorted_results:
        sections.append(generate_report(r['candidate'], r['score']))
        sections.append("-" * 40)
    return "\n".join(sections)