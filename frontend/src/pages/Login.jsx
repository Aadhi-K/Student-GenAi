import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [studentId, setStudentId] = useState("");
  const [username, setUsername] = useState("");
  const [isRegistering, setIsRegistering] = useState(false);
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      const response = await api.post(
        isRegistering ? "/auth/register" : "/auth/login",
        isRegistering
          ? { student_id: studentId, username, email, password }
          : { email, password }
      );

      if (isRegistering) {
        setMessage(response.data.msg);
        setIsRegistering(false);
        return;
      }

      if (!response.data.student_id) {
        setMessage(response.data.msg || "Login failed");
        return;
      }

      localStorage.setItem(
        "student_id",
        response.data.student_id
      );

      localStorage.setItem(
        "username",
        response.data.username
      );

      navigate("/dashboard");
    } catch (error) {
      console.error(error);
      setMessage(isRegistering ? "Registration failed" : "Login failed");
    }
  };

  return (
    <div style={{ padding: "50px" }}>
      <h1>{isRegistering ? "Create Student Account" : "Student Login"}</h1>

      <form onSubmit={handleLogin}>
        {isRegistering && (
          <>
            <input
              placeholder="Student ID"
              value={studentId}
              onChange={(e) => setStudentId(e.target.value)}
              required
            />

            <br />
            <br />

            <input
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />

            <br />
            <br />
          </>
        )}

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
          required
        />

        <br />
        <br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <br />
        <br />

        <button type="submit">
          {isRegistering ? "Register" : "Login"}
        </button>
      </form>

      {message && <p role="alert">{message}</p>}

      <button
        type="button"
        onClick={() => {
          setIsRegistering(!isRegistering);
          setMessage("");
        }}
      >
        {isRegistering ? "Back to login" : "Create an account"}
      </button>
    </div>
  );
}

export default Login;