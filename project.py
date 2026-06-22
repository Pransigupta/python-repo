import pandas as pd

import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/Pransigupta/temperature_data.json/main/temperature_data.json"

df = pd.read_json(url)
print(df.head())

# Drop row where day = Wednesday
df = df[df["day"] != "Wednesday"]

#  Fill missing humidity values with average humidity
avg_humidity = df["humidity_pct"].mean()
df["humidity_pct"] = df["humidity_pct"].fillna(avg_humidity)

#  Create Fahrenheit column
df["fahrenheit"] = (df["temperature_c"] * 1.8) + 32

print("\nModified Data:")
print(df)

# Create pie chart subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Temperature pie chart
ax[0].pie(
    df["temperature_c"],
    labels=df["day"],
    autopct="%1.1f%%"
)
ax[0].set_title("Temperature Distribution")

# Humidity pie chart
ax[1].pie(
    df["humidity_pct"],
    labels=df["day"],
    autopct="%1.1f%%"
)
ax[1].set_title("Humidity Distribution")

plt.tight_layout()

#  Save graph as image
plt.savefig("weather_analysis.png")

plt.show()