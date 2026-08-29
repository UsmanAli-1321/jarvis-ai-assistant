"""
JARVIS AI Assistant - Main Application
A voice and text-based AI assistant that can control your PC
Works on Windows, Mac, and Linux
"""

import os
import sys
import json
from datetime import datetime
from core.assistant import Assistant
from core.voice import VoiceRecognizer
from core.tts import TextToSpeech

class JarvisApp:
    def __init__(self):
        self.assistant = Assistant()
        self.voice_recognizer = VoiceRecognizer()
        self.tts = TextToSpeech()
        self.is_running = True
        self.voice_mode = False
        
    def print_banner(self):
        """Print welcome banner"""
        banner = """
        ╔════════════════════════════════════════════╗
        ║                                            ║
        ║   🤖 JARVIS AI ASSISTANT 🤖               ║
        ║   Your Intelligent PC Assistant           ║
        ║                                            ║
        ║   Commands:                                ║
        ║   • Type commands directly                 ║
        ║   • Say 'voice mode' to use speech         ║
        ║   • Say or type 'help' for commands        ║
        ║   • Say or type 'exit' to quit             ║
        ║                                            ║
        ╚════════════════════════════════════════════╝
        """
        print(banner)
    
    def print_help(self):
        """Display all available commands"""
        help_text = """
        📋 AVAILABLE COMMANDS:
        
        🎙️  VOICE CONTROL:
        • voice mode          - Enable voice recognition
        • voice off           - Disable voice recognition
        • listen              - Start listening for commands
        
        ⏰ TIME & DATE:
        • what time is it     - Get current time
        • what's the date     - Get today's date
        
        🔍 SEARCH & WEB:
        • search [query]      - Search on Google
        • weather [city]      - Get weather info
        
        🖥️  APPLICATION CONTROL:
        • open [app name]     - Open an application
        • close [app name]    - Close an application
        • list apps           - Show running applications
        
        📁 FILE MANAGEMENT:
        • open file [path]    - Open a file
        • list files [path]   - List files in directory
        • create file [path]  - Create a new file
        
        🎨 SYSTEM:
        • screenshot          - Take a screenshot
        • volume [level]      - Set volume (0-100)
        • brightness [level]  - Set screen brightness
        • system info         - Show system information
        • shutdown            - Shutdown computer
        • restart             - Restart computer
        • lock                - Lock screen
        
        💬 CONVERSATION:
        • hello / hi          - Start a conversation
        • how are you         - Ask assistant status
        • thank you           - Say thanks
        
        ⚙️  SETTINGS:
        • settings            - Open settings
        • about               - About JARVIS
        • help                - Show this help menu
        • exit / quit         - Exit the assistant
        
        💡 TIPS:
        • You can use natural language
        • Example: "Open Chrome and search for Python tutorials"
        • Example: "What's the weather in London?"
        """
        print(help_text)
    
    def handle_voice_input(self):
        """Handle voice commands"""
        try:
            self.tts.speak("Listening... Please say a command")
            print("\n🎤 Listening for voice command...")
            
            command = self.voice_recognizer.recognize()
            if command:
                print(f"✅ You said: {command}")
                return command
            else:
                self.tts.speak("Sorry, I didn't catch that. Please repeat.")
                print("❌ No command recognized. Please try again.")
                return None
                
        except Exception as e:
            print(f"❌ Voice recognition error: {e}")
            self.tts.speak("Sorry, there was an error with voice recognition")
            return None
    
    def handle_text_input(self):
        """Handle text commands"""
        try:
            user_input = input("\n📝 You: ").strip()
            return user_input
        except KeyboardInterrupt:
            return "exit"
        except Exception as e:
            print(f"Error reading input: {e}")
            return None
    
    def process_command(self, command):
        """Process and execute commands"""
        if not command:
            return
        
        command_lower = command.lower().strip()
        
        # Exit commands
        if command_lower in ['exit', 'quit', 'goodbye', 'bye']:
            self.tts.speak("Goodbye! Have a great day!")
            print("\n👋 JARVIS: Goodbye! See you next time!")
            self.is_running = False
            return
        
        # Help command
        if command_lower == 'help':
            self.print_help()
            return
        
        # Voice mode toggle
        if command_lower == 'voice mode':
            self.voice_mode = True
            self.tts.speak("Voice mode enabled. I'm listening.")
            print("🎤 Voice mode: ENABLED")
            return
        
        if command_lower == 'voice off':
            self.voice_mode = False
            self.tts.speak("Voice mode disabled.")
            print("🔕 Voice mode: DISABLED")
            return
        
        # Process command through assistant
        response = self.assistant.process_command(command)
        
        # Speak and print response
        print(f"🤖 JARVIS: {response}")
        if self.voice_mode:
            self.tts.speak(response)
    
    def run(self):
        """Main application loop"""
        self.print_banner()
        self.tts.speak("Good day. I am JARVIS, your AI assistant. How can I help you?")
        
        while self.is_running:
            try:
                # Get input based on mode
                if self.voice_mode:
                    command = self.handle_voice_input()
                else:
                    command = self.handle_text_input()
                
                # Process the command
                if command:
                    self.process_command(command)
                    
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user")
                self.is_running = False
            except Exception as e:
                print(f"❌ Error: {e}")
                self.tts.speak("An error occurred. Please try again.")
        
        print("\n✨ JARVIS shutting down...")
        sys.exit(0)


def main():
    """Entry point"""
    try:
        app = JarvisApp()
        app.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
