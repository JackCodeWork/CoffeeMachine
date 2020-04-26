water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def print_state():
    print(f'The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{coffee_beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'${money} of money')


def is_enough(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, not enough water!\n')

    if milk < need_milk:
        print('Sorry, not enough milk!\n')

    if coffee_beans < need_beans:
        print('Sorry, not enough beans!\n')

    if cups < 1:
        print('Sorry, not enough cups\n')

    if water > need_water and milk > need_milk and coffee_beans > need_beans and cups > 1:
        print('I have enough resources, making you a coffee!\n')


def buy():
    global water, milk, coffee_beans, money, cups

    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu::\n")
    if coffee_type == "back":
        pass
    elif int(coffee_type) == 1:
        is_enough(need_water=250, need_beans=16)
        if water >= 250 and coffee_beans >= 16:
            water -= 250
            coffee_beans -= 16
            money += 4
            cups -= 1
        else:
            pass
    elif int(coffee_type) == 2:
        is_enough(need_water=350, need_milk=75, need_beans=20)
        if water >= 350 and milk >= 75 and coffee_beans >= 20:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
            cups -= 1
        else:
            pass
    elif int(coffee_type) == 3:
        is_enough(need_water=200, need_milk=100, need_beans=12)
        if water >= 200 and milk >= 100 and coffee_beans >= 12:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6
            cups -= 1
        else:
            pass
    else:
        print("invalid command")


def fill():
    global water, milk, coffee_beans, money, cups

    water += int(input('Write how many ml of water do you want to add:\n'))
    milk += int(input('Write how many ml of milk do you want to add:\n'))
    coffee_beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
    cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))


def take():
    global money
    money = 0
    print(f'I gave you ${money}')


def main():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            print_state()
        elif action == "exit":
            break
        else:
            print("invalid command")


if __name__ == '__main__':
    main()
