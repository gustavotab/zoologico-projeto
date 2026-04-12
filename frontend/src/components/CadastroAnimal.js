// src/components/CadastroAnimal.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function CadastroAnimal() {
  const [animal, setAnimal] = useState({
    nome: '',
    tipo: '',
    especie: '',
    habitat: '',
    pais_origem: '',
    descricao: '',
    data_nascimento: ''
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setAnimal({ ...animal, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:5000/animais', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(animal)
    })
      .then(response => {
        if (!response.ok) throw new Error("Erro ao cadastrar");
        return response.json();
      })
      .then(() => {
        alert('Animal cadastrado com sucesso!');
        navigate('/');
      })
      .catch(error => alert('Erro ao cadastrar: ' + error.message));
  };

  return (
    <div>
      <h2>Cadastrar Novo Animal</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="nome" placeholder="Nome" value={animal.nome} onChange={handleChange} required />
        <input type="text" name="tipo" placeholder="Tipo (ex: Mamífero)" value={animal.tipo} onChange={handleChange} required />
        <input type="text" name="especie" placeholder="Espécie" value={animal.especie} onChange={handleChange} required />
        <input type="text" name="habitat" placeholder="Habitat" value={animal.habitat} onChange={handleChange} required />
        <input type="text" name="pais_origem" placeholder="País de Origem" value={animal.pais_origem} onChange={handleChange} required />
        <input type="text" name="descricao" placeholder="Descrição" value={animal.descricao} onChange={handleChange} required />
        <input type="date" name="data_nascimento" value={animal.data_nascimento} onChange={handleChange} required />
        <br />
        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
}

export default CadastroAnimal;
