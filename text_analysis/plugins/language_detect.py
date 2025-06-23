class LanguageDetector:
    name = "LangGuesser"
    version = "0.2"
    description = "Guesses language from basic words."

    def analyze(self, text):
        if "la" in text or "bonjour" in text:
            return {"language": "French (guess)"}
        return {"language": "English (guess)"}

    async def async_analyze(self, text):
        return self.analyze(text)

