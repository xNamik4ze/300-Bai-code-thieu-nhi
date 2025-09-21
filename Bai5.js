// TimeDisplay.js
function TimeDisplay({ time }) {
  return <h2>{time}</h2>;
}
export default TimeDisplay;

// Clock.js
import { useEffect, useState } from "react";
import TimeDisplay from "./TimeDisplay";

function Clock() {
  const [time, setTime] = useState(new Date().toLocaleTimeString());

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return <TimeDisplay time={time} />;
}
export default Clock;
