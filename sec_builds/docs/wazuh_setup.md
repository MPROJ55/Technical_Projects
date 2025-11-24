To get things started I am running Ubuntu Server 24.04 we can verify this with 
lsb_release -a 

To get things started I wanted to update system packages  
sudo apt update && sudo apt upgrade -y # Assuming you are not root

There is a script which I will provide that setups wazuh and other related tools which we will be using 
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh 
sudo bash wazuh-install.sh -a -i # -a flag gives you all in one and -i skips the os version check which I recommend

The above script install wazuh manager, FileBeat, Elasticsearch and kibana / ensure you have disk space

if you want to verify that wazuh services are running use 
sudo systemctl status wazuh-manager
sudo systemctl status wazuh-dashboard 
sudo systemnctl status elasticsearch
sudo systemctl status filebeat

for issues you may encounter run 
sudo journalctl -u service_name -n 50 # last 50 lines of the logs

By default aswell wazuh gives you a long complicated password just run
cd /usr/share/wazuh-indexer/openseach-security/tools
bash ./wazuh-passwords-tools.sh -u user_name -p "password" # assumming the script in the correct directory

You can now access your wazuh dashboard and start setting up rules


