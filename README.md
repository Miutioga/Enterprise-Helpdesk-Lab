# Enterprise Hybrid IT Infrastructure & Helpdesk System

## 📖 Project Overview
This project simulates a real-world corporate IT environment, integrating **Windows Server (Active Directory)** and **Linux (LAMP Stack)** to host a functional Helpdesk ticketing system. The infrastructure is secured by an edge firewall (pfSense) and features automated maintenance scripts.

## 🏗️ Network Topology
![Network Diagram](docs/diagram.png)
*(Please upload your diagram to the docs folder)*

## 🛠️ Technologies Used
- **Infrastructure:** VirtualBox, pfSense (Firewall/Router).
- **Identity Management:** Windows Server 2019 (AD DS, DNS, GPO).
- **Web Server:** Ubuntu Server 20.04, Apache, MySQL, PHP (LAMP Stack).
- **Application:** osTicket (Helpdesk System).
- **Automation:** Python (Service Monitoring), Bash Shell (Database Backup).

## 🚀 Key Features
1.  **Hybrid Environment:** Seamless integration between Windows Domain Controller and Linux Web Server.
2.  **Centralized Management:** Users and Policies managed via Active Directory & Group Policy (GPO).
3.  **Network Security:** Traffic segmented and filtered via pfSense Firewall; Internal DNS resolution.
4.  **Self-Healing System:**
    - Python script monitors Apache service status every minute.
    - Automatically restarts the service if a crash is detected.
5.  **Automated Disaster Recovery:** Daily Cronjob backups of the MySQL database.

## 📂 Project Structure
```text
├── configs/            # Configuration snippets (DNS, Crontab)
├── docs/               # Screenshots and Network Diagrams
├── scripts/            # Automation scripts (Python/Bash)
└── README.md           # Project Documentation