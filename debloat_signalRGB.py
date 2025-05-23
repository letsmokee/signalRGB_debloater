import os
import shutil
import ctypes
import sys
from packaging import version

# Correct path to the folder where the .exe or .py is running
SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
KEEP_FILE = os.path.join(SCRIPT_DIR, "keep.txt")

# SignalRGB base install location
SIGNAL_BASE = os.path.join(os.environ["LOCALAPPDATA"], "VortxEngine")

def ensure_keep_file_exists():
    if not os.path.exists(KEEP_FILE):
        with open(KEEP_FILE, "w", encoding="utf-8") as f:
            f.write("# Enter folder names you want to keep (one per line, e.g., ASUS, MSI, XPG)\n")

def load_allowed_folders():
    try:
        with open(KEEP_FILE, "r", encoding="utf-8") as f:
            return {line.strip().lower() for line in f if line.strip() and not line.strip().startswith("#")}
    except:
        return set()

def confirm_continue_with_empty_list():
    return ctypes.windll.user32.MessageBoxW(
        0,
        "No folders were read from keep.txt.\nDo you want to continue and delete all plugins/components?",
        "SignalRGB Debloat",
        0x01 | 0x30  # Yes/No with warning icon
    ) == 1

def notify(title, message):
    try:
        ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)
    except:
        pass

def get_latest_app_folder():
    try:
        app_folders = [f for f in os.listdir(SIGNAL_BASE) if f.lower().startswith("app-")]
        if not app_folders:
            return None
        app_folders.sort(key=lambda f: version.parse(f.replace("app-", "")), reverse=True)
        return os.path.join(SIGNAL_BASE, app_folders[0])
    except:
        return None

def clean_folder(target_folder, allowed_folders):
    deleted_anything = False
    if not os.path.exists(target_folder):
        return False
    for entry in os.listdir(target_folder):
        entry_path = os.path.join(target_folder, entry)
        if os.path.isdir(entry_path) and entry.lower() not in allowed_folders:
            try:
                shutil.rmtree(entry_path, ignore_errors=True)
                deleted_anything = True
            except:
                pass
    return deleted_anything

def main():
    ensure_keep_file_exists()
    allowed_folders = load_allowed_folders()

    if not allowed_folders:
        if not confirm_continue_with_empty_list():
            return

    latest_app_path = get_latest_app_folder()
    if not latest_app_path:
        return

    signal_path = os.path.join(latest_app_path, "Signal-x64")
    plugins_path = os.path.join(signal_path, "Plugins")
    components_path = os.path.join(signal_path, "Components")

    deleted_plugins = clean_folder(plugins_path, allowed_folders)
    deleted_components = clean_folder(components_path, allowed_folders)

    if deleted_plugins or deleted_components:
        notify("SignalRGB Cleaned", "Debloating completed successfully.")

if __name__ == "__main__":
    main()
