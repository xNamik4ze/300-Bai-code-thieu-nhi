// ColorBox.js
function ColorBox({ color }) {
  return (
    <div
      style={{
        width: "200px",
        height: "100px",
        backgroundColor: color,
        marginTop: "10px",
      }}
    />
  );
}
export default ColorBox;

// ColorApp.js
import { useState } from "react";
import ColorBox from "./ColorBox";

function ColorApp() {
  const [color, setColor] = useState("white");
  const colors = ["red", "green", "blue", "yellow"];

  return (
    <div>
      {colors.map((c) => (
        <button key={c} onClick={() => setColor(c)}>
          {c}
        </button>
      ))}
      <ColorBox color={color} />
    </div>
  );
}
export default ColorApp;
