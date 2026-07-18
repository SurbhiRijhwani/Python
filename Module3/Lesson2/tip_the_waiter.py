def total_calc(bill_amount,tip_perc):
    total = bill_amount + (bill_amount * tip_perc / 100)
    total = round(total, 2)
    print(f"The total amount to pay is: {total} rs.")
total_calc(100, 1.5)