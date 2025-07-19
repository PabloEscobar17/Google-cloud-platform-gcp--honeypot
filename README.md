# Cloud Honeypot Deception Portal

Cloud honeypot deployed on Google Cloud Platform. Professional-looking user and admin login portals built with Python Flask to capture and analyze unauthorized access attempts for cybersecurity research.

## Features

- **Realistic Web Portal:** Mimics authentic login and admin panels with professional HTML/CSS.
- **Cloud Deployment:** Hosted on GCP Compute Engine VM for real-world and global attack exposure.
- **Detailed Logging:** Records usernames, passwords, timestamps, IPs, user agents, and endpoints.
- **Firewall Management:** Utilizes Google Cloud VPC firewall rules for secure, controlled access.
- **Multiple Endpoints:** Includes both user and admin login pages to attract diverse attacks.
- **Easy Customization:** Modular templates and styles for branding or research adaptation.
- **Educational Focus:** Designed for learning, analysis, and safe demonstration.

## Setup & Usage

### 1. Deploy to a Google Cloud VM

1. **Create a Compute Engine VM**  
   - OS: Ubuntu 22.04 LTS  
   - Open allowed ports: 5000 (or your chosen port), 22 (for SSH)
2. **SSH into your VM and install required packages:**
    ```
    sudo apt update
    sudo apt install python3 python3-pip git -y
    pip3 install flask
    ```
3. **Clone this repository to your VM:**
    ```
    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
    ```
4. **Run the honeypot app:**
    ```
    python3 app.py
    ```
    *(Change the port in app.py if needed.)*

5. **In your browser:**  
    Go to `http://<VM_EXTERNAL_IP>:5000`

### 2. Directory Structure

your-repo/
├── app.py
├── templates/
│ ├── index.html
│ └── admin.html
├── static/
│ └── style.css
├── logs/
│ └── creds.txt
└── README.md

### 3. Logs

- All login attempts are logged in `logs/creds.txt` with IP address, timestamp, form data, and user agent.

### 4. Screenshots (Recommended)

Insert screenshots of the login page, admin portal, and a snippet of the log file here.

## Security & Ethical Notice

- **Never deploy on a network with sensitive data or production environments.**
- Monitor VM usage and costs on GCP. Delete/stop your VM when not in use.
- Use strictly for educational, research, or authorized demonstration purposes.

## Possible Improvements

- Add IP geolocation analytics and frequency graphs.
- Extend to SSH/FTP honeypots for multi-protocol research.
- Use cloud monitoring or Slack/email alerts for certain attacker behaviors.

## License

MIT License

---

**For further technical help, see the issues section or contact the project maintainer.**
