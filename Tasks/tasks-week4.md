# Tasks

## Dependencies

- [x] Install production dependencies:

  npm install axios react-router-dom @tanstack/react-query zustand react-hook-form zod @hookform/resolvers recharts

- [x] Install dev dependencies:

  npm install -D @types/react-router-dom vitest @testing-library/react @testing-library/jest-dom

- [x] Confirm npm run build still succeeds
- [x] Commit: chore(frontend): install dependencies

---

## TypeScript types

- [x] Create src/types/index.ts
- [x] Define TypeScript interfaces for all API entities matching the DB schema:

  typescript:

  export interface User { id: string; email: string; full_name: string; }
  export interface Company { id: string; name: string; website?: string; industry?: string; notes?: string; }
  export type ApplicationStatus = 'SAVED' | 'APPLIED' | 'PHONE_SCREEN' | 'INTERVIEW' | 'OFFER' | 'ACCEPTED' | 'REJECTED' | 'WITHDRAWN'
  export interface Application { id: string; company_id: string; role_title: string; current_status: ApplicationStatus; ... }
  // ... all entities

- [x] Commit: feat(frontend): add entity type definitions

---

## API client

- [x] Create src/api/client.ts:
    - Axios instance with baseURL read from import.meta.env.VITE_API_URL
    - Request interceptor: attach Authorization: Bearer <token> header if token exists in store (store is not built yet — leave a // TODO comment)
    - Response interceptor: log errors for now (401 handling comes in Month 3)

- [x] Create src/api/auth.ts — stub functions only: login, register, logout, refresh (return Promise<void> for now)

- [x] Create src/api/applications.ts — stub: getApplications, getApplication, createApplication, updateApplication, deleteApplication

- [x] Create .env.development in frontend/:

VITE_API_URL=http://localhost:8000

- [x] Commit: feat(frontend): add axios client and api stubs

---

## Zustand auth store

- [x] Create src/store/auth.ts:

  typescript

  interface AuthState {
    user: User | null
    accessToken: string | null
    setAuth: (user: User, token: string) => void
    clearAuth: () => void
  }

- [x] Wire the Axios request interceptor to read accessToken from the store
- [x] Commit: feat(frontend): add zustand auth store

---

## React Query setup

- [x] Wrap the app in QueryClientProvider in src/main.tsx
- [x] Configure QueryClient with sensible defaults:
    - staleTime: 1000 * 60 (1 minute)
    - retry: 1
- [x] Commit: feat(frontend): configure react query provider

---

## Routing

- [x] Create src/router.tsx with createBrowserRouter
- [x] Define all routes from the spec (placeholder components for now):

  /           → redirect to /dashboard
  /login      → <Login />
  /register   → <Register />
  /dashboard  → <Dashboard />  (protected)
  /applications → <Applications />  (protected)
  /applications/:id → <ApplicationDetail />  (protected)
  /companies  → <Companies />  (protected)
  /companies/:id → <CompanyDetail />  (protected)
  /reminders  → <Reminders />  (protected)

- [x] Create stub page components in src/pages/ — each just renders an <h1> with the page name
- [x] Create src/components/ProtectedRoute.tsx — reads accessToken from store, redirects to /login if null (using useNavigate)
- [x] Wrap all protected routes in <ProtectedRoute />
- [x] Commit: feat(frontend): add routing structure and protected route

---

## Layout components

- [x] Create src/components/layout/AppShell.tsx — outer wrapper with <Outlet />
- [x] Create src/components/layout/Navbar.tsx — app title + logout button placeholder
- [x] Create src/components/layout/Sidebar.tsx — links to all protected routes
- [x] Wire layout into the router as a parent route wrapping all protected routes
- [x] Commit: feat(frontend): add layout components

---

## Hook stubs

- [x] Create src/hooks/useApplications.ts — useQuery calling getApplications, returns typed result
- [x] Create src/hooks/useAuth.ts — reads from Zustand store, exposes user, isAuthenticated
- [x] These are stubs — they won't fetch real data yet (backend auth isn't built)
- [x] Commit: feat(frontend): add react query hook stubs

---

## Quality check

- [x] Run tsc --noEmit — zero TypeScript errors
- [x] Run npx eslint src/ — zero errors
- [x] Run npm run dev — app loads, navigation between stub pages works
- [x] Navigating to a protected route without a token redirects to /login
- [x] Commit: chore(frontend): eslint and typescript clean

---

## Week 4 — Definition of Done

- [x] All routes are defined and navigable in the browser
- [x] Protected routes redirect to /login when no token is in the store
- [x] Layout renders with Navbar and Sidebar on all protected pages
- [x] TypeScript compiler passes with zero errors
- [x] ESLint passes with zero warnings
- [x] React Query provider is configured
- [x] Axios client is set up with interceptor stubs
- [x] Zustand auth store exists with correct shape