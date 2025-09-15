# Iptables GUI Controller

An intuitive and easy-to-use graphical user interface (GUI) application built with Python and Tkinter for managing Linux's `iptables` firewall rules. A simple GUI tool with basic control of iptables. 
As it's from an old school project it may need some adjustements to work. And, Everything has been configured for Ubuntu/Debian so you should find alternatives for other distributions in prerequisites.

---

## 🚀 Features

* **Add Rules:** Easily create new `iptables` rules for specific ports, protocols (TCP/UDP), and IP addresses.
* **Delete Rules:** Remove existing rules with a single click.
* **View Rules:** Display a clear, organized list of all active firewall rules.
* **User-Friendly Interface:** Built with Tkinter to provide a simple, clean, and responsive user experience.

---

## Prerequisites

Before you can run the application, ensure you have the following installed on your system:

* **Python 3.x**
* **python3-venv :** This package is necessary to isolate the running app.
    * On Debian/Ubuntu: `sudo apt-get install python3-venv`
* **`iptables`:** This is the core firewall tool that the application interacts with. It is pre-installed on most Ubuntu relatives distributions.
    * if not on Debian-based: `sudo apt-get install iptables` 

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/depicon/iptable-ctl.git
    cd iptable-ctl
    ```
2.  **Create and activate the virtual environment:** (adapt with you shell)
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    * This creates a new folder named `venv` and activates the isolated environment.

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Make sure you have a `requirements.txt` file listing your project's dependencies, like Tkinter if it's not a standard library, though it usually is.)*

---

## Usage

Since the application requires root privileges to modify `iptables` rules, you must run it with `sudo`.

```bash
sudo python3 interface.py
