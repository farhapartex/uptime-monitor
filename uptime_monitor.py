import os
import time
import csv
import requests
from datetime import datetime
from ping3 import ping

# Configuration
URLS_TO_MONITOR = [
    "https://www.google.com",
    "https://www.github.com",
    "https://fb.com",
    "https://chatgpt.com",
    "https://www.nonexistentwebsite12345.com"  # Test for down site
]
CHECK_INTERVAL = 60  # In seconds
LOG_FILE = "uptime_logs.csv"

# Function to check HTTP status and response time
def check_http_status(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = round((time.time() - start_time) * 1000)  # ms
        status_code = response.status_code
        return status_code, response_time
    except requests.RequestException:
        return None, None

# Function to check ping status
def check_ping_status(url):
    try:
        hostname = url.split("//")[-1].split("/")[0]
        ping_time = ping(hostname)
        if ping_time:
            return round(ping_time * 1000)  # ms
        else:
            return None
    except Exception as e:
        print(f"Error in pinging {url}: {e}")
        return None

# Function to log results to a CSV file
def log_result(url, status, response_time, ping_time):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_data = [timestamp, url, status, response_time, ping_time]

    # Check if file exists for header
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "URL", "HTTP Status", "Response Time (ms)", "Ping Time (ms)"])
        writer.writerow(log_data)

    print(f"[{timestamp}] {url} | HTTP Status: {status} | Response Time: {response_time} ms | Ping Time: {ping_time} ms")

# Main monitoring loop
def start_monitoring():
    while True:
        for url in URLS_TO_MONITOR:
            # Check HTTP status and response time
            status, response_time = check_http_status(url)
            if status is None:
                status = "DOWN"
                response_time = "N/A"

            # Check Ping status
            ping_time = check_ping_status(url)
            if ping_time is None:
                ping_time = "N/A"

            # Log result
            log_result(url, status, response_time, ping_time)

        # Wait before the next check
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("Starting Uptime Monitor...")
    start_monitoring()
