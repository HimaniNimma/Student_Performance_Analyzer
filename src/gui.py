import tkinter as tk
from tkinter import ttk, messagebox
from src.student import Student
from src.analyzer import Analyzer
class App:
    def __init__(self, root):
        self.root = root
        self.analyzer = Analyzer()
        # ---------------- Window ---------------- #
        root.title("🎓 Student Performance Analyzer")
        root.geometry("1100x700")
        root.configure(bg="#F4F6F9")
        root.resizable(False, False)
        # ---------------- Title ---------------- #
        title = tk.Label(
            root,
            text="🎓 Student Performance Analyzer",
            font=("Segoe UI", 22, "bold"),
            bg="#F4F6F9",
            fg="#1E3A8A"
        )
        title.pack(pady=20)
        # ---------------- Student Details Frame ---------------- #
        frm = tk.LabelFrame(
            root,
            text="📝 Add Student Details",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg="#1E3A8A",
            padx=20,
            pady=20,
            bd=2
        )
        frm.pack(fill="x", padx=20, pady=10)
        # ---------------- Roll Number ---------------- #
        tk.Label(
            frm,
            text="Roll No",
            font=("Segoe UI", 10),
            bg="white"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.roll = tk.Entry(
            frm,
            width=15,
            font=("Segoe UI", 10),
            relief="groove",
            bd=2
        )
        self.roll.grid(row=0, column=1, padx=5)
        # ---------------- Name ---------------- #
        tk.Label(
            frm,
            text="Name",
            font=("Segoe UI", 10),
            bg="white"
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.name = tk.Entry(
            frm,
            width=28,
            font=("Segoe UI", 10),
            relief="groove",
            bd=2
        )
        self.name.grid(row=0, column=3, padx=5)
        # ---------------- Marks ---------------- #
        tk.Label(
            frm,
            text="Marks (comma separated)",
            font=("Segoe UI", 10),
            bg="white"
        ).grid(row=0, column=4, padx=10, pady=10, sticky="w")
        self.marks = tk.Entry(
            frm,
            width=35,
            font=("Segoe UI", 10),
            relief="groove",
            bd=2
        )
        self.marks.grid(row=0, column=5, padx=5)
        # ---------------- Add Button ---------------- #
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
            bd=0,
            cursor="hand2",
            padx=15,
            pady=7
        ).grid(row=0, column=6, padx=20)
        # ---------------- Table Style ---------------- #
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="white",
            foreground="#333333",
            rowheight=38,
            font=("Segoe UI", 10),
            fieldbackground="white"
        )
        style.configure(
            "Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Segoe UI", 11, "bold")
        )
        style.map(
            "Treeview.Heading",
            background=[("active", "#1D4ED8")]
        )
        style.map(
            "Treeview",
            background=[("selected", "#2563EB")],
            foreground=[("selected", "white")]
        )
        # ---------------- Student Table ---------------- #
        table_frame = tk.Frame(root, bg="#F4F6F9")
        table_frame.pack(fill="both", expand=True, padx=20)
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side="right", fill="y")
        self.table = ttk.Treeview(
            table_frame,
            columns=("Roll", "Name", "Average"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.table.yview)
        self.table.heading("Roll", text="Roll No")
        self.table.heading("Name", text="Student Name")
        self.table.heading("Average", text="Average")
        self.table.column(
            "Roll",
            width=120,
            anchor="center"
        )
        self.table.column(
            "Name",
            width=450,
            anchor="center"
        )
        self.table.column(
            "Average",
            width=180,
            anchor="center"
        )
        self.table.tag_configure(
            "even",
            background="#F8FAFC"
        )
        self.table.tag_configure(
            "odd",
            background="white"
        )
        self.table.pack(fill="both", expand=True)
        # ---------------- Bottom Buttons ---------------- #
        btn_frame = tk.Frame(root, bg="#F4F6F9")
        btn_frame.pack(pady=15)
        tk.Button(
            btn_frame,
            text="📊 Show Statistics",
            command=self.analyzer.stats,
            bg="#16A34A",
            fg="white",
            activebackground="#15803D",
            activeforeground="white",
            relief="flat",
            bd=0,
            width=15,
            height=2,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).grid(row=0, column=0, padx=12)
        tk.Button(
            btn_frame,
            text="📈 Visualize",
            command=lambda: self.analyzer.visualize(root),
            bg="#9333EA",
            fg="white",
            activebackground="#7E22CE",
            activeforeground="white",
            relief="flat",
            bd=0,
            width=18,
            height=2,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).grid(row=0, column=1, padx=12)
    # ---------------- Footer ---------------- #
        footer = tk.Label(
            root,
            text="Developed by Himani Nimma",
            font=("Segoe UI", 9),
            bg="#F4F6F9",
            fg="gray40"
        )
        footer.pack(pady=(0, 10))
    # Add Student Function
    def add(self):
        roll = self.roll.get().strip()
        name = self.name.get().strip()
        marks_str = self.marks.get().strip()
        # ---------------- Validation ---------------- #
        if not roll or not name or not marks_str:
            messagebox.showerror(
                "Missing Information",
                "Please fill all the fields."
            )
            return
        try:
            marks = list(map(int, marks_str.split(",")))
            if any(mark < 0 or mark > 100 for mark in marks):
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid Marks",
                "Enter marks between 0 and 100 separated by commas.\n\nExample:\n85,90,76,88,95"
            )
            return
        subjects = {
            f"Subject {i+1}": mark
            for i, mark in enumerate(marks)
        }
        student = Student(
            roll,
            name,
            subjects
        )
        self.analyzer.add(student)
        # ---------------- Refresh Table ---------------- #
        self.table.delete(*self.table.get_children())
        for index, student in enumerate(self.analyzer.students):
            tag = "even" if index % 2 == 0 else "odd"
            self.table.insert(
                "",
                "end",
                values=(
                    student.roll,
                    student.name,
                    f"{student.average():.2f}"
                ),
                tags=(tag,)
            )
        # ---------------- Clear Entry Boxes ---------------- #
        self.roll.delete(0, tk.END)
        self.name.delete(0, tk.END)
        self.marks.delete(0, tk.END)
        self.roll.focus()
        # ---------------- Success Message ---------------- #
        messagebox.showinfo(
            "Success",
            "Student record added successfully!"
        )        