import importlib
import logging
from typing import Dict, List, Type, Any

class PluginBase:
    """Base class defining the standard interface for all system-level 
    capabilities.

    Subclasses must implement the 'execute' method to perform specific 
    actions like interacting with the shell, file system, or web browsers.
    """

    def __init__(self, name: str):
        """Initializes the plugin with a unique identifier.

        Args:
            name: The canonical name of the plugin (e.g., 'terminal', 'office').
        """
        self.name = name

    def execute(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Performs a specific task defined by the action and parameters.

        Args:
            action: The operation to perform.
            params: Parameters required for the operation.

        Returns:
            Dict[str, Any]: The outcome of the execution.
        """
        raise NotImplementedError("Plugins must override the 'execute' method.")


class PluginManager:
    """Centralized manager for loading and orchestrating system plugins.

    This class handles the discovery, lifecycle management, and dynamic 
    dispatching of requests across various capability providers.

    Attributes:
        _plugins (Dict[str, PluginBase]): Registry of active plugins.
    """

    def __init__(self):
        """Initializes an empty plugin registry."""
        self._plugins: Dict[str, PluginBase] = {}

    def register_plugin(self, plugin: PluginBase) -> None:
        """Adds a pre-initialized plugin instance to the registry.

        Args:
            plugin: The initialized plugin instance.
        """
        self._plugins[plugin.name] = plugin
        logging.info(f"Plugin '{plugin.name}' registered successfully.")

    def run_capability(self, plugin_name: str, action: str, **kwargs) -> Dict[str, Any]:
        """Dispatches an execution request to a specific plugin.

        Args:
            plugin_name: The name of the target plugin.
            action: The operation to trigger within that plugin.
            **kwargs: Arguments to pass to the plugin execution.

        Returns:
            Dict[str, Any]: Results provided by the plugin.

        Raises:
            KeyError: If the requested plugin is not loaded.
        """
        if plugin_name not in self._plugins:
            raise KeyError(f"Plugin '{plugin_name}' not found.")
        
        return self._plugins[plugin_name].execute(action, kwargs)

    def list_active_plugins(self) -> List[str]:
        """Returns a list of currently registered plugin names.

        Returns:
            List[str]: List of loaded plugin identifiers.
        """
        return list(self._plugins.keys())
