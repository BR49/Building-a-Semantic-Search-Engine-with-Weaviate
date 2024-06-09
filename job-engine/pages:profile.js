// pages/profile.js
import { useState, useEffect } from 'react';

const Profile = ({ email }) => {
  const [profile, setProfile] = useState({});
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const fetchProfile = async () => {
      const res = await fetch(`/api/profile?email=${email}`);
      const data = await res.json();
      setProfile(data);
    };
    fetchProfile();
  }, [email]);

  useEffect(() => {
    const fetchRecommendations = async () => {
      const res = await fetch(`/api/recommendations?email=${email}`);
      const data = await res.json();
      setRecommendations(data);
    };
    fetchRecommendations();
  }, [email]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">User Profile</h1>
      <p><strong>Name:</strong> {profile.name}</p>
      <p><strong>Email:</strong> {profile.email}</p>
      <p><strong>Skills:</strong> {profile.skills?.join(', ')}</p>
      <p><strong>Experience:</strong> {profile.experience}</p>
      <p><strong>Preferences:</strong> {profile.preferences?.join(', ')}</p>
      <h2 className="text-xl font-bold mt-4">Recommended Jobs</h2>
      <ul className="mt-4">
        {recommendations.map((job, index) => (
          <li key={index} className="border-b p-2">
            <h3 className="font-bold">{job.title}</h3>
            <p>{job.company}</p>
            <p>{job.location}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Profile;
