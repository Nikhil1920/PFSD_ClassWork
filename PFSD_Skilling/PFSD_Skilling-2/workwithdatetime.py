from datetime import datetime, timedelta
current_datetime = datetime.now()

# future_date
future_date = current_datetime + timedelta(days=365)
print("Next year from today:", future_date)

# past_date
past_date = current_datetime - timedelta(days=365)
print("Last year from today:", past_date)

# present_date
today_date = current_datetime.date()
print("Today date:", today_date)

# tomorrow_date
tomorrow_date = today_date + timedelta(days=1)
print("Tomorrow date:", tomorrow_date)
