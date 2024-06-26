##############################
# markup, margin, and percent loss lesson
##############################



# packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



######################
# functions
######################

# profit function
def profit(revenue, cost):
    total = revenue - cost
    formatted_total = round(total, 4)
    return formatted_total



# markup percent function
def markup_percent(revenue, cost):
    subtotal1 = revenue - cost
    subtotal2 = subtotal1 / cost

    total = subtotal2 * 100

    formatted_total = f"{total:.2f}%"
    return formatted_total



# markup ratio function
def markup_ratio(revenue, cost):
    subtotal1 = revenue - cost
    subtotal2 = subtotal1 / cost

    total = subtotal2

    formatted_total = round(total, 4)
    return formatted_total



# margin percent function
def margin_percent(revenue, cost):
    subtotal1 = revenue - cost
    subtotal2 = subtotal1 / revenue

    total = subtotal2 * 100

    formatted_total = f"{total:.2f}%"
    return formatted_total



# margin ratio function
def margin_ratio(revenue, cost):
    subtotal1 = revenue - cost
    subtotal2 = subtotal1 / revenue

    total = subtotal2

    formatted_total = round(total, 4)
    return formatted_total



# new profit
def calculate_new_profit(original_profit, loss_percent):
    return (original_profit * (loss_percent / 100))+original_profit



# percent decrease
def calculate_percent_decrease(loss_percent):
    return abs(loss_percent)



# percent difference from original profit to new profit
def calculate_percent_difference(original_profit, new_profit):
    return ((abs(original_profit - new_profit)) / ((original_profit + new_profit) / 2) * 100)



# percent increase needed to go from new profit back to original profit
def calculate_percent_increase_needed(original_profit, new_profit):
    return (((abs(new_profit - original_profit)) / new_profit) * 100)



######################
# end functions
######################



######################
# percent loss and how much it takes to recover lesson
######################

# variables
revenue = 100
cost = 90
original_profit = profit(revenue, cost)
mu_percent = markup_percent(revenue, cost)
mu_ratio = markup_ratio(revenue, cost)
marg_percent = margin_percent(revenue, cost)
marg_ratio = margin_ratio(revenue, cost)

# print initial revenue, cost, profit, markup %, markup ratio, margin %, and margin ratio
print("Revenue:", f'${revenue:,.2f}')
print("Cost:",f'${cost:,.2f}')
print("Original Profit:",f'${original_profit:,.2f}')
print("Markup Percent:",mu_percent)
print("Markup Ratio:",round(mu_ratio, 4))
print("Margin Percent:",marg_percent)
print("Margin Ratio:", round(marg_ratio, 4))


# Input data
loss_percentages = [-1.00, -2.00, -3.00, -4.00, -5.00, -6.00, -7.00, -8.00, -9.00, -10.00, -11.00, -12.00, -13.00, -14.00, -15.00, -16.00, -17.00, -18.00, -19.00, -20.00, -21.00, -22.00, -23.00, -24.00, -25.00, -26.00, -27.00, -28.00, -29.00, -30.00, -31.00, -32.00, -33.00, -34.00, -35.00, -36.00, -37.00, -38.00, -39.00, -40.00, -41.00, -42.00, -43.00, -44.00, -45.00, -46.00, -47.00, -48.00, -49.00, -50.00, -51.00, -52.00, -53.00, -54.00, -55.00, -56.00, -57.00, -58.00, -59.00, -60.00, -61.00, -62.00, -63.00, -64.00, -65.00, -66.00, -67.00, -68.00, -69.00, -70.00, -71.00, -72.00, -73.00, -74.00, -75.00, -76.00, -77.00, -78.00, -79.00, -80.00, -81.00, -82.00, -83.00, -84.00, -85.00, -86.00, -87.00, -88.00, -89.00, -90.00, -91.00, -92.00, -93.00, -94.00, -95.00, -96.00, -97.00, -98.00, -99.00]
original_profit = 10.00

# Calculate data for each column
new_profits = [calculate_new_profit(original_profit, loss) for loss in loss_percentages]
percent_decreases = [calculate_percent_decrease(loss) for loss in loss_percentages]
percent_differences = [calculate_percent_difference(original_profit, new_profit) for new_profit in new_profits]
percent_increases_needed = [calculate_percent_increase_needed(original_profit, new_profit) for new_profit in new_profits]

# Create the DataFrame
data = {
    '% Loss': [f'{loss:.2f}%' for loss in loss_percentages],
    'New Profit': [f'${new_profit:,.2f}' for new_profit in new_profits],
    '% Decrease': [f'{percent:.3f}%' for percent in percent_decreases],
    '% Difference from Original Profit to New Profit': [f'{percent:.3f}%' for percent in percent_differences],
    '% Increase Needed to go from New Profit Back to Original Profit': [f'{percent:.3f}%' for percent in percent_increases_needed],
    'Original Profit': [f'${original_profit:,.2f}'] * len(loss_percentages)
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df.to_string(index=False))



######################
# end percent loss and how much it takes to recover lesson
######################



######################
# visualize loss results
######################

# 2D plot of '% loss' against '% Increase Needed to go from New Profit Back to Original Profit'
# Plotting
plt.figure(figsize=(14, 10))
plt.scatter(df['% Loss'], df['% Increase Needed to go from New Profit Back to Original Profit'], c='b', marker='o', alpha=0.7)
plt.title('Relationship between Percent Loss and Percent Increase Needed to Make Up Loss and Return to Original Profit', fontsize=14)  # Title font size
plt.xlabel('% Loss', fontsize=12)  # X-axis label font size
plt.ylabel('% Needed to Make Up for Loss', fontsize=12)  # Y-axis label font size
# Adjusting x-axis and y-axis ticks
plt.xticks(fontsize=5, rotation=45)  # Rotate x-axis labels by 45 degrees, align to the right, and add padding
plt.yticks(fontsize=5)  # Y-axis tick label font size and add padding

plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()



######################
# end visualize loss results
######################