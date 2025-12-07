# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
#
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# Example calculation
ticker = 'MU'
price = 237.22
shares = 1122.466035
cash = 10000
debt = 14500
fcf = 9700
ebitda = 19000
revenue = 37000
mktCap = price * shares
netDebt = debt-cash
enterpriseValue = mktCap + netDebt
ev_fcf = enterpriseValue / fcf
ev_ebitda = enterpriseValue / ebitda
ev_revenue = enterpriseValue / revenue
ebitda_margin = ebitda / revenue
fcf_margin = fcf / revenue

tol = 100 # dollars in millions
g = 0.000
d = 0.100
dcf_valuation = 0
while abs(enterpriseValue - dcf_valuation) > tol:
    g += 0.0001
    revs = [revenue*(1+g)**n for n in range(0, 6)]
    fcfs = [rev*fcf_margin for rev in revs]
    pvs = []
    for i, fcf in enumerate(fcfs):
        pv = fcf / ((1 + d)**i)
        pvs.append(pv)
    terminalValue = fcfs[5] * (1 + g) / (d - g)
    pv_tv = terminalValue / ((1 + d) ** 5)
    dcf_valuation = sum(pvs) + pv_tv
    print(enterpriseValue - dcf_valuation < tol)

print(f"DCF: {dcf_valuation}")
print(f"EV: {enterpriseValue}")
print(f"Market valuation assumes a {g} terminal growth rate, with tolerance of {tol}")

# print("Revenue:")
# for i, rev in enumerate(revs):
#     print(i, round(rev, 0))
# print("FCF:")
# for i, fcf in enumerate(fcfs):
#     print(i, round(fcf, 0))
# print("PV of FCF:")
# for i, pv in enumerate(pvs):
#     print(i, round(pv, 0))
# print(f"sum of pvs = {sum(pvs)}")
# # how much revenue growth to justify valuation?
#
# print("terminal value:")
# g = 0.05
# terminalValue = fcfs[5] * (1 + g) / (d - g)
# pv_tv = terminalValue / ((1 + d) ** 5)
#
# dcf_valuation = sum(pvs) + pv_tv
# print(f"dcf valuation: {dcf_valuation}")

    



# Check
# print(enterpriseValue == price*shares+debt-cash)

# print(
#     ticker, 
#     round(price, 2), 
#     round(shares, 1), 
#     int(mktCap),
#     int(enterpriseValue),
#     round(ev_fcf, 1),
#     round(ev_ebitda, 1)
# )
