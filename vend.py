# Vendor Purchase Report

vendor_name = input("Enter vendor name: ")
year = int(input("Enter year of association: "))
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

annual_total = 0

print("\nEnter monthly purchase amounts:")
for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    annual_total += amount

print("\n--- Vendor Annual Report ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)
print("Total Annual Purchase:", annual_total)