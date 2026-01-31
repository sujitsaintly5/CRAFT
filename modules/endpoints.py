# modules/endpoints.py

from subprocess import run
from core.config import INTERESTING_ENDPOINT_KEYWORDS

def endpoints(host):
    cmd = f"echo {host} | gau"
    p = run(cmd, shell=True, capture_output=True, text=True)

    if p.returncode != 0:
        return []

    urls = p.stdout.splitlines()
    return [
        u for u in urls
        if any(k in u.lower() for k in INTERESTING_ENDPOINT_KEYWORDS)
    ]
