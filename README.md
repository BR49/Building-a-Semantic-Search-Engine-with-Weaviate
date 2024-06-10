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
python import_data.py
```

Machine Learning Model

Implement the recommendation algorithm:
Ensure recommendation.py is correctly configured.

Front-End Setup
Install Node.js dependencies:

```sh
npm install
```

Run the Next.js development server:

```sh
npm run dev
```


### Data Pipeline Setup (Optional)

1. **Install Apache Airflow**:
- Follow the [Apache Airflow installation guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html).

2. **Trigger the Airflow DAG**:


## Usage

- **Access the Application**:
- Open your browser and go to `http://localhost:3000`.

- **Navigate to the Profile Page**:
- View user details and job recommendations.

- **Dashboard**:
- Check real-time data visualizations.

- **Get Job Recommendations**:
- Based on user skills, receive personalized job suggestions.

## Project Structure
.
├── components
│   └── BarChart.js
├── pages
│   ├── api
│   │   ├── recommendations.js
│   │   ├── profile.js
│   │   └── dashboard.js
│   ├── dashboard.js
│   └── profile.js
├── public
│   └── ...
├── styles
│   └── globals.css
├── airflow_dag.py
├── docker-compose.yml
├── import_data.py
├── recommendation.py
└── README.md


## API Endpoints

- **Profile API**: `/api/profile`
  - Retrieves user profile information.
- **Recommendations API**: `/api/recommendations`
  - Provides job recommendations based on user skills.
- **Dashboard API**: `/api/dashboard`
  - Fetches aggregated job posting data for visualizations.


## Acknowledgements

- [Weaviate](https://weaviate.io/)
- [Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Chart.js](https://www.chartjs.org/)
- [Apache Airflow](https://airflow.apache.org/)













