from typing import Protocol, runtime_checkable, Optional, Dict, Any

@runtime_checkable
class TextAnalyzer(Protocol):
    name: str
    version: str
    description: str

    def analyze(self, text: str) -> Dict[str, Any]:
        ...

    async def async_analyze(self, text: str) -> Optional[Dict[str, Any]]:
        ...
