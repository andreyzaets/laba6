from collections import Counter

data = [
    {"Outlook": "Sunny", "Humidity": "High", "Wind": "Weak", "Play": "No"},
    {"Outlook": "Sunny", "Humidity": "High", "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Humidity": "High", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Humidity": "High", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Humidity": "Normal", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Humidity": "Normal", "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Humidity": "Normal", "Wind": "Strong", "Play":
        "Yes"},
    {"Outlook": "Sunny", "Humidity": "High", "Wind": "Weak", "Play": "No"},
    {"Outlook": "Sunny", "Humidity": "Normal", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Humidity": "High", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Sunny", "Humidity": "Normal", "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Overcast", "Humidity": "High", "Wind": "Strong", "Play": "Yes"},
    {"Outlook": "Overcast", "Humidity": "Normal", "Wind": "Weak", "Play": "Yes"},
    {"Outlook": "Rain", "Humidity": "High", "Wind": "Strong", "Play": "No"},
]

play_count = Counter([row["Play"] for row in data])
outlook_count = Counter([(row["Outlook"], row["Play"]) for row in data])
humidity_count = Counter([(row["Humidity"], row["Play"]) for row in data])
wind_count = Counter([(row["Wind"], row["Play"]) for row in data])

total_play_yes = play_count["Yes"] / len(data)
total_play_no = play_count["No"] / len(data)

# Для 8 варіанту події наступні
# Outlook = Sunny
# Humidity = High
# Wind = Weak
p_outlook_yes = outlook_count[("Sunny", "Yes")] / play_count["Yes"]
p_outlook_no = outlook_count[("Sunny", "No")] / play_count["No"]
p_humidity_yes = humidity_count[("High", "Yes")] / play_count["Yes"]
p_humidity_no = humidity_count[("High", "No")] / play_count["No"]
p_wind_yes = wind_count[("Weak", "Yes")] / play_count["Yes"]
p_wind_no = wind_count[("Weak", "No")] / play_count["No"]

p_yes = p_outlook_yes * p_humidity_yes * p_wind_yes * total_play_yes
p_no = p_outlook_no * p_humidity_no * p_wind_no * total_play_no

p_yes_normalized = p_yes / (p_yes + p_no)
p_no_normalized = p_no / (p_yes + p_no)
print(f"Ймовірність, що матч відбудеться (Yes): {p_yes_normalized:.2f}")
print(f"Ймовірність, що матч не відбудеться (No): {p_no_normalized:.2f}")
