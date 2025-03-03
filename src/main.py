if __name__ == '__main__':
    import tkinter as tk
    from tkinter import messagebox
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    def plot_function():
        try:
            expression = entry.get()

            def f(x):
                return eval(expression)

            x = np.linspace(-10, 10, 400)
            y = f(x)

            ax.clear()

            ax.plot(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title(f'func graphic: {expression}')
            ax.grid(True)

            canvas.draw()
        except Exception as e:
            messagebox.showerror("fault", f"wrong input: {e}")

    root = tk.Tk()
    root.title("Simple calculator")

    entry = tk.Entry(root, width=80)
    entry.pack(pady=10)

    button = tk.Button(root, text="Create a graphic", command=plot_function)
    button.pack(pady=10)

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()
