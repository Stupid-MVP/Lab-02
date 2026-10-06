import secrets
import string

chars = string.ascii_letters + string.digits + string.punctuation
length = int(input("Довжина пароля: "))

password = ""
for _ in range(length):
    password += secrets.choice(chars)
print("Ваш пароль:", password)
print("Кількість символів:", len(password))
if length < 8:
    print("Увага: пароль коротший за 8 символів, він ненадійний!")
