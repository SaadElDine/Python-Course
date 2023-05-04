from menu import MENU

from menu import resources

profit = 0
def check_resources(water,coffee,milk,resources):
    waterr = resources["water"] - water
    coffeer = resources["coffee"] - coffee
    milkr = resources["milk"] - milk
    if waterr > 0 or waterr == 0:
        resources["water"] = waterr
    else:
        print("Sorry there is not enough water.")
        return False
    if coffeer > 0 or coffeer == 0:
        resources["coffee"] = coffeer
    else:
        print("Sorry there is not enough coffee.")
        return False
    if milkr < 0:
        print("Sorry there is not enough milk.")
        return False
    else:
        resources["milk"] = milkr
    return resources

def proccess_coins():
    print("Please insert coins.")
    cost = int(input("how many quarters?: ")) * 0.25
    cost += int(input("how many dimes?: ")) * 0.1
    cost += int(input("how many nickles?: ")) * 0.05
    cost += int(input("how many pennies?: ")) * 0.01
    return cost

def check_transaction(cost_inserted,cost):
    if cost_inserted < cost:
        print("Sorry that's not enough money. Money refunded.")
    elif cost_inserted == cost:
        profit = profit + cost
    else:
        change = round(cost_inserted - cost, 2)
        print(f"Here's  ${change} dollars in change. ")

esp = MENU["espresso"]
should_continue = True
esping = esp["ingredients"]
lat = MENU["latte"]
lating = lat["ingredients"]
cap = MENU["cappuccino"]
caping = cap["ingredients"]
while should_continue:
    answer = input("What would you like? (espresso/latte/cappuccino):")
    if answer == "off":
        should_continue = False
        exit
    elif answer == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources ["coffee"]
        money = profit
        print(f"Water : {water}ml")
        print(f"Milk : {milk}ml")
        print(f"Coffee : {coffee}g")
        print(f"Money: ${money}")
    elif answer == "espresso":
        co = esp["cost"]
        check_resources(esping["water"],esping["coffee"], 0, resources)
        print(f"Your order will cost {co}")
        total = proccess_coins()
        check_transaction(total, esp["cost"])
    elif answer == "latte":
        co = lat["cost"]
        check_resources(lating["water"], lating["coffee"], lating["milk"], resources)
        print(f"Your order will cost ${co}")
        total = proccess_coins()
        check_transaction(total , lat["cost"])
    elif answer == "cappuccino":
        co = cap["cost"]
        check_resources(caping["water"], caping["coffee"], caping["milk"], resources)
        print(f"Your order will cost ${co}")
        total = proccess_coins()
        check_transaction(total, cap["cost"])




