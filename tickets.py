SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(number_of_tickets):
    ticket_cost = number_of_tickets * (TICKET_PRICE)
    ticket_cost += SERVICE_CHARGE
    return ticket_cost

while tickets_remaining >= 1:
    print("Holy shitballs! There are currently {} tickets left!".format(tickets_remaining))
    user_name = input("Sup dawg! What is your name? ")
    num_tickets = input("Chill! How many tickets do you want, {}? ".format(user_name))
    # expect a ValueError and handle it approps
    try:
        num_tickets = int(num_tickets)
        # Rause a value error if the request is for more tickets than are available
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining. Nice try!".format(tickets_remaining))
    except ValueError as err:
        # Include error text
        print("Fuck! That's not a number, you dolt!")
        print("({})".format(err))
    else:
        tickets_total = calculate_price(num_tickets)
        print("Alright! That shit is going to cost $", tickets_total, "dollars, yo!")
        purchase_tickets = input("Do you wanna see this shit or nah?! Y/N? ")
        if purchase_tickets.lower() == "y":
            print("Sold! You are about to see some shit!")
            tickets_remaining -= num_tickets
        else:
            print("Whatevers, thanks anyway {}".format(user_name))

print("SOOOORRRRYYY, this shit is SOLD OUT!")