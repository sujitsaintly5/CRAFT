# modules/passive.py

from subprocess import run

def passive_recon(domain):
    subs = {domain}

    cmds = [
        f"subfinder -d {domain} -silent",
        f"amass enum -passive -d {domain}"
    ]

    for cmd in cmds:
        p = run(cmd, shell=True, capture_output=True, text=True)
        if p.returncode == 0:
            subs.update(p.stdout.splitlines())

    return list(subs)

