# core/normalizer.py

from urllib.parse import urlparse
from core.config import BLOCKED_KEYWORDS, ALLOWED_SCHEMES

def normalize_host(host):
    if not host:
        return None

    host = host.strip()
    if not host.startswith(ALLOWED_SCHEMES):
        host = "http://" + host

    try:
        p = urlparse(host)
    except Exception:
        return None

    if p.scheme not in ALLOWED_SCHEMES:
        return None

    netloc = p.netloc.lower()
    if any(bad in netloc for bad in BLOCKED_KEYWORDS):
        return None

    return f"{p.scheme}://{netloc}"

def normalize_list(items):
    clean = set()
    for i in items:
        if i:
            clean.add(i.strip())
    return sorted(clean)
