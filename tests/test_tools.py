import pytest
from prodigal_automation.tools import register_tool, call_tool

@register_tool("add")
def add(a: int, b: int) -> int:
    return a + b

def test_call_tool():
    assert call_tool("add", a=2, b=3) == 5
    with pytest.raises(KeyError):
        call_tool("nope")
