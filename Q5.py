""" that calculates the current balance of a savings bank account in the end of M months
period. The calculation must reflect the following assumptions:
 In the beginning of the initial month, the balance is init_sum
 Every month, the monthly interest is calculated as int_rate percent of the balance s
 available in the beginning of this month
 Every month, the monthly tax is calculated as tax_rate percent of s - tfl, if
the balance s in the beginning of this month is greater than tfl (tax-free limit).
Otherwise, the monthly tax is 0.
 In the end of each month, the balance is updated by adding the monthly interest
and subtracting the monthly tax. """

def balance(init_sum, int_rate, tfl, tax_rate, M):
    s = init_sum
    interest = s*int_rate/100
    if s > tfl:
        monthly_tax = (s - tfl)*tax_rate/100
    else:
        monthly_tax = 0
    for i in range(M):
        s = s + interest - monthly_tax
    return s



print(balance(10000, 1, 20000, 1, 2))
print("must be approximately 10201")
print(balance(25000, 2, 20000, 1, 2))
print("must be approximately 25904.5")
print(balance(19800, 2, 20000, 1, 2))
print("must be approximately 20597.96")