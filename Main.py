import MachineData


def coin_processing():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    total = float(format(total, '.2f'))
    return total


def is_enough_money(x):
    if UserInputtedMoney > MachineData.MENU[x]['cost']:
        print(f"Here is ${UserInputtedMoney - MachineData.MENU[x]['cost']} your change ")
        print(f"Here is your {x} ☕ Enjoy! ")
        return 0
    else:
        print("Sorry there is not enough Money. Money refunded. ")


def resource_calculations(x):
    if MachineData.resources['water'] > MachineData.MENU[x]['ingredients']['water'] and MachineData.resources['milk'] > MachineData.MENU[x]['ingredients']['milk'] and MachineData.resources['coffee'] > MachineData.MENU[x]['ingredients']['coffee']:
        MachineData.resources['water'] = MachineData.resources['water'] - MachineData.MENU[x]['ingredients']['water']
        MachineData.resources['milk'] = MachineData.resources['milk'] - MachineData.MENU[x]['ingredients']['milk']
        MachineData.resources['coffee'] = MachineData.resources['coffee'] - MachineData.MENU[x]['ingredients']['coffee']
        return 0
    else:
        return 1


def print_report():
    for i in MachineData.resources:
        print(f"{i} : {MachineData.resources[i]}")
    print(f"money : {sum(MoneyHistory)}")


MoneyHistory = [0]
count = 0
condition = True
while condition:

    Order = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    UserInputtedMoney = 0
    accumulatedMoney = 0

    if Order == 'espresso':
        if resource_calculations('espresso') == 0:
            UserInputtedMoney = coin_processing()
            if is_enough_money('espresso') == 0:
                count += 1
                accumulatedMoney = MachineData.MENU[Order]['cost']
        else:
            print('Sorry there is not enough ingredients.😢😢 ')

    elif Order == 'latte':
        if resource_calculations('latte') == 0:
            UserInputtedMoney = coin_processing()
            if is_enough_money('latte') == 0:
                count += 1
                accumulatedMoney = MachineData.MENU[Order]['cost']
        else:
            print('Sorry there is not enough ingredients.😢😢 ')

    elif Order == 'cappuccino':
        if resource_calculations('cappuccino') == 0:
            UserInputtedMoney = coin_processing()
            if is_enough_money('cappuccino') == 0:
                count += 1
                accumulatedMoney = MachineData.MENU[Order]['cost']
        else:
            print('Sorry there is not enough ingredients.😢😢 ')

    elif Order == 'report':
        print_report()

    elif Order == 'off':
        print("Thanks for using me ❤️. Please come again")
        condition = False
    MoneyHistory.append(accumulatedMoney)
