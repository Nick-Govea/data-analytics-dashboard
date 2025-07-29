import pandas as pd

#Read CSV data in Python
df = pd.read_csv('data.csv')

import matplotlib.pyplot as plt

# Convert 'Date' to datetime, if it's not already
df['Date'] = pd.to_datetime(df['Date'])

# Plot 'Hour Slept' (handle possible missing/blank data)
df['Hour Slept'] = pd.to_numeric(df['Hour Slept'], errors='coerce')

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Hour Slept'])
plt.xlabel('Date')
plt.ylabel('Hours Slept')
plt.title('Sleep Over Time')
plt.tight_layout()
plt.show()
