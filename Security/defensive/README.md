
 SOC Homelab

A hands-on SOC / SIEM home lab built on Proxmox with OpenWrt, Ubuntu Server, and Debian-based sensors.

##  Overview
This lab demonstrates defense-in-depth using open-source tools like:
- Wazuh (SIEM + EDR)
- Suricata (NIDS)
- Zeek (Network telemetry)
- Pi-hole (DNS filtering)
- OpenWrt (Network segmentation)
- Cloudflare Tunnel (remote access security)
- AI automation agents (future phase)

##  Architecture
![Architecture Diagram](docs/architecture-diagram.png)

##  Current Components
| Component | OS | Function |
|------------|----|-----------|
| Ubuntu Server | 22.04 LTS | Wazuh/Elastic SIEM |
| Debian Sensor | 12 | Suricata, Zeek |
| Raspberry Pi | OS Lite | VPN, Pi-hole, rsyslog |
| OpenWrt Router | Archer A7 | VLANs, Firewall, Gateway |

##  Deployment Phases
1. Network migration (OpenWrt + Pi)
2. SIEM (Ubuntu Server + Wazuh)
3. Suricata sensors
4. Honeypots + VLAN segmentation
5. AI automation agents
