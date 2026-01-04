# P-Scan - Advanced Python Port Scanner

P-SCAN is a Python-based, multi-threaded port scanner built to explore
network reconnaissance, stealth scanning techniques, and CLI tooling.

## Features
- Multi-threaded TCP port scanning
- Interactive & CLI modes
- Stealth & Ghost scanning modes
- Banner grabbing & service detection
- OS fingerprinting
- Verbose output mode
- Clean CLI UX

## Scan Modes
- **Standard** – Fast, general scanning
- **Verbose** – Detailed service & OS output
- **Stealth** – Slower, reduced probing
- **Ghost** – Ultra-quiet, minimal footprint

➡ Full mode details: [docs/MODES.md](docs/MODES.md)

## Usage
```bash
p-scan 192.168.1.1 -s -v
