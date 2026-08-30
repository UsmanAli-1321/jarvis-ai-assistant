"""Command Handler"""

import os
import subprocess
import platform

class CommandHandler:
    def __init__(self):
        self.platform = platform.system()
    
    def open_application(self, app_name):
        """Open an app"""
        try:
            if self.platform == "Windows":
                os.startfile(app_name)
                return f"Opening {app_name}..."
            elif self.platform == "Darwin":  # macOS
                subprocess.run(['open', '-a', app_name])
                return f"Opening {app_name}..."
            elif self.platform == "Linux":
                subprocess.Popen([app_name])
                return f"Opening {app_name}..."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def take_screenshot(self):
        """Take screenshot"""
        try:
            from PIL import ImageGrab
            import time
            
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            path = f"screenshot_{timestamp}.png"
            img = ImageGrab.grab()
            img.save(path)
            return f"Screenshot saved: {path}"
        except Exception as e:
            return f"Error: {str(e)}"