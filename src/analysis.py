import csv
import os

def get_top_skills(connection):
    """Retrieves the list of skills ordered by their frequency across jobs.

    Args:
        connection (sqlite3.Connection): An active database connection.

    Returns:
        list of tuple: A list of (skill, count) tuples representing skill frequency.
    """
    cursor = connection.cursor()
    # Group and count the occurances of each unique skill key
    cursor.execute("""
        SELECT skill, COUNT(*) FROM job_skills
        GROUP BY skill
        ORDER BY COUNT(*) DESC

    """)
    result =  cursor.fetchall()
    return result

def count_jobs(connection):
    """Counts the total number of job postings in the database.

    Args:
        connection (sqlite3.Connection): An active database connection.

    Returns:
        int: The total count of jobs.
    """
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM jobs

    """)
    result = cursor.fetchone()[0]
    return result

def count_unique_skills(connection):
    """Counts the number of distinct skills extracted across all job postings.

    Args:
        connection (sqlite3.Connection): An active database connection.

    Returns:
        int: The total count of unique skills.
    """
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(DISTINCT skill)
        FROM job_skills

    """)
    result = cursor.fetchone()[0]
    return result

def get_jobs_by_skill(connection, skill):
    """Retrieves all jobs that match a specific skill (case-insensitive search).

    Args:
        connection (sqlite3.Connection): An active database connection.
        skill (str): The skill keyword to filter by.

    Returns:
        list of tuple: List of (title, company, location) matching the specified skill.
    """
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
    """Retrieves companies ordered by the number of job postings they have.

    Args:
        connection (sqlite3.Connection): An active database connection.

    Returns:
        list of tuple: A list of (company, count) tuples representing company hiring frequency.
    """
    cursor = connection.cursor()
    cursor.execute("""
        SELECT company, COUNT(*)
        FROM jobs
        GROUP BY company
        ORDER BY COUNT(*) DESC

    """)

    result = cursor.fetchall()
    return result

def export_to_csv(results, filename, header):
    """Exports structured database query results to a CSV file.

    Args:
        results (list of tuple): The database rows/results to write.
        filename (str): Target filename inside the 'results' directory.
        header (list of str): List of column headers for the CSV file.
    """
    # Create the target results directory if it does not exist
    os.makedirs("results", exist_ok=True)

    with open(f"results/{filename}", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write column headers first
        writer.writerow(header)

        # Write all data rows
        for row in results:
            writer.writerow(row)
        

