

import './App.css'

function App() {


  return (
    <div className="relative min-h-screen flex items-center justify-center text-gray-800 p-4 overflow-hidden">

      {/* Video de fondo */}
      <video
        className="absolute inset-0 w-full h-full object-cover z-0"
        autoPlay
        muted
        loop
        playsInline
      >
        <source src="https://cdn.pixabay.com/video/2023/10/10/184370-873181596_large.mp4" type="video/mp4" />
        Tu navegador no soporta video.
      </video>

      {/* Capa oscura semi-transparente para contraste */}
      <div className="absolute inset-0 bg-black/50 z-0"></div>

      {/* Contenedor principal con efecto glassmorphism */}
      <div className="relative z-10 w-full max-w-6xl min-h-[90vh] bg-white/20 backdrop-blur-lg rounded-2xl shadow-xl ring-1 ring-white/10 flex flex-col">

        {/* Header */}
        <header className="border-b border-white/20 px-6 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold drop-shadow-md text-white">✨ Mi App Moderna</h1>
          <nav className="flex gap-6">
            <a href="/" className="hover:text-yellow-300 transition">Inicio</a>
            <a href="/about" className="hover:text-yellow-300 transition">Acerca</a>
            <a href="/dashboard" className="hover:text-yellow-300 transition">Dashboard</a>
          </nav>
        </header>

        {/* Contenido */}
        <main className="flex-1 p-6 overflow-y-auto text-white">
          
            <h2 className="text-xl font-semibold">Bienvenido</h2>
            <p className="mt-2 text-gray-200">
              Este es un ejemplo de aplicación moderna con fondo animado y efecto glassmorphism.
            </p>
          
        </main>

        {/* Footer */}
        <footer className="border-t border-white/20 text-sm text-center py-4 text-white/70">
          © 2025 Mi App Moderna
        </footer>
      </div>
    </div>
  )
}

export default App
