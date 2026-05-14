# Password Security Auditor Pro

A professional password auditing tool that evaluates password strength using rule-based analysis, Shannon entropy calculation, common password dictionary screening, privacy-preserving breach detection with the Have I Been Pwned API (K-Anonymity), batch processing, and JSON report export.

---

## Features

- Password Strength Analysis
- Shannon Entropy Calculation
- Common Password Dictionary Check
- Have I Been Pwned Breach Detection (K-Anonymity)
- Batch Audit
- JSON report export
- Modular Python architecture

---

## Installation

```bash
git clone https://github.com/cchokaaa/password-security-auditor.git
cd password-security-auditor

python -m venv venv

# Git Bash
source venv/Scripts/activate

pip install -r requirements.txt
```

---

## Usage

### Single password check

```bash
python main.py "Password123!"
```

### Batch audit from file

```bash
python main.py --file sample/passwords.txt
```

### Export JSON report

```bash
python main.py "Password123!" --json report.json
```

---

## How It Works

### 1. Password Strength Analysis

The tool evaluates whether the password contains:

- At least 12 characters
- Uppercase letters
- Lowercase letters
- Digits
- Special characters

Each satisfied criterion contributes one point to the final score.

### 2. Shannon Entropy Calculation

Entropy is estimated using the following formula:

```text
Entropy = Length × log2(CharacterSetSize)
```

This provides an estimate of the theoretical password search space.

### 3. Common Password Dictionary Check

The password is compared against a local dictionary of known weak passwords stored in:

```text
sample/common_passwords.txt
```

### 4. Have I Been Pwned Breach Detection

The password is converted to a SHA-1 hash.

Only the first five characters of the hash are sent to the HIBP API.

The remaining hash suffix is matched locally, ensuring the plaintext password is never transmitted.

### 5. JSON Report Export

Analysis results can be saved to a JSON file for automation or further processing.

---

## Project Structure

```text
password-security-auditor/
│
├── main.py
├── password_checker.py
├── entropy_calculator.py
├── breach_checker.py
├── report_generator.py
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
└── sample/
    ├── passwords.txt
    └── common_passwords.txt
```

---

## Example Output

```text
Password: Password123!
Strength: Strong
Entropy: 78.4 bits
Dictionary Match: No
Breached: Yes (12543 times)
Recommendations:
- Consider using a password manager.
```

---

## JSON Output Example

```json
{
  "password": "Password123!",
  "score": 5,
  "strength": "Strong",
  "entropy": 78.4,
  "entropy_rating": "Strong",
  "dictionary_match": false,
  "breached": true,
  "breach_count": 12543,
  "recommendations": []
}
```

---

## Skills Demonstrated

- Password Security
- Information Theory
- K-Anonymity
- Threat Intelligence
- REST API Integration
- Python Engineering
- JSON Reporting

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.