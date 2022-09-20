import tkinter as tk
from PIL import ImageTk
from tkmacosx import Button

bg_colour = "#435C56"

# Create the window
window = tk.Tk()
window.title("Biocore")

# frame widget
frame1 = tk.Frame(window, width=800, height=600, bg=bg_colour)
frame1.grid(row=0, column=0)
#prevent widgets from affecting parent frame
frame1.pack_propagate(False)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file="assets/biocore.png")
logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
logo_widget.image = logo_img
logo_widget.pack()

# label widget
tk.Label(frame1, text="LEITOR DE ARQUIVOS NCBI SRA", bg=bg_colour, fg="white", font=("TkMenuFont", 14)).pack()

# button widget
Button(frame1, text="Pesquisa Geral", borderless=True , bg=bg_colour, fg="white", font=("TkHeadingFont", 20, 'underline'), cursor="hand2", bd=0, activebackground=bg_colour, bordercolor=bg_colour, focuscolor=bg_colour, highlightbackground=bg_colour).pack()

Button(frame1, text="Pesquisa Detalhada", borderless=True , bg=bg_colour, fg="white", font=("TkHeadingFont", 20, 'underline'), cursor="hand2", bd=0, activebackground=bg_colour, bordercolor=bg_colour, focuscolor=bg_colour, highlightbackground=bg_colour).pack()

Button(frame1, text="Lista de Metadados", borderless=True , bg=bg_colour, fg="white", font=("TkHeadingFont", 20, 'underline'), cursor="hand2", bd=0, activebackground=bg_colour, bordercolor=bg_colour, focuscolor=bg_colour, highlightbackground=bg_colour).pack()

Button(frame1, text="Download de arquivos", borderless=True , bg=bg_colour, fg="white", font=("TkHeadingFont", 20, 'underline'), cursor="hand2", bd=0, activebackground=bg_colour, bordercolor=bg_colour, focuscolor=bg_colour, highlightbackground=bg_colour).pack()



# run app
window.mainloop()