# Create a new file called data_presenter.py.
# Open the CupcakeInvoices.csv.
open_file = open("CupcakeInvoices.csv")
# Loop through all the data and print each row.

for row in open_file:
    print(row)

# Loop through all the data and print the type of cupcakes purchased.

for row in open_file:
    values = row.split(',')
    print(values[2])

# Loop through all the data and print out the total for each invoice 
# (Note: this data is not provided by the csv, you will need to calculate it. 
# Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float.
# Research how to do this.).

for row in open_file:
    values = row.split(',')
    total = int(values[3]) * float(values[4])
    print(total)

# Loop through all the data, and print out the total for all invoices combined.
total = 0

for row in open_file:
    values = row.split(',')
    total = total + (int(values[3]) * float(values[4]))

# Close your open file.

open_file.close()

# Challenge: Do some research and see if you can limit your floats to never exceed to characters
# after the decimal point.

# Going Further
# Explore the graphing tools covered in today’s lecture. 
# See if you can implement one of them to display the total income of
# chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.