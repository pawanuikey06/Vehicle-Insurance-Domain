import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# Debug: Check the resolved root path
project_root = from_root()
print(f"Project Root: {project_root}")  # Debugging line

# Constants for log configuration
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Number of backup log files to keep

# Construct log file path
log_dir_path = os.path.join(os.getcwd(), LOG_DIR)


# Debug: Check directory path
print(f"Log Directory Path: {log_dir_path}")  # Debugging line

# Ensure directory exists
if not os.path.exists(log_dir_path):
    try:
        os.makedirs(log_dir_path, exist_ok=True)
        print(f"Logs directory created at: {log_dir_path}")  # Debugging line
    except Exception as e:
        print(f"Error creating logs directory: {e}")  # Debugging line

log_file_path = os.path.join(log_dir_path, LOG_FILE)

# Debug: Check file path
print(f"Log File Path: {log_file_path}")  # Debugging line

def configure_logger():
    logger = logging.getLogger()

    if logger.hasHandlers():
        return

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler
    try:
        file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
    except Exception as e:
        print(f"Error creating file handler: {e}")  # Debugging line

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)  # Change to DEBUG
    logger.addHandler(console_handler)

# Configure logger
configure_logger()


