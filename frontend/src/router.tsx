import { createBrowserRouter, Navigate } from "react-router-dom";
import AppShell from "./components/layout/AppShell";
import ProtectedRoute from "./components/ProtectedRoute";

// Pages
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Applications from "./pages/Applications";
import ApplicationDetail from "./pages/ApplicationDetail";
import Companies from "./pages/Companies";
import CompanyDetail from "./pages/CompanyDetail";
import Reminders from "./pages/Reminders";

export const router = createBrowserRouter([
  // PUBLIC ROUTES (no layout)
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/register",
    element: <Register />,
  },

  // PROTECTED APP (with layout)
  {
    path: "/",
    element: (
      <ProtectedRoute>
        <AppShell />
      </ProtectedRoute>
    ),
    children: [
      {
        index: true,
        element: <Navigate to="/dashboard" replace />,
      },
      {
        path: "dashboard",
        element: <Dashboard />,
      },
      {
        path: "applications",
        element: <Applications />,
      },
      {
        path: "applications/:id",
        element: <ApplicationDetail />,
      },
      {
        path: "companies",
        element: <Companies />,
      },
      {
        path: "companies/:id",
        element: <CompanyDetail />,
      },
      {
        path: "reminders",
        element: <Reminders />,
      },
    ],
  },
]);