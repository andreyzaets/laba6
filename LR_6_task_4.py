from collections import Counter
import pandas as pd

url = "https://raw.githubusercontent.com/susanli2016/Machine-Learning-withPython/master/data/renfe_small.csv"
df = pd.read_csv(url)
df = df[["price", "train_type", "origin", "destination", "train_class"]].dropna()
df["price_category"] = pd.cut(df["price"], bins=3, labels=["low", "medium",
                                                           "high"])
train_type_count = Counter(zip(df["train_type"], df["price_category"]))
origin_count = Counter(zip(df["origin"], df["price_category"]))
destination_count = Counter(zip(df["destination"], df["price_category"]))
class_count = Counter(zip(df["train_class"], df["price_category"]))
price_category_count = Counter(df["price_category"])


def calculate_probability(category, attribute, attribute_count,
                          price_category_count):
    return (
        attribute_count.get((attribute, category), 0) /
        price_category_count[category]
        if price_category_count[category]
        else 0
    )


train_type = "AVE"
origin = "MADRID"
destination = "BARCELONA"
train_class = "Preferente"
probabilities = {}
for category in price_category_count.keys():
    p_train_type = calculate_probability(
        category, train_type, train_type_count, price_category_count
    )
p_origin = calculate_probability(
    category, origin, origin_count, price_category_count
)
p_destination = calculate_probability(
    category, destination, destination_count, price_category_count
)
p_class = calculate_probability(
    category, train_class, class_count, price_category_count
)
p_category = price_category_count[category] / len(df)

probabilities[category] = (
        p_train_type * p_origin * p_destination * p_class * p_category
)

total_prob = sum(probabilities.values())
for category in probabilities:
    probabilities[category] /= total_prob if total_prob else 1
probabilities = list(probabilities.values())
formatted_probabilities = list(map("{:.2f}".format, probabilities))
print(
    f"Ймовірності для кожної категорії вартості квитка з параметрами({train_type}, {train_class}, {origin}, {destination}): ",
    formatted_probabilities)
