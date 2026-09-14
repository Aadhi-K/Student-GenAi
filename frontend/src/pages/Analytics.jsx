import { useEffect, useState } from "react";
import api from "../services/api";

function Analytics() {

  const [performance, setPerformance] = useState(null);
  const [error, setError] = useState("");

  const studentId =
    localStorage.getItem("student_id");

  useEffect(() => {

    api.get(`/assessment/performance/${studentId}`)
      .then((res) => setPerformance(res.data))
      .catch((requestError) => {
        console.error(requestError);
        setError("Unable to load performance analytics.");
      });

  }, [studentId]);

  if (error) {
    return <p role="alert">{error}</p>;
  }

  if (
    performance &&
    performance.message
  ) {
    return (
      <h2>No Test History Found</h2>
    );
  }

  return (

    <div>

      <h1>Performance Analytics</h1>

      {
        performance &&
        <>
          <h3>
            Tests Taken :
            {performance.tests_taken}
          </h3>

          <h3>
            Average Score :
            {performance.average_score}
          </h3>

          <h3>
            Best Score :
            {performance.best_score}
          </h3>

          <h3>
            Lowest Score :
            {performance.lowest_score}
          </h3>
        </>
      }

    </div>
  );
}

export default Analytics;