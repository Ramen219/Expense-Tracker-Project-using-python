import matplotlib.pyplot as plt
from utils import spending_by_category

# Generate a report visualizing spending by category
def generate_report():
    categories = spending_by_category()
    if not categories:
        print("No data available for generating a report.")
        return

    labels = categories.keys()
    sizes = categories.values()

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.title("Spending by Category")
    plt.show()
