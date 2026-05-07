import customtkinter as ctk
from tkinter import filedialog
import threading
import time

# -----------------------------
# APP CONFIG
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()

app.geometry("1100x750")
app.title("Cyber APK Analyzer")

# -----------------------------
# TITLE
# -----------------------------

title = ctk.CTkLabel(
    app,
    text="CYBER APK ANALYZER",
    font=("Consolas", 34, "bold"),
    text_color="#00FF99"
)

title.pack(pady=20)

# -----------------------------
# SUBTITLE
# -----------------------------

subtitle = ctk.CTkLabel(
    app,
    text="Android Security Analysis Interface",
    font=("Consolas", 14),
    text_color="#AAAAAA"
)

subtitle.pack(pady=5)

# -----------------------------
# STATUS LABEL
# -----------------------------

status_label = ctk.CTkLabel(
    app,
    text="[ SYSTEM READY ]",
    font=("Consolas", 14, "bold"),
    text_color="#00FF99"
)

status_label.pack(pady=10)

# -----------------------------
# PROGRESS BAR
# -----------------------------

progress = ctk.CTkProgressBar(
    app,
    width=600,
    progress_color="#00FF99"
)

progress.pack(pady=10)

progress.set(0)

# -----------------------------
# OUTPUT TERMINAL
# -----------------------------

output = ctk.CTkTextbox(
    app,
    width=950,
    height=500,
    font=("Consolas", 14),
    text_color="#00FF99",
    fg_color="#111111",
    border_width=2,
    border_color="#00FF99"
)

output.pack(pady=25)

# -----------------------------
# TYPING EFFECT
# -----------------------------

def type_text(text, delay=0.01):

    for char in text:
        output.insert("end", char)
        output.see("end")
        output.update()
        time.sleep(delay)

# -----------------------------
# SMOOTH PROGRESS
# -----------------------------

def animate_progress(target):

    current = progress.get()

    while current < target:
        current += 0.01
        progress.set(current)
        app.update()
        time.sleep(0.01)

# -----------------------------
# ANALYSIS FUNCTION
# -----------------------------

def run_analysis(file_path):

    output.delete("1.0", "end")

    # STEP 1
    status_label.configure(text="[ LOADING APK ]")

    animate_progress(0.2)

    logs = [
        "[+] Initializing APK analysis engine...\n",
        "[+] Parsing AndroidManifest.xml...\n",
        "[+] Preparing analysis modules...\n\n"
    ]

    for log in logs:
        type_text(log)

    time.sleep(0.5)

    # STEP 2
    status_label.configure(text="[ ENUMERATING PERMISSIONS ]")

    animate_progress(0.5)

    logs2 = [
        "[+] Enumerating application permissions...\n",
        "[+] Checking exported activities...\n",
        "[+] Collecting metadata...\n\n"
    ]

    for log in logs2:
        type_text(log)

    time.sleep(0.5)

    # STEP 3
    status_label.configure(text="[ ANALYZING COMPONENTS ]")

    animate_progress(0.8)

    logs3 = [
        "[+] Running component analysis...\n",
        "[+] Mapping APK structure...\n",
        "[+] Finalizing security report...\n\n"
    ]

    for log in logs3:
        type_text(log)

    time.sleep(0.5)

    # OUTPUT SECTION

    type_text("========== APK INFORMATION ==========\n\n", 0.003)

    type_text(f"Selected APK:\n{file_path}\n\n", 0.002)

    type_text("Package Name:\ncom.cyber.demo.application\n\n", 0.002)

    # PERMISSIONS

    type_text("========== PERMISSIONS ==========\n\n", 0.003)

    permissions = [
        "android.permission.INTERNET",
        "android.permission.ACCESS_NETWORK_STATE",
        "android.permission.CAMERA",
        "android.permission.READ_EXTERNAL_STORAGE",
        "android.permission.WRITE_EXTERNAL_STORAGE",
        "android.permission.ACCESS_WIFI_STATE"
    ]

    for perm in permissions:
        type_text(f"[+] {perm}\n", 0.002)

    # ACTIVITIES

    type_text("\n========== ACTIVITIES ==========\n\n", 0.003)

    activities = [
        "MainActivity",
        "LoginActivity",
        "SettingsActivity",
        "DashboardActivity",
        "ProfileActivity"
    ]

    for act in activities:
        type_text(f"[+] {act}\n", 0.002)

    # FINAL STATUS

    animate_progress(1.0)

    status_label.configure(
        text="[ ANALYSIS COMPLETE ]",
        text_color="#00FF99"
    )

# -----------------------------
# BUTTON FUNCTION
# -----------------------------

def analyze_apk():

    file_path = filedialog.askopenfilename(
        filetypes=[("APK Files", "*.apk")]
    )

    if not file_path:
        return

    thread = threading.Thread(
        target=run_analysis,
        args=(file_path,)
    )

    thread.start()

# -----------------------------
# ANALYZE BUTTON
# -----------------------------

analyze_button = ctk.CTkButton(
    app,
    text="SELECT APK",
    command=analyze_apk,
    width=220,
    height=45,
    font=("Consolas", 16, "bold"),
    fg_color="#00AA66",
    hover_color="#00CC88",
    text_color="black"
)

analyze_button.pack(pady=10)

# -----------------------------
# FOOTER
# -----------------------------

footer = ctk.CTkLabel(
    app,
    text="Cybersecurity GUI Prototype • Python + CustomTkinter",
    font=("Consolas", 12),
    text_color="#777777"
)

footer.pack(pady=15)

# -----------------------------
# RUN APP
# -----------------------------

app.mainloop()