# modules/vulnmap.py

from subprocess import run

def vulnmap(host):
    cmd = f"nuclei -u {host} -severity medium,high,critical -silent"
    p = run(cmd, shell=True, capture_output=True, text=True)
    return p.stdout.splitlines() if p.returncode == 0 else []
