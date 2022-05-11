import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
// import faker from 'faker';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    // title: {
    //   display: true,
    //   text: 'Chart.js Bar Chart',
    // },
  },
};

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

export const data = {
  labels,
  datasets: [
    {
      label: 'Steps completed per month',
      data: [100,500,300,200,900,100,250],//labels.map(() => 300),
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
    },
//     {
//       label: 'Dataset 2',
//       data: [200,900,600,250,800,500,300],//labels.map(() => 500),
//       backgroundColor: 'rgba(53, 162, 235, 0.5)',
//     },
  ],
};

export function BarChart() {
  return <Bar options={options} data={data} />;
}
