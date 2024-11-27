import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont

# Configuração da janela principal
root = tk.Tk()
root.title("Quiz")
root.geometry("800x600")  # Definir tamanho da janela

# Carregar a fonte Playfair Display após inicializar a janela
font_path = "PlayfairDisplay-Regular.ttf"
playfair_font = tkFont.Font(root=root, family="Playfair Display", size=12)

# Definir as perguntas e respostas
questions = [
    {
        "question": 'QUAL FOI A ORIGEM DA XEROX ANTES DE SE TORNAR LÍDER EM FOTOCOPIADORAS?',
        "answers": [
            {"text": "Haloid Photographic Company", "correct": True},
            {"text": "Xerox PARC", "correct": False},
            {"text": "Microsoft", "correct": False},
            {"text": "IBM", "correct": False},
        ]
    },
    {
        "question": 'QUAL INOVAÇÃO DO XEROX PARC FOI A BASE PARA A COMPUTAÇÃO PESSOAL MODERNA?',
        "answers": [
            {"text": "Computação em nuvem", "correct": False},
            {"text": "Interface gráfica", "correct": True},
            {"text": "Processadores de texto", "correct": False},
            {"text": "Armazenamento SSD", "correct": False},
        ]
    },
    {
        "question": 'QUAL TECNOLOGIA PIONEIRA FOI CRIADA PELA XEROX, MAS AMPLAMENTE EXPLORADA PELA APPLE E MICROSOFT?',
        "answers": [
            {"text": "Impressora 3D", "correct": False},
            {"text": "Banco de dados relacionais", "correct": False},
            {"text": "Processador de texto", "correct": False},
            {"text": "Mouse", "correct": True},
        ]
    },
    {
        "question": "O QUE EXPLICA A PERDA DE LIDERANÇA DA XEROX NO MERCADO DE TECNOLOGIA?",
        "answers": [
            {"text": "Falta de inovação tecnológica", "correct": False},
            {"text": "Concorrência direta com o Google", "correct": False},
            {"text": "Má qualidade dos produtos", "correct": False},
            {"text": "Foco excessivo no mercado de copiadoras", "correct": True},
        ]
    },
    {
        "question": "QUAL FOI O PRIMEIRO COMPUTADOR PESSOAL DESENVOLVIDO PELA XEROX COM INTERFACE GRÁFICA?",
        "answers": [
            {"text": "Xerox Star", "correct": False},
            {"text": "Xerox Alto", "correct": True},
            {"text": "Apple Lisa", "correct": False},
            {"text": "IBM PC", "correct": False},
        ]
    },
    {
        "question": "QUAL ERA A OCUPAÇÃO DE JOHN SCULLEY ANTES DE SER CONTRATADO PELA APPLE?",
        "answers": [
            {"text": "Diretor de tecnologia na IBM", "correct": False},
            {"text": "Consultor de marketing para a Microsoft", "correct": False},
            {"text": "Engenheiro da Xerox", "correct": False},
            {"text": "Presidente da PepsiCo", "correct": True},
        ]
    },
    {
        "question": "QUAL FOI A CONTRIBUIÇÃO INICIAL MAIS NOTÁVEL DE JOHN SCULLEY PARA A APPLE?",
        "answers": [
            {"text": "Aumentar o orçamento publicitário da Apple", "correct": True},
            {"text": "Desenvolver o design do Macintosh", "correct": False},
            {"text": "Criar o primeiro iPhone", "correct": False},
            {"text": "Estabelecer lojas físicas da Apple", "correct": False},
        ]
    },
    {
        "question": "POR QUE JOHN SCULLEY DECIDIU DEMITIR STEVE JOBS DA APPLE EM 1985?",
        "answers": [
            {"text": "Conflitos de liderança e diferenças na visão estratégica", "correct": True},
            {"text": "Falhas na gestão financeira", "correct": False},
            {"text": "Desempenho insatisfatório do Macintosh", "correct": False},
            {"text": "Pressão de investidores externos", "correct": False},
        ]
    },
    {
        "question": "QUAL LIVRO JOHN SCULLEY ESCREVEU SOBRE SUA EXPERIÊNCIA NA APPLE?",
        "answers": [
            {"text": "A Segunda Era Digital", "correct": False},
            {"text": "Odisséia: Da Pepsi à Apple", "correct": True},
            {"text": "Inovação Disruptiva: Lições da Tecnologia", "correct": False},
            {"text": "Os Bastidores do Vale do Silício", "correct": False},
        ]
    },
    {
        "question": "QUAL FOI UMA DAS PRINCIPAIS INOVAÇÕES SOB A LIDERANÇA DE SCULLEY NA APPLE?",
        "answers": [
            {"text": "Desenvolvimento do iPhone", "correct": False},
            {"text": "Criação do iPod", "correct": False},
            {"text": "Introdução do sistema iOS", "correct": False},
            {"text": "Lançamento do PowerBook", "correct": True},
        ]
    },
]

# Funções para controle do quiz
current_question_index = 0
total_correct = 0


def start_game():
    global current_question_index, total_correct
    current_question_index = 0
    total_correct = 0
    next_question()


def next_question():
    global current_question_index
    if current_question_index < len(questions):
        display_question(questions[current_question_index])
    else:
        finish_game()


def display_question(question_data):
    question_label.config(text=question_data["question"])

    # Remover respostas anteriores
    for widget in answers_frame.winfo_children():
        widget.destroy()

    # Exibir novas respostas
    for answer in question_data["answers"]:
        answer_button = ttk.Button(answers_frame, text=answer["text"], width=50, command=lambda a=answer: select_answer(a))
        answer_button.pack(pady=5)


def select_answer(answer):
    global current_question_index, total_correct
    if answer["correct"]:
        total_correct += 1
        messagebox.showinfo("Correto!", "Você acertou a pergunta!")
    else:
        messagebox.showerror("Errado", "Resposta incorreta!")

    current_question_index += 1
    next_question()


def finish_game():
    performance = (total_correct / len(questions)) * 100
    if performance >= 90:
        message = "Excelente :)"
    elif performance >= 70:
        message = "Bom :)"
    elif performance >= 50:
        message = "Regular"
    else:
        message = "Pode Melhorar :("

    messagebox.showinfo("Fim de Jogo", f"Você acertou {total_correct} de {len(questions)} perguntas.\nResultado: {message}")
    restart_game()


def restart_game():
    restart = messagebox.askyesno("Reiniciar", "Deseja reiniciar o quiz?")
    if restart:
        start_game()


# Estilo do ttk
style = ttk.Style()
style.configure("TButton", font=("Playfair Display", 12), padding=10, background="#F2EBF1", foreground="#000000")
style.map("TButton",
          background=[('active', '#D4C4E2'), ('pressed', '#D4C4E2')])

style.configure("TFrame", background="#F2EBF1")

# Cor de fundo da janela principal
root.configure(bg="#F2EBF1")

# Layout
question_label = tk.Message(root, text="Clique no botão abaixo para começar o Quiz", font=playfair_font, bg="#D4C4E2", border="10px", width=600)
question_label.pack(pady=20, anchor="center")

start_button = ttk.Button(root, text="Iniciar Quiz", width=20, command=start_game, style="TButton")
start_button.pack(pady=10)

# Frame para as respostas
answers_frame = ttk.Frame(root, style="TFrame")
answers_frame.pack()

root.mainloop()
