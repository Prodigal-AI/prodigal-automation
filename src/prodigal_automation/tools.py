from typing import Callable, Dict, Any

_TOOL_REGISTRY: Dict[str, Callable[..., Any]] = {}

def register_tool(name: str):
    def decorator(fn: Callable[..., Any]):
        _TOOL_REGISTRY[name] = fn
        return fn
    return decorator

def call_tool(name: str, **kwargs):
    if name not in _TOOL_REGISTRY:
        raise KeyError(f"Tool '{name}' not found")
    return _TOOL_REGISTRY[name](**kwargs)
