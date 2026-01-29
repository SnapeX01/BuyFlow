"""
Configuration module for Project Aurora.
Handles application-wide constants and settings.
"""

APP_NAME = "Project Aurora"
VERSION = "1.0.0"

DATABASE = {
    "host": "localhost",
    "port": 5432,
    "name": "aurora_db",
    "user": "admin",
    "timeout": 30
}

LOG_LEVEL = "INFO"
ENABLE_AUDIT_LOGS = True
