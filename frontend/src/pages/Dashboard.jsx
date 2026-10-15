import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const navigate = useNavigate();
  const username = localStorage.getItem("username");
  const studentId = localStorage.getItem("student_id");

  const handleLogout = () => {
    localStorage.removeItem("username");
    localStorage.removeItem("student_id");
    navigate("/");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Welcome, {username}</h1>

      <h3>Student ID: {studentId}</h3>

      <h2>Quick Actions</h2>
      <div
      style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, minmax(0, 1fr))",
          gap: "20px",
          marginTop: "20px",
          width: "100%",
        }}
      >
        {/* PDF Upload */}
        <Link to="/upload-pdf">
          <button style={{ width: "100%", height: "60px" }}>
            Upload Study Material
          </button>
        </Link>

        {/* Mock Test */}
        <Link to="/mock-test">
          <button style={{ width: "100%", height: "60px" }}>
            Start Mock Test
          </button>
        </Link>

        {/* Study Plan */}
        <Link to="/study-plan">
          <button style={{ width: "100%", height: "60px" }}>
             Generate Study Plan
          </button>
        </Link>

        {/* RAG Chatbot */}
        <Link to="/chatbot">
          <button style={{ width: "100%", height: "60px" }}>
             RAG Chatbot
          </button>
        </Link>

        {/* Global LLM */}
        <Link to="/global-llm">
          <button style={{ width: "100%", height: "60px" }}>
             Global LLM
          </button>
        </Link>

        {/* Analytics */}
        <Link to="/analytics">
          <button style={{ width: "100%", height: "60px" }}>
            View Analytics
          </button>
        </Link>
      </div>
      {/* Logout aligned to the right */}
      <div
        style={{
          display: "flex",
          paddingBottom: "50px",
          marginTop: "50px",
        }}
      >
        <button onClick={handleLogout}>Logout</button>
      </div>
    </div>
  );
}

export default Dashboard;