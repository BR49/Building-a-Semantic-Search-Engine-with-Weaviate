# Job Recommendation System

This project extends a job recommendation system using Weaviate and a machine learning model for enhanced recommendations. 
The front end is built with Next.js and Tailwind CSS, and data visualizations are created using Chart.js. The project also includes a data pipeline using Apache Airflow.

## Features

- Job postings stored and queried from Weaviate
- User-specific job recommendations using a custom machine learning model
- Real-time data visualizations using Chart.js
- Dynamic user profile and dashboard pages
- Automated data pipeline with Apache Airflow

## Setup

### Prerequisites

- Docker
- Node.js
- Python

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/BR49/Building-a-Semantic-Search-Engine-with-Weaviate.git
   
   cd job-engine

Weaviate Setup
Start Weaviate with Docker:
```sh
docker-compose down
```

Import Job Postings Data:

Ensure you have a dataset (e.g., linkedin_job_postings.csv).
Run the data import script:

```sh
pip install weaviate-client pandas
python import.py
```












