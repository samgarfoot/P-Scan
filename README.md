# P-Scan - Advanced Python Port Scanner

P-SCAN is a Python-based, multi-threaded port scanner built to explore
network reconnaissance, stealth scanning techniques, and CLI tooling.

## Project Overview

P-SCAN was built as a hands-on learning project to deeply understand how
port scanners and reconnaissance tools work under the hood, rather than
relying on existing tools like Nmap.

The goal was not to replace professional scanners, but to explore:
- How TCP connections behave at scale
- How scan speed and probing techniques affect detectability
- How different operational modes change network footprint
- How to design a clean, usable CLI security tool in Python

Throughout the project, I focused on writing clear, modular code,
implementing multiple scanning strategies, and balancing performance,
stealth, and usability.

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

## Key Learning Outcomes

- Implemented multi-threaded network scanning in Python
- Gained practical understanding of TCP connection behavior
- Explored stealth scanning concepts and detection trade-offs
- Designed an interactive and CLI-driven user experience
- Improved code structure and documentation for maintainability

## Usage
```bash
p-scan 192.168.1.1 -s -v

