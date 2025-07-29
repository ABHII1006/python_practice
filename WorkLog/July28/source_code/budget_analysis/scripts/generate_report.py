
import pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv("/home/abhishek/budget_analysis/data/categorized_transactions.csv")
# /home/abhishek/budget_analysis/data/categorized_transactions.csv
expenses = df1[df1['Amount'] < 0]
category_totals = expenses.groupby('Category')['Amount'].sum().abs()

plt.figure(figsize=(6, 6))
plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
plt.title("Expense Breakdown by Category - July 2025")
plt.tight_layout()
plt.savefig("reports/expense_pie_chart.png")




df1=pd.read_csv("/home/abhishek/budget_analysis/data/categorized_transactions.csv")
expenses = df1[df1['Amount'] < 0]
category_totals = expenses.groupby('Category')['Amount'].sum().abs()
plt.figure(figsize=(5, 8))
category_totals.sort_values().plot(kind='barh', color='skyblue')
plt.xlabel("Total Spent (₹)")
plt.title("Expenses per Category - July 2025")
plt.tight_layout()
plt.savefig("reports/expense_bar_chart.png")
