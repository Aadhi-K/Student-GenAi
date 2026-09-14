import { useState } from "react";
import api from "../services/api";

function GlobalLLM() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const askGlobal = async (event) => {
    event.preventDefault();

    if (!question.trim()) return;

    setLoading(true);
    setError("");

    try {
      const response = await api.post(
        "/tutor/ask",
        { question }
      );

      setAnswer(response.data.answer);
    } catch (requestError) {
      console.error(requestError);
      setError("Unable to reach the global assistant right now.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>

      <h1>Global AI Assistant</h1>

      <form onSubmit={askGlobal}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a general study question"
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

export default GlobalLLM;