# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Line(s) in Original Code | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution | Security — High | 56 | `os.system()` executes a shell command and can introduce command injection risks. | Removed shell execution and used a normal print statement. |
| Weak MD5 hash | Security — High | 45 | MD5 is not suitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Dynamic expression evaluation | Security — Medium | 40 | `eval()` can execute arbitrary Python expressions. | Replaced it with a validated numeric multiplier. |
| Broad exception handling | Code quality / Security | 22–25 | Bare `except` hides errors. | Checked whether the patient record exists before updating it. |
| Mutable default argument | Code quality | 13 | A default list can be shared between function calls. | Changed the default to `None`. |
| Hardcoded secret | Security | 68, 77 | A master key was embedded in the source and printed. | Removed the hardcoded key and its output. |
| Unused imports and variables | Code quality / Style | 4, 29, 39, 61 | Unused names reduced readability and triggered warnings. | Removed unused imports and variables. |
| Missing documentation and naming issues | Maintainability | Multiple | Functions lacked docstrings and one function used camelCase. | Added docstrings and adopted snake_case naming. |
| File handling | Code quality | 53–55 | The file was opened without an explicit encoding and closed manually. | Used a context manager and UTF-8 encoding. |
| Formatting issues | Style | Multiple | The file had long lines and lacked a final newline. | Corrected formatting and added a final newline. |

## Verification

- Original Pylint score: 5.19/10.
- Final Pylint score: 10.00/10.
- Final Bandit report: No issues identified.
- Final Flake8 report: No violations reported.
