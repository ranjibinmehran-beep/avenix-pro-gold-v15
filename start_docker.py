import subprocess
import sys
import time

print("="*60)
print("🦅 Launching Avenix Pro Gold V8.5 in Hugging Face Docker Container 🦅")
print("="*60)

# 1. Start the trading bot scanner in the background
print("[Docker] Launching bot.py background market scanner...")
bot_process = subprocess.Popen([sys.executable, "bot.py"])

# Give the bot a moment to write initial status
time.sleep(2)

# 2. Start Streamlit on port 7860 (Hugging Face's default expected port)
print("[Docker] Launching dashboard.py Streamlit UI on Port 7860...")
try:
    subprocess.run([
        "streamlit", "run", "dashboard.py",
        "--server.port", "7860",
        "--server.address", "0.0.0.0",
        "--server.headless", "true"
    ])
except KeyboardInterrupt:
    print("[Docker] Shutting down services...")
    bot_process.terminate()
