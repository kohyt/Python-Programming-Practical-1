#  q7_generate_payroll.py

# get input
name = input("Enter name:")
hours = int(input("Enter number of hours worked weekly:"))
pay_rate = float(input("Enter hourly pay rate:"))
cpf = int(input("Enter CPF contribution rate(%):"))
gross_pay = hours * pay_rate
cpf_cont = cpf / 100 * gross_pay
net_pay = gross_pay - cpf_cont 

# output result
print("Payroll statement for {0}".format(name))
print("Number of hours worked in week: {0}".format(hours))
print("Hourly pay rate: ${0:.2f}".format(pay_rate))
print("Gross pay = ${0:.2f}".format(gross_pay))
print("CPF contribution at {0}% = ${1:.2f}".format(cpf,cpf_cont))
print("Net pay = ${0:.2f}".format(net_pay))

