# 🛡️ Valheim Command Center ENTERPRISE

Sistema profesional de administración remota para servidores de **Valheim** usando:

- 🤖 Discord Bot
- 🔌 RCON
- 🖥️ GUI interactiva
- 📋 Consola integrada
- ⚙️ config.ini
- 🔐 Permisos por roles
- 🚫 Gestión de bans
- ✅ Gestión de whitelist
- 🛡️ Gestión de admins
- 🔄 Modo GUI / TERMINAL / SERVICE

Proyecto creado por **ChatGPT OpenAI y Azzlaer**.

---

# 🚀 Características

## 💬 Chat Bridge Discord → Valheim

Todo mensaje escrito en el canal configurado será enviado automáticamente al servidor Valheim usando:

```bash
say
```

Ejemplo:

```text
UsuarioDiscord: hola mundo
```

---

# 🛡️ Administración remota

## Canal ADMIN

Permite ejecutar comandos:

```bash
addAdmin 76561198000000000
removeAdmin 76561198000000000
adminlist
```

---

# 🚫 Sistema de baneados

## Canal BANEADOS

Permite:

```bash
ban PlayerName
banSteamId 76561198000000000
unban PlayerName
```

---

# ✅ Sistema de permitidos

## Canal PERMITIDOS

Permite:

```bash
addPermitted 76561198000000000
removePermitted 76561198000000000
permitted
```

---

# 🖥️ GUI ENTERPRISE

El proyecto incluye una interfaz gráfica profesional con:

- Consola integrada
- Logs en tiempo real
- Estado ONLINE/OFFLINE
- Botón START
- Botón STOP
- Consola interactiva RCON

---

# 📦 Modos del sistema

## GUI
Panel visual recomendado.

```ini
MODE = GUI
```

---

## TERMINAL
Modo consola tradicional.

```ini
MODE = TERMINAL
```

---

## SERVICE
Modo servidor persistente con auto-reinicio.

```ini
MODE = SERVICE
```

---

# 📄 config.ini

Ejemplo:

```ini
[DISCORD]
TOKEN = TU_TOKEN_AQUI

CHANNEL_CHAT = 111111111111111111
CHANNEL_ADMIN = 222222222222222222
CHANNEL_BAN = 333333333333333333
CHANNEL_PERMIT = 444444444444444444

ADMIN_ROLE = Admin

[RCON]
HOST = 127.0.0.1
PORT = 25575
PASSWORD = tu_password

[SYSTEM]
MODE = GUI
```

---

# 🤖 Crear el bot de Discord

## 1. Ir al portal de Discord

https://discord.com/developers/applications

---

## 2. Crear aplicación

- New Application
- Nombre del bot
- Create

---

## 3. Crear BOT

- Menú → Bot
- Add Bot

---

## 4. Activar intents

En la sección BOT activar:

- MESSAGE CONTENT INTENT
- SERVER MEMBERS INTENT (opcional)

---

## 5. Obtener TOKEN

Copiar el token y colocarlo en:

```ini
TOKEN =
```

---

# 🔗 Invitar el bot al servidor

## OAuth2 → URL Generator

Seleccionar:

### Scope
- bot

### Permissions
- View Channels
- Read Messages
- Send Messages
- Read Message History

Abrir URL generada e invitar el bot.

---

# 📋 Crear canales Discord

Crear:

- 💬 chat
- 🛡️ adminlist
- 🚫 baneados
- ✅ permitidos

---

# 🔐 Permisos recomendados

## Rol ADMIN

Crear rol:

```text
Admin
```

Asignarlo a usuarios autorizados.

---

# ⚙️ Requisitos

## Python

Recomendado:

- Python 3.11+

---

## Librerías

Instalar:

```bash
pip install discord.py
pip install mcrcon
```

---

# ▶️ Ejecutar proyecto

```bash
python main.py
```

---

# 🧠 Consola interactiva GUI

La GUI incluye consola integrada para ejecutar:

```bash
say hola
save
shutdown
kick PlayerName
```

---

# 📄 Logs

Todos los eventos son guardados en:

```text
app.log
```

---

# 🔥 Características ENTERPRISE

- Multi canal
- Logs persistentes
- GUI profesional
- Bridge Discord ↔ Valheim
- Control remoto
- Seguridad por roles
- Arquitectura escalable
- Consola interactiva
- Compatible con Windows

---

# 📌 Comandos compatibles

Documentación oficial:

https://github.com/Tristan-dvr/ValheimRcon/blob/master/commands.md

---

# ❤️ Créditos

Proyecto creado por:

- ChatGPT OpenAI
- Azzlaer

Para:

- LatinBattle.com

---

# ⚠️ Aviso

Este proyecto es una herramienta administrativa remota para servidores Valheim y requiere acceso válido al servidor RCON.

Uso bajo responsabilidad del administrador del servidor.
