import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import StudyPlan from "./pages/StudyPlan";
import MockTest from "./pages/MockTest";
import Chatbot from "./pages/Chatbot";
import GlobalLLM from "./pages/GlobalLLM";
import Analytics from "./pages/Analytics";
import UploadPDF from "./pages/UploadPDF";


function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/study-plan"
          element={<StudyPlan />}
        />

        <Route
          path="/mock-test"
          element={<MockTest />}
        />

        <Route
          path="/chatbot"
          element={<Chatbot />}
        />

        <Route
          path="/global-llm"
          element={<GlobalLLM />}
        />

        <Route
          path="/analytics"
          element={<Analytics />}
        />
        <Route
          path="/upload-pdf"
          element={<UploadPDF />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;