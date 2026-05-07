-- BANCO DE DADOS (POSTGRESQL)
CREATE DATABASE todo_api;

CREATE TABLE lista_tarefas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    descricao TEXT,
    status BOOLEAN DEFAULT FALSE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO lista_tarefas (nome, descricao, status)
VALUES 
('Projeto API ToDo', 'Finalizar backend da aplicacao', true),
('Estudar Docker', 'Aprender containerizacao de apps', false),
('Deploy no Render', 'Publicar API online', true);