from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests
import pandas as pd

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('update_job_postings', default_args=default_args, schedule_interval='@daily')

def update_job_postings():
    job_df = pd.read_csv('linkedin_job_postings.csv')
    weaviate_url = "http://localhost:8080/v1/objects"
    
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
    
    for index, row in job_df.iterrows():
        import_job_data(row)

update_task = PythonOperator(task_id='update_job_postings', python_callable=update_job_postings, dag=dag)
