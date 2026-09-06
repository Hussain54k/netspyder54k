import requests
import sys

def search_username(username):
    print(f"\n[*] NetSpyder54k: Scanning for username '{username}'...")
    print("====================================================")
    
    platforms = {
        "Instagram": f"https://instagram.com{username}/",
        "TikTok": f"https://tiktok.com@{username}",
        "Snapchat": f"https://snapchat.com{username}",
        "Telegram": f"https://t.me{username}",
        "Line (Public Post)": f"https://line.me{username}"
    }

    for platform, url in platforms.items():
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(url, headers=headers, timeout=5)
            
            if response.status_code == 200:
                print(f"[+] FOUND on {platform}: {url}")
            else:
                print(f"[-] Not Found on {platform}")
        except requests.ConnectionError:
            print(f"[!] Error: Could not connect to {platform}")
        except requests.Timeout:
            print(f"[!] Timeout: {platform} did not respond")

def search_phone_osint(phone):
    print(f"\n[*] NetSpyder54k: Searching Phone footprint for '{phone}'...")
    print("====================================================")
    print("[!] Info: Automated API phone OSINT requires private database access.")
    print(f"[+] Tip: For manual OSINT, search phone number format on Telegram or Snapchat lookup.")

def main():
    print("=========================================")
    print("     NetSpyder54k (Profile Scanner)     ")
    print("=========================================")
    print("1. Search by Username (بحث باليوزر)")
    print("2. Search by Phone Number (بحث برقم الجوال)")
    
    choice = input("\nChoose an option (1-2): ").strip()
    
    if choice == '1':
        user = input("Enter target Username: ").strip()
        search_username(user)
    elif choice == '2':
        phone = input("Enter Phone Number (with country code, e.g., +9665...): ").strip()
        search_phone_osint(phone)
    else:
        print("[-] Invalid choice.")

if __name__ == "__main__":
    main()
