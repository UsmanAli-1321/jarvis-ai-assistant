"""Text-to-Speech Module"""

class TextToSpeech:
    def __init__(self):
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            print("✅ Text-to-Speech ready")
        except ImportError:
            print("⚠️  Please install: pip install pyttsx3")
            self.engine = None
    
    def speak(self, text):
        """Convert text to speech"""
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