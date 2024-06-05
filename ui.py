import tkinter as tk
from tkinter import filedialog, messagebox
from validator import validate_file, export_errors
from read_file import read_file


class FileValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Validator")
        self.file_path = tk.StringVar()
        self.error_list = []
        self.error_counts = {}

        self.create_widgets()


    def create_widgets(self):
        self.file_label = tk.Label(self.root, text="Select File:")
        self.file_label.grid(row=0, column=0, padx=5, pady=5)

        self.file_entry = tk.Entry(self.root, textvariable=self.file_path, width=50)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        self.validate_button = tk.Button(self.root, text="Validate", command=self.validate_file)
        self.validate_button.grid(row=0, column=3, padx=5, pady=5)

        self.export_button = tk.Button(self.root, text="Export Errors", command=self.export_errors)
        self.export_button.grid(row=0, column=4, padx=5, pady=5)

        self.close_button = tk.Button(self.root, text="Close", command=self.root.quit)
        self.close_button.grid(row=0, column=5, padx=5, pady=5)

        self.error_summary = tk.Listbox(self.root, width=150, height=5)
        self.error_summary.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

        self.error_listbox = tk.Listbox(self.root, width=150, height=15)
        self.error_listbox.grid(row=2, column=0, columnspan=6, padx=5, pady=5)


    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)


    def validate_file(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file.")
            return

        self.error_list = []
        self.error_counts = {}
        self.file_content = {} 
        read_file(file_path, self.file_content)

        validate_file(file_path, self.error_list, self.error_counts)
        self.display_errors()


    def display_errors(self):
        self.error_summary.delete(0, tk.END)
        error_sum_title = f'{"Map Name":50} | {"Status":12} | {"Errors":12} | {"Warnings":12} | {"Information":12}'
        print(f"{self.error_counts = }")
        self.error_summary.insert(tk.END, error_sum_title)
        for mapName, status in self.error_counts.items():
            error_str = f'{mapName:55} | {status["status"]:12} | {status["errors"]:12} | {status["warnings"]:12} | {status["info"]:12}'
            print(f"{error_str = }")
            self.error_summary.insert(tk.END, error_str) 

        self.error_listbox.delete(0, tk.END)
        error_title = f"{'File':50} | {'Line':20} | {'Error':20}"
        self.error_listbox.insert(tk.END, error_title)
        for error in self.error_list:
            if 'line_number' in error:
                error_str = f"{error['file_name']:50} | {error['line_number']:20} | {error['error_description']:50}"
            elif 'rule_number' in error:
                error_str = f"{error['rule_number']} | x | {error['error_description']}"
            self.error_listbox.insert(tk.END, error_str)


    def export_errors(self):
        if not self.error_list:
            messagebox.showinfo("Info", "No errors to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            export_errors(self.error_list, file_path)
            messagebox.showinfo("Info", "Errors exported successfully.")

