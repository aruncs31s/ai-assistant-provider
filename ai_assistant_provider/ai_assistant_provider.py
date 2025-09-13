
import abc
from enum import Enum
import time

class AiProviderStatus(Enum):
    IDLE = "Idle"
    BUSY = "Busy"
    ERROR = "Error"
    OFFLINE = "Offline"
class AiProviderList(Enum):
    OLLAMA = "Ollama"
    ALEXA = "Alexa"
    GITHUB_GPT_5 = "GitHub GPT-5"
    
class AiProvider(abc.ABC):
    def __init__(self):
        self._status = AiProviderStatus.IDLE
        """Initializing answer to empty string"""
        self._answer = ""
        self._messages = []
        self.question_asked_time = 0.0
        self.answer_time = 0.0
        self.response_time = 0.0

    @abc.abstractmethod
    def ask(self, prompt: str) -> str:
        """Abstract method that must be implemented by subclasses"""
        pass
    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Abstract method that must be implemented by subclasses"""
        pass
    @property
    def status(self) -> AiProviderStatus:
        """Property getter for status"""
        return self._status

    @status.setter
    def status(self, value: AiProviderStatus) -> None:
        """Property setter for status"""
        self._status = value
    
    @property
    def answer(self) -> str:
        """Property getter for answer"""
        return self._answer
    @answer.setter
    def answer(self, value: str) -> None:
        """Property setter for answer"""
        self.answer_time = time.time()
        self._answer = value
        
    @property
    def messages(self) -> list[dict[str, str]]:
        """Property getter for messages"""
        return self._messages

    @messages.setter
    def messages(self, value: list[dict[str, str]]) -> None:
        """Property setter for messages"""
        """ For getting question response time """
        self.question_asked_time = time.time()
        self._messages = value
    
    def add_message(self, role: str, content: str) -> None:
        """Method to add a message to the messages list"""
        self._messages.append({"role": role, "content": content})
    def clear_messages(self) -> None:
        """Method to clear the messages list"""
        self._messages = []
        print("Conversation history cleared")

    def show_conversation_history(self) -> None:
        """Display the current conversation history"""
        print(f"\n📝 Conversation History ({len(self.messages)} messages):")
        for i, msg in enumerate(self.messages):
            print(f"  {i+1}. {msg['role'].upper()}: {msg['content'][:100]}{'...' if len(msg['content']) > 100 else ''}")
        print()

    def get_conversation_stats(self) -> dict:
        """Get statistics about the current conversation"""
        user_messages = [msg for msg in self.messages if msg['role'] == 'user']
        assistant_messages = [msg for msg in self.messages if msg['role'] == 'assistant']

        total_chars = sum(len(msg['content']) for msg in self.messages)

        return {
            'total_messages': len(self.messages),
            'user_messages': len(user_messages),
            'assistant_messages': len(assistant_messages),
            'total_characters': total_chars,
            'avg_message_length': total_chars / len(self.messages) if self.messages else 0
        }
    def get_response_time(self) -> float:
        """Calculate the response time for the last operation"""
        if self.answer_time > 0 and self.question_asked_time > 0:
            self.response_time = self.answer_time - self.question_asked_time
            return self.response_time
        else:
            return 0.0 


