import React, { useEffect, useState } from 'react';

function Cuidados() {
  const [cuidados, setCuidados] = useState([]);
  const [formData, setFormData] = useState({
    animal_id: '',
    descricao: '',
    data_cuidado: ''
  });

  useEffect(() => {
    fetch('http://localhost:5000/cuidados')
      .then(response => response.json())
      .then(data => setCuidados(data));
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:5000/cuidados', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    })
      .then(res => res.json())
      .then(() => {
        setFormData({ animal_id: '', descricao: '', data_cuidado: '' });
        return fetch('http://localhost:5000/cuidados');
      })
      .then(res => res.json())
      .then(data => setCuidados(data));
  };

  return (
    <div>
      <h2>📋 Lista de Cuidados</h2>
      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>ID</th>
            <th>ID Animal</th>
            <th>Descrição</th>
            <th>Data do Cuidado</th>
          </tr>
        </thead>
        <tbody>
          {cuidados.map(cuidado => (
            <tr key={cuidado.id}>
              <td>{cuidado.id}</td>
              <td>{cuidado.animal_id}</td>
              <td>{cuidado.descricao}</td>
              <td>{new Date(cuidado.data_cuidado).toLocaleDateString('pt-BR')}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h3>➕ Cadastrar Novo Cuidado</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="animal_id"
          placeholder="ID do Animal"
          value={formData.animal_id}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="descricao"
          placeholder="Descrição"
          value={formData.descricao}
          onChange={handleChange}
          required
        />
        <input
          type="date"
          name="data_cuidado"
          value={formData.data_cuidado}
          onChange={handleChange}
          required
        />
        <br />
        <button type="submit">Salvar</button>
      </form>
    </div>
  );
}

export default Cuidados;
