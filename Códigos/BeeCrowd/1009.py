seller_name = input()
fixed_salary = float(input())
total_sales = float(input())

bonus = 0.15 * total_sales

final_salary = fixed_salary + bonus

print("TOTAL = R$ {:.2f}".format(final_salary))
