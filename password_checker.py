import getpass
import string

print("================================")
print("     PASSWORD STRENGTH CHECKER")
print("================================")

password = getpass.getpass("Enter a test password: ")

score = 0

if len(password) >= 15:
    score += 2
elif len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1
import getpass
import string
common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin123",
    "letmein",
    "welcome123"
]

if any(char.isdigit() for char in password):
    score += 1

if any(char in string.punctuation for char in password):
    score += 1

print("\n--- PASSWORD ANALYSIS ---")
print("Password length:", len(password))

if password.lower() in common_passwords:
    strength = "WEAK"
elif "1234" in password or "abcd" in password.lower():
    strength = "WEAK"
elif score <= 2:
    strength = "WEAK"
elif score <= 4:
    strength = "MODERATE"
else:
    strength = "STRONG"

print("Password Strength:", strength)

# Calculate the password security score
security_score = round((score / 6) * 100)

# Common passwords and predictable patterns receive low scores
if password.lower() in common_passwords:
    security_score = min(security_score, 20)
elif "1234" in password or "abcd" in password.lower():
    security_score = min(security_score, 30)

print("Password Security Score:", security_score, "/100")


if len(password) < 15:
    print("Recommendation: Use at least 15 characters.")
print("\n--- COMMON PASSWORD CHECK ---")

if password.lower() in common_passwords:
    print("WARNING: This is a commonly used password!")
    print("Recommendation: Choose a unique password.")

elif "1234" in password or "abcd" in password.lower():
    print("WARNING: Predictable password pattern detected!")
    print("Recommendation: Avoid common sequences.")

else:
    print("No common password patterns detected.")

print("Security checks completed.")
