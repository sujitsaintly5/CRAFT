# core/reducer.py

def reduce_noise(data):
    """
    Reduce obvious noise WITHOUT deleting everything.
    Penalize instead of removing.
    """
    for host, info in data.items():
        penalty = 0

        tech_blob = " ".join(info.get("tech", [])).lower()

        if "cloudflare" in tech_blob:
            penalty -= 2
        if not info.get("endpoints"):
            penalty -= 1
        if not info.get("vulns"):
            penalty -= 1

        info["risk_penalty"] = penalty

    return data
