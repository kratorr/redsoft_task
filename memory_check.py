import psutil
import time
import json


from datetime import datetime


def memory_check():
    disk_usage = []
    for part in psutil.disk_partitions(all=True):
        usage = psutil.disk_usage(part.mountpoint)
        disk_usage.append({
            'mountpoint': part.mountpoint,
            'total': usage.total,
            'used': usage.used
        })
    return disk_usage


def main():
    while True:
        disk_usage = memory_check()
        disk_usage.append(datetime.now().isoformat())
        with open('memory_status.json', 'w') as f:
            json.dump(disk_usage, f)
        time.sleep(60)


if __name__ == '__main__':
    main()
