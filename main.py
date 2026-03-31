# ============================================
# Valheim Discord RCON Bridge ENTERPRISE
# Full System: Discord Channels + GUI Console + RCON
# ============================================

import discord
from mcrcon import MCRcon
import configparser
import threading
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# =========================
# LOAD CONFIG
# =========================
config = configparser.ConfigParser()
config.read("config.ini")

DISCORD_TOKEN = config["DISCORD"]["TOKEN"]
CHANNEL_CHAT = int(config["DISCORD"]["CHANNEL_CHAT"])
CHANNEL_ADMIN = int(config["DISCORD"]["CHANNEL_ADMIN"])
CHANNEL_BAN = int(config["DISCORD"]["CHANNEL_BAN"])
CHANNEL_PERMIT = int(config["DISCORD"]["CHANNEL_PERMIT"])
ADMIN_ROLE = config["DISCORD"].get("ADMIN_ROLE", "Admin")

RCON_HOST = config["RCON"]["HOST"]
RCON_PORT = int(config["RCON"]["PORT"])
RCON_PASSWORD = config["RCON"]["PASSWORD"]

MODE = config["SYSTEM"]["MODE"]

# =========================
# GLOBAL
# =========================
bot_running = False
gui_console = None

# =========================
# LOGGER
# =========================
def log(msg):
    ts = time.strftime("[%H:%M:%S]")
    full = f"{ts} {msg}"

    with open("app.log", "a", encoding="utf-8") as f:
        f.write(full + "\n")

    print(full)

    if gui_console:
        gui_console.insert(tk.END, full + "\n")
        gui_console.see(tk.END)

# =========================
# RCON
# =========================
def send_rcon(cmd):
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            res = mcr.command(cmd)
            log(f"[RCON] {cmd} -> {res}")
            return res
    except Exception as e:
        log(f"[RCON ERROR] {e}")
        return str(e)

# =========================
# PERMISSIONS
# =========================
def is_admin(member):
    return any(role.name == ADMIN_ROLE for role in member.roles)

# =========================
# DISCORD SETUP
# =========================
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# =========================
# DISCORD EVENTS
# =========================
@client.event
async def on_ready():
    log(f"[SYSTEM] Bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.strip()
    user = message.author.display_name

    log(f"[DISCORD] {message.channel.name} | {user}: {content}")

    # ================= CHAT =================
    if message.channel.id == CHANNEL_CHAT:
        send_rcon(f"say {user}: {content}")
        return

    # ================= ADMIN =================
    if message.channel.id == CHANNEL_ADMIN:
        if not is_admin(message.author):
            await message.reply("❌ No tienes permisos")
            return

        res = send_rcon(content)
        await message.reply(f"📋 Resultado:\n{res}")
        return

    # ================= BAN =================
    if message.channel.id == CHANNEL_BAN:
        if not is_admin(message.author):
            await message.reply("❌ No tienes permisos")
            return

        res = send_rcon(content)
        await message.reply(f"🚫 Resultado:\n{res}")
        return

    # ================= PERMIT =================
    if message.channel.id == CHANNEL_PERMIT:
        if not is_admin(message.author):
            await message.reply("❌ No tienes permisos")
            return

        res = send_rcon(content)
        await message.reply(f"✅ Resultado:\n{res}")
        return

# =========================
# GUI COMMAND EXECUTION
# =========================
def execute_local_command(command):
    command = command.strip()

    if not command:
        return

    log(f"> {command}")
    response = send_rcon(command)

    if response:
        log(f"[RCON RESPONSE]\n{response}")

# =========================
# BOT CONTROL
# =========================
def start_bot():
    global bot_running

    if bot_running:
        log("[SYSTEM] Ya corriendo")
        return

    def run():
        global bot_running
        bot_running = True
        try:
            client.run(DISCORD_TOKEN)
        except Exception as e:
            log(e)
        bot_running = False

    threading.Thread(target=run, daemon=True).start()
    log("[SYSTEM] Bot iniciado")


def stop_bot():
    try:
        loop = client.loop
        loop.call_soon_threadsafe(loop.stop)
        log("[SYSTEM] Bot detenido")
    except Exception as e:
        log(e)

# =========================
# GUI
# =========================
def run_gui():
    global gui_console

    root = tk.Tk()
    root.title("Valheim Enterprise Panel")
    root.geometry("1000x700")

    tk.Label(root, text="VALHEIM ENTERPRISE PANEL", font=("Segoe UI", 18, "bold")).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack()

    tk.Button(frame, text="START", bg="green", fg="white", width=12, command=start_bot).grid(row=0, column=0, padx=5)
    tk.Button(frame, text="STOP", bg="red", fg="white", width=12, command=stop_bot).grid(row=0, column=1, padx=5)

    status = tk.Label(root, text="OFFLINE", fg="red")
    status.pack()

    def refresh():
        status.config(text="ONLINE" if bot_running else "OFFLINE", fg="green" if bot_running else "red")
        root.after(1000, refresh)

    refresh()

    # OUTPUT CONSOLE
    gui_console = ScrolledText(root, bg="#0f172a", fg="#22c55e", height=25)
    gui_console.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # INPUT CONSOLE
    input_frame = tk.Frame(root)
    input_frame.pack(fill=tk.X, padx=10, pady=5)

    entry = tk.Entry(input_frame, bg="#111", fg="#0f0", insertbackground="white")
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def send_command(event=None):
        cmd = entry.get()
        if not cmd:
            return

        execute_local_command(cmd)
        entry.delete(0, tk.END)

    entry.bind("<Return>", send_command)

    tk.Button(input_frame, text="Enviar", command=send_command).pack(side=tk.RIGHT, padx=5)

    root.mainloop()

# =========================
# SERVICE MODE
# =========================
def run_service():
    while True:
        try:
            client.run(DISCORD_TOKEN)
        except Exception as e:
            log(e)
            time.sleep(5)

# =========================
# MAIN
# =========================
if __name__ == "__main__":

    if MODE == "GUI":
        run_gui()

    elif MODE == "TERMINAL":
        client.run(DISCORD_TOKEN)

    elif MODE == "SERVICE":
        run_service()

    else:
        print("Modo inválido")
