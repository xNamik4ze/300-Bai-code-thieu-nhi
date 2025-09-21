// TaskItem.js
function TaskItem({ text }) {
  return <li>{text}</li>;
}
export default TaskItem;

// TodoApp.js
import { useState } from "react";
import TaskItem from "./TaskItem";

function TodoApp() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState("");

  const addTask = () => {
    if (input.trim() !== "") {
      setTasks([...tasks, input]);
      setInput("");
    }
  };

  return (
    <div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Nhập công việc"
      />
      <button onClick={addTask}>Thêm</button>
      <ul>
        {tasks.map((task, index) => (
          <TaskItem key={index} text={task} />
        ))}
      </ul>
    </div>
  );
}
export default TodoApp;
