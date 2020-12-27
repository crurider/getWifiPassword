import subprocess

interfaceInfo = subprocess.call(["netsh", "wlan", "show", "interfaces"]).split("\n")
networkName = [line.split(':')[0] for line in interfaceInfo if "Profile" in line]

print(networkName)
