\# Lab 5: Static Code Analysis — Reflection



\*\*1. What is static code analysis?\*\*



Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, and coding-style problems early in software development.



\*\*2. What is the difference between Pylint, Bandit, and Flake8?\*\*



Pylint checks code quality, naming, documentation, and programming practices. Bandit identifies potentially insecure Python coding patterns. Flake8 checks coding style, whitespace, line length, and unused imports.



\*\*3. What issues did you identify and fix?\*\*



The original program contained unsafe expression evaluation, shell command execution, weak hashing, a hardcoded secret, broad exception handling, a mutable default argument, unused variables, and formatting problems. I corrected these issues by using safer operations, validating inputs, improving file handling, adding documentation, and following Python style conventions.



\*\*4. How does static code analysis improve software quality?\*\*



Static analysis helps identify issues before deployment, improves readability and maintainability, and reduces security risks. However, static analysis cannot find every logical error, so programs must also be tested by running them with appropriate inputs.



