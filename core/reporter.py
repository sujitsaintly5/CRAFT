# core/reporter.py

import json, os
from core.config import REPORT_JSON, REPORT_MD

def write_report(data):
    os.makedirs(os.path.dirname(REPORT_JSON), exist_ok=True)

    with open(REPORT_JSON, "w") as f:
        json.dump(data, f, indent=4)

    with open(REPORT_MD, "w") as f:
        f.write("# ReconX Report\n\n")
        for host, info in sorted(
            data.items(),
            key=lambda x: x[1].get("score", 0),
            reverse=True
        ):
            f.write(f"## {host}\n")
            f.write(f"- Risk: {info['risk']}\n")
            f.write(f"- Score: {info['score']}\n\n")

            for key in ("tech", "endpoints", "vulns"):
                vals = info.get(key)
                if vals:
                    f.write(f"**{key.upper()}**\n")
                    for v in vals:
                        f.write(f"- {v}\n")
                    f.write("\n")

            f.write("---\n\n")

    print("[+] Report generated successfully")
