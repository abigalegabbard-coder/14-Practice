prices = [25.00, 50.00, 75.00, 100.00, 150.00]

def discount(percent):
    return f"{(percent*0.80):.2f}"

disounted_prices = list(map(discount, prices))
print(disounted_prices)