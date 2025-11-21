# lorchPro

AI-First Projektmanagement-Software für Schornsteinfeger und Energieberater mit Chat-Interface.

## Tech Stack

### Backend
- **Framework**: Django 5.0+ mit Django REST Framework
- **Sprache**: Python 3.12
- **Datenbank**: PostgreSQL 16
- **Cache**: Redis 7
- **Async/Realtime**: Django Channels (WebSockets)
- **Tasks**: Celery
- **AI**: Azure OpenAI Service (GPT-4o, Whisper, Vision)

### Frontend
- **Framework**: Next.js 14.2+ (App Router)
- **Sprache**: TypeScript
- **Styling**: Tailwind CSS v4
- **UI Components**: shadcn/ui (Radix UI)
- **State Management**: Zustand
- **HTTP Client**: Axios

### Infrastructure
- **Containerization**: Docker + Docker Compose
- **Deployment**: Railway
- **API Documentation**: OpenAPI 3.0 (drf-spectacular)

## Entwicklungsmodi

### Vollständig gedockert
Alle Services (Backend, Frontend, DBs) laufen in Docker:
```bash
docker-compose up --build
```

### Hybrid-Modus (schnellere Frontend-Entwicklung)
Backend + DBs in Docker, Frontend lokal:
```bash
# Terminal 1: Backend-Services
docker-compose -f docker-compose.dev.yml up

# Terminal 2: Frontend
cd frontend
npm install
npm run dev
```

## Setup-Anleitung

### Voraussetzungen
- Docker Desktop installiert
- Node.js 20+ (für Hybrid-Modus)
- Python 3.12+ (optional, für lokale Entwicklung)

### Erste Schritte

1. **Environment-Variablen konfigurieren**
   ```bash
   cp .env.example .env
   # Editiere .env und fülle deine Werte ein
   ```

2. **Services starten**
   ```bash
   docker-compose up --build
   ```

3. **Migrations ausführen**
   ```bash
   docker-compose exec backend python manage.py migrate
   ```

4. **Superuser erstellen**
   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

5. **Zugriff**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api/
   - API Dokumentation: http://localhost:8000/api/docs/
   - Django Admin: http://localhost:8000/admin

## API-Schnittstellen

Die API unterstützt zwei Authentifizierungsmethoden:
- **JWT** (für Frontend)
- **API-Keys** (für externe Programme)

Vollständige API-Dokumentation verfügbar unter `/api/docs/` (Swagger UI) und `/api/redoc/` (ReDoc).

## Projektstruktur

```
lorchPro/
├── backend/           # Django Backend
│   ├── core/          # Projekt-Settings
│   ├── apps/          # Django-Apps
│   └── requirements/  # Python-Dependencies
├── frontend/          # Next.js Frontend
│   └── src/
│       ├── app/       # App Router
│       ├── components/
│       ├── lib/
│       ├── store/
│       └── types/
├── docker-compose.yml
└── .env.example
```

## License

Proprietary










