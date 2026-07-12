import { create } from "zustand";
import { persist } from "zustand/middleware";

const useAuthStore = create(
  persist(
    (set) => ({
      accessToken: null,
      refreshToken: null,
      user: null,

      login: (tokens) =>
        set({
          accessToken: tokens.access,
          refreshToken: tokens.refresh,
        }),

      logout: () =>
        set({
          accessToken: null,
          refreshToken: null,
          user: null,
        }),

      setUser: (user) =>
        set({
          user,
        }),
    }),
    {
      name: "intellidocs-auth",
    }
  )
);

export default useAuthStore;