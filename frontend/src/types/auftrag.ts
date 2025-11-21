/**
 * Auftrag Types (Vorbereitung für spätere Features)
 */

export enum AuftragTyp {
  FEUERSTAETTENSCHAU = 'FEUERSTAETTENSCHAU',
  KEHRUNG = 'KEHRUNG',
  ENERGIEBERATUNG = 'ENERGIEBERATUNG',
  SONSTIGE = 'SONSTIGE',
}

export enum AuftragStatus {
  GEPLANT = 'GEPLANT',
  IN_BEARBEITUNG = 'IN_BEARBEITUNG',
  ABGESCHLOSSEN = 'ABGESCHLOSSEN',
  BERICHT_ERSTELLT = 'BERICHT_ERSTELLT',
}

export enum MangelKategorie {
  KRITISCH = 'KRITISCH',
  UNKRITISCH = 'UNKRITISCH',
  HINWEIS = 'HINWEIS',
}

export interface Kunde {
  id: string
  name: string
  firma?: string
  strasse: string
  plz: string
  ort: string
  telefon?: string
  email?: string
  notizen?: string
}

export interface Mangel {
  id: string
  objekt: string
  beschreibung: string
  kategorie: MangelKategorie
  massnahme?: string
  frist?: string
  fotos?: Foto[]
  created_at: string
}

export interface Foto {
  id: string
  datei: string
  thumbnail?: string
  beschreibung?: string
  mangel?: string
  created_at: string
}

export interface Auftrag {
  id: string
  kunde: Kunde
  mitarbeiter?: {
    id: string
    first_name: string
    last_name: string
  }
  typ: AuftragTyp
  status: AuftragStatus
  datum: string
  objektadresse?: string
  notizen?: string
  maengel?: Mangel[]
  fotos?: Foto[]
  created_at: string
  updated_at: string
}

