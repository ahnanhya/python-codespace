import matplotlib.pyplot as plt

# Sample data for sales over 5 years
years = [2019, 2020, 2021, 2022, 2023]
sales = [150000, 180000, 210000, 230000, 250000]

# Create a bar chart
plt.bar(years, sales, color='blue')

# Adding title and labels
plt.title('Company Sales Over 5 Years')
plt.xlabel('Year')
plt.ylabel('Sales in USD')

# Display the chart
plt.show()
