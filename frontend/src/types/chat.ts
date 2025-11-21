/**
 * Chat Types (Vorbereitung für spätere Features)
 */

export enum MessageType {
  TEXT = 'TEXT',
  AUDIO = 'AUDIO',
  PHOTO = 'PHOTO',
  SYSTEM = 'SYSTEM',
}

export interface ChatMessage {
  id: string
  sender?: {
    id: string
    first_name: string
    last_name: string
  }
  message: string
  message_type: MessageType
  ai_extraction?: Record<string, any>
  created_at: string
}

