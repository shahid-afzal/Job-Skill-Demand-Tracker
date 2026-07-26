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
    extracted_skills = []
    description = description.lower()

    for skill in SKILLS:
        if skill.lower() in description:
            extracted_skills.append(skill)
    return extracted_skills

