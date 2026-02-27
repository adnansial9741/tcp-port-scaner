import socket
import argparse
import logging
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# ---------------------------
# Setup Logging
# ---------------------------
if not os.path.exists('logs'):
    os.makedirs("logs")
logging.basicConfig(
    filename="logs/scan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)    
# ---------------------------
# Port Scan Function
# ---------------------------
def scan_port(host, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))

            if result == 0:
                status = "OPEN"
            elif result == 111:
                status = "CLOSED"
            else:
                status = "FILTERED"

            return port, status

    except socket.timeout:
        return port, "FILTERED"
    except Exception as e:
        return port, f"ERROR ({e})"

# ---------------------------
# Main Scanner Logic
# ---------------------------

def run_scan(host, start_port, end_port, threads, timeout):

    print(f"\nStarting scan on {host}")
    print(f"Scanning ports {start_port} - {end_port}")
    print("-" * 40)

    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {
            executor.submit(scan_port, host, port, timeout): port
            for port in range(start_port, end_port + 1)
        }

        for future in as_completed(futures):
            port, status = future.result()
            message = f"Port {port}: {status}"
            print(message)
            logging.info(message)

            if status == "OPEN":
                open_ports.append(port)

    print("\nScan Completed.")
    print(f"Open Ports: {open_ports}")

# ---------------------------
# Argument Parser
# ---------------------------

def main():
    parser = argparse.ArgumentParser(description="TCP Port Scanner")

    parser.add_argument("--host", required=True, help="Target host (IP or domain)")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout per port")

    args = parser.parse_args()

    # Resolve hostname
    try:
        host_ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print("Invalid host.")
        return

    run_scan(host_ip, args.start, args.end, args.threads, args.timeout)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")


    