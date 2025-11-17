
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
new_customers = customers_month2 - customers_month1             # difference
inactive_customers = customers_month1 - customers_month2        # difference
all_customers = customers_month1 | customers_month2             # union

print("\nRegular customers:", regular_customers)
print("New customers:", new_customers)
print("Inactive customers:", inactive_customers)
print("All customers served:", all_customers)

station_counts = {}

for booking in raw_bookings_month1:
    station = booking[1]
    station_counts[station] = station_counts.get(station, 0) + 1

print("\nStation activity (Month 1):", station_counts)


busiest_station = max(station_counts.items(), key=lambda x: x[1])
print("Busiest station:", busiest_station)



customer_hours = {}

for booking in raw_bookings_month1:
    cust, station, day, hours = booking
    customer_hours[cust] = customer_hours.get(cust, 0) + hours

print("\nTotal hours per customer (Month 1):", customer_hours)

# --------------------------
# 6. Required Dictionary Methods Examples
# --------------------------

example_dict = {}
example_dict.setdefault("C001", 0)
example_dict.update({"C002": 5})
copy_of_dict = example_dict.copy()
keys_list = list(example_dict.keys())
values_list = list(example_dict.values())

items_list = list(example_dict.items())


removed = example_dict.pop("C002")
last_removed = example_dict.popitem()

# fromkeys example (creating a clean dictionary template)
zero_hours = dict.fromkeys(all_customers, 0)

print("\nDictionary method examples:")
print("setdefault:", example_dict)
print("copy:", copy_of_dict)
print("keys:", keys_list)
print("values:", values_list)
print("items:", items_list)
print("fromkeys template:", zero_hours)


# --------------------------
# SUMMARY REPORT
# --------------------------

print("\n----- Monthly Summary Report -----")
print(f"Total unique customers: {len(customers_month1)}")
print(f"Regular customers (both months): {regular_customers}")
print(f"New customers: {new_customers}")
print(f"Inactive customers: {inactive_customers}")
print(f"Busiest station in Month 1: {busiest_station[0]} with {busiest_station[1]} bookings")
print("Total cycling hours per customer:", customer_hours)



