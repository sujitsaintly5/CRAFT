# CRAFT

### Custom Reconnaissance Automation Framework Tool for Offensive Security

ReconX is a modular, decision-driven reconnaissance automation framework designed for offensive security, penetration testing, and bug bounty reconnaissance.

Unlike traditional recon scripts that simply aggregate tool output, ReconX focuses on attack surface prioritization — helping security testers decide where to spend their limited manual testing time.

## ⚠️ Disclaimer
This tool is intended ONLY for authorized security testing, educational labs, and bug bounty programs where you have explicit permission.
The author is not responsible for misuse.

## 🎯 Why ReconX Exists
### Most recon tools answer:
```
“What assets exist?”
```
### ReconX answers:
```
“Which assets matter the most to attack?”
```

### In real-world offensive security:

 1. Time is limited
 2. Noise is high
 3. Blind scanning wastes effort

### ReconX reduces noise by:

 1. Correlating recon data
 2. Penalizing low-signal hosts
 3. Prioritizing high-risk attack surfaces

## 🧠 Core Philosophy
### ReconX follows real attacker methodology:

 1. Discover attack surface
 2. Validate what is actually reachable
 3. Understand technology context
 4. Identify high-value endpoints
 5. Map known vulnerability signals
 6. Prioritize targets using risk heuristics
 7. Hand off results to manual testing

 - ❌ No auto-exploitation
 - ❌ No brute forcing
 - ❌ No weaponized payloads

 - ✔ Ethical
 - ✔ Practical
 - ✔ Realistic

## 🏗 Architecture Overview

```
Target Domain
     ↓
Passive Asset Discovery
     ↓
Live Host Validation
     ↓
Technology Fingerprinting
     ↓
Endpoint Intelligence
     ↓
Vulnerability Signal Mapping
     ↓
Noise Reduction
     ↓
Risk Scoring
     ↓
Actionable Recon Report
```
### ReconX is a decision engine, not just a scanner.

## 📁 Project Structure

```
ReconX/
├── recon.py                # Main execution engine
│
├── core/
│   ├── config.py           # Global configuration
│   ├── executor.py         # Concurrent execution engine
│   ├── normalizer.py       # Data cleanup & normalization
│   ├── reducer.py          # False-positive reduction
│   ├── scorer.py           # Risk scoring logic
│   └── reporter.py         # Report generation
│
├── modules/
│   ├── passive.py          # Passive subdomain discovery
│   ├── live.py             # Live host validation
│   ├── fingerprint.py      # Technology detection
│   ├── endpoints.py        # Endpoint intelligence
│   └── vulnmap.py          # Vulnerability signal mapping
│
└── output/
    ├── report.json         # Machine-readable report
    └── report.md           # Human-readable report
```

## 🔧 Dependencies

Tool & Purpose
```
subfinder      Passive subdomain enumration
amass          Passive asset discovery
httpx          HTTP probing endpoint descovery
gau            Historical endpoint descovery
nuclei         Vulnerability signal mapping
```
### Note - ReconX does not replace these tools - It coordinates and contextualizes them.

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/reconx.git
cd reconx
```
### 2️⃣ Install System Dependencies

```
sudo apt update
sudo apt install -y subfinder amass httpx nuclei golang
```
Install gau:
```
go install github.com/lc/gau/v2/cmd/gau@latest
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
source ~/.bashrc
```
Verify:
```
subfinder -h
amass -h
httpx -h
gau -h
nuclei -version
```
### 3️⃣ Python Environment (Recommended)

```
python3 -m venv venv
source venv/bin/activate
```

## ▶️ Usage
### Basic Recon
```
python3 recon.py -d example.com
```
ReconX will:
 1. Discover subdomains
 2. Validate live hosts
 3. Extract technologies
 4. Identify interesting endpoints
 5. Map vulnerability signals
 6. Generate prioritized reports

## 📊 Output Explained
``` output/report.json ```

Machine-readable output for:
 1. Further automation
 2. Integration with other tools
 3. Data analysis

``` output/report.md ```

Human-readable report optimized for:
 1. Manual testing
 2. Bug bounty workflows
 3. Pentest planning

Each host includes:
 1. Risk level (HIGH/MEDIUM/LOW)
 2. Risk score
 3. Technology stack
 4. Integrating endpoints
 5. Vulnerability signals

## 🔥 How Bug Hunters Use ReconX
1. Run recon on target scope
2. Sort by HIGH risk
3. Manually test:
   - Authentication flows
   - IDORs
   - File uploads
   - API logic
4. Ignore LOW risk noise
5. Write high-quality reports
ReconX saves hours of wasted testing

## 🧮 Risk Scoring (High-Level)
Risk is calculated using:
- Admin or sensitive subdomains
- Presence of high-value endpoints
- Vulnerability signals
- Technology-specific risk
- Noise penalties(CDN, static hosts)
Scores are heuristic-based, not CVSS-designed to reflect real attacker behavior.

## 🛡 Safety & Design Choices

- No aut-exploitation
- No destructive actions
- Graceful degradation if tools are missing
- Clear failure visibility
- Conservative defaults

ReconX is safe by design

## 🧪 Tested Environment
- Kali Linux
- Debian-based pentesting environments
- Python3.10+

## 🚀 Roadmap (Optional Enhancements)
- Dependency health checks
- Configuration scoring profiles
- Burp integration
- HTML reporting
- Multi-target batch mode

## 👤 Author
Build as a hands-on offensive security project to demonstrate:
- Recon automation
- Attack surface analysis
- Engineering discipline
- Pentesting mindset

----Sujit Saintly (Sujit Kumar) ------
