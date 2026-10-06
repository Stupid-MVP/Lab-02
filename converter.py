import secrets
import string

chars = string.ascii_letters + string.digits + string.punctuation
length = int(input("Довжина пароля: "))

password = ""
for _ in range(length):
    password += secrets.choice(chars)
print("Ваш пароль:", password)
