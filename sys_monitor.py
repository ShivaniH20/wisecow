#!/usr/bin/env python3
"""
Simple System Health Monitor
Usage: python3 sys_monitor.py --cpu 80 --mem 80 --disk 90 --proc sshd --log sys_monitor.log
"""

import psutil, argparse, logging
from datetime import datetime

p = argparse.ArgumentParser()
p.add_argument('--cpu', type=int, default=80, help='CPU % threshold')
p.add_argument('--mem', type=int, default=80, help='Memory % threshold')
p.add_argument('--disk', type=int, default=90, help='Disk % threshold (root /)')
p.add_argument('--proc', type=str, default='', help='Process name to check (optional)')
p.add_argument('--log', type=str, default='sys_monitor.log', help='Log file path')
args = p.parse_args()

logging.basicConfig(filename=args.log,
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

def alert(msg):
    print(msg)                 # prints to console
    logging.warning(msg)       # also writes to log file

def main():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu >= args.cpu:
        alert(f'CPU high: {cpu}% (threshold {args.cpu}%)')
    else:
        logging.info(f'CPU OK: {cpu}%')

    if mem >= args.mem:
        alert(f'Memory high: {mem}% (threshold {args.mem}%)')
    else:
        logging.info(f'Memory OK: {mem}%')

    if disk >= args.disk:
        alert(f'Disk usage high: {disk}% (threshold {args.disk}%)')
    else:
        logging.info(f'Disk OK: {disk}%')

    if args.proc:
        found = any(p.info.get('name') == args.proc for p in psutil.process_iter(['name']))
        if not found:
            alert(f'Process NOT running: {args.proc}')
        else:
            logging.info(f'Process running: {args.proc}')

if __name__ == '__main__':
    main()
