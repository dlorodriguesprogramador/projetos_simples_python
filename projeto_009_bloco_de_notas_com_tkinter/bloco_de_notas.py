import tkinter as tk
from tkinter import filedialog, messagebox

# Funções principais
def novo_arquivo():
    text_area.delete(1.0, tk.END)

def abrir_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if caminho:
        with open(caminho, "r", encoding="utf-8") as file:
            conteudo = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, conteudo)

def salvar_arquivo():
    caminho = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Arquivos de Texto", "*.txt")])
    if caminho:
        with open(caminho, "w", encoding="utf-8") as file:
            conteudo = text_area.get(1.0, tk.END)
            file.write(conteudo)
            messagebox.showinfo("Salvo", "Arquivo salvo com sucesso!")

# Interface
janela = tk.Tk()
janela.title("Bloco de Notas Simples")

text_area = tk.Text(janela, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# Menu
menu_bar = tk.Menu(janela)
arquivo_menu = tk.Menu(menu_bar, tearoff=0)
arquivo_menu.add_command(label="Novo", command=novo_arquivo)
arquivo_menu.add_command(label="Abrir", command=abrir_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=janela.quit)

menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
janela.config(menu=menu_bar)

janela.mainloop()