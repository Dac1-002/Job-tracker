import { useAuthStore } from "../store/auth";

export function useAuth() {
  const user = useAuthStore((state) => state.user);
  const accessToken = useAuthStore((state) => state.accessToken);
  const setAuth = useAuthStore((state) => state.setAuth);
  const clearAuth = useAuthStore((state) => state.clearAuth);

  return {
    user,
    accessToken,
    setAuth,
    clearAuth,
    isAuthenticated: !!accessToken,
  };
}