import tkinter as tk

# inititalization
window = tk.Tk()
frame = tk.Frame(window)

# frame tweaks
window.title('Calculator')
button = tk.Button(window, text='Test', width=25, command=window.destroy)
input = tk.Entry(window, width=50, )

# packing everything into window
frame.pack()
button.pack()

txt_input = tk.Text()

# run
window.mainloop()