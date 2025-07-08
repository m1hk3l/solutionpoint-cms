
import ReactDOM from "react-dom/client";

const Test = () => {
  return (
    <div style={{ color: "red", fontSize: "2rem", textAlign: "center" }}>
      Test
    </div>
  );
};

const rootEl = document.getElementById("test");
if (rootEl){
    const root = ReactDOM.createRoot(rootEl)
    root.render(<Test />)
}