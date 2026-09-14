import { useState } from "react";
import api from "../services/api";

function MockTest() {

  const [subject, setSubject] = useState("");
  const [difficulty, setDifficulty] = useState("Medium");
  const [numQuestions, setNumQuestions] = useState(5);
  const [test, setTest] = useState(null);
  const [answers, setAnswers] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generateTest = async () => {

    const studentId = localStorage.getItem("student_id");

    setLoading(true);
    setError("");
    setResult(null);

    try {

      const response = await api.post(
        "/mock-test/generate",
        {
          student_id: studentId,
          subject: subject,
          difficulty: difficulty,
          num_questions: Number(numQuestions)
        }
      );

      console.log(response.data);
      setTest(response.data);
      setAnswers(Array(response.data.questions.length).fill(""));

    } catch (error) {

      console.log(error.response?.data);

      setError("Failed to generate test. Upload relevant study material first.");
    } finally {
      setLoading(false);
    }
  };

  const submitTest = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await api.post(
        "/mock-test/submit",
        {
          test_id: test.test_id,
          student_id: localStorage.getItem("student_id"),
          answers
        }
      );

      setResult(response.data);
    } catch (submitError) {
      console.error(submitError);
      setError("Failed to submit test.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Generate Mock Test</h1>

      <input
        type="text"
        placeholder="Subject"
        value={subject}
        onChange={(e) => setSubject(e.target.value)}
      />

      <br /><br />

      <select
        value={difficulty}
        onChange={(e) => setDifficulty(e.target.value)}
      >
        <option>Easy</option>
        <option>Medium</option>
        <option>Hard</option>
      </select>

      <br /><br />

      <input
        type="number"
        min="1"
        value={numQuestions}
        onChange={(e) => setNumQuestions(e.target.value)}
      />

      <br /><br />

      <button onClick={generateTest} disabled={loading}>
        {loading ? "Generating..." : "Generate Test"}
      </button>

      {error && <p role="alert">{error}</p>}

        {test && (
          <section>
            <h2>{test.subject} Practice Test</h2>
            <p>{test.questions.length} questions | {test.difficulty} difficulty</p>

            {test.questions.map((question, index) => (
              <fieldset key={`${question.question}-${index}`}>
                <legend>{index + 1}. {question.question}</legend>
                {question.options.map((option) => (
                  <label key={option}>
                    <input
                      type="radio"
                      name={`question-${index}`}
                      value={option}
                      checked={answers[index] === option}
                      onChange={() => {
                        const nextAnswers = [...answers];
                        nextAnswers[index] = option;
                        setAnswers(nextAnswers);
                      }}
                    />
                    {option}
                  </label>
                ))}
              </fieldset>
            ))}

            <br />

            {!result && (
              <button onClick={submitTest} disabled={loading}>
                {loading ? "Submitting..." : "Submit Test"}
              </button>
            )}

            {result && (
              <div>
                <h2>Test complete</h2>
                <p>You scored {result.score} out of {result.total} ({result.percentage}%).</p>
                <p>Weak topics found: {result.weak_topics?.length || 0}</p>
              </div>
            )}
          </section>
        )}
    </div>
  );
}

export default MockTest;