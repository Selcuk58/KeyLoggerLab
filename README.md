# KeyLoggerLab

Educational Python project demonstrating how keyboard event logging works.

This project logs keyboard events locally with timestamps and demonstrates concepts often discussed in cybersecurity and malware analysis such as:

- Keyboard event hooks  
- Local keystroke logging  
- Windows autostart persistence via registry  
- Background tasks using threading  
- Simulated log file upload  

⚠️ **Important**

This project is created for **educational and research purposes only**.  
All logged data remains on the local machine unless the code is modified.

The goal of this project is to demonstrate how keyboard input monitoring works and to help understand techniques often analyzed in cybersecurity and malware research.

---

## Features

- Logs keyboard events
- Adds timestamps to each keystroke
- Optional Windows autostart
- Background upload simulation
- Demonstrates threading in Python

---

## Example Log Output


```
2026-03-15 21:34:10 - h
2026-03-15 21:34:11 - e
2026-03-15 21:34:11 - l
2026-03-15 21:34:12 - l
2026-03-15 21:34:12 - o
```

Installation

Clone the repository:

```
git clone https://github.com/Selcuk58/KeyLoggerLab.git

cd KeyLoggerLab
```

Install dependencies:

```
pip install keyboard requests
```

Usage

Run the program:

```
python main.py
```

When the program starts you will see a consent message:

```
Educational KeyLogger Demo
Allow this program to add itself to Windows autostart? (yes/no)
```

If the user selects:

yes → program adds itself to Windows autostart

no → program runs without persistence

How it Works

The program performs the following steps:

Ask the user for permission to enable autostart.

Optionally create a registry entry:

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```

Start a keyboard hook using the keyboard Python library.

Log each key press with a timestamp.

Run background tasks such as periodic uploads using threads.

Project Structure

```
KeyLoggerLab
│
├ main.py
├ output.txt
└ README.md
```

Antivirus Notice

Some antivirus software may flag this project as suspicious.

This happens because the program demonstrates behaviors that are commonly used by malware, such as:

capturing keyboard events

creating Windows autostart registry entries

running background threads

sending files over HTTP

Even though this project is purely educational, security software may still detect it.

Testing the Project Safely

If your antivirus blocks the program during testing, you should not disable your antivirus completely.

Instead use one of the following methods.

1. Add a Folder Exclusion (Recommended)

You can add your project folder as an exclusion in your antivirus software.

Example workflow for Windows Defender:

```
Windows Security
↓
Virus & Threat Protection
↓
Manage Settings
↓
Exclusions
↓
Add Exclusion → Folder
```

Then select your project directory:

```
C:\Users\YourUser\Projects\KeyLoggerLab
```

This allows you to test the project while keeping the rest of your system protected.

2. Use a Virtual Machine

Another recommended approach is to run the program inside a virtual machine.

Examples:

VirtualBox

VMware

Hyper-V

Benefits:

isolated environment

no risk to your main system

commonly used in cybersecurity research

Educational Purpose

This project demonstrates concepts commonly studied in:

cybersecurity

malware analysis

operating system monitoring

event-driven programming

The goal is to understand how such techniques work, not to misuse them.

Disclaimer

This software is provided for educational purposes only.

Do not use this software to monitor systems without explicit permission.
The author is not responsible for any misuse.

Author

GitHub:
https://github.com/Selcuk58