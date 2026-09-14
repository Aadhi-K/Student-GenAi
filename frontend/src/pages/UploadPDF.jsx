import { useState } from "react";
import api from "../services/api";

function UploadPDF() {

  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadPDF = async () => {
    if (!file) {
      setMessage("Choose a PDF before uploading.");
      return;
    }

    setLoading(true);
    setMessage("");

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    formData.append(
      "student_id",
      localStorage.getItem("student_id")
    );

    try {
      const response = await api.post(
        "/pdf/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );
      setMessage(response.data.message);
    } catch (error) {
      console.error(error);
      setMessage("PDF upload failed. Check that the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>

      <h1>Upload Study Material</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      <button onClick={uploadPDF} disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>

      {message && <p role="status">{message}</p>}

    </div>
  );
}

export default UploadPDF;