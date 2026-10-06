To get things started I am running Ubuntu Server 24.04 we can verify this with<br>
lsb_release -a <br>
<br>
To get things started I wanted to update system packages  <br>
sudo apt update && sudo apt upgrade -y # Assuming you are not root <br>

There is a script which I will provide that setups wazuh and other related tools which we will be using  <br>
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh <br>
sudo bash wazuh-install.sh -a -i # -a flag gives you all in one and -i skips the os version check which I recommend <br>
<br>
The above script install wazuh manager, FileBeat, Elasticsearch and kibana / ensure you have disk space <br>
<br>
if you want to verify that wazuh services are running use <br>
sudo systemctl status wazuh-manager <br>
sudo systemctl status wazuh-dashboard <br>
sudo systemnctl status elasticsearch <br>
sudo systemctl status filebeat <br>
<br>
for issues you may encounter run <br>
sudo journalctl -u service_name -n 50 # last 50 lines of the logs <br>

By default aswell wazuh gives you a long complicated password just run <br>
cd /usr/share/wazuh-indexer/openseach-security/tools <br>
bash ./wazuh-passwords-tools.sh -u user_name -p "password" # assumming the script in the correct directory <br>
<br>
You can now access your wazuh dashboard and start setting up rules <br>


