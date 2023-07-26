# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

cash = 0
count = 1
multiple = 50
min_comm = 30 # До 2000 у.е включительно
max_comm = 600 # C 40000 до 5000000 включительно
oper = True
TAX = 5000000 # Налог на богатство
MINLIMIT = 2000 # Минимальный диапазон для ставки 1.5%
MAXLIMIT = 40000 # Максимальный диапазон для ставки 1.5%

while oper:
    action = input('Введите действие: "Пополнить", "Снять" "Выйти" ')
    if action == 'Выйти':
        print('Операция завершена, заберите карту')

    elif action == 'Пополнить':
        summ = int(input('Введите сумму пополнения кратную 50 у.е: '))
        if summ % multiple != 0:
            print('Некорректная сумма для пополнения, попробуйте ввести другую ссумму')

        elif count <= 3 and summ <= TAX:
            cash += summ
            count += 1

        elif count <= 3 and summ > TAX:
            cash += summ - summ / 100 * 10
            count += 1
    
        elif count > 3 and summ <= TAX:
            cash += summ - summ / 100 * 3
            count += 1

        elif count > 3 and summ > TAX:
            cash += summ - summ / 100 * 13
            count += 1

    elif action == 'Снять':
        summ = int(input('Введите сумму снятия кратную 50 у.е: '))

        if summ % multiple != 0:
            print('Некорректная сумма для снятия, попробуйте ввести другую ссумму')

        elif count <= 3:

            if summ <= MINLIMIT and summ + min_comm <= cash: 
                cash = cash - (summ + min_comm)
                count += 1
                print(f'Сумма снятия: {summ} комиссия: {min_comm} баланс: {cash}')

            elif summ >= MINLIMIT and summ <= MAXLIMIT and summ + summ / 100 * 1.5 <= cash:
                cash = cash - (summ + summ / 100 * 1.5)
                count += 1
                print(f'Сумма снятия: {summ} комиссия: {summ / 100 * 1.5} баланс: {cash}')

            elif summ > MAXLIMIT and summ <= TAX and summ + max_comm <= cash:
                cash = cash - (summ + max_comm)
                count += 1
                print(f'Сумма снятия: {summ} комиссия: {max_comm} баланс: {cash}')

            elif summ > TAX and summ + summ / 100 * 11.5 <= cash:
                cash = cash - (summ + summ / 100 * 11.5)
                count += 1
                print(f'Сумма снятия: {summ} комиссия: {summ / 100 * 11.5} баланс: {cash}')

            else:
                print(f'Сумма: {summ} превышает остаток: {cash} с учетом комиссии')

        elif count > 3:

            if summ <= MINLIMIT and summ + (min_comm + summ / 100 * 3) <= cash: 
                cash = cash - (summ + (min_comm + summ / 100 * 3))
                count += 1
                print(f'Сумма снятия: {summ} комиссия: {min_comm + summ / 100 * 3} баланс: {cash}')

            elif summ >= MINLIMIT and summ <= MAXLIMIT and summ + summ / 100 * 4.5 <= cash:
                cash = cash - (summ + summ / 100 * 4.5)
                count += 1
                print(f'Сумма снятия: {summ} комиссия: {summ / 100 * 4.5} баланс: {cash}')

            elif summ > MAXLIMIT and summ <= TAX and summ + (max_comm + summ / 100 * 3) <= cash:
                cash = cash - (summ + (max_comm + summ / 100 * 3))
                count += 1
                print(f'Сумма снятия: {summ} комиссия: {max_comm  + summ / 100 * 3} баланс: {cash}')

            elif summ > TAX and summ + summ / 100 * 14.5 <= cash:
                cash = cash - (summ + summ / 100 * 14.5)
                count += 1
                print(f'Сумма снятия: {summ} комиссия: {summ / 100 * 14.5} баланс: {cash}')
            else:
                print(f'Сумма: {summ} превышает остаток: {cash} с учетом комиссии')
    else:
        oper = False
    print(f'Баланс: {cash}')