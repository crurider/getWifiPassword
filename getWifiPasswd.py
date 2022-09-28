import subprocess

# helper method
def clean_output(strng):
    strng = strng.replace(":", "").strip()
    return strng[:strng.index("\\")]

# cmd command: "netsh wlan show profiles" 
wlan_data = str(subprocess.check_output(["netsh", "wlan", "show", "profiles"])).split("\n")

# cleaning
for i in wlan_data:
    profiles = i.split("All User Profile")
for i in profiles:
    if "User profiles" in i:
        profiles.remove(i)
for i in range(len(profiles)):
    profiles[i] = clean_output(profiles[i])

# cmd command: "netsh wlan show profile NETWORK key=clear"
results = []
for i in profiles:
    profile_info = (str(subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])))
    if "Key Content" in profile_info:
        results.append(profile_info)

# cleaning
results_clean = []
for i in results:
    spl = i.split("Key Content")
    spl[0] = spl[0][spl[0].find(" "):spl[0].find("on interface")].strip()
    spl[1] = clean_output(spl[1])
    temp = "Network: " + spl[0] + ", Password: " + spl[1]
    results_clean.append(temp)

for i in results_clean:
    print(i)