from .detection import calculate_intersection

__version__ = "0.1.0"

def detect(text, truncate_size=2048):
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    return calculate_intersection(text, truncate_size=truncate_size)

