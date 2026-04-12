CREATE TABLE IF NOT EXISTS animais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
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

INSERT INTO animais (nome, tipo, especie, habitat, pais_origem, descricao, data_nascimento) VALUES
('Leão', 'Mamífero', 'Felino', 'Savanas', 'África', 'Rei da selva', '2010-04-01'),
('Elefante', 'Mamífero', 'Proboscídeo', 'Florestas', 'África', 'Maior animal terrestre', '2008-09-21'),
('Águia', 'Ave', 'Ave de Rapina', 'Montanhas', 'América do Norte', 'Visão aguçada', '2012-07-11');

INSERT INTO cuidados (animal_id, descricao, data_cuidado) VALUES
(1, 'Alimentação com carne', '2025-05-01'),
(2, 'Banho semanal', '2025-05-03'),
(3, 'Exame veterinário', '2025-05-04');

SELECT * FROM animais;
SELECT * FROM cuidados;
