# Lab-02: Python-утиліти

Лабораторна робота №2: налаштування середовища розробки та Git workflow.
Проєкт складається з незалежних консольних утиліт на Python. Кожну
розробляє окремий учасник команди в окремій гілці, а зміни потрапляють
у main через Pull Request із code review.

## Команда

| Учасник | Роль | Модуль |
|---------|------|--------|
| Шульга Андрій Сергійович (@shulgaaa294-stack) | Team lead | calculator |
| Грицюк Назар Олександрович (@SkyDreammer-exe) | Developer | converter |
| Смоляр Орест Миколайович (@Mphiza) | QA | password_generator |

## Структура репозиторію

Lab-02/
├── calculator/
│   └── calculator.py
├── converter/
│   └── converter.py
├── password_generator/
│   └── password_generator.py   (у розробці)
├── .gitignore
└── README.md

## Модулі

### Калькулятор (calculator/calculator.py)

Запитує два цілих числа та знак операції. Підтримує додавання 
і віднімання, виводить результат у термінал.

### Конвертер (converter/converter.py)

Конвертація одиниць виміру в консолі.

### Генератор паролів (password_generator/password_generator.py)

Генерація випадкових паролів. Модуль у розробці.

## Технологічний стек

Python 3, Git, GitHub, GitHub Desktop, VS Code.

## Встановлення та запуск

1. Встановіть Python 3 з [python.org](https://www.python.org/downloads/).
   У Windows під час встановлення позначте *Add python.exe to PATH*.
   Перевірка: python --version.
2. Склонуйте репозиторій і перейдіть у його папку:
   git clone git@github.com:Stupid-MVP/Lab-02.git
   cd Lab-02
3. Запустіть потрібну утиліту:
   python calculator/calculator.py
   python converter/converter.py
   Якщо команда python не працює, спробуйте python3 або py.
4. Вводьте дані за підказками в терміналі й натискайте Enter.

## Правила роботи з Git

- у main напряму не комітимо, лише через Pull Request;
- кожна задача має окрему гілку: feature/назва для коду, docs/назва
  для документації;
- повідомлення комітів пишемо за Conventional Commits, наприклад
  feat: add converter module;
- кожен Pull Request перевіряє хоча б один учасник команди,
  злиття відбувається після схвалення.

## Статус

Статус: модулі готові до тестування.
Проєкт розробляємо!!
