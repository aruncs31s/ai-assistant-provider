# AI Assistant Provider

Version : 0.0.6
## Installation

```bash
pip install ai-assistant-provider
```

## Usage
```python
from ai_assistant_provider import AiProvider
class MyAiProvider(AiProvider):
    def __init__(self):
        super().__init__()
    # You must implement this method
    @property
    def name(self) -> str:
        return "Some AI Provider"
    
    def ask(self, prompt: str) -> str:
        self.add_message("user", prompt)
        response = f"Response to: {prompt}"
        self.add_message("assistant", response)
        self.answer = response
        return response
# Usage
provider = MyAiProvider()
response = provider.ask("Hello, how are you?")
print(f"Status: {provider.status}")
print(f"Response: {response}")
```