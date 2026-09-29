import re

password = input("Enter your password: ")

score = 0

print("\nChecking password...")

if len(password) >= 8:
    score += 1
else:
    print("❌ Use at least 8 characters")

if re.search(r"[A-Z]", password):
    score += 1
else:
    print("❌ Add an uppercase letter")

if re.search(r"[a-z]", password):
    score += 1
else:
    print("❌ Add a lowercase letter")

if re.search(r"[0-9]", password):
    score += 1
else:
    print("❌ Add a number")

if re.search(r"[^A-Za-z0-9]", password):
    score += 1
else:
    print("❌ Add a special character")

print("\n--------------------------")
print("Password Score:", score, "/ 5")

if score <= 2:
    print("Strength: WEAK ❌")
elif score <= 4:
    print("Strength: MEDIUM ⚠️")
else:
    print("Strength: STRONG ✅")

print("--------------------------")