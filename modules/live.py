# modules/live.py

from subprocess import run

def is_live(host):
    cmd = f"echo {host} | httpx -silent -follow-redirects"
    p = run(cmd, shell=True, capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else None
