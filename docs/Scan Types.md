## 🔍 Scan Types

P-SCAN supports multiple scan types to control the **port range** being scanned, allowing users to balance speed and coverage. These scan types were implemented to demonstrate practical control over scan scope, performance, and accuracy.

### Standard Scan
- **Ports:** `1 – 1024`
- Focuses on the most commonly used and well-known services
- Fast and efficient
- Ideal for quick reconnaissance

### Full Scan
- **Ports:** `1 – 65535`
- Scans all possible TCP ports
- Slower but comprehensive
- Useful for deep enumeration and lab environments

### Custom Scan
- **Ports:** User-defined range
- Allows precise targeting of specific services or port blocks
- Example: `8000 – 9000`
- Best for focused testing and experimentation
