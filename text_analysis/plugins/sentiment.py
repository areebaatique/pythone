class SentimentAnalyzer:
    name = "DummySentiment"
    version = "0.1"
    description = "Simple sentiment based on keywords."

    def analyze(self, text):
        score = 1 if "good" in text else -1 if "bad" in text else 0
        return {"sentiment": score}

    async def async_analyze(self, text):
        return self.analyze(text)


