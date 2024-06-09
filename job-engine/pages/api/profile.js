// pages/api/profile.js
import axios from 'axios';

export default async function handler(req, res) {
  const { email } = req.query;
  const response = await axios.get(`http://localhost:8080/v1/objects/${email}`);
  res.status(200).json(response.data.properties);
}

