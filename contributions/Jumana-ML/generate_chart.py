import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. SETUP: Load the dataset
# Make sure "amman_market_data.csv" is in the same folder as this script
file_path = "amman_market_data.csv"

if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' was not found.")
else:
    df = pd.read_csv(file_path)
    df = df.copy()

    # 2. DATA INSPECTION: Quick look at the structure
    print("--- Dataset Information ---")
    df.info()
    rows, cols = df.shape
    print(f"\nDimensions: {rows} rows and {cols} columns.")

    # 3. DATA PROCESSING: Sorting for Dominant Category Logic
    # We sort by Order ID, then by Line Total (Largest amount first)
    # This ensures the most expensive item in every order appears at the top
    df = df.sort_values(by=['order_id', 'line_total'], ascending=[True, False])
    
    # Calculate the total amount for each order (Sum of all items in the cart)
    df['order_total'] = df.groupby('order_id')['line_total'].transform('sum')

    # 4. AGGREGATION: Create an 'Orders' level dataframe
    # 'line_total': sum (The full price the customer paid)
    # 'category': 'first' (The category of the most expensive item in that order)
    orders = df.groupby('order_id').agg({
        'line_total': 'sum',
        'category': 'first'
    }).reset_index()

    # 5. ANALYSIS: Calculate Average Order Value (AOV) per Category
    # We group by the dominant category and find the mean of the total order values
    aov_data = orders.groupby('category')['line_total'].mean().sort_values(ascending=False)

    # 6. PROFESSIONAL VISUALIZATION: Setting up the High-Res Chart
    # 'white' style for a clean, corporate look
    sns.set_theme(style="white") 
    plt.figure(figsize=(14, 8), dpi=300) # 300 DPI for high-definition quality

    # Create the Bar Plot
    # hue=index ensures every category gets a unique color without warnings
    ax = sns.barplot(
        x=aov_data.values, 
        y=aov_data.index, 
        hue=aov_data.index, 
        palette="viridis", 
        legend=False
    )

    # 7. DATA LABELS: Adding the exact JOD value at the end of each bar
    # Using a manual loop for better understanding
    row_counter = 0
    for val in aov_data.values:
        # Put text at (X = value + small gap, Y = current row index)
        # .2f formats the number to 2 decimal places
        ax.text(val + 1.5, row_counter, f'{val:.2f} JOD', 
                va='center', fontweight='bold', color='#333333')
        row_counter = row_counter + 1

    # 8. TYPOGRAPHY: Titles and Subtitles
    plt.title("Books & Electronics Lead the Market in Average Order Value", 
              fontsize=18, fontweight='bold', pad=25, loc='left', color='#1a1a1a')

    # Adding an analytical subtitle explaining our "Dominant Category" finding
    plt.text(0, -0.6, "Analysis based on dominant category per transaction | High-value academic books drive 'Books' AOV.", 
             fontsize=11, color='gray', style='italic')

    plt.xlabel("Average Order Value (JOD)", fontsize=12, fontweight='semibold')
    plt.ylabel("Product Category", fontsize=12, fontweight='semibold')

    # 9. FINAL POLISH: Removing unnecessary borders (Chart Junk)
    sns.despine(left=True, bottom=True)
    ax.grid(axis='x', linestyle='--', alpha=0.3) # Subtle vertical grid lines

    # 10. SAVE & EXPORT: Saving the file in HD
    output_filename = 'market_analysis_professional.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    
    print(f"\nDone! Your professional chart is saved as '{output_filename}'")
    
    # Display the result on screen
    plt.show()