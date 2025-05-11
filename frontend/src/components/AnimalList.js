// src/components/AnimalList.js
import React, { useEffect, useState } from 'react';

function AnimalList() {
  const [animais, setAnimais] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/animais')
      .then(res => res.json())
      .then(data => setAnimais(data))
      .catch(err => console.error("Erro ao buscar animais:", err));
  }, []);

  return (
    <div>
      <h2>Lista de Animais</h2>
      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Tipo</th>
            <th>Espécie</th>
            <th>Habitat</th>
            <th>País de Origem</th>
            <th>Descrição</th>
            <th>Data de Nascimento</th>
          </tr>
        </thead>
        <tbody>
          {animais.map(animal => (
            <tr key={animal.id}>
              <td>{animal.id}</td>
              <td>{animal.nome}</td>
              <td>{animal.tipo}</td>
              <td>{animal.especie}</td>
              <td>{animal.habitat}</td>
              <td>{animal.pais_origem}</td>
              <td>{animal.descricao}</td>
              <td>{animal.data_nascimento}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AnimalList;
