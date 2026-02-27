# TCP Port Scanner 🔐

A multithreaded TCP port scanner built using Python.

## Features

- Scan single host
- Custom port range
- Multithreaded scanning
- Timeout handling
- Logging system
- Clean CLI interface

## Usage

```bash
python scanner.py --host 192.168.1.1 --start 20 --end 100 --threads 100

## 🛠 Technologies Used

- Python 3
- socket module
- concurrent.futures (ThreadPoolExecutor)
- argparse
- logging

---

## 📂 Project Structure


## Arguments

| Argument  | Description              |
|-----------|--------------------------|
| --host    | Target IP or domain      |
| --start   | Starting port            |
| --end     | Ending port              |
| --threads | Number of threads        |
| --timeout | Timeout per port         |


---

## ⚙ How It Works

1. Resolves hostname to IP address.
2. Creates TCP socket for each port.
3. Attempts connection using `connect_ex()`.
4. Classifies ports:
   - OPEN → Successful connection
   - CLOSED → Connection refused
   - FILTERED → Timeout / no response
5. Uses ThreadPoolExecutor for concurrent scanning.
6. Logs results with timestamps.

---

## 🔒 Ethical Notice

This tool is intended for:

- Educational purposes
- Authorized penetration testing
- Lab environments

Unauthorized scanning of networks without permission is illegal.

---

## 🎓 Learning Outcomes

This project demonstrates understanding of:

- TCP/IP Networking
- Socket Programming
- Concurrency in Python
- CLI Application Development
- Logging Systems
- Error Handling in Network Applications

---

## 📌 Future Improvements

- Banner Grabbing
- UDP Scanning
- Service Detection
- OS Fingerprinting
- GUI Version
- JSON / CSV Export

---

## 👨‍💻 Author

Your Name  
BS Computer Science  
Cybersecurity Focus

