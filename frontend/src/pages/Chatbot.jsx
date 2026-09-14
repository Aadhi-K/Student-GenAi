import { useState } from "react";
import api from "../services/api";

function Chatbot() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async (event) => {
    event.preventDefault();

    if (!question.trim()) return;

    setLoading(true);
    setError("");

    try {
      const response = await api.post(
        "/chat/local",
        {
          student_id: localStorage.getItem("student_id"),
          question
        }
      );

      setAnswer(response.data.answer);
    } catch (requestError) {
      console.error(requestError);
      setError("Unable to get an answer right now.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>

      <h1>RAG Chatbot</h1>

      <form onSubmit={askQuestion}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask about your uploaded material"
        />

        <button type="submit" disabled={loading}>
          {loading ? "Thinking..." : "Ask"}
        </button>
      </form>

      {error && <p role="alert">{error}</p>}
      <p>{answer}</p>

    </div>
  );
}

export default Chatbot;