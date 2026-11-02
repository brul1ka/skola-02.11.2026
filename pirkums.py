balance = int(input("Kads ir tavs budžets? (raksti tikai cipari): "))
phone_price = int(input("Kada cena ir pie telefona? (raksti tikai cipari): "))

if balance >= phone_price:
    print("Viedtālruni var nopirkt uzreiz")
elif balance < phone_price:
    print(f"Nepietiek vēl {phone_price - balance} EUR")
else:
    print("notika kļuda")