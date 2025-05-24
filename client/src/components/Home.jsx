import React, { useEffect, useRef } from "react";
import ReactSpeedometer from "react-d3-speedometer";
import { Chart } from "chart.js/auto";
import "./index.css";
const Home = () => {
  const statusData = [
    ["Clear", "Trouble", "Critical", "Clear"],
    ["Critical", "Clear", "Trouble", "Clear"],
    ["Clear", "Clear", "Clear", "Critical"],
  ];

  const getStatusColor = (status) => {
    switch (status) {
      case "Clear":
        return "#4CAF50"; // Green
      case "Trouble":
        return "#FF9800"; // Orange
      case "Critical":
        return "#F44336"; // Red
      default:
        return "#ccc";
    }
  };
  const RAMUsage = () => {
    const chartRef = useRef(null);

    useEffect(() => {
      if (chartRef.current) {
        const ctx = chartRef.current.getContext("2d");

        // Sample data for RAM usage over months
        new Chart(ctx, {
          type: "line",
          data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
            datasets: [
              {
                label: "RAM Usage",
                data: [40, 80, 60, 100, 120, 60, 40],
                fill: true,
                backgroundColor: "rgba(99, 102, 241, 0.2)",
                borderColor: "rgba(99, 102, 241, 1)",
                tension: 0.4,
              },
            ],
          },
          options: {
            responsive: true,
            scales: {
              y: {
                beginAtZero: true,
                max: 140,
                ticks: {
                  stepSize: 20,
                },
              },
            },
            plugins: {
              legend: {
                display: false,
              },
            },
          },
        });
      }
    }, []);
  };
  return (
    <div>
      <ReactSpeedometer
        maxValue={100}
        value={120}
        needleColor="red"
        startColor="green"
        segments={5}
        endColor="blue"
        height={200}
      />
      <div className="grid grid-cols-4 gap-4 p-4">
        {statusData.flatMap((row, rowIndex) =>
          row.map((status, colIndex) => (
            <div
              key={`${rowIndex}-${colIndex}`}
              className="w-16 h-16 rounded-full flex items-center justify-center text-white text-sm font-medium shadow-md"
              style={{
                backgroundColor: getStatusColor(status),
              }}
            >
              {status}
            </div>
          ))
        )}
      </div>
      <RAMUsage />
    </div>
  );
};

export default Home;
