def get_inputs():

# Location selection
	bonus_rate = 0
	location_name = ''

	location_choice = int(input('Which city do you work in? (1-Seattle, 2-Lynnwood, 3-Bellevue): '))

	if location_choice == 1:
		location_name = 'Seattle'
		bonus_rate = 10
	elif location_choice == 2:
		location_name = 'Lynnwood'
		bonus_rate = 5
	elif location_choice == 3:
		location_name = 'Bellevue'
		bonus_rate = 15
	else:
		location_name = 'N/A'
		bonus_rate = 0

	# 📦 Work stats
	while True:
		try:
			orders = int(input('How many orders?: '))
			if orders < 0:
				print("❌ Orders can't be negative. Try again.")
				continue
			break
		except ValueError:
			print("❌ Enter a whole number.")
		
	while True:
		try:
			price_per_order = float(input('Average price per order?: '))
			if price_per_order < 0:
				print("❌Price can't be negative. Try again")
				continue
			break
		except ValueError:
			print("❌ Enter a whole number.")

	while True:		
			try:
				hours_worked = float(input('How many hours did you work?: '))
				if hours_worked < 0:
					print("❌Hours can't be negative. Try again")
					continue
				break
			except ValueError:
				print("❌ Enter a whole number.")
	
	# Tax selection
	while True:
		try:
			tax_rate = float(input('What is your tax percentage? (1–50): '))
			if tax_rate <= 0 or tax_rate > 50:
				print("❌ Wrong! Enter number from 1 to 50.")
				continue
			break
			
		except ValueError:
			print("❌ Wrong! Enter valid number, for example: 10, 15 or 20.")
			
	return {"location_name":location_name,
            "bonus_rate": bonus_rate,
            "orders": orders,
            "price_per_order": price_per_order,
            "hours_worked": hours_worked,
            "tax_rate": tax_rate
            }

def calculate_earnings(data):
	orders = data["orders"]
	price_per_order = data["price_per_order"]
	bonus_rate = data["bonus_rate"]
	hours_worked = data["hours_worked"]
	tax_rate = data["tax_rate"]

	base_earnings = orders * price_per_order
	bonus_amount = base_earnings * (bonus_rate / 100)
	total_before_tax = base_earnings + bonus_amount
	tax_value = total_before_tax * (tax_rate / 100)
	net_earnings = total_before_tax - tax_value
	earnings_per_hour = net_earnings / hours_worked
	return {
		"base_earnings": base_earnings,
		"bonus_amount": bonus_amount,
		"total_before_tax": total_before_tax,
		"tax_value": tax_value,
		"net_earnings": net_earnings,
		"earnings_per_hour": earnings_per_hour
		}
#data = get_inputs()
#result = calculate_earnings(data)


def print_report(data, result):
	print('\n========== DAILY REPORT ==========')
	print(f"Location: {data['location_name']} (+{data['bonus_rate']}%)")
	print(f"Total before tax: ${result['total_before_tax']:.2f}")
	print(f"Tax ({data['tax_rate']}%): -${result['tax_value']:.2f}")
	print(f"Net earnings: ${result['net_earnings']:.2f}")
	print(f"Earnings per hour: ${result['earnings_per_hour']:.2f}")
	
def main():
	data = get_inputs()
	result = calculate_earnings(data)
	print_report(data, result)

if __name__ == "__main__":
	main()