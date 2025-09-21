// StudentCard.js
import { useState } from "react";

function StudentCard({ name, age, className }) {
  const [showDetail, setShowDetail] = useState(false);

  return (
    <div style={{ border: "1px solid #ccc", padding: 10, margin: 10 }}>
      <h3>{name}</h3>
      <button onClick={() => setShowDetail(!showDetail)}>
        {showDetail ? "Ẩn chi tiết" : "Xem chi tiết"}
      </button>
      {showDetail && (
        <p>
          Tuổi: {age} - Lớp: {className}
        </p>
      )}
    </div>
  );
}
export default StudentCard;

// StudentApp.js
import StudentCard from "./StudentCard";

function StudentApp() {
  const students = [
    { name: "Nguyễn Văn A", age: 20, className: "D24CNPM1" },
    { name: "Trần Thị B", age: 21, className: "D24CNPM2" },
    { name: "Lê Văn C", age: 22, className: "D24CNPM3" },
  ];

  return (
    <div>
      {students.map((s, index) => (
        <StudentCard
          key={index}
          name={s.name}
          age={s.age}
          className={s.className}
        />
      ))}
    </div>
  );
}
export default StudentApp;
