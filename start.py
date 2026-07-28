import subprocess
import sys
import time
import os

print("="*60)
print("🦅 Launching Multi-Timeframe Trading Bot Suite on Cloud Server 🦅")
print("="*60)

# Get port from environment variables (Render uses dynamic PORT, Liara uses 8000 by default)
port = os.environ.get("PORT", "8000")

# 1. Start the trading bot scanner in the background
print("[System] Launching bot.py background market scanner...")
bot_process = subprocess.Popen([sys.executable, "bot.py"])

# Give the bot a moment to start and write initial status
time.sleep(2)

# 2. Start the Streamlit web dashboard in the foreground
print(f"[System] Launching dashboard.py Streamlit UI on Port {port}...")
try:
    subprocess.run([
        "streamlit", "run", "dashboard.py",
        "--server.port", port,
        "--server.address", "0.0.0.0",
        "--server.headless", "true"
    ])
except KeyboardInterrupt:
    print("[System] Shutting down services...")
    bot_process.terminate()
