import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(
    filename='logs/run_log.txt',
    level=logging.INFO,
    format='%(asctime)s - Script ran',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info('')


df = pd.read_csv("/home/abhishek/budget_analysis/data/transactions.csv")

# print(df.head())
df['Date'] = pd.to_datetime(df['Date'])


df['Month'] = df['Date'].dt.strftime('%B')

print(df.dtypes)
def categorize(description):
    description = description.lower()

    if "salary" in description or "freelance" in description:
        return "Income"
    elif "uber" in description or "taxi" in description:
        return "Transport"
    elif "netflix" in description or "spotify" in description:
        return "Entertainment"
    elif "walmart" in description or "grocery" in description:
        return "Groceries"
    elif "mcdonald" in description or "starbucks" in description:
        return "Dining Out"
    elif "rent" in description:
        return "Rent"
    else:
        return "Uncategorized"

df['Category'] = df['Description'].apply(categorize)
# print(df["Category"])
# print(df["Description"])

df.to_csv("data/categorized_transactions.csv", index=False)

