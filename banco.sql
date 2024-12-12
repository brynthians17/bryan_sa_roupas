-- Criação da tabela Fornecedores
CREATE TABLE Fornecedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18),
    endereco VARCHAR(255),
    telefone VARCHAR(15),
    email VARCHAR(100)
);

-- Criação da tabela usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL
);

-- Inserir dados na tabela Fornecedores
INSERT INTO Fornecedores (nome, cnpj, endereco, telefone, email)
VALUES
('Fornecedor de Tecidos LTDA', '12.345.678/0001-90', 'Rua das Flores, 123', '(11) 98765-4321', 'contato@tecidos.com'),
('Malhas e Fios SA', '98.765.432/0001-12', 'Av. Central, 456', '(21) 92345-6789', 'suporte@malhasefios.com');

-- Criação da tabela Produtos (relacionada à tabela Fornecedores)
CREATE TABLE Produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2),
    quantidade_em_estoque INT DEFAULT 0,
    fornecedor_id INT,
    FOREIGN KEY (fornecedor_id) REFERENCES Fornecedores(id) ON DELETE SET NULL
);

-- Inserir dados na tabela Produtos
INSERT INTO Produtos (nome, descricao, preco, quantidade_em_estoque, fornecedor_id)
VALUES
('Camiseta Básica', 'Camiseta 100% algodão, ideal para o dia a dia', 29.90, 100, 1),
('Calça Jeans', 'Calça jeans tradicional, com modelagem reta', 79.90, 50, 2);

-- Inserir dados na tabela usuarios
INSERT INTO usuarios (nome_usuario, senha)
VALUES ('carlos', 'senha123');

-- Criação da tabela Funcionários
CREATE TABLE Funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    data_admissao DATE,
    salario DECIMAL(10, 2),
    email VARCHAR(100),
    telefone VARCHAR(15),
    senha VARCHAR(255) NOT NULL
);

-- Inserir dados na tabela Funcionários (com a senha)
INSERT INTO Funcionarios (nome, cargo, data_admissao, salario, email, telefone, senha)
VALUES
('Ana', 'Vendedora', '2023-01-15', 2000.00, 'ana@lojaroupas.com', '(31) 99876-5432', 'senhaAna123'),
('Carlos', 'Gerente', '2022-10-01', 3500.00, 'carlos@lojaroupas.com', '(31) 91234-5678', 'senhaCarlos123');

-- Criação da tabela Compras (relacionada à tabela Produtos)
CREATE TABLE Compras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    quantidade INT NOT NULL,
    data_compra DATE NOT NULL,
    preco_total DECIMAL(10, 2),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id) ON DELETE CASCADE
);

-- Inserir dados na tabela Compras
INSERT INTO Compras (produto_id, quantidade, data_compra, preco_total)
VALUES
(1, 20, '2024-12-01', 598.00), -- Compra de 20 camisetas (R$ 29.90 cada)
(2, 10, '2024-12-05', 799.00); -- Compra de 10 calças jeans (R$ 79.90 cada)
