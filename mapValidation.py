import tkinter as tk
from tkinter import filedialog, messagebox
import xml.etree.ElementTree as ET

class FileValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Map Validation")

        self.file_path = tk.StringVar()
        self.error_list = []

        self.create_widgets()


    def create_widgets(self):
        self.file_label = tk.Label(self.root, text="Select File:")
        self.file_label.grid(row=0, column=0, padx=5, pady=5)

        self.file_entry = tk.Entry(self.root, textvariable=self.file_path, width=50)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        self.validate_button = tk.Button(self.root, text="Validate", command=self.validate_file)
        self.validate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.error_listbox = tk.Listbox(self.root, width=70, height=15)
        self.error_listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.export_button = tk.Button(self.root, text="Export Errors", command=self.export_errors)
        self.export_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)


    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)


    def validate_text_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines, start=1):
                # Example validation: Check if line contains 'ERROR'
                if 'ERROR' in line:
                    error_info = {
                        'error_description': 'Line contains ERROR',
                        'line_number': line_num,
                        'line_content': line.strip(),
                        'file_name': file_path
                    }
                    self.error_list.append(error_info)


    def validate_xml_file(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        if len(root) > 1:
            error_info = {
                'rule_number': 1,
                'rule_content': 'XML has more than 5 children',
                'error_description': 'XML validation failed',
            }
            self.error_list.append(error_info)


    def validate_file(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file.")
            return

        self.error_list = []

        if file_path.endswith('.txt'):
            self.validate_text_file(file_path)
        elif file_path.endswith('.xml'):
            self.validate_xml_file(file_path)
        else:
            messagebox.showerror("Error", "Unsupported file format.")
            return

        self.display_errors()


    def display_errors(self):
        self.error_listbox.delete(0, tk.END)
        for error in self.error_list:
            if 'line_number' in error:
                error_str = f"File: {error['file_name']} | Line: {error['line_number']} | Error: {error['error_description']}"
            elif 'rule_number' in error:
                error_str = f"Rule: {error['rule_number']} | Error: {error['error_description']}"
            self.error_listbox.insert(tk.END, error_str)


    def export_errors(self):
        if not self.error_list:
            messagebox.showinfo("Info", "No errors to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                for error in self.error_list:
                    file.write(str(error) + "\n")
            messagebox.showinfo("Info", "Errors exported successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileValidatorApp(root)
    root.mainloop()

