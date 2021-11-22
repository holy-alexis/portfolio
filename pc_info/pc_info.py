import psutil
import platform
from datetime import datetime


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def Get_PC_Info():
    s = "<html><p align=\"center\"><br>SYSTEM INFO:<br><br>"

    s += "="*10 + "System Information" + "="*10 + "<br>"
    uname = platform.uname()
    s += f"System: {uname.system}" + "<br>"
    s += f"Node Name: {uname.node}" + "<br>"
    s += f"Release: {uname.release}" + "<br>"
    s += f"Version: {uname.version}" + "<br>"
    s += f"Machine: {uname.machine}" + "<br>"
    s += f"Processor: {uname.processor}" + "<br>"
    s += "="*10 + "Boot Time" + "="*10 + "<br>"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    s += f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}" + "<br>"
    s += "="*10 + "CPU Info" + "="*10 + "<br>"
    s += "Physical cores:" + str(psutil.cpu_count(logical=False)) + "<br>"
    s += "Total cores:" + str(psutil.cpu_count(logical=True)) + "<br>"
    cpufreq = psutil.cpu_freq()
    s += f"Max Frequency: {cpufreq.max:.2f}Mhz" + "<br>"
    s += f"Min Frequency: {cpufreq.min:.2f}Mhz" + "<br>"
    s += f"Current Frequency: {cpufreq.current:.2f}Mhz" + "<br>"
    s += "CPU Usage Per Core:" + "<br>"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        s += f"Core {i}: {percentage}%" + "<br>"
    s += f"Total CPU Usage: {psutil.cpu_percent()}%" + "<br>"
    s += "="*10 + "Memory Information" + "="*10 + "<br>"
    svmem = psutil.virtual_memory()
    s += f"Total: {get_size(svmem.total)}" + "<br>"
    s += f"Available: {get_size(svmem.available)}" + "<br>"
    s += f"Used: {get_size(svmem.used)}" + "<br>"
    s += f"Percentage: {svmem.percent}%" + "<br>"

    s += "="*10 + "Disk Information" + "="*10 + "<br>"
    s += "Partitions and Usage:" + "<br>"
    partitions = psutil.disk_partitions()
    for partition in partitions:
        s += f"=== Device: {partition.device} ===" + "<br>"
        s += f"  Mountpoint: {partition.mountpoint}" + "<br>"
        s += f"  File system type: {partition.fstype}" + "<br>"
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        s += f"  Total Size: {get_size(partition_usage.total)}" + "<br>"
        s += f"  Used: {get_size(partition_usage.used)}" + "<br>"
        s += f"  Free: {get_size(partition_usage.free)}" + "<br>"
        s += f"  Percentage: {partition_usage.percent}%" + "<br>"
    return s
