// pages/dashboard.js
import { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';

const Dashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch('/api/dashboard');
      const data = await res.json();
      setData(data);
    };
    fetchData();
  }, []);

  const chartData = {
    labels: data.map(item => item.label),
    datasets: [
      {
        label: 'Job Applications',
        data: data.map(item => item.value),
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      }
    ]
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <Bar data={chartData} />
    </div>
  );
};

export default Dashboard;
