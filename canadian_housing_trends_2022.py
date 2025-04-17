# Canadian Housing Trends – 2022
# This script simulates average housing prices and generates a chart

import pandas as pd
import matplotlib.pyplot as plt

# Simulate dataset
data = {
    "Date": pd.date_range(start="2022-01-01", periods=12, freq='M'),
    "Vancouver": [1100000, 1120000, 1135000, 1150000, 1160000, 1175000, 1180000, 1170000, 1165000, 1155000, 1140000, 1130000],
    "Toronto": [980000, 1000000, 1020000, 1035000, 1050000, 1060000, 1065000, 1055000, 1040000, 1020000, 1010000, 990000],
    "Calgary": [430000, 435000, 440000, 445000, 450000, 455000, 458000, 457000, 456000, 452000, 449000, 445000],
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv("canada_housing_prices_2022.csv", index=False)

# Create the plot
plt.figure(figsize=(10, 6))
for city in ['Vancouver', 'Toronto', 'Calgary']:
    plt.plot(df['Date'], df[city], label=city)

plt.title("Monthly Average Housing Prices in 2022")
plt.xlabel("Date")
plt.ylabel("Average Price (CAD)")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("canada_housing_prices_2022.png")
plt.show()
