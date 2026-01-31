# core/config.py

TOOLS = {
    "subfinder": "subfinder",
    "amass": "amass",
    "httpx": "httpx",
    "gau": "gau",
    "nuclei": "nuclei",
}

MAX_WORKERS = 5
HTTP_TIMEOUT = 10

ALLOWED_SCHEMES = ("http", "https")
BLOCKED_KEYWORDS = ("localhost", "127.0.0.1", ".internal", ".local")

INTERESTING_ENDPOINT_KEYWORDS = (
    "admin", "api", "upload", "export", "debug", "reset", "manage"
)

RISK_THRESHOLDS = {
    "HIGH": 10,
    "MEDIUM": 5
}

OUTPUT_DIR = "output"
REPORT_JSON = "output/report.json"
REPORT_MD = "output/report.md"
