
# Ask user to enter the initial stock level, cast to integer and save as initial_stock_level
initial_stock_level = int(input("Please enter the initial stock level: "))

# Ask user to enter the planning horizon (number of months to plan), cast to integer and save as no_of_months
no_of_months = int(input("Please enter the number of months to plan: "))

# Set an Accumulator for the dictionary of monthly sales
monthly_sales = {}

# For each month, ask user to enter the forecasted sale
# To do this loop through the month using a range
for month in range(1, no_of_months+1):
    
    # Ask user to enter the forecasted sale for the month, cast to integer and save as forecast
    forecast = int(input(f"Please enter the planned sales quantity for month-{month}: "))

    # Add the forecast to the dictionary of monthly sales
    monthly_sales[month] = forecast



# Print the resulting production quantities for each month

# Loop through the dictionary of monthly sales: 
for month, forecast in monthly_sales.items():  
    
    # Check if forecast_sales > Initial Stock
    if initial_stock_level > forecast:
        print(f"Production quantity for Month {month} - 0")
        
        # Update the stock level
        initial_stock_level -= forecast

    # Else:
    else:
        # How much do you have to produce for this month?
        quantity_produced = forecast - initial_stock_level
        
        # Print the Production Quantity
        print(f"Production quantity for Month {month} - {quantity_produced}")
        
        # Update the stock level
        initial_stock_level += quantity_produced - forecast
