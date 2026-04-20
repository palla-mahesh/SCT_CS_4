import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# ---------------- Global Variables ---------------- #
logging_enabled = False
log_data = []

# ---------------- Functions ---------------- #
def start_logging():
    global logging_enabled
    logging_enabled = True
    status_var.set("Status: Logging ON ✅")

def stop_logging():
    global logging_enabled
    logging_enabled = False
    status_var.set("Status: Logging OFF ⛔")

def clear_logs():
    global log_data
    log_data.clear()
    text_area.delete("1.0", tk.END)
    messagebox.showinfo("Cleared", "Logs cleared successfully!")

def export_logs():
    if not log_data:
        messagebox.showwarning("No Data", "No logs to save!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            for line in log_data:
                f.write(line + "\n")
        messagebox.showinfo("Saved", "Logs exported successfully!")

def on_key(event):
    if not logging_enabled:
        return

    key = event.keysym

    # Mask letters for privacy
    if len(key) == 1:
        key_display = "*"
    else:
        key_display = f"<{key}>"

    timestamp = datetime.now().strftime("%H:%M:%S")
    log_entry = f"{timestamp} - {key_display}"

    log_data.append(log_entry)
    text_area.insert(tk.END, log_entry + "\n")
    text_area.see(tk.END)


# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Safe Key Event Logger 🔐")
root.geometry("500x400")
root.config(bg="#1e1e2f")

# Title
tk.Label(root, text="Safe Key Event Logger",
         font=("Arial", 16, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Status
status_var = tk.StringVar(value="Status: Logging OFF ⛔")
tk.Label(root, textvariable=status_var,
         bg="#1e1e2f", fg="yellow").pack()

# Input Box
tk.Label(root, text="Type here (logging inside app only):",
         bg="#1e1e2f", fg="white").pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.bind("<Key>", on_key)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Start ▶️", command=start_logging,
          bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Stop ⛔", command=stop_logging,
          bg="#f44336", fg="white", width=10).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Clear 🧹", command=clear_logs,
          bg="#ff9800", fg="white", width=10).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="Export 📁", command=export_logs,
          bg="#2196F3", fg="white", width=10).grid(row=0, column=3, padx=5)

# Log Display
text_area = tk.Text(root, height=12, width=60)
text_area.pack(pady=10)

# Run
root.mainloop()