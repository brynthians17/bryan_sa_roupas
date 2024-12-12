import tkinter as tk
from tkinter import messagebox

def abrir_menu_principal():
    # Criação de uma nova janela para o menu principal
    menu_principal = tk.Tk()
    menu_principal.title("Menu Principal")
    
    # Adicione widgets ao menu principal conforme necessário
    label = tk.Label(menu_principal, text="Bem-vindo ao Menu Principal!")
    label.pack(pady=20)

    # Inicia o loop principal da nova janela
    menu_principal.mainloop()

def autenticar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario:
        messagebox.showinfo("Login Bem-Sucedido", "Bem-vindo!")
        login.destroy()
        abrir_menu_principal()
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha incorretos!")


# Tela de Login
login = tk.Tk()
login.title("Login")
login.geometry("400x300")
login.configure(bg="#8B0000")

titulo_login = tk.Label(login, text="Login do Sistema", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
titulo_login.pack(pady=20)

frame_login = tk.Frame(login, bg="#8B0000")
frame_login.pack(pady=10)

label_usuario = tk.Label(frame_login, text="Usuário:", font=("Arial", 14), bg="#8B0000", fg="white")
label_usuario.grid(row=0, column=0, pady=5, sticky="e")
entry_usuario = tk.Entry(frame_login, font=("Arial", 14), width=20)
entry_usuario.grid(row=0, column=1, pady=5)

label_senha = tk.Label(frame_login, text="Senha:", font=("Arial", 14), bg="#8B0000", fg="white")
label_senha.grid(row=1, column=0, pady=5, sticky="e")
entry_senha = tk.Entry(frame_login, font=("Arial", 14), show="*", width=20)
entry_senha.grid(row=1, column=1, pady=5)

btn_login = tk.Button(login, text="Entrar", font=("Arial", 14, "bold"), bg="green", fg="white", command=autenticar)
btn_login.pack(pady=20)

login.mainloop()

# Função para abrir a janela de registro de funcionários
def abrir_registro_funcionarios():
    def registrar_funcionario():
        nome = entry_nome.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        endereco = entry_endereco.get()

        if not nome or not telefone or not email or not endereco:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        messagebox.showinfo("Sucesso", f"Funcionário {nome} registrado com sucesso!")
        limpar_campos()

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)

    # Criar uma nova janela
    janela_registro = tk.Toplevel(root)
    janela_registro.title("Registro de Funcionários")
    janela_registro.geometry("400x500")
    janela_registro.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_registro, text="Registro de Funcionários", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome
    label_nome = tk.Label(janela_registro, text="Nome:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome.pack(anchor="w", padx=20, pady=5)
    entry_nome = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_nome.pack(padx=20, pady=5)

    # Telefone
    label_telefone = tk.Label(janela_registro, text="Telefone:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_telefone.pack(anchor="w", padx=20, pady=5)
    entry_telefone = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_telefone.pack(padx=20, pady=5)

    # E-mail
    label_email = tk.Label(janela_registro, text="E-mail:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_email.pack(anchor="w", padx=20, pady=5)
    entry_email = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_email.pack(padx=20, pady=5)

    # Endereço
    label_endereco = tk.Label(janela_registro, text="Endereço:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_endereco.pack(anchor="w", padx=20, pady=5)
    entry_endereco = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_endereco.pack(padx=20, pady=5)

    # Botão Registrar
    btn_registrar = tk.Button(janela_registro, text="Registrar", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_funcionario)
    btn_registrar.pack(pady=20)

# Função para excluir um funcionário
def excluir_funcionario():
    def confirmar_exclusao():
        nome_funcionario = entry_nome_funcionario.get()

        if not nome_funcionario:
            messagebox.showerror("Erro", "Por favor, insira o nome do funcionário!")
            return

        # Simulação de exclusão (Você pode adicionar lógica de exclusão real aqui)
        resposta = messagebox.askyesno("Confirmação", f"Você tem certeza que deseja excluir o funcionário '{nome_funcionario}'?")
        if resposta:
            messagebox.showinfo("Sucesso", f"Funcionário {nome_funcionario} excluído com sucesso!")
            entry_nome_funcionario.delete(0, tk.END)
        else:
            messagebox.showinfo("Cancelado", "Exclusão cancelada!")

    # Criar uma nova janela para excluir funcionário
    janela_exclusao = tk.Toplevel(root)
    janela_exclusao.title("Excluir Funcionário")
    janela_exclusao.geometry("400x300")
    janela_exclusao.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_exclusao, text="Excluir Funcionário", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome do Funcionário
    label_nome_funcionario = tk.Label(janela_exclusao, text="Nome do Funcionário:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome_funcionario.pack(anchor="w", padx=20, pady=5)
    entry_nome_funcionario = tk.Entry(janela_exclusao, font=("Arial", 12), width=30)
    entry_nome_funcionario.pack(padx=20, pady=5)

    # Botão Confirmar Exclusão
    btn_excluir = tk.Button(janela_exclusao, text="Excluir Funcionário", font=("Arial", 14, "bold"), bg="green", fg="white", command=confirmar_exclusao)
    btn_excluir.pack(pady=20)

# Função para abrir a janela de registro de fornecedores
def abrir_registro_fornecedores():
    def registrar_fornecedor():
        nome = entry_nome.get()
        categoria = entry_categoria.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        cnpj = entry_cnpj.get()

        if not nome or not categoria or not email or not telefone or not cnpj:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        messagebox.showinfo("Sucesso", f"Fornecedor {nome} registrado com sucesso!")
        limpar_campos()

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_categoria.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_cnpj.delete(0, tk.END)

    # Criar uma nova janela
    janela_registro = tk.Toplevel(root)
    janela_registro.title("Registro de Fornecedores")
    janela_registro.geometry("400x600")
    janela_registro.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_registro, text="Registro de Fornecedores", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome do Fornecedor
    label_nome = tk.Label(janela_registro, text="Nome do Fornecedor:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome.pack(anchor="w", padx=20, pady=5)
    entry_nome = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_nome.pack(padx=20, pady=5)

    # Categoria
    label_categoria = tk.Label(janela_registro, text="Categoria:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_categoria.pack(anchor="w", padx=20, pady=5)
    entry_categoria = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_categoria.pack(padx=20, pady=5)

    # E-mail
    label_email = tk.Label(janela_registro, text="E-mail:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_email.pack(anchor="w", padx=20, pady=5)
    entry_email = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_email.pack(padx=20, pady=5)

    # Telefone
    label_telefone = tk.Label(janela_registro, text="Telefone:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_telefone.pack(anchor="w", padx=20, pady=5)
    entry_telefone = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_telefone.pack(padx=20, pady=5)

    # CNPJ
    label_cnpj = tk.Label(janela_registro, text="CNPJ:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_cnpj.pack(anchor="w", padx=20, pady=5)
    entry_cnpj = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_cnpj.pack(padx=20, pady=5)

    # Botão Registrar
    btn_registrar = tk.Button(janela_registro, text="Registrar", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_fornecedor)
    btn_registrar.pack(pady=20)
 
def excluir_fornecedor():
    def confirmar_exclusao():
        nome_fornecedor = entry_nome_fornecedor.get()

        if not nome_fornecedor:
            messagebox.showerror("Erro", "Por favor, insira o nome do fornecedor!")
            return

        # Simulação de exclusão (Você pode adicionar lógica de exclusão real aqui)
        resposta = messagebox.askyesno("Confirmação", f"Você tem certeza que deseja excluir o fornecedor '{nome_fornecedor}'?")
        if resposta:
            messagebox.showinfo("Sucesso", f"fornecedor {nome_fornecedor} excluído com sucesso!")
            entry_nome_fornecedor.delete(0, tk.END)
        else:
            messagebox.showinfo("Cancelado", "Exclusão cancelada!")

    # Criar uma nova janela para excluir funcionário
    janela_exclusao = tk.Toplevel(root)
    janela_exclusao.title("Excluir Funcionário")
    janela_exclusao.geometry("400x300")
    janela_exclusao.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_exclusao, text="Excluir fornecedor", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome do Funcionário
    label_nome_fornecedor = tk.Label(janela_exclusao, text="CNPJ fornecedor:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome_fornecedor.pack(anchor="w", padx=20, pady=5)
    entry_nome_fornecedor = tk.Entry(janela_exclusao, font=("Arial", 12), width=30)
    entry_nome_fornecedor.pack(padx=20, pady=5)

    # Botão Confirmar Exclusão
    btn_excluir = tk.Button(janela_exclusao, text="Excluir fornecedor", font=("Arial", 14, "bold"), bg="red", fg="white", command=confirmar_exclusao)
    btn_excluir.pack(pady=20)


# Função para abrir a janela de registro de produtos
def abrir_registro_produtos():
    def registrar_produto():
        nome = entry_nome.get()
        descricao = entry_descricao.get()
        preco = entry_preco.get()
        fornecedor = entry_fornecedor.get()

        if not nome or not descricao or not preco or not fornecedor:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        messagebox.showinfo("Sucesso", f"Produto {nome} registrado com sucesso!")
        limpar_campos()

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        entry_fornecedor.delete(0, tk.END)

    # Criar uma nova janela
    janela_registro = tk.Toplevel(root)
    janela_registro.title("Registro de Produtos")
    janela_registro.geometry("400x500")
    janela_registro.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_registro, text="Registro de Produtos", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome do Produto
    label_nome = tk.Label(janela_registro, text="Nome do Produto:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome.pack(anchor="w", padx=20, pady=5)
    entry_nome = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_nome.pack(padx=20, pady=5)

    # Descrição
    label_descricao = tk.Label(janela_registro, text="Descrição:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_descricao.pack(anchor="w", padx=20, pady=5)
    entry_descricao = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_descricao.pack(padx=20, pady=5)

    # Preço
    label_preco = tk.Label(janela_registro, text="Preço:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_preco.pack(anchor="w", padx=20, pady=5)
    entry_preco = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_preco.pack(padx=20, pady=5)

    # Fornecedor
    label_fornecedor = tk.Label(janela_registro, text="Fornecedor:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_fornecedor.pack(anchor="w", padx=20, pady=5)
    entry_fornecedor = tk.Entry(janela_registro, font=("Arial", 12), width=30)
    entry_fornecedor.pack(padx=20, pady=5)

    # Botão Registrar
    btn_registrar = tk.Button(janela_registro, text="Registrar", font=("Arial", 14, "bold"), bg="green", fg="white", command=registrar_produto)
    btn_registrar.pack(pady=20)

# Função para abrir a janela de compra de produtos
def abrir_compra_produto():
    def realizar_compra():
        nome_fornecedor = entry_fornecedor.get()
        nome_produto = entry_produto.get()
        quantidade = entry_quantidade.get()

        if not nome_fornecedor or not nome_produto or not quantidade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro positivo!")
            return

        # Simulação de compra (Você pode adicionar lógica real de compra aqui)
        messagebox.showinfo("Sucesso", f"Compra realizada com sucesso!\n"
                                        f"Fornecedor: {nome_fornecedor}\n"
                                        f"Produto: {nome_produto}\n"
                                        f"Quantidade: {quantidade}")
        limpar_campos()

    def limpar_campos():
        entry_fornecedor.delete(0, tk.END)
        entry_produto.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)

    # Criar uma nova janela
    janela_compra = tk.Toplevel(root)
    janela_compra.title("Compra de Produtos")
    janela_compra.geometry("400x400")
    janela_compra.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_compra, text="Compra de Produtos", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome do Fornecedor
    label_fornecedor = tk.Label(janela_compra, text="Nome do Fornecedor:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_fornecedor.pack(anchor="w", padx=20, pady=5)
    entry_fornecedor = tk.Entry(janela_compra, font=("Arial", 12), width=30)
    entry_fornecedor.pack(padx=20, pady=5)

    # Nome do Produto
    label_produto = tk.Label(janela_compra, text="Nome do Produto:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_produto.pack(anchor="w", padx=20, pady=5)
    entry_produto = tk.Entry(janela_compra, font=("Arial", 12), width=30)
    entry_produto.pack(padx=20, pady=5)

    # Quantidade
    label_quantidade = tk.Label(janela_compra, text="Quantidade:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_quantidade.pack(anchor="w", padx=20, pady=5)
    entry_quantidade = tk.Entry(janela_compra, font=("Arial", 12), width=30)
    entry_quantidade.pack(padx=20, pady=5)

    # Botão Realizar Compra
    btn_comprar = tk.Button(janela_compra, text="Comprar", font=("Arial", 14, "bold"), bg="green", fg="white", command=realizar_compra)
    btn_comprar.pack(pady=20)

def excluir_produto():
    def confirmar_exclusao():
        nome_produto = entry_nome_produto.get()
        quantidade = entry_quantidade.get()

        if not nome_produto or not quantidade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro positivo!")
            return

        resposta = messagebox.askyesno(
            "Confirmação", 
            f"Você tem certeza que deseja excluir {quantidade} unidades do produto '{nome_produto}'?"
        )
        if resposta:
            messagebox.showinfo("Sucesso", f"{quantidade} unidades do produto '{nome_produto}' foram excluídas com sucesso!")
            limpar_campos()
        else:
            messagebox.showinfo("Cancelado", "Exclusão cancelada!")

    def limpar_campos():
        entry_nome_produto.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)

    # Criar uma nova janela
    janela_exclusao = tk.Toplevel(root)
    janela_exclusao.title("Excluir Produto")
    janela_exclusao.geometry("400x300")
    janela_exclusao.configure(bg="#8B0000")

    # Título
    titulo = tk.Label(janela_exclusao, text="Excluir Produto", font=("Arial", 20, "bold"), bg="#8B0000", fg="white")
    titulo.pack(pady=20)

    # Nome do Produto
    label_nome_produto = tk.Label(janela_exclusao, text="Nome do Produto:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_nome_produto.pack(anchor="w", padx=20, pady=5)
    entry_nome_produto = tk.Entry(janela_exclusao, font=("Arial", 12), width=30)
    entry_nome_produto.pack(padx=20, pady=5)

    # Quantidade
    label_quantidade = tk.Label(janela_exclusao, text="Quantidade:", font=("Arial", 12, "bold"), bg="#8B0000", fg="white")
    label_quantidade.pack(anchor="w", padx=20, pady=5)
    entry_quantidade = tk.Entry(janela_exclusao, font=("Arial", 12), width=30)
    entry_quantidade.pack(padx=20, pady=5)

    # Botão Confirmar Exclusão
    btn_excluir = tk.Button(janela_exclusao, text="Excluir Produto", font=("Arial", 14, "bold"), bg="green", fg="white", command=confirmar_exclusao)
    btn_excluir.pack(pady=20)

# Função para sair do programa
def sair_programa():
    root.quit()

# Menu Principal
root = tk.Tk()
root.title("Menu do ADM")
root.geometry("800x600")
root.configure(bg="#8B0000")

# Título do Menu
titulo = tk.Label(root, text="Menu do ADM", font=("Arial", 30, "bold"), bg="#8B0000", fg="white")
titulo.pack(pady=20)

# Frame para organizar as seções
frame_menu = tk.Frame(root, bg="#8B0000")
frame_menu.pack(expand=True)

# Seção de Funcionários
frame_func = tk.Frame(frame_menu, bg="#8B0000", relief="groove", bd=2)
frame_func.grid(row=0, column=0, padx=20, pady=10)

label_func = tk.Label(frame_func, text="Funcionários", font=("Arial", 16, "bold"), bg="#8B0000", fg="white")
label_func.pack(pady=10)

btn_regis_func = tk.Button(frame_func, text="Registrar Funcionário", font=("Arial", 12), width=20, command=abrir_registro_funcionarios)
btn_regis_func.pack(pady=5)

btn_excluir_func = tk.Button(frame_func, text="Excluir Funcionário", font=("Arial", 12), width=20, command=excluir_funcionario)
btn_excluir_func.pack(pady=5)

# Seção de Produtos
frame_prod = tk.Frame(frame_menu, bg="#8B0000", relief="groove", bd=2)
frame_prod.grid(row=0, column=1, padx=20, pady=10)

label_prod = tk.Label(frame_prod, text="Produtos", font=("Arial", 16, "bold"), bg="#8B0000", fg="white")
label_prod.pack(pady=10)

btn_regis_prod = tk.Button(frame_prod, text="Registrar Produto", font=("Arial", 12), width=20, command=abrir_registro_produtos)
btn_regis_prod.pack(pady=5)

btn_comprar_prod = tk.Button(frame_prod, text="Comprar Produto", font=("Arial", 12), width=20, command=abrir_compra_produto)
btn_comprar_prod.pack(pady=5)

btn_excluir_prod = tk.Button(frame_prod, text="Excluir Produto", font=("Arial", 12), width=20, command=excluir_produto)
btn_excluir_prod.pack(pady=5)

# Seção de Fornecedores
frame_forn = tk.Frame(frame_menu, bg="#8B0000", relief="groove", bd=2)
frame_forn.grid(row=0, column=2, padx=20, pady=10)

label_forn = tk.Label(frame_forn, text="Fornecedores", font=("Arial", 16, "bold"), bg="#8B0000", fg="white")
label_forn.pack(pady=10)

btn_regis_forn = tk.Button(frame_forn, text="Registrar Fornecedor", font=("Arial", 12), width=20, command=abrir_registro_fornecedores)
btn_regis_forn.pack(pady=5)

btn_excluir_forn = tk.Button(frame_forn, text="Excluir Fornecedor", font=("Arial", 12), width=20, command=excluir_fornecedor)
btn_excluir_forn.pack(pady=5)

# Botão Sair
btn_sair = tk.Button(root, text="Sair", font=("Arial", 16, "bold"), width=20, command=sair_programa, bg="red", fg="white")
btn_sair.pack(pady=30)

root.mainloop()    
