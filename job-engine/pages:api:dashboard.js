// pages/api/dashboard.js
import axios from 'axios';

export default async function handler(req, res) {
  const response = await axios.get('http://localhost:8080/v1/graphql', {
    query: `
      {
        Aggregate {
          JobPosting {
            meta {
              count
            }
          }
        }
      }
    `,
  });
  res.status(200).json(response.data.data.Aggregate.JobPosting);
}
