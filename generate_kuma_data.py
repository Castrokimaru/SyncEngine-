import json
import time
import random
import os
import uuid
from datetime import datetime, timezone

# --- CONFIGURATION ---
LOG_RATE_PER_SECOND = 2
ERROR_PERCENTAGE = 5
LOG_FORMAT = "text"  # "text" or "json"
OUTPUT_LOG_FILE = "uptime-kuma.log"
DATA_DIR = "data"
SIMULATION_DURATION_SECONDS = 60  # Run for 1 minute for this demo

# --- LOG TEMPLATES ---
# Text: 2024-05-22T12:00:00Z [MODULE] LEVEL: msg (trace_id)
TEXT_TEMPLATE = "{timestamp} [{module}] {level}: {msg} (trace_id: {trace_id})"

# JSON: {"time":"2024-05-22T12:00:00Z","module":"SERVER","level":"info","msg":"Welcome to Uptime Kuma","trace_id":"..."}
# (Will use json.dumps for JSON format)


# --- MODULE DATA ---
MODULES = ["SERVER", "AUTH", "MONITOR", "DB", "MANAGE"]

MESSAGES = {
    "SERVER": {
        "info": ["Welcome to Uptime Kuma", "Loading modules", "Uptime Kuma Version: 1.23.11", "Env: production", "Data Dir: ./data"],
        "debug": ["Importing express", "Importing redbean-node", "Importing jsonwebtoken", "Adding route", "Init the server"],
        "warn": ["Your Node.js version: 18.0.0 is not officially supported"],
        "error": ["Failed to prepare your database: Connection lost"]
    },
    "AUTH": {
        "info": ["Login by username + password. IP=192.168.1.5", "Successfully logged in user admin. IP=192.168.1.5", "Login by token. IP=127.0.0.1"],
        "debug": ["afterLogin", "afterLogin ok", "check auto login"],
        "warn": ["Incorrect username or password for user guest. IP=10.0.0.42", "Invalid token. IP=172.16.0.5"],
        "error": ["Error changing 2FA token. IP=192.168.1.10"]
    },
    "MONITOR": {
        "info": ["Added Monitor: 5 User ID: 1", "Get Monitor: 3 User ID: 1", "Resume Monitor: 1 User ID: 1"],
        "debug": ["Globalping create measurement", "gRPC response: {\"status\":\"OK\"}", "MQTT connected"],
        "warn": ["Monitor #2 is down: 503 Service Unavailable", "TCP timeout triggered"],
        "error": ["Error adding Monitor: undefined", "DNS resolve error: ENOTFOUND"]
    },
    "DB": {
        "info": ["Connected to the database", "Database Patched Successfully", "Closing the database"],
        "debug": ["SQLite config:", "PRAGMA journal_mode", "Database.getSize()"],
        "warn": ["Max database connections capped to 100"],
        "error": ["Database migration failed", "SQLITE_BUSY: database is locked"]
    },
    "MANAGE": {
        "info": ["Delete Monitor: 12 User ID: 1", "Clear Heartbeats Monitor: 5 User ID: 1", "Clear Statistics User ID: 1"],
        "debug": [],
        "warn": [],
        "error": []
    }
}

def get_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def emit_log(module, level, msg):
    timestamp = get_timestamp()
    trace_id = str(uuid.uuid4())[:8]
    if LOG_FORMAT == "json":
        log_entry = {
            "time": timestamp,
            "module": module.upper(),
            "level": level.lower(),
            "msg": msg,
            "trace_id": trace_id
        }
        print(json.dumps(log_entry))
        with open(OUTPUT_LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    else:
        log_line = TEXT_TEMPLATE.format(
            timestamp=timestamp,
            module=module.upper(),
            level=level.upper(),
            msg=msg,
            trace_id=trace_id
        )
        print(log_line)
        with open(OUTPUT_LOG_FILE, "a") as f:
            f.write(log_line + "\n")


# --- BEHAVIORAL SIMULATION ---
def simulate_behavior():
    start_time = time.time()
    next_spike = start_time + random.randint(10, 20)
    in_spike = False
    spike_end = 0

    while time.time() - start_time < SIMULATION_DURATION_SECONDS:
        current_time = time.time()

        # Determine current log rate
        current_rate = LOG_RATE_PER_SECOND
        if in_spike:
            current_rate *= 5
            if current_time > spike_end:
                in_spike = False
                next_spike = current_time + random.randint(20, 40)
        elif current_time > next_spike:
            in_spike = True
            spike_end = current_time + random.randint(3, 7)
            emit_log("SERVER", "info", "Traffic spike detected - Increasing worker pool")

        # Random module and level
        module = random.choice(MODULES)

        # Error cascade simulation
        if random.random() * 100 < ERROR_PERCENTAGE:
            level = "error"
            if module == "DB":
                emit_log("DB", "error", "SQLITE_BUSY: database is locked")
                emit_log("MONITOR", "error", "Failed to save heartbeat to DB for monitor #5")
                emit_log("MONITOR", "error", "Failed to save heartbeat to DB for monitor #12")
            else:
                if level in MESSAGES[module] and MESSAGES[module][level]:
                    msg = random.choice(MESSAGES[module][level])
                    emit_log(module, level, msg)
                else:
                    # Fallback if no error messages defined
                    emit_log(module, "error", f"Unexpected internal error in {module}")
        else:
            level = random.choice(["info", "info", "info", "debug", "debug", "warn"])
            if level in MESSAGES[module] and MESSAGES[module][level]:
                msg = random.choice(MESSAGES[module][level])
                emit_log(module, level, msg)
            else:
                # Fallback to info if the chosen level is empty for that module
                if MESSAGES[module]["info"]:
                    msg = random.choice(MESSAGES[module]["info"])
                    emit_log(module, "info", msg)

        time.sleep(1.0 / current_rate)


# --- FILE SYSTEM MOCKING ---
def mock_filesystem():
    print(f"Creating mock production structure in ./{DATA_DIR}...")

    # Create directories
    dirs = [
        DATA_DIR,
        os.path.join(DATA_DIR, "upload"),
        os.path.join(DATA_DIR, "screenshots"),
        os.path.join(DATA_DIR, "docker-tls")
    ]
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"  Created directory: {d}")

    # Dummy .env
    with open(".env", "w") as f:
        f.write("PORT=3001\nDATA_DIR=./data\nNODE_ENV=production\n")
    print("  Created .env")

    # Dummy db-config.json
    db_config = {"type": "sqlite"}
    with open(os.path.join(DATA_DIR, "db-config.json"), "w") as f:
        json.dump(db_config, f, indent=4)
    print("  Created data/db-config.json")

    # Dummy kuma.db (empty file)
    with open(os.path.join(DATA_DIR, "kuma.db"), "w") as f:
        f.write("")
    print("  Created data/kuma.db")


# --- MAIN ---
if __name__ == "__main__":
    mock_filesystem()
    print(f"\nStarting log simulation (Format: {LOG_FORMAT})...")
    print(f"Outputting to {OUTPUT_LOG_FILE}\n")

    # Initialize log file
    with open(OUTPUT_LOG_FILE, "w") as f:
        pass

    try:
        simulate_behavior()
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

    print(f"\nSimulation complete. Logs saved to {OUTPUT_LOG_FILE}")
