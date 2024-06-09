from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Vectorize job descriptions and user skills
vectorizer = TfidfVectorizer(stop_words='english')
job_descriptions = job_df['description'].tolist()
user_skills = user_df['skills'].apply(lambda x: ' '.join(x.split(','))).tolist()

job_vectors = vectorizer.fit_transform(job_descriptions)
user_vectors = vectorizer.transform(user_skills)

# Compute similarity
similarity_matrix = cosine_similarity(user_vectors, job_vectors)

# Get top N recommendations for each user
top_n = 5
recommendations = {}

for i, user in user_df.iterrows():
    similar_jobs = np.argsort(similarity_matrix[i])[::-1][:top_n]
    recommendations[user['email']] = job_df.iloc[similar_jobs][['title', 'company', 'location']].to_dict('records')


def store_recommendations(email, recs):
    for rec in recs:
        data = {
            "class": "UserProfile",
            "id": email,
            "properties": {
                "recommendations": recs
            }
        }
        response = requests.post(f"{weaviate_url}/{email}", json=data)
        return response

for email, recs in recommendations.items():
    store_recommendations(email, recs)

