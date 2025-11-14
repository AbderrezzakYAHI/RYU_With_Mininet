<p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue" /> <img src="https://img.shields.io/badge/SDN-Ryu%204.32-green" /> <img src="https://img.shields.io/badge/Mininet-2.2.2-orange" /> <img src="https://img.shields.io/badge/Status-Working-success" /> </p>

SDN Virtual Network Topologies

Python • Mininet • Ryu Controller

This repository provides SDN (Software-Defined Networking) topologies for academic and research use, especially for the Master IR 2020 project.
The project demonstrates SDN virtual networks using Python, Mininet, and Ryu as a remote controller.

📁 Project Structure
.
├── SDN_Mininet.py             # Main topology file for Mininet
├── requirements.txt           # Required Python packages
├── SDN_Mininet.png            # Topology diagram
├── SDN_Mininet_1.png          # Alternative diagram
├── SDN_Mininet_1.py           # Main Toppology File for Mininet
├── SDN_Mininet_vlan.png       # VLAN-based topology diagram
├── SDN_mininet.py             # Main Topology 
└── README.md                  # Project documentation

⚙️ Installation Guide
1. Install Mininet (2.2.2)
sudo apt-get update
sudo apt-get install mininet

2. Install Ryu Controller (4.32)
pip install ryu==4.32

3. Install Project Requirements
pip install -r requirements.txt


▶️ Running the SDN Topology in Mininet
Start your topology using:
sudo mn --custom SDN_mininet.py --topo irs2020 --controller=remote

Start your Ryu controller in a second terminal:
ryu-manager ryu_app.py
Replace ryu_app.py with your actual Ryu script.)


🧪 Example Output
When launching Mininet with the provided script, you should see:
Switches created (ex: s1, s2, s3…)
Hosts assigned to VLANs (if using VLAN file)
Links established
Remote controller successfully connected
Ping tests showing connectivity depending on your rules

You can test connectivity with:
pingall


🌍 FR – Version Française
Topologies SDN du Réseau Virtuel
Ce dépôt contient plusieurs topologies SDN créées avec Python, Mininet et le contrôleur Ryu dans le cadre du projet Master IR 2020.
Les schémas réseau disponibles :
SDN_Mininet.png
SDN_Mininet_1.png
SDN_Mininet_vlan.png

Guide d'installation
✔ 1. Installer Mininet 2.2.2
sudo apt-get install mininet

✔ 2. Installer Ryu 4.32
pip install ryu==4.32

✔ 3. Installer les dépendances du projet
pip install -r requirements.txt

Exécution dans Mininet
sudo mn --custom SDN_mininet.py --topo irs2020 --controller=remote


Démarrer ensuite le contrôleur Ryu :
ryu-manager ryu_app.py
