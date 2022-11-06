import requests
import boto3
import json

job_API = 'https://www.arbeitnow.com/api/job-board-api'

s3_client = boto3.client("s3")

def get_job_data():
    print("start getting data")
    response = requests.get(job_API)
    get_data = response.json()["data"]
    return get_data

def job_data(get_data):
    result = [0]
    for job in get_data["data "]:
        
        Job_tamplate = ({
            "id": job["slug"],
            "title": job["title"],
            "description": job["description"]
            
        })


def save_job_data(jobs):
    for job in jobs:

         job_template = ({
            "id": job["slug"],
            "title": job["title"],
            "description": job["description"]
            
        })
        
    job_template_json = json.dumps(job_template)

    s3_client.upload_file('/learningtask','lambda101jay', job_template)

        
    

def handle(event, context):
    return job_data()

    


    




