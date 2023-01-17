def calculate_net(gross, vat):
    return round(gross / (1 + vat/100), 2)

print("Wartość netto ze 100 zł brutto to", calculate_net(100, 23), "zł")
