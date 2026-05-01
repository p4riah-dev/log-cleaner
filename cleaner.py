import os
import sys
import argparse
from datetime import datetime

LOG_PATHS = [
    "/var/log/auth.log",
    "/var/log/syslog",
    "/var/log/kern.log",
    "/var/log/messages",
    "~/.bash_history"
]

def clean_log(path):
    try:
        expanded = os.path.expanduser(path)
        if os.path.exists(expanded):
            with open(expanded, 'w') as f:
                f.write('')
            print(f"[+] Cleaned: {path}")
        else:
            print(f"[-] Not found: {path}")
    except PermissionError:
        print(f"[!] Permission denied: {path}")
    except Exception as e:
        print(f"[!] Error on {path}: {e}")

def clean_temp():
    temp_dirs = ["/tmp", "/var/tmp"]
    for d in temp_dirs:
        try:
            for f in os.listdir(d):
                fp = os.path.join(d, f)
                if os.path.isfile(fp):
                    os.remove(fp)
                    print(f"[+] Removed: {fp}")
        except Exception as e:
            print(f"[!] Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Log Cleaner Tool')
    parser.add_argument('--mode', choices=['full', 'selective'], 
                       default='full', help='Cleaning mode')
    parser.add_argument('--target', help='Specific log file (selective mode)')
    args = parser.parse_args()

    print(f"[*] Log Cleaner started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    if args.mode == 'full':
        print("[*] Running full clean...")
        for log in LOG_PATHS:
            clean_log(log)
        clean_temp()
    elif args.mode == 'selective':
        if not args.target:
            print("[!] Selective mode requires --target")
            sys.exit(1)
        clean_log(args.target)

    print("-" * 50)
    print("[*] Clean complete.")

if __name__ == "__main__":
    main()
