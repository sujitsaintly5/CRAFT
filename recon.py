# recon.py

from core.executor import run_concurrent
from core.reducer import reduce_noise
from core.scorer import score
from core.reporter import write_report

from modules.passive import passive_recon
from modules.live import is_live
from modules.fingerprint import fingerprint
from modules.endpoints import endpoints
from modules.vulnmap import vulnmap

def run(domain):
    print("[*] Recon started:", domain)

    subs = passive_recon(domain)
    print("[+] Subdomains:", len(subs))

    live = run_concurrent(is_live, subs)
    live_hosts = [h for h, v in live.items() if v]

    print("[+] Live hosts:", len(live_hosts))

    tech = run_concurrent(fingerprint, live_hosts)
    eps = run_concurrent(endpoints, live_hosts)
    vulns = run_concurrent(vulnmap, live_hosts)

    data = {}
    for h in live_hosts:
        data[h] = {
            "live": True,
            "tech": tech.get(h, []),
            "endpoints": eps.get(h, []),
            "vulns": vulns.get(h, [])
        }

    data = reduce_noise(data)

    for h in data:
        s, r = score(h, data[h])
        data[h]["score"] = s
        data[h]["risk"] = r

    write_report(data)

if __name__ == "__main__":
    import sys
    run(sys.argv[1])
