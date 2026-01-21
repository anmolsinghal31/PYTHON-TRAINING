import re

def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

    if re.match(pattern, password):
        return True
    return False

# Example Usage
pw = "StrongPass123!"
print(f"Password '{pw}' is valid: {validate_password(pw)}")




#2ND PART
import re

sample_text = "Password\n123"

# 1. re.IGNORECASE: Matches text regardless of letter case
print("--- IGNORECASE ---")
print(f"Standard: {re.findall(r'password', 'PASSWORD')}")
print(f"Modifier: {re.findall(r'password', 'PASSWORD', re.IGNORECASE)}")

# 2. re.MULTILINE: ^ and $ match start/end of lines rather than just the whole string
print("\n--- MULTILINE ---")
multi_line_str = "Line1\nLine2"
print(f"Standard: {re.findall(r'^Line2', multi_line_str)}")
print(f"Modifier: {re.findall(r'^Line2', multi_line_str, re.MULTILINE)}")

# 3. re.DOTALL: The dot (.) character matches newlines (\n)
print("\n--- DOTALL ---")
print(f"Standard: {re.findall(r'Pass.*123', sample_text)}")
print(f"Modifier: {re.findall(r'Pass.*123', sample_text, re.DOTALL)}")