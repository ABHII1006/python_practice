import pandas as pd

df = pd.read_csv("/home/abhishek/budget_analysis/data/transactions.csv")

# print(df.head())

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

