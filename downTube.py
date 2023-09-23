import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from pytube import YouTube
from moviepy.editor import AudioFileClip

# Função para baixar e processar o vídeo
def baixar_video():
    url = url_entry.get()
    formato = formato_combo.get()

    yt = YouTube(url)

    if formato == 'mp3':
        download_e_converter_para_mp3(yt)
    else:
        baixar_video(yt, formato)

# Função para baixar e converter o vídeo para MP3
def download_e_converter_para_mp3(yt):
    stream = yt.streams.filter(only_audio=True).first()
    progress_var.set("Baixando...")
    root.update()
    file_path = stream.download(output_path="videos")
    progress_var.set("Download concluído. Convertendo para mp3...")
    root.update()

    clip = AudioFileClip(file_path)
    clip.write_audiofile(file_path.replace(".mp4", ".mp3"))

    os.remove(file_path)
    progress_var.set("Conversão concluída.")
    root.update()

# Função para baixar o vídeo no formato especificado
def baixar_video(yt, formato):
    if formato == 'mkv':
        stream = yt.streams.filter(file_extension='webm').get_highest_resolution()
    elif formato == 'mp4':
        stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()

    progress_var.set("Baixando...")
    root.update()
    stream.download(output_path="videos")
    progress_var.set("Download concluído.")
    root.update()

# Criar a janela principal
root = ThemedTk(theme="arc")
root.geometry('600x400')
root.title("DownTube - Baixador de Vídeos do YouTube")  

# Elementos da interface gráfica (UI)
logo = tk.PhotoImage(file="logo.png")
logo_label = ttk.Label(root, image=logo)
dev_label = ttk.Label(root, text="Desenvolvido por: Uélinton Morelli")
title = ttk.Label(root, text="DownTube - Baixador de Vídeos do YouTube", font=("Helvetica", 16))
url_label = ttk.Label(root, text="URL do YouTube:")
url_entry = ttk.Entry(root, width=50)
formato_label = ttk.Label(root, text="Formato:")
formato_combo = ttk.Combobox(root, values=["mp3", "mp4", "mkv"], state="readonly")
download_button = ttk.Button(root, text="Baixar", command=baixar_video)
progress_var = tk.StringVar()
progress_var.set("Esperando...")
progress_label = ttk.Label(root, textvariable=progress_var)

# Organizar elementos da interface gráfica
logo_label.pack(pady=10)
dev_label.pack(pady=10)
title.pack(pady=10)
url_label.pack()
url_entry.pack(pady=5)
formato_label.pack()
formato_combo.pack(pady=5)
download_button.pack(pady=10)
progress_label.pack()

# Rodar o loop principal
root.mainloop()
