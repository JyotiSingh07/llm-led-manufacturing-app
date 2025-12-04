import { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");

  const ask = async () => {
    const res = await axios.post("http://localhost:8000/ask", {
      question,
    });
    setResponse(res.data.answer);
  };

  return (
    <div style={{ padding: 40, maxWidth: 700 }}>
      <h2>LED Manufacturing Q&A (LLM Powered)</h2>

      <textarea
        style={{ width: "100%", height: 90 }}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask LED manufacturing questions..."
      />

      <button onClick={ask} style={{ marginTop: 10, padding: 10 }}>
        Ask
      </button>

      <div style={{ marginTop: 20, padding: 15, background: "#eee" }}>
        <h3>Response:</h3>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;
