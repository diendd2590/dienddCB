import re
def is_binary(text: str) -> bool:
    raww = text.replace(" ", "")
    return bool(re.fullmatch(r'[01]+', raww))

def is_hex(text: str) -> bool:
    raww = text.replace(" ", "")
    return bool(re.fullmatch(r'[0-9a-fA-F]+', raww))

def is_base32(text: str) -> bool:
    raww = text.replace(" ", "").rstrip("=")
    return bool(re.fullmatch(r'[A-Z2-7]+', raww))

def is_base64(text: str) -> bool:
    raww = text.replace(" ", "").rstrip("=")
    return bool(re.fullmatch(r'[A-Za-z0-9+/]+', raww))

def is_morse(text: str) -> bool:
    raww = text.strip()
    return bool(re.fullmatch(r'[.\-\s/]+', raww))