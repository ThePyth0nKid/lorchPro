'use client'

import { useAuthStore } from '@/store/auth'

export default function DashboardPage() {
  const user = useAuthStore((state) => state.user)

  if (!user) return null

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Welcome Section */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">
          Willkommen, {user.first_name}!
        </h1>
        <p className="text-gray-600 mt-2">Rolle: {user.rolle}</p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-semibold mb-2 text-gray-700">
            Offene Aufträge
          </h3>
          <p className="text-3xl font-bold text-blue-600">0</p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-semibold mb-2 text-gray-700">
            In Bearbeitung
          </h3>
          <p className="text-3xl font-bold text-yellow-600">0</p>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-semibold mb-2 text-gray-700">
            Abgeschlossen
          </h3>
          <p className="text-3xl font-bold text-green-600">0</p>
        </div>
      </div>

      {/* Aufträge List */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4 text-gray-900">
          Meine Aufträge
        </h2>
        <p className="text-gray-600">Noch keine Aufträge vorhanden.</p>
      </div>
    </div>
  )
}

