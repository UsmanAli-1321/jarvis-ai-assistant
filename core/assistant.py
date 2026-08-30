"""AI Assistant - Command Processing"""

from datetime import datetime

class Assistant:
    def __init__(self):
        pass
    
    def process_command(self, command):
        """Process user commands"""
        command_lower = command.lower().strip()
        
        # TIME
        if 'time' in command_lower:
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
        
        # DATE
        if 'date' in command_lower:
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today's date is {current_date}"
        
        # GREETINGS
        if command_lower in ['hello', 'hi', 'hey']:
            return "Hello! How can I help you today?"
        
        if 'how are you' in command_lower:
            return "I'm working perfectly! Ready to assist you."
        
        # OPEN APPS
        if command_lower.startswith('open '):
            app = command_lower.replace('open ', '')
            return f"Opening {app}..."
        
        # DEFAULT
        return f"I understood '{command}' but I'm not sure how to respond. Type 'help' for commands."