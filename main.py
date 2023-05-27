import random
import datetime
from fpdf import FPDF

# Set up the PDF object
pdf = FPDF()
pdf.add_page()

# Set up the font and font size
pdf.set_font("Arial", size=12)

# # Generate a random merchant number between 100 and 999
# merchant_num = str(random.randint(100, 999))

# Generate a random building number between 100 and 999
building_num = str(random.randint(100, 999))

# Generate a random street name
streets = ['Oak', 'Maple', 'Elm', 'Cedar', 'Pine']
street_name = random.choice(streets) + ' Street'

# Generate a random town and postal code
towns = ['Anytown', 'Sometown', 'Othertown']
town = random.choice(towns)
postal_code = str(random.randint(10000, 99999))

# Create the merchant name and location string
merchants = ["A", "B", "C", "D"]
merchant_name = "Merchant " + str(random.choice(merchants))
location = "Location: " + building_num + " " + street_name + ", " + town + ", " + postal_code

# Add the merchant name and location
pdf.cell(0, 10, merchant_name + ", " + location, 0, 1)
pdf.cell(0, 10, "", ln=1)

# add Randomize date and time
current_year_str = str(datetime.datetime.now().year)
day = str(random.randint(1, 28)).zfill(2)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month = random.choice(months)
year = current_year_str

hour = str(random.randint(0, 23)).zfill(2)
minute = str(random.randint(0, 59)).zfill(2)
second = str(random.randint(0, 59)).zfill(2)
time = f"{hour}:{minute}:{second}"

pdf.cell(0, 10, f"Date: {day} {month} {year}", ln=1)
pdf.cell(0, 10, f"Time: {time}", ln=1)
pdf.cell(0, 10, "", ln=1)

# Add the Visa sales information
terminals = ['Visa', 'MasterCard', 'NETS']
terminal = random.choice(terminals)
pdf.cell(0, 10, terminal + " Sales:", ln=1)
num_transactions = random.randint(1, 10)
total_sales_amount = "{:.2f}".format(random.uniform(100, 1000))
total_fees = "{:.2f}".format(float(total_sales_amount) * 0.025)
pdf.cell(0, 10, f"Number of Transactions:        {num_transactions}", 0, 1)
pdf.cell(0, 10, f"Total Sales Amount:            ${total_sales_amount}", 0, 1)
pdf.cell(0, 10, f"Total Fees:                    ${total_fees}", 0, 1)
pdf.cell(0, 10, "", ln=1)

# Add the settlement amount, batch number, and terminal ID
settlement_amount = "{:.2f}".format(float(total_sales_amount) - float(total_fees))
batch_number = str(random.randint(100000, 999999))
terminal_id = str(random.randint(100000000, 999999999))
pdf.cell(0, 10, f"Settlement Amount:             ${settlement_amount}", ln=1)
pdf.cell(0, 10, f"Batch Number:                  {batch_number}", 0, 1)
pdf.cell(0, 10, f"Terminal ID:                   {terminal_id}", 0, 1)
pdf.cell(0, 10, "", ln=1)

# Add the transaction details
pdf.cell(0, 10, "Transaction Details:", ln=1)
pdf.cell(0, 10, "Date       Time     Amount        Fee", 0, 1)

for i in range(num_transactions):
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    year = "23"
    hour = random.randint(1, 12)
    minute = random.randint(0, 59)
    am_pm = random.choice(["AM", "PM"])
    amount = "{:.2f}".format(random.uniform(10, 100))
    fee = "{:.2f}".format(float(amount) * 0.025)
    pdf.cell(0, 10, f"{day}/{month}/{year}   {hour}:{minute:02d} {am_pm}  ${amount}       ${fee}", 0, 1)

pdf.cell(0, 10, "", ln=1)

# Add the signature line
pdf.cell(0, 10, "Signature:", ln=1)
pdf.cell(0, 10, "_________________________", ln=1)
pdf.cell(0, 10, "", ln=1)

# Save the PDF
rand_num = str(random.randint(10000, 99999))
pdf.output(rand_num + "_receipt.pdf")
