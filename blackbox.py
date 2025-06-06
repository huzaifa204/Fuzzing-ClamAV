import os
import random
import subprocess
import string
from datetime import datetime

# Create output & log directories
os.makedirs("outputs", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def generate_random_pdf(filename, size=512):
    content = ''.join(random.choices(string.printable, k=size))
    with open(filename, 'wb') as f:
        f.write(content.encode('utf-8', 'ignore'))

def scan_with_clamav(filepath):
    result = subprocess.run(
        ['clamscan', filepath],
        capture_output=True,
        text=True
    )
    return result

for i in range(10):  # number of fuzzing attempts
    fname = f"outputs/fuzzed_{i}.pdf"
    generate_random_pdf(fname)

    result = scan_with_clamav(fname)

    log_filename = f"logs/scan_log_{i}.txt"
    with open(log_filename, 'w') as log:
        log.write(f"=== File: {fname} ===\n")
        log.write(f"Return Code: {result.returncode}\n")
        log.write(f"STDOUT:\n{result.stdout}\n")
        log.write(f"STDERR:\n{result.stderr}\n")

    if result.returncode != 0:
        print(f"[!] Anomaly on file {fname}: Code {result.returncode}")

