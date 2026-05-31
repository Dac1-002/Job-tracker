import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside style={{ padding: "10px", width: "200px" }}>
      <h3>Menu</h3>

      <nav style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/applications">Applications</Link>
        <Link to="/companies">Companies</Link>
        <Link to="/reminders">Reminders</Link>
      </nav>
    </aside>
  );
}