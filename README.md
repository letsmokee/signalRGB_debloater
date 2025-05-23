# 🧹 SignalRGB Debloater

![Logo](./icon.png)

![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Platform: Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)

A lightweight Windows utility that removes unwanted RGB control plugins from [SignalRGB](https://www.signalrgb.com/) to save CPU usage — automatically and silently.

---

## 💡 Why?

SignalRGB installs support for *all* major RGB brands by default, whether you use them or not. These plugins:

- Reinstall every time SignalRGB updates.
- Consume unnecessary CPU in the background.
- Add clutter and overhead.

This tool **cleans** the `Plugins` and `Components` folders of SignalRGB and **only keeps** the brands you care about.

---

## ⚙️ Features

- ✅ Automatically detects the latest installed version of SignalRGB.
- ✅ Deletes unused folders in both `Plugins` and `Components`.
- ✅ Keeps only the folders listed in `keep.txt` (created automatically).
- ✅ Safe prompt if no folders are listed — you choose whether to continue.
- ✅ Case-insensitive matching.
- ✅ Fully portable – just drop it next to `keep.txt` and run.
- ✅ Notification after successful cleanup.

---

## 📂 Example `keep.txt`

```
ASUS
MSI
Generic
XPG
```

Anything **not listed** here will be deleted on each SignalRGB update.

---

## 📝 How to Use

1. 📥 Download or compile the script to `.exe` (see below).
2. 🧾 On first run, it generates a `keep.txt` file next to the `.exe`.
3. ✍️ Edit `keep.txt` and list **only** the folders you want to keep.
4. ▶️ Run the app manually or automatically on startup.
5. ✅ Done! Unwanted plugins/components will be deleted.

---

## 🖥️ Path It Cleans

The script targets folders like:

```
C:\Users\<YourName>\AppData\Local\VortxEngine\app-*/Signal-x64/Plugins
C:\Users\<YourName>\AppData\Local\VortxEngine\app-*/Signal-x64/Components
```

Automatically handles version changes like `app-2.4.57`, `app-2.5.0`, etc.

---

## 🛠️ Compile to EXE

Use [`auto-py-to-exe`](https://github.com/brentvollebregt/auto-py-to-exe) to build a single executable:

```bash
pyinstaller --noconsole --onefile debloat_signalRGB.py
```

- ✅ `--onefile`: makes it portable
- ✅ `--noconsole`: runs silently (no terminal window)

---

## 🚀 Add to Windows Startup

You can run this tool automatically at each Windows boot using one of two methods:

### 🗂️ Method 1: Startup Folder (simplest)

1. Press `Win + R`, type `shell:startup`, press **Enter**.
2. Copy and paste a shortcut to your `.exe` into that folder.
3. Done! It will run each time you log in.

### 🕒 Method 2: Task Scheduler (recommended for admin/silent run)

1. Open **Task Scheduler** (search it in the Start Menu).
2. Click **Create Task** (not *Basic Task*).
3. Under the **General** tab:
   - Name: `SignalRGB Debloater`
   - Check **Run with highest privileges**
   - Set **Configure for** to your OS (e.g. Windows 10/11)
4. Under the **Triggers** tab:
   - Click **New...**
   - Begin the task: **At log on**
   - Optionally restrict to specific user
5. Under the **Actions** tab:
   - Click **New...**
   - Action: **Start a program**
   - Browse for your `.exe` file
6. Click **OK**, and enter your password if prompted

This will run silently in the background on every login, even with UAC restrictions.

---

## 🧹 Before vs After (Visual Example)

| Before (Default)        | After (Debloated)      |
|-------------------------|------------------------|
| ASUS, MSI, Gigabyte, NZXT, Razer, CoolerMaster, Thermaltake, ... | ASUS, MSI |

This removes folders that SignalRGB installs but you don’t use.

---

## 📄 License

MIT — do what you want, no warranty.  
Pull requests welcome!

---

## 🙏 Credits

Developed to solve a real-world annoyance with SignalRGB.  
Inspired by frustration. Powered by Python. 😅

---
