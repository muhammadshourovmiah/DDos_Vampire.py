import os
import time
import socket
import random
import requests

def print_logo():
    os.system("clear")
    print("\033[92m")
    print("   ╔══════════════════════════════════════════════════════════════╗")
    print("   ║                   VAMPIRE SQUAD TOOL                         ║")
    print("   ╚══════════════════════════════════════════════════════════════╝")
    print("\n")
    print("   _____      _                __     ______  _    _   _____ ")
    print("  / ____|    | |               \\ \\   / / __ \\| |  | | / ____|")
    print(" | |    _   _| |__   ___ _ __   \\ \\_/ / |  | | |  | || (___  ")
    print(" | |   | | | | '_ \\ / _ \\ '__|   \\   /| |  | | |  | | \\___ \\ ")
    print(" | |___| |_| | |_) |  __/ |       | | | |__| | |__| | ____) |")
    print("  \\_____\\__, |_.__/ \\___|_|       |_|  \\____/ \\____/ |_____/ ")
    print("         __/ |                                                ")
    print("        |___/                                                 ")
    print("\033[94m")
    print("   ╔══════════════════════════════════════════════════════════════════════╗")
    print("   ║                    DEVELOPER INFORMATION                             ║")
    print("   ╠══════════════════════════════════════════════════════════════════════╣")
    print("   ║  👤 Coded By  : MUHAMMAD SHOUROV (Vampire)                           ║")
    print("   ║  🖊️ Author     : Vampire Squad                                        ║")
    print("   ║  🔗 Facebook  : https://www.facebook.com/Junior.Writer.SHourov      ║")
    print("   ║  📘 Team  Page: https://www.facebook.com/profile.php?id=61574803393816 ║")
    print("   ║  🏛️ Team  Name: Vampire Squad                                        ║")
    print("   ╠══════════════════════════════════════════════════════════════════════╣")
    print("   ║  🔥 Tool Version: 2.0.0                                              ║")
    print("   ╚══════════════════════════════════════════════════════════════════════╝")
    print("\n")

def login():
    print("\033[92m")
    print("   ╔════════════════════════════╗")
    print("   ║      LOGIN TO CONTINUE     ║")
    print("   ╚════════════════════════════╝")
    attempts = 0
    while attempts < 3:
        username = input("\n   ➤ Enter Username: ")
        password = input("   ➤ Enter Password: ")
        if username == "Vampire_Squad" and password == "SH404":
            print("\n   ✅ Login Successful!\n")
            time.sleep(1)
            os.system("clear")
            return True
        else:
            attempts += 1
            print(f"\n   ❌ Invalid Credentials! Attempts Left: {3 - attempts}\n")
    print("\n   ❌ Access Denied! Exiting...\n")
    exit()

def loading_bar():
    print("\033[91m")
    for i in range(101):
        time.sleep(0.01)
        print(f"\r   ➤ Loading: [{'#' * (i//5)}{' ' * (20 - (i//5))}] {i}%", end='', flush=True)
    print("\n\n")

def get_target_details():
    print("\033[93m")
    print("   ╔══════════════════════════════════════════╗")
    print("   ║          ENTER TARGET DETAILS            ║")
    print("   ╚══════════════════════════════════════════╝")
    target_ip = input("   ➤ Enter Target IP or Domain: ")
    return target_ip

def ip_tracker(ip):
    print("\n\033[96m   ➤ Tracking IP Info...\n")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response["status"] == "success":
            print(f"   ➤ IP: {response['query']}")
            print(f"   ➤ Country: {response['country']}")
            print(f"   ➤ Region: {response['regionName']}")
            print(f"   ➤ City: {response['city']}")
            print(f"   ➤ ISP: {response['isp']}")
            print(f"   ➤ Org: {response['org']}")
            print(f"   ➤ Lat/Lon: {response['lat']}, {response['lon']}")
        else:
            print("   ❌ Failed to fetch IP info.")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def ping_test(ip):
    print("\n\033[95m   ➤ Running Ping Test...\n")
    response = os.system(f"ping -c 4 {ip}")
    if response == 0:
        print("   ✅ Ping Successful!")
    else:
        print("   ❌ Ping Failed or Host Unreachable.")

def main():
    print_logo()
    if login():
        loading_bar()
        while True:
            print("\n\033[92m   ╔══════════════════════════╗")
            print("   ║     TOOL MAIN MENU       ║")
            print("   ╚══════════════════════════╝")
            print("   [1] IP Tracker")
            print("   [2] Ping Test")
            print("   [3] Exit")
            choice = input("\n   ➤ Select Option: ")

            if choice == '1':
                target = get_target_details()
                ip_tracker(target)
            elif choice == '2':
                target = get_target_details()
                ping_test(target)
            elif choice == '3':
                print("\n   ⚠️ Exiting Tool...\n")
                break
            else:
                print("   ❌ Invalid Choice!")

if __name__ == "__main__":
    main()
