"""System Information"""

import platform
import psutil

class SystemInfo:
    def get_system_info(self):
        """Get system info"""
        return f"""
📊 SYSTEM INFO:
OS: {platform.system()} {platform.release()}
Processor: {platform.processor()}
Python: {platform.python_version()}
"""
    
    def get_cpu_info(self):
        """Get CPU info"""
        cpu_percent = psutil.cpu_percent(interval=1)
        return f"CPU Usage: {cpu_percent}%"
    
    def get_memory_info(self):
        """Get RAM info"""
        memory = psutil.virtual_memory()
        return f"RAM Usage: {memory.percent}% ({memory.used / (1024**3):.1f}GB / {memory.total / (1024**3):.1f}GB)"