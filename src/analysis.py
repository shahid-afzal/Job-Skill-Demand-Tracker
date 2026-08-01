def get_top_skills(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT skill, COUNT(*) FROM job_skills
        GROUP BY skill
        ORDER BY COUNT(*) DESC

    """)
    result =  cursor.fetchall()
    return result

def count_jobs(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM jobs

    """)
    result = cursor.fetchone()[0]
    return result

def count_unique_skills(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(DISTINCT skill)
        FROM job_skills

    """)
    result = cursor.fetchone()[0]
    return result

def get_jobs_by_skill(connection, skill):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            title,
            company,
            location
        FROM jobs
        JOIN job_skills
        ON jobs.job_id = job_skills.job_id
        WHERE LOWER(skill) = LOWER(?)
    
    """, (skill,))

    result = cursor.fetchall()
    return result

def get_top_companies(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT company, COUNT(*)
        FROM jobs
        GROUP BY company
        ORDER BY COUNT(*) DESC

    """)

    result = cursor.fetchall()
    return result
