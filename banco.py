import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Função para conectar ao banco de dados
def conectar_bd():
    conn = sqlite3.connect('sistema.db')
    return conn

# Função para criar as tabelas no banco de dados, caso não existam
def criar_tabelas():
    conn = conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        telefone TEXT,
                        email TEXT,
                        endereco TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        categoria TEXT,
                        email TEXT,
                        telefone TEXT,
                        cnpj TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        descricao TEXT,
                        preco REAL,
                        fornecedor TEXT)''')
    
    conn.commit()
    conn.close()

# Funções para registrar no banco de dados
def registrar_funcionario_bd(nome, telefone, email, endereco):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcionarios (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)", 
                   (nome, telefone, email, endereco))
    conn.commit()
    conn.close()

def registrar_fornecedor_bd(nome, categoria, email, telefone, cnpj):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO fornecedores (nome, categoria, email, telefone, cnpj) VALUES (?, ?, ?, ?, ?)", 
                   (nome, categoria, email, telefone, cnpj))
    conn.commit()
    conn.close()

def registrar_produto_bd(nome, descricao, preco, fornecedor):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, descricao, preco, fornecedor) VALUES (?, ?, ?, ?)", 
                   (nome, descricao, preco, fornecedor))
    conn.commit()
    conn.close()

# Funções para excluir registros
def excluir_funcionario(id_funcionario):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario,))
    conn.commit()
    conn.close()

def excluir_fornecedor(id_fornecedor):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fornecedores WHERE id = ?", (id_fornecedor,))
    conn.commit()
    conn.close()

def excluir_produto(id_produto):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conn.commit()
    conn.close()

# Função para registrar um novo funcionário
def registrar_funcionario():
    def salvar_funcionario():
        nome = entry_nome_funcionario.get()
        telefone = entry_telefone_funcionario.get()
        email = entry_email_funcionario.get()
        endereco = entry_endereco_funcionario.get()
        
        if nome and telefone and email and endereco:
            registrar_funcionario_bd(nome, telefone, email, endereco)
            messagebox.showinfo("Sucesso", "Funcionário registrado com sucesso!")
            registrar_funcionario_window.destroy()
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    
    registrar_funcionario_window = tk.Toplevel(root)
    registrar_funcionario_window.title("Registrar Funcionário")
    registrar_funcionario_window.geometry("400x400")

    tk.Label(registrar_funcionario_window, text="Nome").pack(pady=5)
    entry_nome_funcionario = tk.Entry(registrar_funcionario_window)
    entry_nome_funcionario.pack(pady=5)

    tk.Label(registrar_funcionario_window, text="Telefone").pack(pady=5)
    entry_telefone_funcionario = tk.Entry(registrar_funcionario_window)
    entry_telefone_funcionario.pack(pady=5)

    tk.Label(registrar_funcionario_window, text="Email").pack(pady=5)
    entry_email_funcionario = tk.Entry(registrar_funcionario_window)
    entry_email_funcionario.pack(pady=5)

    tk.Label(registrar_funcionario_window, text="Endereço").pack(pady=5)
    entry_endereco_funcionario = tk.Entry(registrar_funcionario_window)
    entry_endereco_funcionario.pack(pady=5)

    tk.Button(registrar_funcionario_window, text="Salvar", command=salvar_funcionario).pack(pady=20)

# Função para registrar um novo fornecedor
def registrar_fornecedor():
    def salvar_fornecedor():
        nome = entry_nome_fornecedor.get()
        categoria = entry_categoria_fornecedor.get()
        email = entry_email_fornecedor.get()
        telefone = entry_telefone_fornecedor.get()
        cnpj = entry_cnpj_fornecedor.get()
        
        if nome and categoria and email and telefone and cnpj:
            registrar_fornecedor_bd(nome, categoria, email, telefone, cnpj)
            messagebox.showinfo("Sucesso", "Fornecedor registrado com sucesso!")
            registrar_fornecedor_window.destroy()
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    
    registrar_fornecedor_window = tk.Toplevel(root)
    registrar_fornecedor_window.title("Registrar Fornecedor")
    registrar_fornecedor_window.geometry("400x400")

    tk.Label(registrar_fornecedor_window, text="Nome").pack(pady=5)
    entry_nome_fornecedor = tk.Entry(registrar_fornecedor_window)
    entry_nome_fornecedor.pack(pady=5)

    tk.Label(registrar_fornecedor_window, text="Categoria").pack(pady=5)
    entry_categoria_fornecedor = tk.Entry(registrar_fornecedor_window)
    entry_categoria_fornecedor.pack(pady=5)

    tk.Label(registrar_fornecedor_window, text="Email").pack(pady=5)
    entry_email_fornecedor = tk.Entry(registrar_fornecedor_window)
    entry_email_fornecedor.pack(pady=5)

    tk.Label(registrar_fornecedor_window, text="Telefone").pack(pady=5)
    entry_telefone_fornecedor = tk.Entry(registrar_fornecedor_window)
    entry_telefone_fornecedor.pack(pady=5)

    tk.Label(registrar_fornecedor_window, text="CNPJ").pack(pady=5)
    entry_cnpj_fornecedor = tk.Entry(registrar_fornecedor_window)
    entry_cnpj_fornecedor.pack(pady=5)

    tk.Button(registrar_fornecedor_window, text="Salvar", command=salvar_fornecedor).pack(pady=20)

# Função para registrar um novo produto
def registrar_produto():
    def salvar_produto():
        nome = entry_nome_produto.get()
        descricao = entry_descricao_produto.get()
        preco = entry_preco_produto.get()
        fornecedor = entry_fornecedor_produto.get()
        
        if nome and descricao and preco and fornecedor:
            registrar_produto_bd(nome, descricao, preco, fornecedor)
            messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")
            registrar_produto_window.destroy()
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    
    registrar_produto_window = tk.Toplevel(root)
    registrar_produto_window.title("Registrar Produto")
    registrar_produto_window.geometry("400x400")

    tk.Label(registrar_produto_window, text="Nome").pack(pady=5)
    entry_nome_produto = tk.Entry(registrar_produto_window)
    entry_nome_produto.pack(pady=5)

    tk.Label(registrar_produto_window, text="Descrição").pack(pady=5)
    entry_descricao_produto = tk.Entry(registrar_produto_window)
    entry_descricao_produto.pack(pady=5)

    tk.Label(registrar_produto_window, text="Preço").pack(pady=5)
    entry_preco_produto = tk.Entry(registrar_produto_window)
    entry_preco_produto.pack(pady=5)

    tk.Label(registrar_produto_window, text="Fornecedor").pack(pady=5)
    entry_fornecedor_produto = tk.Entry(registrar_produto_window)
    entry_fornecedor_produto.pack(pady=5)

    tk.Button(registrar_produto_window, text="Salvar", command=salvar_produto).pack(pady=20)

# Função para exibir a tabela de funcionários com opção de exclusão
def exibir_funcionarios():
    janela_funcionarios = tk.Toplevel(root)
    janela_funcionarios.title("Funcionários")
    janela_funcionarios.geometry("800x600")
    janela_funcionarios.configure(bg="#8B0000")

    tree_funcionarios = ttk.Treeview(janela_funcionarios, columns=("ID", "Nome", "Telefone", "Email", "Endereço"), show="headings")
    tree_funcionarios.heading("ID", text="ID")
    tree_funcionarios.heading("Nome", text="Nome")
    tree_funcionarios.heading("Telefone", text="Telefone")
    tree_funcionarios.heading("Email", text="Email")
    tree_funcionarios.heading("Endereço", text="Endereço")
    tree_funcionarios.pack(fill=tk.BOTH, expand=True)
    
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    for row in cursor.fetchall():
        tree_funcionarios.insert("", "end", values=row)
    
    conn.close()

    # Função para excluir o funcionário selecionado
    def excluir_funcionario_selecionado():
        selected_item = tree_funcionarios.selection()
        if selected_item:
            id_funcionario = tree_funcionarios.item(selected_item)["values"][0]
            excluir_funcionario(id_funcionario)
            tree_funcionarios.delete(selected_item)
            messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")
        else:
            messagebox.showwarning("Erro", "Selecione um funcionário para excluir.")

    # Botão de excluir
    tk.Button(janela_funcionarios, text="Excluir", font=("Arial", 14, "bold"), bg="red", fg="white", command=excluir_funcionario_selecionado).pack(pady=10)

# Função para exibir a tabela de fornecedores com opção de exclusão
def exibir_fornecedores():
    janela_fornecedores = tk.Toplevel(root)
    janela_fornecedores.title("Fornecedores")
    janela_fornecedores.geometry("800x600")
    janela_fornecedores.configure(bg="#8B0000")

    tree_fornecedores = ttk.Treeview(janela_fornecedores, columns=("ID", "Nome", "Categoria", "Email", "Telefone", "CNPJ"), show="headings")
    tree_fornecedores.heading("ID", text="ID")
    tree_fornecedores.heading("Nome", text="Nome")
    tree_fornecedores.heading("Categoria", text="Categoria")
    tree_fornecedores.heading("Email", text="Email")
    tree_fornecedores.heading("Telefone", text="Telefone")
    tree_fornecedores.heading("CNPJ", text="CNPJ")
    tree_fornecedores.pack(fill=tk.BOTH, expand=True)
    
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fornecedores")
    for row in cursor.fetchall():
        tree_fornecedores.insert("", "end", values=row)
    
    conn.close()

    # Função para excluir o fornecedor selecionado
    def excluir_fornecedor_selecionado():
        selected_item = tree_fornecedores.selection()
        if selected_item:
            id_fornecedor = tree_fornecedores.item(selected_item)["values"][0]
            excluir_fornecedor(id_fornecedor)
            tree_fornecedores.delete(selected_item)
            messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
        else:
            messagebox.showwarning("Erro", "Selecione um fornecedor para excluir.")

    # Botão de excluir
    tk.Button(janela_fornecedores, text="Excluir", font=("Arial", 14, "bold"), bg="red", fg="white", command=excluir_fornecedor_selecionado).pack(pady=10)

# Função para exibir a tabela de produtos com opção de exclusão
def exibir_produtos():
    janela_produtos = tk.Toplevel(root)
    janela_produtos.title("Produtos")
    janela_produtos.geometry("800x600")
    janela_produtos.configure(bg="#8B0000")

    tree_produtos = ttk.Treeview(janela_produtos, columns=("ID", "Nome", "Descrição", "Preço", "Fornecedor"), show="headings")
    tree_produtos.heading("ID", text="ID")
    tree_produtos.heading("Nome", text="Nome")
    tree_produtos.heading("Descrição", text="Descrição")
    tree_produtos.heading("Preço", text="Preço")
    tree_produtos.heading("Fornecedor", text="Fornecedor")
    tree_produtos.pack(fill=tk.BOTH, expand=True)
    
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    for row in cursor.fetchall():
        tree_produtos.insert("", "end", values=row)
    
    conn.close()

    # Função para excluir o produto selecionado
    def excluir_produto_selecionado():
        selected_item = tree_produtos.selection()
        if selected_item:
            id_produto = tree_produtos.item(selected_item)["values"][0]
            excluir_produto(id_produto)
            tree_produtos.delete(selected_item)
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        else:
            messagebox.showwarning("Erro", "Selecione um produto para excluir.")

    # Botão de excluir
    tk.Button(janela_produtos, text="Excluir", font=("Arial", 14, "bold"), bg="red", fg="white", command=excluir_produto_selecionado).pack(pady=10)

# Tela principal
root = tk.Tk()
root.title("Sistema de Gestão")
root.geometry("400x400")
root.configure(bg="#8B0000")

criar_tabelas()

tk.Button(root, text="Registrar Funcionário", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_funcionario).pack(pady=10)
tk.Button(root, text="Registrar Fornecedor", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_fornecedor).pack(pady=10)
tk.Button(root, text="Registrar Produto", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_produto).pack(pady=10)

tk.Button(root, text="Ver Funcionários", font=("Arial", 14, "bold"), bg="blue", fg="white", command=exibir_funcionarios).pack(pady=10)
tk.Button(root, text="Ver Fornecedores", font=("Arial", 14, "bold"), bg="blue", fg="white", command=exibir_fornecedores).pack(pady=10)
tk.Button(root, text="Ver Produtos", font=("Arial", 14, "bold"), bg="blue", fg="white", command=exibir_produtos).pack(pady=10)

root.mainloop()
