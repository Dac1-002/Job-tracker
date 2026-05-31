import { Outlet } from "react-router-dom";

export default function AppShell() {
  return (
    <div>
      {/* Layout wrapper (navbar/sidebar will go here later) */}

      <main>
        <Outlet />
      </main>
    </div>
  );
}