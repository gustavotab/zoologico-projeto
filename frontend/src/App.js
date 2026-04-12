// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import AnimalList from './components/AnimalList';
import CadastroAnimal from './components/CadastroAnimal';
import Cuidados from './components/Cuidados'; // 👈 Importa o novo componente

function App() {
  return (
    <Router>
      <div className="App">
        <h1>🦁 Sistema do Zoológico</h1>
        <nav style={{ marginBottom: '20px' }}>
          <Link to="/" style={{ marginRight: '10px' }}>Listar Animais</Link>
          <Link to="/cadastro" style={{ marginRight: '10px' }}>Cadastrar Animal</Link>
          <Link to="/cuidados">Gerenciar Cuidados</Link> {/* 👈 Novo menu */}
        </nav>

        <Routes>
          <Route path="/" element={<AnimalList />} />
          <Route path="/cadastro" element={<CadastroAnimal />} />
          <Route path="/cuidados" element={<Cuidados />} /> {/* 👈 Nova rota */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
