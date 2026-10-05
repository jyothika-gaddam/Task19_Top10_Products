import pandas as pd
import matplotlib.pyplot as plt

# Load the Superstore dataset
df = pd.read_csv("superstore.csv")

# Aggregate sales by product, sort descending, and select the top 10
top10 = (
    df.groupby("Product Name", as_index=False)["Sales"]
      .sum()
      .sort_values("Sales", ascending=False)
      .head(10)
)

top10.insert(0, "Rank", range(1, len(top10) + 1))
top10.to_csv("top10_products_by_sales.csv", index=False)

# Create chart
plot_df = top10.sort_values("Sales", ascending=True)
plt.figure(figsize=(12, 7))
plt.barh(plot_df["Product Name"], plot_df["Sales"])
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.title("Top 10 Products by Sales")
plt.tight_layout()
plt.savefig("top10_products_by_sales.png", dpi=200, bbox_inches="tight")
plt.show()

print(top10)
