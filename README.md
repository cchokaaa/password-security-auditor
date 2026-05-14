# Password Security Auditor Pro

A professional password auditing tool that evaluates password strength using rule-based analysis, Shannon entropy calculation, common password dictionary screening, privacy-preserving breach detection with the Have I Been Pwned API (K-Anonymity), batch processing, and JSON report export.

---

## Features

- Rule-based password strength analysis
- Shannon entropy calculation
- Common password dictionary check
- Have I Been Pwned breach detection
- Batch auditing from a text file
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

### Analyze a Single Password

```bash
python main.py "Password123!"
```

### Export JSON Report

```bash
python main.py "Password123!" --json report.json
```

### Batch Audit

```bash
python main.py --file sample/passwords.txt
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

The password is compared against a local dictionary of known weak passwords stored in `sample/common_passwords.txt`.

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
Entropy: 78.66 bits (Strong)
Dictionary Match: No
Breached: Yes (12543 times)
--------------------------------------------------
```

---

## Skills Demonstrated

- Python
- Cybersecurity
- Password Security
- Shannon Entropy
- K-Anonymity
- REST API Integration
- JSON Serialization
- CLI Development
- Modular Software Design

---

## License

This project is for educational and portfolio purposes.