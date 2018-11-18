# Date Time Calculation
import datetime
import calendar

BALANCE = 100000
INTEREST_RATE = 0.12
MONTHLY_PAYMENT = 5000

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month - today.day
start_date = today + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date

while BALANCE > 0:
    interest_charge = (INTEREST_RATE / 12) * BALANCE
    BALANCE += interest_charge
    BALANCE -= MONTHLY_PAYMENT
        
    BALANCE = 0 if BALANCE < 0 else round(BALANCE, 2)
    
    print(end_date, BALANCE)
    
    days_in_current_month = calendar.monthrange(today.year, today.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
    