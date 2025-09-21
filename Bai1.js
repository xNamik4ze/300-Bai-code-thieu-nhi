// CounterDisplay.js
function CounterDisplay({ value }) {
  return <h2>Giá trị hiện tại: {value}</h2>;
}
export default CounterDisplay;

// CounterApp.js
import { useState } from "react";
import CounterDisplay from "./CounterDisplay";

function CounterApp() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <CounterDisplay value={count} />
      <button onClick={() => setCount(count - 1)}>-</button>
      <button onClick={() => setCount(count + 1)}>+</button>
    </div>
  );
}
export default CounterApp;
