# 🌐 **IP-SPOOFER with Tor**

Protect your online privacy with this powerful Python script. **IP-SPOOFER** automatically changes your IP address using Tor, enhancing your security and anonymity online.

---

## 🔒 **Privacy and Security**

- Change your IP address automatically at custom intervals.
- Stay anonymous while browsing, web scraping, or conducting security testing.
- Protect your identity from prying eyes with seamless TOR integration.

---

## ⚙️ **Features**

✅ Cross-platform support: Works on **Windows**, **Linux**, **Ubuntu**, **Kali**, and **Raspberry Pi**.  
✅ Automatic Tor installation for Windows (Expert Bundle).  
✅ Customizable time intervals and change cycles.  
✅ Proxy settings: **SOCKS5 - 127.0.0.1:9050** for all requests.  
✅ Lightweight and efficient with real-time IP display.  

---

## 🚀 **Get Started**

### 1️⃣ **Installation (Windows & Linux)**

Clone the repository and get started in minutes!

```bash
# Clone the repository
git clone https://github.com/OnyxDeveploment/IPSpoofer.git

# Change directory
cd IPSpoofer

# Run the script
sudo python3 IPspoofer.py
```

---

### 2️⃣ **Windows Tor Setup (Automatic)**

No manual setup needed! The script automatically downloads the **Tor Expert Bundle** and runs the Tor service.  
Ensure your proxy settings are configured to **127.0.0.1:9050**.

---

## 📦 **Configuration Options**

- **IP Change Interval:** Set the time (in seconds) to change your IP automatically.  
- **IP Change Cycles:** Choose how many times to change the IP (`0` for infinite).  
- **Wireless Interface (Optional):** Future functionality for network interface management.

---

## 🧰 **Requirements**

Ensure you have the following installed:

- **Python 3.7+**  
- **PIP**  
- **TOR** (Automatically installed by the script)  

**Linux Only:**  
```bash
sudo apt update && sudo apt install tor -y
```

---

## 💡 **Usage Example**

Example to change IP every 60 seconds for 10 cycles:

```bash
sudo python3 IPspoofer.py
```

```
Enter your wireless interface name (e.g., wlan0): wlan0
[+] Time interval to change IP (seconds) [default=60]: 60
[+] Number of times to change IP [0 for infinite]: 10
```

---

## 🌍 **Verify Your IP**

To confirm your new IP, visit:

- [https://whatismyipaddress.com](https://whatismyipaddress.com)  
- [https://ipinfo.io](https://ipinfo.io)  

---

## 🔑 **Important Notes**

- Use for educational and ethical purposes only.  
- Ensure Tor is running while using this script.  
- Make sure your system proxy is set to **127.0.0.1:9050**.

---

## 🤝 **Contributing**

Want to improve IP-Spoofer? Fork the repo, create a new branch, and submit a pull request!  

---

## 📜 **License**

This project is licensed under the **MIT License** – free to use, modify, and distribute.

---

🚀 **Start spoofing your IP today and browse securely with IP-SPOOFER!**

