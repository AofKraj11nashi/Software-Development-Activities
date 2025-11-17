
#__________________________________
#CityBikeGo Data Analytic Script
# Uses: Sets, Tuples, Dictionaries


#1. RAW BOOKING DATA

raw_bookings_month1 = [
    ("C001", "Leeds Central", "Weekday", 2),
    ("C002", "Hyde Park", "Weekend", 1),
    ("C003", "University", "Weekday", 3),
    ("C001", "Hyde Park", "Weekend", 1),
    ("C004", "Leeds Central", "Weekday", 2),
]

raw_bookings_month2 = [
    ("C002", "Hyde Park", "Weekday", 2),
    ("C003", "Leeds Central", "Weekend", 4),
    ("C005", "University", "Weekday", 1),
    ("C006", "Leeds Central", "Weekend", 2),
    ("C001", "University", "Weekend", 3),
]
#2. UNIQUE Customers

customers_month1 = {booking[0] for booking in raw_bookings_month1}
customers_month2 = {booking[0] for booking in raw_bookings_month2}

print("\033[92mUnique customers in Month 1:\033[0m", customers_month1)
print("\033[93mUnique customers in Month 2:\033[0m", customers_month2)
print("\033[94mNumber of unique customers Month 1:\033[0m", len(customers_month1))
print("\033[95mUnique customers in Month 1:\033[0m", customers_month1)


regular_customers = customers_month1 & customers_month2
