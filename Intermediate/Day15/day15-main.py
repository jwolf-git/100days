import day15_menu


def make_coffee():
    coffee_choice = input("What would you like? (espresso / latte / cappuccino): ").lower()
    if coffee_choice == 'off':
        print("Shutting down for maintenance..goodbye")
        quit()
    elif coffee_choice == 'report':
        print(f"Water: {day15_menu.resources['water']}ml")
        print(f"Milk: {day15_menu.resources['milk']}ml")
        print(f"Coffee: {day15_menu.resources['coffee']}g")
        print(f"Money: ${day15_menu.resources['money']}")
        make_coffee()
    elif coffee_choice == 'latte':
        check_resources(water_cost=day15_menu.MENU['latte']['ingredients']['water'],
                        coffee_cost=day15_menu.MENU['latte']['ingredients']['coffee'],
                        milk_cost=day15_menu.MENU['latte']['ingredients']['milk'])
        change = collect_money(day15_menu.MENU["latte"]["cost"], 'latte')
        consume_resources('latte')
        print(f"Here is ${change} in change.")
        print("Here is your latte. Enjoy!")
    elif coffee_choice == 'cappuccino':
        check_resources(water_cost=day15_menu.MENU['cappuccino']['ingredients']['water'],
                        coffee_cost=day15_menu.MENU['cappuccino']['ingredients']['coffee'],
                        milk_cost=day15_menu.MENU['cappuccino']['ingredients']['milk'])
        change = collect_money(day15_menu.MENU["cappuccino"]["cost"], 'cappuccino')
        consume_resources('cappuccino')
        print(f"Here is ${change} in change.")
        print("Here is your cappuccino. Enjoy!")
    elif coffee_choice == 'espresso':
        check_resources(water_cost=day15_menu.MENU['espresso']['ingredients']['water'],
                        coffee_cost=day15_menu.MENU['espresso']['ingredients']['coffee'],
                        milk_cost=day15_menu.MENU['espresso']['ingredients']['milk'])
        change = collect_money(day15_menu.MENU["espresso"]["cost"], 'espresso')
        print(f"Here is ${change} in change.")
        consume_resources('espresso')
        print("Here is your espresso. Enjoy!")
    else:
        print("Sorry, that's not a valid choice. Try again!")
    make_coffee()


def consume_resources(coffee_type):
    if day15_menu.resources['water'] < day15_menu.MENU[coffee_type]['ingredients']['water'] or day15_menu.resources['water'] < day15_menu.MENU[coffee_type]['ingredients']['milk'] or day15_menu.resources['water'] < day15_menu.MENU[coffee_type]['ingredients']['coffee']:
        print('Sorry, not enough resources, try again!')
        make_coffee()
    else:
        day15_menu.resources['water'] = day15_menu.resources['water'] - day15_menu.MENU[coffee_type]['ingredients']['water']
        day15_menu.resources['coffee'] = day15_menu.resources['coffee'] - day15_menu.MENU[coffee_type]['ingredients']['coffee']


def check_resources(water_cost, coffee_cost, milk_cost):
    if water_cost > day15_menu.resources['water']:
        print("Sorry, there is not enough water! Please make another selection or turn off for maintenance.")
        make_coffee()
    elif coffee_cost > day15_menu.resources['coffee']:
        print("Sorry, there is not enough coffee! Please make another selection or turn off for maintenance.")
        make_coffee()
    elif milk_cost > day15_menu.resources['milk']:
        print("Sorry, there is not enough milk! Please make another selection or turn off for maintenance.")
        make_coffee()


def collect_money(price, coffee_type):
    quarters = (int(input("How many quarters? "))) * .25
    dimes = (int(input("How many dimes? "))) * .1
    nickles = (int(input("How many nickles? "))) * .05
    pennies = (int(input("How many pennies? "))) * .01
    total = quarters + dimes + nickles + pennies
    if total < price:
        print("Sorry that's not enough money. Money refunded!")
        make_coffee()
    day15_menu.resources['money'] = day15_menu.resources['money'] + day15_menu.MENU[coffee_type]['cost']
    return round(total - price, 2)


make_coffee()
