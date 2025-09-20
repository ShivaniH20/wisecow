#!/usr/bin/env python3
"""
Simple App Health Checker
Usage: python app_check.py --url http://localhost:8080/ --log app_health.log
"""

import requests
import argparse
import logging

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--url', required=False, default='http://localhost:8080/', help='URL to check')
parser.add_argument('--log', default='app_health.log', help='Log file name')
args = parser.parse_args()

# Logging setup
logging.basicConfig(filename=args.log, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Check application status
try:
    r = requests.get(args.url, timeout=5)
    status = r.status_code
    if 200 <= status < 300:
        print(f'UP: {args.url} -> HTTP {status}')
        logging.info(f'UP: {args.url} -> HTTP {status}')
    else:
        print(f'DOWN: {args.url} -> HTTP {status}')
        logging.warning(f'DOWN: {args.url} -> HTTP {status}')
except Exception as e:
    print(f'ERROR: Could not reach {args.url} -> {e}')
    logging.error(f'ERROR: Could not reach {args.url} -> {e}')
