import { useState } from "react";
import api from "../services/api";

function StudyPlan() {

  const [subject, setSubject] = useState("");
  const [days, setDays] = useState(7);

  const [plan, setPlan] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const generatePlan = async () => {
    const studentId = localStorage.getItem("student_id");
    if (!subject.trim()) return;

    setLoading(true);
    setError("");

    try {

      const response = await api.post(
        "/study-plan/generate",
        {
          student_id: studentId,
          subject: subject,
          days: Number(days)
        }
      );

      const generatedPlan = response.data.study_plan;
      setPlan(
        typeof generatedPlan === "string"
          ? generatedPlan
          : JSON.stringify(generatedPlan, null, 2)
      );

    } catch (requestError) {

      console.error(requestError);

      setError("Failed to generate plan. Upload relevant study material first.");
    } finally {
      setLoading(false);

    }
  };

  return (
    <div style={{ padding: "20px" }}>

      <h2>Generate Study Plan</h2>

      <input
        placeholder="Subject Name"
        value={subject}
        onChange={(e) => setSubject(e.target.value)}
      />

      <br /><br />

      <input
        type="number"
        value={days}
        onChange={(e) => setDays(e.target.value)}
      />

      <br /><br />

      <button onClick={generatePlan} disabled={loading}>
        {loading ? "Generating..." : "Generate Study Plan"}
      </button>

      {error && <p role="alert">{error}</p>}

      <br /><br />

      <textarea
        rows="20"
        cols="100"
        value={plan}
        readOnly
      />

    </div>
  );
}

export default StudyPlan;