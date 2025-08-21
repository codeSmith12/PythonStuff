import tkinter as tk
from tkinter import ttk

def demo_app():
    root = tk.Tk()
    root.title("Tkinter Widgets Demo")
    root.geometry("800x600")

    # === Frames for organization ===
    top_frame = tk.Frame(root, pady=10)
    top_frame.pack(fill="x")

    mid_frame = tk.Frame(root, pady=10)
    mid_frame.pack(fill="x")

    bottom_frame = tk.Frame(root, pady=10)
    bottom_frame.pack(fill="both", expand=True)

    # === Basic Widgets ===
    tk.Label(top_frame, text="Label Widget").pack(side="left", padx=10)
    tk.Button(top_frame, text="Click Me", command=lambda: print("Button clicked!")).pack(side="left", padx=10)

    entry = tk.Entry(top_frame)
    entry.pack(side="left", padx=10)
    entry.insert(0, "Type here")

    tk.Text(top_frame, height=3, width=25).pack(side="left", padx=10)

    # === Selection Widgets ===
    tk.Label(mid_frame, text="Selection Widgets:").pack(anchor="w")

    var_check = tk.IntVar()
    tk.Checkbutton(mid_frame, text="Check me", variable=var_check).pack(anchor="w")

    var_radio = tk.StringVar(value="Option1")
    tk.Radiobutton(mid_frame, text="Option 1", variable=var_radio, value="Option1").pack(anchor="w")
    tk.Radiobutton(mid_frame, text="Option 2", variable=var_radio, value="Option2").pack(anchor="w")

    listbox = tk.Listbox(mid_frame, height=4)
    for fruit in ["Apple", "Banana", "Cherry"]:
        listbox.insert(tk.END, fruit)
    listbox.pack(side="left", padx=10)

    tk.Spinbox(mid_frame, from_=0, to=10).pack(side="left", padx=10)
    tk.Scale(mid_frame, from_=0, to=100, orient="horizontal").pack(side="left", padx=10)

    # === Advanced Widgets ===
    tk.Label(bottom_frame, text="Advanced Widgets:").pack(anchor="w")

    canvas = tk.Canvas(bottom_frame, width=150, height=100, bg="white")
    canvas.create_rectangle(20, 20, 100, 80, fill="blue")
    canvas.pack(side="left", padx=10)

    message = tk.Message(bottom_frame, text="This is a wrapped message widget.", width=150)
    message.pack(side="left", padx=10)

    pw = tk.PanedWindow(bottom_frame)
    pw.add(tk.Label(pw, text="Left Pane", bg="lightgray"))
    pw.add(tk.Label(pw, text="Right Pane", bg="lightblue"))
    pw.pack(side="left", padx=10)

    # === ttk Widgets ===
    notebook = ttk.Notebook(bottom_frame)
    tab1 = tk.Frame(notebook, bg="lightyellow")
    tab2 = tk.Frame(notebook, bg="lightgreen")
    notebook.add(tab1, text="Tab 1")
    notebook.add(tab2, text="Tab 2")
    notebook.pack(side="left", padx=10)

    tree = ttk.Treeview(bottom_frame)
    tree.insert("", "end", text="Parent")
    tree.insert("", "end", text="Child")
    tree.pack(side="left", padx=10)

    progress = ttk.Progressbar(bottom_frame, orient="horizontal", length=150, mode="determinate")
    progress['value'] = 50
    progress.pack(side="left", padx=10)

    # === Menu Example ===
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    demo_app()
