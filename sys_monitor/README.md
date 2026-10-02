# PC System Monitor

A simple, real-time Python system monitoring tool designed to track CPU and RAM usage on Windows. The script periodically checks hardware performance and triggers native Windows toast notifications when resource consumption exceeds pre-defined thresholds.

## Features

- **Real-Time Monitoring**: Continuously tracks CPU percentage and RAM usage (percentage and GB consumed).
- **Desktop Alerts**: Sends native Windows system notification toasts when CPU load exceeds 80% or RAM load exceeds 85%.
- **Lightweight**: Minimal performance footprint using `psutil` and `win10toast`.

## Prerequisites

- Python 3.8+
- Windows OS (for native toast notifications)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/DzoniBRO/sys_monitor.git