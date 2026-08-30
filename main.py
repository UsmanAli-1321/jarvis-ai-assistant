"""
JARVIS AI Assistant - All-in-One Version
Simple version that works without complex folder structure
"""

from datetime import datetime

# ============ VOICE RECOGNITION ============
class VoiceRecognizer:
    def __init__(self):
        self.recognizer = None
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            print("✅ Voice recognition initialized")
        except ImportError:
            print("⚠️  speech_recognition not installed")
            self.recognizer = None
    
    def recognize(self):
        if not self.recognizer:
            return None
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("🎤 Listening...")
                audio = self.recognizer.listen(source, timeout=10)
            text = self.recognizer.recognize_google(audio)
            return text
        except:
            return None

# ============ TEXT-TO-SPEECH ============
class TextToSpeech:
    def __init__(self):
        self.engine = None
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            print("✅ Text-to-Speech initialized")
        except ImportError:
            print("⚠️  pyttsx3 not installed")
            self.engine = None
    
    def speak(self, text):
        if not text:
            return
        if not self.engine:
            print(f"🔊 {text}")
            return
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            print(f"🔊 {text}")

# ============ AI ASSISTANT ============
class Assistant:
    def __init__(self):
        pass
    
    def process_command(self, command):
        command_lower = command.lower().strip()
        
        # TIME
        if 'time' in command_lower:
            return f"The current time is {datetime.now().strftime('%I:%M %p')}"
        
        # DATE
        if 'date' in command_lower:
            return f"Today's date is {datetime.now().strftime('%A, %B %d, %Y')}"
        
        # GREETINGS
        if command_lower in ['hello', 'hi', 'hey']:
            return "Hello! How can I help you today?"
        
        if 'how are you' in command_lower:
            return "I'm working perfectly! Ready to assist you."
        
        if 'thank you' in command_lower or 'thanks' in command_lower:
            return "You're welcome! Happy to help."
        
        # OPEN APPS
        if command_lower.startswith('open '):
            app = command_lower.replace('open ', '')
            return f"Opening {app}..."
        
        # HELP
        if command_lower == 'help':
            return """📋 AVAILABLE COMMANDS:
- what time is it
- what's the date
- hello / hi
- how are you
- open [app name]
- thank you
- exit"""
        
        return f"I understood '{command}' but I'm not sure how to respond. Type 'help' for commands."

# ============ MAIN APP ============
class JarvisApp:
    def __init__(self):
        self.assistant = Assistant()
        self.voice_recognizer = VoiceRecognizer()
        self.tts = TextToSpeech()
        self.is_running = True
        self.voice_mode = False
    
    def print_banner(self):
        banner = """
╔════���═══════════════════════════════════════╗
║                                            ║
║   🤖 JARVIS AI ASSISTANT 🤖               ║
║   Your Intelligent PC Assistant           ║
║                                            ║
║   Commands:                                ║
║   • Type commands directly                 ║
║   • Say 'voice mode' to use speech         ║
║   • Type 'help' for all commands           ║
║   • Type 'exit' to quit                    ║
║                                            ║
╚════════════════════════════════════════════╝
"""
        print(banner)
    
    def run(self):
        self.print_banner()
        self.tts.speak("Good day. I am JARVIS, your AI assistant. How can I help you?")
        
        while self.is_running:
            try:
                if self.voice_mode:
                    command = self.voice_recognizer.recognize()
                    if command:
                        print(f"📝 You said: {command}")
                else:
                    command = input("\n📝 You: ").strip()
                
                if not command:
                    continue
                
                command_lower = command.lower()
                
                # EXIT
                if command_lower in ['exit', 'quit', 'goodbye']:
                    self.tts.speak("Goodbye! Have a great day!")
                    print("👋 JARVIS: Goodbye!")
                    break
                
                # VOICE MODE
                if command_lower == 'voice mode':
                    self.voice_mode = True
                    self.tts.speak("Voice mode enabled")
                    print("🎤 Voice mode: ON")
                    continue
                
                if command_lower == 'voice off':
                    self.voice_mode = False
                    print("🔕 Voice mode: OFF")
                    continue
                
                # PROCESS COMMAND
                response = self.assistant.process_command(command)
                print(f"🤖 JARVIS: {response}")
                
                if self.voice_mode:
                    self.tts.speak(response)
                    
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
        
        print("\n✨ JARVIS shutting down...")

def main():
    try:
        app = JarvisApp()
        app.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")

if __name__ == "__main__":
    main()
