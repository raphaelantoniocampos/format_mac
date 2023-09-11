import tkinter as tk
import pyperclip

def format_mac():
    mac = paste_entry.get()
    char = mac[2]
    if char.isalnum():
        segmentos = []
        for i in range(0, len(mac), 2):
            segmento = mac[i:i+2]
            segmentos.append(segmento)
        formatted_mac = ":".join(segmentos)
    else:
        formatted_mac = mac.replace(char, ':')

    pyperclip.copy(formatted_mac)
    result_text['text'] = formatted_mac
    copied_text['text'] = "Copiado para a área de transferência."
    

window = tk.Tk()
window.geometry("300x160")
window.title("Formatar MAC")

window.eval('tk::PlaceWindow . center')

paste_text = tk.Label(window, text='Colar MAC')
paste_text.pack(padx=10, pady=5)

paste_entry = tk.Entry(window, width=20)
paste_entry.pack(padx=10, pady=5)

button = tk.Button(window, text='Formatar', command=format_mac)
button.pack(padx=10, pady=5)

result_text = tk.Label(window, text='')
result_text.pack(padx=10, pady=5)

copied_text = tk.Label(window, text='')
copied_text.pack(padx=10, pady=5)

window.mainloop()
