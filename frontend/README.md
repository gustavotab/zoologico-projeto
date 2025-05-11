# 🦁 Sistema de Gerenciamento de Zoológico

Este projeto foi desenvolvido como parte do desafio técnico para a vaga de estágio da equipe Devs CIEE/PR.  
Ele consiste em um sistema web completo para o gerenciamento de animais e cuidados em um zoológico, utilizando tecnologias modernas no frontend e backend.

---

## 🚀 Funcionalidades

### 🐾 Animais
- Listagem de animais
- Cadastro de novo animal
- Edição de informações
- Remoção

### 🩺 Cuidados
- Listagem de cuidados aplicados aos animais
- Cadastro de novo cuidado (alimentação, banho, exame etc.)

---

## 💻 Tecnologias Utilizadas

### Frontend:
- [React.js](https://reactjs.org/)
- React Router DOM
- Fetch API
- HTML5 + CSS3

### Backend:
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- Flask-CORS
- MySQL Connector

### Banco de Dados:
- [MySQL 8.0](https://dev.mysql.com/)

---

## 🗃️ Estrutura do Projeto

zoologico-projeto/
├── backend/ # API Flask + MySQL
│ ├── app.py
│ ├── routes.py
│ ├── models.py
│ ├── database.py
├── frontend/
│ └── src/
│ ├── components/
│ │ ├── AnimalList.js
│ │ ├── CadastroAnimal.js
│ │ └── Cuidados.js
│ └── App.js
├── screenshots/
│ ├── lista-animais.png
│ └── cuidados.png
└── README.md



---

## ⚙️ Como rodar o projeto localmente

### 🔧 Pré-requisitos
- Python 3.10+
- MySQL 8.0
- Node.js + npm

---

### 🔹 1. Clonar o repositório
```bash
git clone https://github.com/gustavotab/zoologico-projeto.git
cd zoologico-projeto
🔹 2. Configurar o banco de dados
Acesse o MySQL Workbench e crie o banco:

CREATE DATABASE zoologico;
Crie as tabelas:

CREATE TABLE IF NOT EXISTS animais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(100),
    especie VARCHAR(100),
    habitat VARCHAR(100),
    pais_origem VARCHAR(100),
    descricao TEXT,
    data_nascimento DATE
);

CREATE TABLE IF NOT EXISTS cuidados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT,
    descricao TEXT NOT NULL,
    data_cuidado DATE NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES animais(id)
);
Insira dados de exemplo:

INSERT INTO animais (nome, tipo, especie, habitat, pais_origem, descricao, data_nascimento)
VALUES
('Leão', 'Mamífero', 'Felino', 'Savanas', 'África', 'Rei da selva', '2010-04-01');
🔹 3. Rodar o backend (Flask API)
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
A API estará disponível em: http://localhost:5000

🔹 4. Rodar o frontend (React)
cd frontend
npm install
npm start
A aplicação será iniciada em: http://localhost:3000

## 📸 Prints

### 📋 Lista de Animais
![Lista de Animais](./screenshots/lista-animais.png)

### 🩺 Cuidados
![Cuidados](./screenshots/cuidados.png)


📌 Sobre os diferenciais
O desafio citava como diferenciais o uso de SQL Server e API em .NET Core.
Neste projeto, utilizei MySQL e Flask (Python) para maior agilidade no desenvolvimento e por familiaridade técnica.
Estou totalmente aberto e disponível para evoluir o projeto com essas tecnologias em versões futuras, mostrando minha adaptabilidade e aprendizado constante.

🙋‍♂️ Autor
Gustavo Taborda
Desenvolvedor em formação | Entusiasta em full-stack
[LinkedIn](https://www.linkedin.com/in/gustavoandradetaborda/) · [GitHub](https://github.com/gustavotab)

📌 Observação Final
Mesmo se o projeto não estiver 100% completo, entreguei com total dedicação para demonstrar minha evolução em lógica, backend e frontend.
Foi um desafio de aprendizado e superação — e estou aberto a feedbacks para continuar crescendo!

🏁 Obrigado pela oportunidade!