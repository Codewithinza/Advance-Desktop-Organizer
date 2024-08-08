import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class DesktopCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pastel Desktop Cleaner")
        self.root.geometry("500x300")
        self.root.configure(bg="#f5e3e0")  # Pastel background color
        
        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(self.root, text="Advanced Organizer", font=("Helvetica", 16), bg="#f5e3e0", fg="#333")
        title_label.pack(pady=10)

        select_folder_button = tk.Button(self.root, text="Select Desktop Folder", command=self.select_folder, bg="#d7e9d7", fg="#333", font=("Helvetica", 12))
        select_folder_button.pack(pady=20)

        self.organize_button = tk.Button(self.root, text="Organize Desktop", command=self.organize_desktop, bg="#c6d7eb", fg="#333", font=("Helvetica", 12))
        self.organize_button.pack(pady=20)
        self.organize_button.config(state=tk.DISABLED)

        self.status_label = tk.Label(self.root, text="", bg="#f5e3e0", fg="#333", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.organize_button.config(state=tk.NORMAL)
            self.status_label.config(text=f"Selected: {self.folder_path}")

    def organize_desktop(self):
        file_types = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
            "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
            "Music": [".mp3", ".wav", ".aac"],
            "Videos": [".mp4", ".mov", ".avi"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Code": [".py", ".js", ".html", ".css", ".java"],
        }

        for folder_name, extensions in file_types.items():
            folder_path = os.path.join(self.folder_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for file in os.listdir(self.folder_path):
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension in extensions:
                    shutil.move(os.path.join(self.folder_path, file), folder_path)

        self.status_label.config(text="Desktop Organized Successfully!", fg="#4CAF50")
        messagebox.showinfo("Success", "Your desktop has been organized!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopCleanerApp(root)
    root.mainloop()
