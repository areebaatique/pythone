class WordCountAnalyzer:
    name = "WordCounter"
    version = "1.0"
    description = "Counts the number of words."

    def analyze(self, text):
        return {"word_count": len(text.split())}

    async def async_analyze(self, text):
        return self.analyze(text)

