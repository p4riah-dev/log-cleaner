# log-cleaner

Automated log cleaning and obfuscation tool for Linux systems.

## Features
- Clear bash history
- Clean system logs
- Remove temp files
- Wipe application logs

## Usage
```bash
python3 cleaner.py --mode full
python3 cleaner.py --mode selective --target auth.log
```

## Supported Logs
- /var/log/auth.log
- /var/log/syslog
- /var/log/kern.log
- ~/.bash_history

## Requirements
- Python 3.x
- Root privileges

## Disclaimer
For authorized system administration only.
