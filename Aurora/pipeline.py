"""
Pipeline module simulating data processing workflow.
"""

from logger import info
from security import validate_input

def process_data(data):
    info("Starting data processing pipeline")

    if not validate_input(data):
        info("Invalid input detected, aborting pipeline")
        return None

    result = data.upper()
    info("Pipeline completed successfully")
    return result

if __name__ == "__main__":
    sample = "aurora"
    output = process_data(sample)
    print("Output:", output)
