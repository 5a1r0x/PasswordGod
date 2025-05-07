# 🧩 USAGE.md

> A quick reference to get you up and running with **PasswordGod** — your terminal-powered, secure password generator.

---

## 📥 Prerequisites

* **Python 3.8+** installed on your system
* Clone or download the repository:

  ```bash
  git clone https://github.com/5a1r0x/PasswordGod.git
  cd PasswordGod
  ```
* **Optional:** create and activate a virtual environment:

  ```bash
  python3 -m venv venv
  source venv/bin/activate   # Linux & macOS
  .\venv\Scripts\activate  # Windows
  ```
* Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

---

## 🚀 Basic Usage

Run the script directly from the terminal:

```bash
python passwordgod.py -h
```

* `-l 16`: generates a password of length 16 characters

**Sample output**:

```
[PASSWORD] xD7!gK2f#Q1mR8zW
```

---

## 📖 Options & Arguments

| Option            | Description                                   | Example |
| ----------------- | --------------------------------------------- | ------- |
| `-l`, `--length`  | **Required.** Password length (12–100)        | `-l 20` |
| `-a`, `--amount`  | Number of passwords to generate               | `-a 5`  |
| `-s`, `--symbols` | Include symbols in the password               | `-s`    |
| `-f`, `--file`    | Save generated passwords to `PasswordGod.txt` | `-f`    |
| `-v`, `--verbose` | Verbose mode (prints additional details)      | `-v`    |

> ⚠️ The minimum length is 12 and the maximum is 100. Values outside this range will trigger an error.

---

## 🎯 Advanced Examples

1. **Generate 3 passwords of 24 characters including symbols**:

   ```bash
   python passwordgod.py -l 24 -a 3 -s
   ```
2. **Generate 1 password of 12 characters, save to file and show verbose info**:

   ```bash
   python passwordgod.py -l 12 -f -v
   ```
3. **Generate 10 passwords of 16 characters without symbols**:

   ```bash
   python passwordgod.py --length 16 --amount 10
   ```

---

## 📂 Output File

When using the `-f` option:

* Passwords are appended to `PasswordGod.txt` in the current directory.
* Each password is written on a new line.

---

## 📋 Verbose Mode

Enable `-v` to display the parameters used:

```
[INFO] Password length: 12
[INFO] Amount: 1
[INFO] Symbols: False
[INFO] File: True
```

---

## 💡 Tips & Best Practices

* Combine `-s` and `-a` to quickly generate multiple secure passwords.
* Use shell redirection (`>`, `>>`) if you prefer custom file management.
* **Security reminder**: avoid committing `PasswordGod.txt` to public repositories.

---

**Happy securing with PasswordGod!** 🔐
