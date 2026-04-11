import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Force Matplotlib to use 'Agg' backend to save files without opening a popup window
matplotlib.use('Agg')

def generate_market_analysis_chart():
    """
    Main function to process sales data and generate a high-resolution 
    Average Order Value (AOV) chart.
    """
    
    # 1. PATH CONFIGURATION
    # Using 'r' before the string to handle backslashes in Windows paths correctly
    base_path = r"C:\Users\DELL\m4-s2-Jumana\contributions\Jumana-ML"
    data_file = os.path.join(base_path, "amman_market_data.csv")
    output_image = os.path.join(base_path, "market_analysis_high_res.png")

    # Check if the CSV file exists at the specified path
    if not os.path.exists(data_file):
        print(f"Error: Could not find the file at: {data_file}")
        return

    # 2. DATA PROCESSING
    # Load the dataset into a Pandas DataFrame
    df = pd.read_csv(data_file)
    
    # Sort data by Order ID and Line Total (Descending) 
    # This puts the most expensive item of each order at the top
    df = df.sort_values(by=['order_id', 'line_total'], ascending=[True, False])
    
    # Aggregate data: Sum the total money per order and pick the 'first' (dominant) category
    orders = df.groupby('order_id').agg({
        'line_total': 'sum',
        'category': 'first'
    }).reset_index()

    # Calculate the Average Order Value (AOV) for each category
    aov_data = orders.groupby('category')['line_total'].mean().sort_values(ascending=False)

    # 3. VISUALIZATION SETUP
    # Set a clean professional theme and high-definition resolution (300 DPI)
    sns.set_theme(style="white")
    plt.figure(figsize=(14, 8), dpi=300)

    # Create the horizontal bar plot
    # hue=index avoids warnings in newer Seaborn versions
    ax = sns.barplot(
        x=aov_data.values, 
        y=aov_data.index, 
        hue=aov_data.index, 
        palette="viridis", 
        legend=False
    )

    # 4. DATA LABELING (For beginners: using a manual counter)
    row_index = 0
    for value in aov_data.values:
        # Place text: X position = value + 1.5 (gap), Y position = row number
        # .2f formats the number to 2 decimal places
        ax.text(value + 1.5, row_index, f'{value:.2f} JOD', 
                va='center', fontweight='bold', color='#333333')
        row_index = row_index + 1

    # 5. CHART TYPOGRAPHY & TITLES
    plt.title("Books & Electronics Lead the Market in Average Order Value", 
              fontsize=18, fontweight='bold', pad=25, loc='left')

    # Add subtitle explaining the "Dominant Category" logic
    plt.text(0, -0.6, "Analysis based on dominant category | High-value items drive the Books AOV.", 
             fontsize=11, color='gray', style='italic')

    plt.xlabel("Average Order Value (JOD)", fontsize=12, fontweight='semibold')
    plt.ylabel("Product Category", fontsize=12, fontweight='semibold')

    # 6. FINAL CLEANUP
    # Remove chart borders for a modern look
    sns.despine(left=True, bottom=True)
    ax.grid(axis='x', linestyle='--', alpha=0.3) # Add light vertical grid lines

    # 7. EXPORTING
    # Save the file to the specific project folder and close the plot to free memory
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.close() 
    
    print(f"Success! The professional chart has been saved to:\n{output_image}")

# Execute the function
if __name__ == "__main__":
    generate_market_analysis_chart()