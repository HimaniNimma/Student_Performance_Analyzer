import tkinter as tk
from tkinter import ttk, messagebox
from src.student import Student
from src.analyzer import Analyzer
class App:
    def __init__(self, root):
        self.analyzer = Analyzer()
        title = tk.Label(
             root,
             text="🎓 Student Performance Analyzer",
             font=("Segoe UI", 22, "bold"),
             bg="#F4F6F9",
             
             fg="#1E3A8A"
        )
        title.pack(pady=20)
        root.title("🎓 Student Performance Analyzer")
        root.geometry("1100x700")
        root.configure(bg="#F4F6F9")
        root.resizable(False, False)
        frm = tk.LabelFrame(
            root,
            text="📝 Add Student Details",
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#1E3A8A",
            padx=20,
            pady=20,
            bd=2
        )        
        frm.pack(fill="x", padx=25, pady=20)
        tk.Label(
            frm,
            text="Roll No",
            font=("Segoe UI", 10),
            bg="#FFFFFF"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")        
        self.roll = tk.Entry(
            frm,
            width=12,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1
        ); self.roll.grid(row=0, column=1, padx=5)
        tk.Label(
            frm,
            text="Name",
            font=("Segoe UI", 10),
            bg="#FFFFFF"
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")        
        self.name = tk.Entry(
            frm,
            width=20,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1
        ); self.name.grid(row=0, column=3, padx=5)
        tk.Label(
            frm,
            text="Marks (comma-separated)",
            font=("Segoe UI", 10),
            bg="#FFFFFF"
        ).grid(row=0, column=4, padx=10, pady=10, sticky="w")
        self.marks = tk.Entry(
            frm,
            width=25,
            font=("Segoe UI", 10),
            relief="solid",
            bd=1
        ); self.marks.grid(row=0, column=5, padx=5)
        tk.Button(
            frm,
            text="➕ Add Student",
            command=self.add,
            font=("Segoe UI", 10, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6
        ).grid(
            row=0,
            column=6,
            padx=15,
            pady=10
        )
        self.table = ttk.Treeview(root, columns=("Roll", "Name", "Average"), show="headings")
        self.table.heading("Roll", text="Roll No")
        self.table.heading("Name", text="Name")
        self.table.heading("Average", text="Average Marks")
        self.table.pack(fill="both", expand=True, padx=10, pady=5)
        btns = tk.Frame(root); btns.pack(pady=5)
        tk.Button(
            btns,
            text="📊 Show Statistics",
            command=self.analyzer.stats,
            bg="#16A34A",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=18,
            relief="flat",
            cursor="hand2"
        ).grid(row=0, column=0, padx=15)
        tk.Button(
            btns,
            text="📈 Visualize",
            command=lambda: self.analyzer.visualize(root),
            bg="#9333EA",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=18,
            relief="flat",
            cursor="hand2"
        ).grid(row=0, column=1, padx=15)
    def add(self):
        roll, name, marks_str = self.roll.get().strip(), self.name.get().strip(), self.marks.get().strip()
        if not roll or not name or not marks_str:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        try:
            marks = list(map(int, marks_str.split(",")))
            if any(m < 0 or m > 100 for m in marks): raise ValueError
            subjects = {f"Sub{i+1}": m for i, m in enumerate(marks)}
        except:
            messagebox.showerror("Error", "Marks must be numbers (0-100) separated by commas.")
            return
        student = Student(roll, name, subjects)
        self.analyzer.add(student)
        self.table.delete(*self.table.get_children())
        for s in self.analyzer.students:
            self.table.insert("", "end", values=(s.roll, s.name, f"{s.average():.2f}"))
        self.roll.delete(0, tk.END); self.name.delete(0, tk.END); self.marks.delete(0, tk.END)
