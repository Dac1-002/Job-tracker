export default function Navbar() {
  return (
    <nav style={{ display: "flex", justifyContent: "space-between", padding: "10px" }}>
      {/* App title */}
      <h2>Job Tracker</h2>

      {/* Logout button placeholder */}
      <button onClick={() => console.log("logout clicked")}>
        Logout
      </button>
    </nav>
  );
}