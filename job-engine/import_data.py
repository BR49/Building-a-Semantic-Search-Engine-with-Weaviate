import requests
import pandas as pd

# Load datasets
job_df = pd.read_csv('linkedin_job_postings.csv')
user_df = pd.read_csv('user_profiles.csv')

# Weaviate URL
weaviate_url = "http://localhost:8080/v1/objects"

# Function to import job data
def import_job_data(row):
    data = {
        "class": "JobPosting",
        "properties": {
            "title": row['title'],
            "company": row['company'],
            "location": row['location'],
            "description": row['description'],
            "postedDate": row['postedDate']
        }
    }
    response = requests.post(weaviate_url, json=data)
    return response

# Function to import user data
def import_user_data(row):
    data = {
        "class": "UserProfile",
        "properties": {
            "name": row['name'],
            "email": row['email'],
            "skills": row['skills'].split(','),
            "experience": row['experience'],
            "preferences": row['preferences'].split(',')
        }
    }
    response = requests.post(weaviate_url, json=data)
    return response

# Import data
for index, row in job_df.iterrows():
    import_job_data(row)

for index, row in user_df.iterrows():
    import_user_data(row)
