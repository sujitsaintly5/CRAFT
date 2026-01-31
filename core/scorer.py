# core/scorer.py

from core.config import RISK_THRESHOLDS

def score(host, info):
    s = 0

    if "admin" in host:
        s += 5
    if info.get("endpoints"):
        s += 4
    if info.get("vulns"):
        s += 6

    tech = " ".join(info.get("tech", [])).lower()
    if "wordpress" in tech:
        s += 3
    if "php" in tech:
        s += 2

    s += info.get("risk_penalty", 0)

    if s >= RISK_THRESHOLDS["HIGH"]:
        return s, "HIGH"
    if s >= RISK_THRESHOLDS["MEDIUM"]:
        return s, "MEDIUM"
    return s, "LOW"
