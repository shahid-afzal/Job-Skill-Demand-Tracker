SKILLS = [
    "Python",
    "SQL",
    "PostgreSQL",
    "MySQL",
    "SQLite",
    "Flask",
    "FastAPI",
    "Django",
    "Docker",
    "Git",
    "GitHub",
    "Linux",
    "AWS",
    "Azure",
    "GCP",
    "Pandas",
    "NumPy",
    "Power BI",
    "Excel",
    "JavaScript",
    "React",
    "Node.js",
]

def extract_skills(description):
    """Extracts known skills from a job description by matching keywords.

    Args:
        description (str): The text of the job description to analyze.

    Returns:
        list: A list of skills found in the job description.
    """
    extracted_skills = []
    description = description.lower()

    # Search for each pre-defined skill keyword in the lowercased description
    for skill in SKILLS:
        if skill.lower() in description:
            extracted_skills.append(skill)
    return extracted_skills

