import tkinter as tk
from tkinter import messagebox, Toplevel
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.student import Student
class Analyzer:
    def __init__(self): 
        self.students = []
    def add(self, student):
        for i, s in enumerate(self.students):
            if s.roll == student.roll:  
                self.students[i] = student
                return
        self.students.append(student)
    def stats(self):
        if not self.students:
            messagebox.showerror("Error", "No student records!")
            return
        popup = Toplevel()
        popup.title("Class Performance Dashboard")
        popup.geometry("520x500")
        popup.configure(bg="#111827")
        avgs = np.array([s.average() for s in self.students])
        names = [s.name for s in self.students]
        class_avg = np.mean(avgs)
        median = np.median(avgs)
        std_dev = np.std(avgs)
        highest = np.max(avgs)
        lowest = np.min(avgs)
        top_student = names[np.argmax(avgs)]
        low_student = names[np.argmin(avgs)]
        grades = {
            "A (>=85)": np.sum(avgs >= 85),
            "B (70-84)": np.sum((avgs >= 70) & (avgs < 85)),
            "C (50-69)": np.sum((avgs >= 50) & (avgs < 70)),
            "Fail (<50)": np.sum(avgs < 50),
        }
        tk.Label(popup, text="📊 Class Performance Overview",
                 font=("Segoe UI Semibold", 17),
                 bg="#111827", fg="white").pack(pady=20)

        info = f"""
Total Students: {len(self.students)}

Class Average: {class_avg:.2f}
Median Score: {median:.2f}
Standard Deviation: {std_dev:.2f}

Top Performer: {top_student} ({highest:.2f})
Lowest Performer: {low_student} ({lowest:.2f})
"""
        tk.Label(popup, text=info,
                 font=("Segoe UI", 12),
                 bg="#111827", fg="#D1D5DB",
                 justify="left").pack(pady=10)

        tk.Label(popup, text="Grade Distribution",
                 font=("Segoe UI Semibold", 14),
                 bg="#111827", fg="#60A5FA").pack(pady=10)

        for grade, count in grades.items():
            tk.Label(popup, text=f"{grade}: {count}",
                     font=("Segoe UI", 11),
                     bg="#111827", fg="white").pack()
    def visualize(self, parent):
        if not self.students:
            messagebox.showerror("Error", "No student records!")
            return

        popup = Toplevel(parent)
        popup.title("Performance Chart")
        popup.geometry("950x550")
        popup.configure(bg="white")

        names = [s.name for s in self.students]
        avgs = [s.average() for s in self.students]

        fig_width = max(7, len(names) * 1.2)

        fig, ax = plt.subplots(figsize=(fig_width, 5), dpi=100)

        bars = ax.bar(
            names,
            avgs,
            color="#4DA6FF",
            edgecolor="#1E3A8A",
            linewidth=1.5,
            width=0.55
        )

        # Chart Title
        ax.set_title(
            "Average Marks per Student",
            fontsize=18,
            fontweight="bold",
            pad=20
        )

        # Axis Labels
        ax.set_ylabel(
            "Marks",
            fontsize=12,
            fontweight="bold"
        )

        ax.set_xlabel(
            "Students",
            fontsize=12,
            fontweight="bold"
        )

        # Leave space above tallest bar
        ax.set_ylim(0, 110)

        # Grid
        ax.grid(axis="y", linestyle="--", alpha=0.4)

        # Rotate names
        plt.xticks(rotation=30, ha="right")

        # Value labels
        for bar, val in zip(bars, avgs):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                val + 1.5,
                f"{val:.1f}",
                ha="center",
                va="bottom",
                fontsize=10,
                fontweight="bold"
            )

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  
        