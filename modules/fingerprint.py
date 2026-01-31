# modules/fingerprint.py

from subprocess import run

def fingerprint(host):
    cmd = f"echo {host} | httpx -silent -tech-detect"
    p = run(cmd, shell=True, capture_output=True, text=True)
    return p.stdout.splitlines() if p.returncode == 0 else []
