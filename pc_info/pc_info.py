import psutil
import platform
from datetime import datetime


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def Get_PC_Info():
    uname = platform.uname()
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    cpufreq = psutil.cpu_freq()
    svmem = psutil.virtual_memory()
    partitions = psutil.disk_partitions()
    info = f'''<html><p align="center"><br>SYSTEM INFO:<br><br>
{"="*10} System Information {"="*10} <br>
System: {uname.system} <br>
Node Name: {uname.node} <br>
Release: {uname.release} <br>
Version: {uname.version} <br>
Machine: {uname.machine} <br>
Processor: {uname.processor} <br>
{"="*10} Boot Time {"="*10} <br>
Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second} <br>
{"="*10} CPU Info {"="*10} <br>
Physical cores: {psutil.cpu_count(logical=False)} <br>
Total cores: {psutil.cpu_count(logical=True)} <br>
Max Frequency: {cpufreq.max:.2f}Mhz <br>
Min Frequency: {cpufreq.min:.2f}Mhz <br>
Current Frequency: {cpufreq.current:.2f}Mhz <br>
CPU Usage Per Core: <br>'''
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        info += f"Core {i}: {percentage}% <br>"

    info += f'''Total CPU Usage: {psutil.cpu_percent()}% <br>
{"="*10} Memory Information {"="*10} <br>
Total: {get_size(svmem.total)} <br>
Available: {get_size(svmem.available)} <br>
Used: {get_size(svmem.used)} <br>
Percentage: {svmem.percent}% <br>
{"="*10} Disk Information {"="*10} <br>
Partitions and Usage: <br>'''
    for partition in partitions:
        info += f'''=== Device: {partition.device} === <br>
   Mountpoint: {partition.mountpoint} <br>
   File system type: {partition.fstype} <br>'''
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        info += f'''  Total Size: {get_size(partition_usage.total)} <br>
       Used: {get_size(partition_usage.used)} <br>
       Free: {get_size(partition_usage.free)} <br>
       Percentage: {partition_usage.percent}% <br>'''
    return info
