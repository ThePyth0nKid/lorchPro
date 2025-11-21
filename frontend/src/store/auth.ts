/**
 * Zustand Auth Store
 * Verwaltet Authentifizierungsstatus und User-Daten
 */

import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { User } from '@/types/user'
import api from '@/lib/api'

interface AuthState {
  user: User | null
  isAuthenticated: boolean
  isLoading: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => void
  fetchUser: () => Promise<void>
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      isAuthenticated: false,
      isLoading: false,

      /**
       * Login mit Email und Passwort
       */
      login: async (email: string, password: string) => {
        set({ isLoading: true })
        try {
          // JWT-Token anfordern
          const response = await api.post('/token/', { email, password })
          const { access, refresh } = response.data

          // Tokens im LocalStorage speichern
          if (typeof window !== 'undefined') {
            localStorage.setItem('access_token', access)
            localStorage.setItem('refresh_token', refresh)
          }

          // User-Daten abrufen
          await useAuthStore.getState().fetchUser()

          set({ isAuthenticated: true, isLoading: false })
        } catch (error) {
          set({ isLoading: false })
          throw error
        }
      },

      /**
       * Logout: Tokens entfernen und State zurücksetzen
       */
      logout: () => {
        if (typeof window !== 'undefined') {
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
        }
        set({ user: null, isAuthenticated: false })
      },

      /**
       * Aktuellen User von API abrufen
       */
      fetchUser: async () => {
        try {
          const response = await api.get('/users/me/')
          set({
            user: response.data,
            isAuthenticated: true,
          })
        } catch (error) {
          set({
            user: null,
            isAuthenticated: false,
          })
          throw error
        }
      },
    }),
    {
      name: 'auth-storage',
      partialize: (state) => ({
        user: state.user,
      }),
    }
  )
)

