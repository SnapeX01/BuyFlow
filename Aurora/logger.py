"""
Logging utility for Project Aurora.
Provides standardized logging across modules.
"""

import datetime

def log_event(level, message):
    timestamp = datetime.datetime.utcnow().isoformat()
    formatted = f"[{timestamp}] [{level}] {message}"
    print(formatted)

def info(message):
    log_event("INFO", message)

def warning(message):
    log_event("WARNING", message)

def error(message):
    log_event("ERROR", message)
