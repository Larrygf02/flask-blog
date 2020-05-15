from sqlalchemy import inspect

def to_dict(obj, ignore=None):
    if ignore is None:
        ignore = []
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs if c.key not in ignore}

def exists(obj):
    if obj.count() >= 1:
        return True
    return False