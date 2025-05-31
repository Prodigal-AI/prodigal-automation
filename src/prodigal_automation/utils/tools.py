import json
from datetime import datetime

def print_json(data):
    """Helper to pretty print JSON data."""
    print(json.dumps(data, indent=4, default=json_serializer))

def json_serializer(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime)):
        return obj.isoformat()
    # For Pydantic v2 models, use model_dump()
    if hasattr(obj, 'model_dump'):
        return obj.model_dump()
    # For Pydantic v1 models (if still in use), use dict()
    elif hasattr(obj, 'dict'):
        return obj.dict()
    raise TypeError ("Type %s not serializable" % type(obj))