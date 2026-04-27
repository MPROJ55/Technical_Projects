import nmap3
import json

# global intialization of nmap 
scanner = nmap3.Nmap()

# testing libary functions and organzing output in pretty json    
def test_scan():
    scan = nmap3.Nmap()
    # use a website that allows ports scanning 
    results = scan.scan_top_ports("google.com")    
    # results wil be in json
    print(json.dumps(results, indent=4))
    
def target_fetch():
    target = input("Enter the Target (IP or Domain): ").strip()
    return target
 
 # scans for top ports
def top_scan(target):   
    print(f".....starting scan on top ports of  {target}")
    results = scanner.scan_top_ports(target)
    print(json.dumps(results,indent=4))
# intiates tcp scan
def tcp_scap():
    print(f".....starting TCP Scan on {target}")
    results = scanner.nmap_version_detection(target)
    print(json.dumps(results, indent=4))
# intiates tcp scan
def udp_scan():
    print(f".....starting UDP Scan on {target}")
    results = scanner.nmap_udp_scan(target)
    print(json.dumps(results, indent=4))
    

def main():
    while True: 
        print("\n=== Port Scanner ===")
        print("1. Top Ports Scan")
        print("2. TCP Scan")
        print("3. UDP Scan")
        print("4. Exit")
        
        choice = input("\nSelect scan type: ").strip()

        if choice == "4":
            print("Exiting...")
            break

        target = target_fetch()

        if choice == "1":
            top_scan(target)
        elif choice == "2":
            tcp_scan(target)
        elif choice == "3":
            udp_scan(target)
        else:
            print("Invalid option.")



if __name__ == "__main__": 
    main()
