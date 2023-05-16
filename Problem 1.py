arr = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
# Group the jobs by the values of their deadline
sameDeadline = {}
for job in arr:
    key = job[1]
    if key not in sameDeadline:
        sameDeadline[key] = [job]
    else:
        sameDeadline[key].append(job)
# Find the maximum profit value in each deadline for each group
max_profits = {}
for key, profitValue in sameDeadline.items():
    max_profit_of_each_deadline = max(job[2] for job in profitValue)
    max_profits[key] = max_profit_of_each_deadline
# Print the maximum value for each group
for key, max_profit in max_profits.items():
    print(f"job id that has been done {key}: profit value = {max_profit}")
print("Maximum profit:",sum(max_profits.values()))
print("Number of jobs done:",len(max_profits) )

