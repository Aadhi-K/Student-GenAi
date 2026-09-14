import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div>
      <Link to="/dashboard">Dashboard</Link> |
      <Link to="/study-plan">Study Plan</Link> |
      <Link to="/mock-test">Mock Test</Link> |
      <Link to="/chatbot">Chatbot</Link> |
      <Link to="/global-llm">Global LLM</Link> |
      <Link to="/analytics">Analytics</Link>
    </div>
  );
}

export default Navbar;