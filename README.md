# Python Network Troubleshooting Tool

## 📌 Project Overview

The Python Network Troubleshooting Tool is a beginner-friendly networking project developed using Python. It helps users perform basic network checks and understand common connectivity and DNS resolution results.

This project is designed to practise Python programming, networking fundamentals, and basic network troubleshooting.

## 🎯 Objectives

- Check network connectivity using the ping command.
- Resolve domain names into IPv4 addresses using DNS.
- Understand basic network troubleshooting techniques.
- Practise Python modules, variables, conditions, and exception handling.

## ✨ Features

### 1. Ping Connectivity Checker
- Accepts an IP address or hostname.
- Runs the Windows ping command.
- Displays a success or failure result.
- Shows the ping command output.

### 2. DNS Checker
- Accepts a website hostname.
- Attempts to resolve the hostname into an IPv4 address.
- Displays the resolved address when successful.
- Handles DNS resolution errors.

## 🛠️ Technologies Used

- Python 3
- Python `subprocess` module
- Python `socket` module
- Windows Command Prompt / PowerShell
- Visual Studio Code

## 📂 Project Structure

```text
Python-Network-Troubleshooter/
├── ping_tool.py
├── dns_checker.py
└── README.md
```

## ⚙️ Requirements

- Python 3 installed on your computer.
- Windows operating system for the current ping implementation.
- Visual Studio Code or another Python editor (optional).

## 🚀 How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/Sonadi1027/Python-network-troubleshooter.git
```

### Step 2: Open the Project Folder

Open the downloaded project folder in Visual Studio Code.

### Step 3: Run the Ping Connectivity Checker

```bash
python ping_tool.py
```

Enter an IP address or hostname when prompted.

Example test targets:

- `8.8.8.8` — public DNS server.
- `192.0.2.1` — reserved documentation address for a likely ping failure test.

### Step 4: Run the DNS Checker

```bash
python dns_checker.py
```

Example successful lookup:

```text
google.com
```

Example failure test:

```text
this-domain-should-not-exist-123456.invalid
```

## 🧪 Testing

The project includes basic tests for:

- Successful ping responses.
- Failed ping attempts.
- Successful DNS resolution.
- Failed DNS resolution.

Actual results may vary depending on network connectivity, DNS settings, and firewall rules. A failed ping does not always mean that a host is offline.

## 📚 Learning Outcomes

Through this project, I am learning:

- Basic networking concepts such as IP addresses, ping, and DNS.
- Python variables, user input, conditions, and exception handling.
- Using Python modules to run system commands and perform DNS lookups.
- Basic network troubleshooting and testing.
- Managing a programming project using GitHub.

## 🔮 Future Improvements

- Add a TCP port connectivity checker.
- Create a menu-driven interface.
- Save test results in a report file.
- Add timestamps and clearer error messages.
- Improve input validation and testing.

## 👩‍💻 Author

Created as a beginner networking and Python learning project.

## 📄 License

This project is intended for educational and portfolio purposes.
