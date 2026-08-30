"""Voice Recognition Module"""

class VoiceRecognizer:
    def __init__(self):
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            print("✅ Voice recognition ready")
        except ImportError:
            print("⚠️  Please install: pip install SpeechRecognition pydub")
            self.recognizer = None
    
    def recognize(self, timeout=10):
        """Listen and recognize voice"""
        if not self.recognizer:
            return None
        
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("🎤 Listening...")
                audio = self.recognizer.listen(source, timeout=timeout)
            
            text = self.recognizer.recognize_google(audio)
            print(f"✅ You said: {text}")
            return text
        except:
            return None