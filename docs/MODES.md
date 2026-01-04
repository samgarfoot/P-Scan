# 🔧 Scan Modes Overview

P-SCAN implements multiple scanning modes designed to demonstrate how different reconnaissance strategies affect speed, visibility, and information depth.
Each mode modifies scanner behavior such as timeout values, output verbosity, and probing intensity, allowing the user to choose the appropriate approach based on their objective.

## 🟢 Standard Mode (Default)
Purpose: Balanced, general-purpose scanning
<br>
Use Case: Quick enumeration with minimal configuration

### Behaviour
- Uses default socket timeout
- Scans ports at normal speed
- Minimal output (open ports only)
- No additional probing or delays
### Characteristics
- Fast and efficient
- Lowest complexity
- Ideal for initial reconnaissance
### Trade-offs
- No detailed service or OS information
- More detectable than slower modes due to speed

## 🔵 Verbose Mode

Purpose: Maximum visibility and learning
<br>
Use Case: Debugging, analysis, and deeper inspection

### Behaviour
- Displays service names for open ports
- Captures and prints service banners when available
- Performs basic OS fingerprinting from banner data
- Outputs detailed scan results in real time
### Characteristics
- Information-rich output
- Helpful for understanding service exposure
- Best suited for controlled environments or labs
### Trade-offs
- More network interaction
- Slightly noisier due to additional probing
- Not designed for stealth

## 🟡 Stealth Mode

Purpose: Reduced detectability
<br>
Use Case: Quiet scanning with lower network footprint

### Behaviour
- Increases socket timeout
- Slows scan rate intentionally
- Limits aggressive probing
- Reduces likelihood of triggering basic IDS/IPS alerts
### Characteristics
- Slower than standard scans
- Lower traffic footprint
- More discreet scanning pattern
### Trade-offs
- Increased scan duration
- Less banner data collected
- Still not fully invisible to advanced detection systems

## 🟣 Ghost Mode
Purpose: Maximum stealth and minimal footprint
<br>
Use Case: Demonstrating ultra-low-noise reconnaissance concepts

### Behavior
- Uses significantly increased timeouts
- Extremely slow scanning pace
- Minimal probing after connection
- Prioritises discretion over speed or detail
### Characteristics
- Quietest scan mode available
- Designed to minimize observable patterns
- Demonstrates trade-offs between speed and detection risk
### Trade-offs
- Very slow
- Limited service information
- Intended for educational and experimental use

## 📊 Scan Mode Comparison

| Mode     | Scan Speed | Verbosity Level | Stealth Level | Network Footprint | Best Use Case |
|----------|------------|-----------------|---------------|-------------------|---------------|
| Standard | Fast       | Low             | Low           | Normal            | Quick port discovery |
| Verbose  | Medium     | High            | Low           | Higher            | Detailed analysis & learning |
| Stealth  | Slow       | Medium          | Medium        | Reduced           | Quiet reconnaissance |
| Ghost    | Very Slow  | Low             | High          | Minimal           | Ultra-low noise scanning |

