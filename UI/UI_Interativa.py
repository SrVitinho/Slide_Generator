import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Deu certo!")

# nomeando nossa ui
root = tk.Tk()
root.title("M.A.R.T.A")

#selecionando arquivo
def select_file():
    filetypes = (
        ('text files', '*.wordx'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


caminho_arquivo_selecionado = ""

def select_file():
    filetypes = (
        ('text files', '*.wordx'),
        ('All files', '*.*')
    )

    global caminho_arquivo_selecionado
    caminho_arquivo_selecionado = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=caminho_arquivo_selecionado
    )

# Função chamada quando o botão é clicado
def exibir_texto():
    texto = entrada_texto.get()
    label_resultado.config(text="Texto inserido: " + texto)


# Rótulo de instrução
label_instrucao = tk.Label(root, text="Digite seu email:")
label_instrucao.pack()

# Entrada de texto
entrada_texto = tk.Entry(root)
entrada_texto.pack()

# Botão para exibir o texto
botao_exibir = tk.Button(root, text="Exibir Email", command=exibir_texto)
botao_exibir.pack()

# Rótulo para exibir o texto inserido
label_resultado = tk.Label(root, text="")
label_resultado.pack()

#botao para enviar arquivos para a IA
texto_documento = tk.Text(root, height=10, width=40)
texto_documento.pack(padx=20, pady=10)

#vitinho! e na proxima linha que vc altera a funcao do botao enviar , logo apos o : command
botao = tk.Button(root, text="Enviar arquivos!", command=showinfo)
botao.pack(padx=20, pady=20)

root.mainloop()
