# Syspingd

Syspingd is a custom Linux daemon that monitors the availability of your home lab server. It periodically checks if the server is up and running, sending notifications to keep you informed about its status.

## Features

- **Continuous Monitoring**: Regularly pings your designated server.
- **Desktop Notifications**: Uses `dunstify` to send notifications when the server goes down or comes back online.
- **Customizable**: Easily change the server address, ping interval, and notification settings.
- **Logging**: Maintains a log file for monitoring events.

## Prerequisites

- A Linux-based operating system
- GCC or another C compiler
- Python 3.x (for the ping script)
- `dunstify` installed on your system for notifications

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/de3p1k/syspingd.git
   cd syspingd

2. **Modify the Source Code**
   
   Open the syspingd.c file and change the path of ping.py to the correct location on your system.

3. **Prepare the Log File**
   
   Create a log file in your desired directory and replace <PATH TO YOUR LOG FILE> in ping.py with the path to this log file.

   ```bash
   touch /path/to/your/logfile.txt

5. **Modify the Notification Icon**

   Open ping.py and replace <PATH TO YOUR ICON> with the path to any icon you'd like to be displayed along with the notification.

6. ** Compile the Daemon**

   ```bash
   gcc -o syspingd syspingd.c

7. **Move the Binary to PATH**

   Ensure that the syspingd binary is in your PATH or in a location that can be accessed from any terminal session.

   ```bash
   sudo mv syspingd /usr/local/bin/

## Usage
```bash
syspingd
