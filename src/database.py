import sqlite3
from datetime import datetime

def connect_database():
    connection = sqlite3.connect("jobs.db")
    return connection

def create_jobs_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            job_id  TEXT PRIMARY KEY,
            title  TEXT,
            company  TEXT,
            location TEXT,
            description  TEXT,
            created  TEXT,
            category  TEXT,
            redirect_url  TEXT,
            date_fetched  TEXT
        )
    """)
    connection.commit()

def insert_job(connection, job):
    job_id = job["id"]
    company = job["company"]["display_name"]
    title  = job["title"]
    location = job["location"]["display_name"]
    description = job["description"]
    created = job["created"]
    category = job["category"]["label"]
    redirect_url = job["redirect_url"]
    date_fetched  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor = connection.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO jobs (job_id, title, company, location, description, created, category, redirect_url, date_fetched)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (job_id, title, company, location, description, created, category, redirect_url, date_fetched))
    connection.commit()


def insert_jobs(connection, jobs):
    for job in jobs:
        insert_job(connection, job)


def get_all_jobs(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    return jobs


#Job Skills database design

def create_job_skills_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_skills(
            job_id TEXT,
            skill TEXT,
            date_fetched TEXT,
            PRIMARY KEY (job_id, skill)

        )
    
    """)
    connection.commit()

def insert_job_skill(connection, job_id, skill, date_fetched):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO job_skills(job_id, skill, date_fetched)
        VALUES(?,?,?)
    """, (job_id, skill, date_fetched))

    connection.commit()

def insert_job_skills(connection, job_id, skills, date_fetched):
    for skill in skills:
        insert_job_skill(connection, job_id, skill, date_fetched)