import subprocess
import sys
import streamlit as st

# --- AUTOMATIC BACKGROUND BOT LAUNCHER FOR HUGGING FACE SPACES ---
@st.cache_resource
def start_background_bot():
    try:
        print("[Avenix Cloud] Launching bot.py background market scanner...")
        # Start bot.py as a separate background process
        process = subprocess.Popen([sys.executable, "bot.py"])
        return process
    except Exception as e:
        print(f"[Avenix Cloud Error] Failed to start background bot: {e}")
        return None

# Trigger the background bot exactly once on app startup
bot_process = start_background_bot()

# Now run the entire dashboard interface
try:
    import dashboard
except Exception as e:
    st.error(f"خطا در اجرای داشبورد آونیکس: {e}")
