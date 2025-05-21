from typing import Callable, Dict, Any

_TOOL_REGISTRY: Dict[str, Callable[..., Any]] = {}

def register_tool(name: str, fn: Callable[..., Any]) -> None:
    """Register fn under the given name."""
    _TOOL_REGISTRY[name] = fn

def call_tool(name: str, **kwargs) -> Any:
    """Invoke a previously-registered tool."""
    if name not in _TOOL_REGISTRY:
        raise KeyError(f"Tool '{name}' not found")
    return _TOOL_REGISTRY[name](**kwargs)
