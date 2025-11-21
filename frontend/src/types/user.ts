/**
 * User Types
 */

export enum UserRole {
  ADMIN = 'ADMIN',
  AUSSENDIENST = 'AUSSENDIENST',
  BUERO = 'BUERO',
}

export interface User {
  id: string
  email: string
  username: string
  first_name: string
  last_name: string
  rolle: UserRole
  telefon?: string
  is_active: boolean
  is_staff: boolean
  created_at: string
  updated_at: string
}

export interface APIKey {
  id: string
  name: string
  key: string
  created_at: string
  expires_at?: string
  last_used_at?: string
}

