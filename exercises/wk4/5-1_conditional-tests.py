# Firm class that we'll use to facilitate creation of new stock objects. 
class Firm:
    def __init__(self, ticker, price, shares, cash, debt, fcf, ebitda, revenue):
        self.ticker = ticker
        self.price = price
        self.shares = shares
        self.cash = cash
        self.debt = debt
        self.fcf = fcf
        self.ebitda = ebitda
        self.revenue = revenue

    @property
    def mkt_cap(self):
        return self.price * self.shares

    @property
    def net_debt(self):
        return self.debt - self.cash

    @property
    def enterprise_value(self):
        return self.mkt_cap + self.net_debt

    @property
    def ev_fcf(self):
        return self.enterprise_value / self.fcf

    @property
    def ev_ebitda(self):
        return self.enterprise_value / self.ebitda

    @property
    def ev_revenue(self):
        return self.enterprise_value / self.revenue

    @property
    def ebitda_margin(self):
        return self.ebitda / self.revenue

    @property
    def fcf_margin(self):
        return self.fcf / self.revenue

# Micron Technology
MU = Firm(
    ticker = 'MU',
    price = 237.22,
    shares = 1122.466035,
    cash = 10000,
    debt = 14500,
    fcf = 9700,
    ebitda = 19000,
    revenue = 37000
)

# ClearWater
#17.865,
CLW = Firm(
    ticker = 'CLW',
    price = 17.865,
    shares = 16.038,
    cash = 34.4,
    debt = 336,
    fcf = 0.1,
    ebitda = 0,
    revenue = 1384,
)
firms = [MU, CLW]

for firm in firms:
    input_firm = firm
    
    tol = 100 # dollars in millions
    g = -0.5
    d = 0.100
    dcf_value = 0
    while abs(input_firm.enterprise_value - dcf_value) > tol:
        g += 0.0001
        revs = [input_firm.revenue*(1+g)**n for n in range(0, 6)]
        fcfs = [rev*input_firm.fcf_margin for rev in revs]
        pvs = []
        for i, fcf in enumerate(fcfs):
            pv = fcf / ((1 + d)**i)
            pvs.append(pv)
        terminal_value = fcfs[5] * (1 + g) / (d - g)
        pv_tv = terminal_value / ((1 + d) ** 5)
        dcf_value = sum(pvs) + pv_tv
        print(input_firm.enterprise_value - dcf_value < tol)
    
    stocks = []
    stocks.append((input_firm.ticker, input_firm.price, input_firm.enterprise_value, g))
    print(f"Ticker\t Price\t\t EV ($M)\t g*")
    print(f"{input_firm.ticker}\t ${input_firm.price:,.2f}\t ${input_firm.enterprise_value:,.0f}\t {g:.0%}")
    print(f"DCF: {dcf_value}")
    print(f"EV: {input_firm.enterprise_value}")
    print(f"Market valuation assumes a {g} terminal growth rate, with tolerance of {tol}")

print(stocks)
