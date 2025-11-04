sudo apt update && sudo apt upgrade -y
sudo apt install net-tools curl vim htop ufw -y
sudo ufw allow OpenSSH
sudo ufw enable

if want to clone a repo and implemnt a git servber 
sudo apt install git
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git clone https://github.com/<yourusername>/soc-homelab.git
cd soc-homelab

These commands install wazuh filebeat elastic search and kibana(plugin)
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
sudo bash wazuh-install.sh -a
