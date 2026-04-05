from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class BaseBrain(ABC):
    """Abstract base class representing a swappable AI intelligence provider.

    This class defines the interface for different 'Brains' (e.g., Gemini, 
    Ollama, Qwen) used within the ANIC ecosystem. It allows the orchestrator 
    to switch providers at runtime without modifying the business logic.

    Attributes:
        provider_name (str): Human-readable name of the provider.
        model_name (str): Specific model version being used.
    """

    def __init__(self, provider_name: str, model_name: str):
        """Initializes the Brain provider with basic configuration.

        Args:
            provider_name: Canonical name of the AI service.
            model_name: Specific version/variant of the model.
        """
        self.provider_name = provider_name
        self.model_name = model_name

    @abstractmethod
    def generate_response(
        self, 
        prompt: str, 
        context: Optional[List[Dict[str, str]]] = None,
        stream: bool = False
    ) -> Any:
        """Generates a text response based on the provided prompt and context.

        Args:
            prompt: The user input or system instruction.
            context: A list of previous interaction turns (history).
            stream: Whether to stream the response chunks or return all at once.

        Returns:
            The generated response content or a generator if streaming.

        Raises:
            ConnectionError: If the provider API is unreachable.
            RateLimitError: If the provider's quota has been exceeded.
        """
        pass

    @abstractmethod
    def switch_model(self, new_model_name: str) -> bool:
        """Dynamically switches the active model within the same provider.

        Args:
            new_model_name: The target model version.

        Returns:
            bool: True if the switch was successful, False otherwise.
        """
        pass

class GeminiProvider(BaseBrain):
    """Implementation of the Google Gemini AI provider.

    Showcases integration with multimodal capabilities and high-availability 
    cloud endpoints.
    """

    def generate_response(self, prompt: str, context: Optional[List[Dict[str, str]]] = None, stream: bool = False) -> str:
        """Mocked implementation of Gemini text generation."""
        return f"[Mock Gemini Response] based on '{prompt[:20]}...'"

    def switch_model(self, new_model_name: str) -> bool:
        """Mocked model switching logic."""
        self.model_name = new_model_name
        return True
