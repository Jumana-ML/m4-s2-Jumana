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
    Average Order Value (AOV) chart, compatible with any machine.
    """
    
    # 1. DYNAMIC PATH CONFIGURATION
    # This line automatically detects the folder where this .py script is saved
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Join the directory path with filenames (Works on Windows, Mac, and Linux)
    data_file = os.path.join(current_directory, "amman_market_data.csv")
    output_image = os.path.join(current_directory, "market_analysis_high_res.png")

    # Check if the CSV file exists in the current folder
    if not os.path.exists(data_file):
        print(f"Error: Could not find the file at: {data_file}")
        print("Make sure the CSV file is in the same folder as this script.")
        return

    # 2. DATA PROCESSING
    df = pd.read_csv(data_file)
    
    # Sort data: Largest line_total first for each order to find the dominant category
    df = df.sort_values(by=['order_id', 'line_total'], ascending=[True, False])
    
    # Aggregate data: Total money per order and the 'first' (most expensive) category
    orders = df.groupby('order_id').agg({
        'line_total': 'sum',
        'category': 'first'
    }).reset_index()

    # Calculate the Average Order Value (AOV) for each category
    aov_data = orders.groupby('category')['line_total'].mean().sort_values(ascending=False)

    # 3. VISUALIZATION SETUP (High Definition 300 DPI)
    sns.set_theme(style="white")
    plt.figure(figsize=(14, 8), dpi=300)

    # Create the horizontal bar plot
    ax = sns.barplot(
        x=aov_data.values, 
        y=aov_data.index, 
        hue=aov_data.index, 
        palette="viridis", 
        legend=False
    )

    # 4. DATA LABELING (Manual loop for clarity)
    row_index = 0
    for value in aov_data.values:
        # Place JOD text at the end of each bar
        ax.text(value + 1.5, row_index, f'{value:.2f} JOD', 
                va='center', fontweight='bold', color='#333333')
        row_index = row_index + 1

    # 5. CHART TYPOGRAPHY & TITLES
    plt.title("Books & Electronics Lead the Market in Average Order Value", 
              fontsize=18, fontweight='bold', pad=25, loc='left')

    plt.text(0, -0.6, "Analysis based on dominant category | High-value items drive the Books AOV.", 
             fontsize=11, color='gray', style='italic')

    plt.xlabel("Average Order Value (JOD)", fontsize=12, fontweight='semibold')
    plt.ylabel("Product Category", fontsize=12, fontweight='semibold')

    # 6. FINAL CLEANUP
    sns.despine(left=True, bottom=True)
    ax.grid(axis='x', linestyle='--', alpha=0.3)

    # 7. EXPORTING
    # Save the file to the same directory as the script
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.close() 
    
    print(f"Success! The chart has been saved to the script's folder:\n{output_image}")

# Execute the function
if __name__ == "__main__":
    generate_market_analysis_chart()