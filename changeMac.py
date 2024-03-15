import subprocess

def main():
    interface = "eth0"
    new_mac = "22:11:22:33:44:56" 

    print("Turning down interface")
    subprocess.run(["ifconfig", interface, "down"])

    print("Changing hardware address of", interface, "to", new_mac)
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

    print("New MAC address:", new_mac)

    print("Bringing interface", interface, "up")
    subprocess.run(["ifconfig", interface, "up"])

if __name__ == "__main__":
    main()
