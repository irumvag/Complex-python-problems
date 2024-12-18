"""
(7% Investment Return) Some investment advisors say that it's reasonable to expect a 7% return over 
the long term in the stock market. Assuming that you begin with $1000 and leave your money invested,
calculate and display how much money you'll have after 10, 20 and 30 years. Use the following formula
for determining these amounts: a = p(1 + r)"
where
p is the original amount invested (i.e., the principal of $1000),
r is the annual rate of return (7%),
n is the number of years (10, 20 or 30) and
a is the amount on deposit at the end of the nth year.
"""
p=1000
r=7/100
n=[10,20,30]
a=[p*((1+r)**k) for k in n]
print("The original amount invested (i.e., the principal of $1000).")
k=0
for i in a:
    print(f"The 7% investment return after {n[k]} years is the following {i:.2f}$.")
    k+=1