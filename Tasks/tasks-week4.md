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

- [ ] Create src/api/client.ts:
    - Axios instance with baseURL read from import.meta.env.VITE_API_URL
    - Request interceptor: attach Authorization: Bearer <token> header if token exists in store (store is not built yet — leave a // TODO comment)
    - Response interceptor: log errors for now (401 handling comes in Month 3)

- [ ] Create src/api/auth.ts — stub functions only: login, register, logout, refresh (return Promise<void> for now)

- [ ] Create src/api/applications.ts — stub: getApplications, getApplication, createApplication, updateApplication, deleteApplication

- [ ] Create .env.development in frontend/:

VITE_API_URL=http://localhost:8000

- [ ] Commit: feat(frontend): add axios client and api stubs

---

## Zustand auth store

- [ ] Create src/store/auth.ts:

  typescript

  interface AuthState {
    user: User | null
    accessToken: string | null
    setAuth: (user: User, token: string) => void
    clearAuth: () => void
  }

- [ ] Wire the Axios request interceptor to read accessToken from the store
- [ ] Commit: feat(frontend): add zustand auth store

---

## React Query setup

- [ ] Wrap the app in QueryClientProvider in src/main.tsx
- [ ] Configure QueryClient with sensible defaults:
    - staleTime: 1000 * 60 (1 minute)
    - retry: 1
- [ ] Commit: feat(frontend): configure react query provider

---

## Routing

- [ ] Create src/router.tsx with createBrowserRouter
- [ ] Define all routes from the spec (placeholder components for now):

  /           → redirect to /dashboard
  /login      → <Login />
  /register   → <Register />
  /dashboard  → <Dashboard />  (protected)
  /applications → <Applications />  (protected)
  /applications/:id → <ApplicationDetail />  (protected)
  /companies  → <Companies />  (protected)
  /companies/:id → <CompanyDetail />  (protected)
  /reminders  → <Reminders />  (protected)

- [ ] Create stub page components in src/pages/ — each just renders an <h1> with the page name
- [ ] Create src/components/ProtectedRoute.tsx — reads accessToken from store, redirects to /login if null (using useNavigate)
- [ ] Wrap all protected routes in <ProtectedRoute />
- [ ] Commit: feat(frontend): add routing structure and protected route

---

## Layout components

- [ ] Create src/components/layout/AppShell.tsx — outer wrapper with <Outlet />
- [ ] Create src/components/layout/Navbar.tsx — app title + logout button placeholder
- [ ] Create src/components/layout/Sidebar.tsx — links to all protected routes
- [ ] Wire layout into the router as a parent route wrapping all protected routes
- [ ] Commit: feat(frontend): add layout components

---

## Hook stubs

- [ ] Create src/hooks/useApplications.ts — useQuery calling getApplications, returns typed result
- [ ] Create src/hooks/useAuth.ts — reads from Zustand store, exposes user, isAuthenticated
- [ ] These are stubs — they won't fetch real data yet (backend auth isn't built)
- [ ] Commit: feat(frontend): add react query hook stubs

---

## Quality check

- [ ] Run tsc --noEmit — zero TypeScript errors
- [ ] Run npx eslint src/ — zero errors
- [ ] Run npm run dev — app loads, navigation between stub pages works
- [ ] Navigating to a protected route without a token redirects to /login
- [ ] Commit: chore(frontend): eslint and typescript clean

---

## Week 4 — Definition of Done

- [ ] All routes are defined and navigable in the browser
- [ ] Protected routes redirect to /login when no token is in the store
- [ ] Layout renders with Navbar and Sidebar on all protected pages
- [ ] TypeScript compiler passes with zero errors
- [ ] ESLint passes with zero warnings
- [ ] React Query provider is configured
- [ ] Axios client is set up with interceptor stubs
- [ ] Zustand auth store exists with correct shape