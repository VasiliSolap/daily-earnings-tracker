# 📍 Location selection
def get_inputs():
    # 📍 Location selection
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
			
    while True:
    	try:
    		tax_rate = float(input('What is your tax percentage? (1–50): '))
    		if tax_rate <= 0 or tax_rate > 50:
    			print("❌ Wrong! Enter number from 1 to 50.")
    			continue
    		break
    	except ValueError:
    		print("❌ Wrong! Enter valid number, for example: 10, 15 or 20.")
		
    return {
        "location_name": location_name,
        "bonus_rate": bonus_rate,
        "orders": orders,
        "price_per_order": price_per_order,
        "hours_worked": hours_worked,
        "tax_rate": tax_rate}
	
data = get_inputs()
print(data)
# 💵 Base earnings
base_earnings = orders * price_per_order

# 🌆 Location bonus
bonus_multiplier = bonus_rate / 100
bonus_amount = base_earnings * bonus_multiplier
earnings_after_bonus = base_earnings + bonus_amount

# 💸 Tax selection


# 📊 Calculations
tax_value = earnings_after_bonus * (tax_rate / 100)
net_earnings = earnings_after_bonus - tax_value
earnings_per_hour = net_earnings / hours_worked

# ✅ Final report
print(f"\n📍 Location: {location_name} (+{bonus_rate}%)")
print(f"💵 Total earnings before tax: ${earnings_after_bonus:.2f}")
print(f"💸 Tax ({tax_rate}%): -${tax_value:.2f}")
print(f"💰 Net earnings: ${net_earnings:.2f}")
print(f"⏱ Earnings per hour: ${earnings_per_hour:.2f}")

from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")

with open("daily_report.txt", "a") as file:
		file.write('\n')
		file.write(f'==={today}===\n')
		file.write(f"Location: {location_name} (+{bonus_rate}%)\n")
		file.write(f"Total before tax: ${earnings_after_bonus:.2f}\n")
		file.write(f"Tax ({tax_rate}%): -${tax_value:.2f}\n")
		file.write(f"Net earnings: ${net_earnings:.2f}\n")
		file.write(f"Earnings per hour: ${earnings_per_hour:.2f}\n")
		
with open("daily_report.txt", "r") as file:
	lines = file.readlines()
	

if len(lines)<48: 
	recent_lines=lines
else:
	recent_lines=lines[-48:]

totals=[]

for line in lines:
 	if "Net earnings:" in line:
 		value = float(line.split("$")[1])
 		totals.append(value)
 		
if totals:
 	weekly_totals = sum(totals)
 	print(f"💵Weekly total ernings: ${weekly_totals:.2f}")
else:
 	print("❌No earnings found in file")


 	
 	
#numbered = [f'{i}:{line.strip()}' for i, line in enumerate(recent_lines, start=1)]
#print("\n".join(numbered))




