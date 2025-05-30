# src/prodigal_automation/tools/manager.py

from typing import Any, Callable, Dict

# global registry
_TOOL_REGISTRY: Dict[str, Callable[..., Any]] = {}

def register_tool(name: str, fn: Callable[..., Any]) -> None:
    """
    Register a new tool under `name`.
    """
    if name in _TOOL_REGISTRY:
        raise KeyError(f"Tool '{name}' already registered")
    _TOOL_REGISTRY[name] = fn

def call_tool(name: str, **kwargs) -> Any:
    """
    Call a registered tool by name, passing through kwargs.
    """
    if name not in _TOOL_REGISTRY:
        raise KeyError(f"Tool '{name}' not found")
    return _TOOL_REGISTRY[name](**kwargs)
