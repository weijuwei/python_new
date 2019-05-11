# psutil is a cross-platform library for retrieving information on
# running processes and system utilization (CPU, memory, disks, network,
# sensors) in Python

#     # functions
#     "pid_exists", "pids", "process_iter", "wait_procs",             # proc
#     "virtual_memory", "swap_memory",                                # memory
#     "cpu_times", "cpu_percent", "cpu_times_percent", "cpu_count",   # cpu
#     "cpu_stats",  # "cpu_freq", "getloadavg"
#     "net_io_counters", "net_connections", "net_if_addrs",           # network
#     "net_if_stats",
#     "disk_io_counters", "disk_partitions", "disk_usage",            # disk
#     # "sensors_temperatures", "sensors_battery", "sensors_fans"     # sensors
#     "users", "boot_time",                                           # others


import psutil,datetime

# print(psutil.users())  #用户

# print(psutil.cpu_stats())  # cpu统计

# print(psutil.disk_partitions())  # 硬盘分区

# # print(psutil.disk_usage('d:\\'))

# print(datetime.datetime.fromtimestamp(psutil.boot_time ()).strftime("%Y-%m-%d %H: %M: %S"))  # 启动时间

# print(psutil.net_if_addrs())  # 返回每个网卡关联的地址

# print(psutil.virtual_memory())  # 返回虚拟内存

# print(psutil.net_connections())

# print(psutil.pids())  # 查看系统全部进程

p = psutil.Process(14192)  # 查看单个进程

print(p.name())  # 进程名字
print(p.status())  # 进程运行转台
print(p.open_files())  # 进程打开的文件
print(p.num_threads())  # 进程开启的线程数
print(p.memory_info())  # 进程内存rss,vms信息