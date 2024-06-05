import tkinter as tk
from ui import FileValidatorApp

def main():
    error_list = []
    error_counts = {} 

    root = tk.Tk()
    app = FileValidatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

