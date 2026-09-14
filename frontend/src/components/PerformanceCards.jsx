function PerformanceCards({ data }) {
  return (
    <div>
      <h3>Tests Taken : {data.tests_taken}</h3>
      <h3>Average Score : {data.average_score}%</h3>
      <h3>Best Score : {data.best_score}%</h3>
      <h3>Lowest Score : {data.lowest_score}%</h3>
    </div>
  );
}

export default PerformanceCards;