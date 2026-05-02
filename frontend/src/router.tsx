import { createBrowserRouter, Navigate } from "react-router-dom";
import App from "./App";
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
  {
    path: "/",
    element: <App />,
    children: [
      // redirect /
      {
        index: true,
        element: <Navigate to="/dashboard" replace />,
      },

      // public routes
      {
        path: "login",
        element: <Login />,
      },
      {
        path: "register",
        element: <Register />,
      },

      // protected routes
      {
        path: "dashboard",
        element: (
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        ),
      },
      {
        path: "applications",
        element: (
          <ProtectedRoute>
            <Applications />
          </ProtectedRoute>
        ),
      },
      {
        path: "applications/:id",
        element: (
          <ProtectedRoute>
            <ApplicationDetail />
          </ProtectedRoute>
        ),
      },
      {
        path: "companies",
        element: (
          <ProtectedRoute>
            <Companies />
          </ProtectedRoute>
        ),
      },
      {
        path: "companies/:id",
        element: (
          <ProtectedRoute>
            <CompanyDetail />
          </ProtectedRoute>
        ),
      },
      {
        path: "reminders",
        element: (
          <ProtectedRoute>
            <Reminders />
          </ProtectedRoute>
        ),
      },
    ],
  },
]);