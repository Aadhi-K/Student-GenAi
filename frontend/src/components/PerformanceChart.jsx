import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

function PerformanceChart({ data }) {
  return (
    <BarChart width={500} height={300} data={data}>
      <XAxis dataKey="subject" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="score" />
    </BarChart>
  );
}

export default PerformanceChart;