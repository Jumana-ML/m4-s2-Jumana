import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Force Matplotlib to use 'Agg' backend to save files without a popup window
matplotlib.use('Agg')

def generate_market_analysis_chart():
    """
    Main function to process sales data and generate a high-resolution 
    Average Order Value (AOV) chart.
    """
    
    # 1. PATH SETUP: Automatically detect the script's folder for cross-device compatibility
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Define file paths for the input data and output image
    file_path = os.path.join(current_directory, "amman_market_data.csv")
    output_image = os.path.join(current_directory, "market_analysis_high.png")

    # Check if the CSV file exists in the directory
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return
    else:
        # Load the dataset
        df = pd.read_csv(file_path)
        df = df.copy()

        # 2. DATA INSPECTION: Print basic info and dimensions
        print("--- Dataset Info ---")
        df.info()
        rows, cols = df.shape
        print(f"\nThe dataset contains {rows} rows and {cols} columns.")

        # 3. DATA PROCESSING: Sorting to identify the dominant category per order
        # Sort by order_id and line_total (Highest value first)
        df = df.sort_values(by=['order_id', 'line_total'], ascending=[True, False])
        
        # Calculate total order value and add it to the original dataframe
        df['order_total'] = df.groupby('order_id')['line_total'].transform('sum')

        # 4. DATA AGGREGATION: Grouping by Order ID
        # Extract total sum and the 'first' (most expensive) category per order
        orders = df.groupby('order_id').agg({
            'line_total': 'sum',
            'category': 'first'
        }).reset_index()

        print("\n--- Orders Summary (First 5 rows) ---")
        print(orders.head())

        # 5. ANALYSIS: Calculate Average Order Value (AOV) per category
        aov_data = orders.groupby('category')['line_total'].median().sort_values(ascending=False)

        # 6. PROFESSIONAL VISUALIZATION: Chart setup and styling
        sns.set_theme(style="white")
        plt.figure(figsize=(14, 8), dpi=300) # High-definition resolution

        # Draw bars with unique colors based on category names
        ax = sns.barplot(
            x=aov_data.values, 
            y=aov_data.index, 
            hue=aov_data.index, 
            palette="viridis", 
            legend=False
        )

        # 7. DATA LABELING: Adding numeric labels to each bar (Beginner-friendly loop)
        row_index = 0
        for value in aov_data.values:
            # Place text at (X=value + offset, Y=row_index) formatted to 2 decimal places
            ax.text(value + 1.5, row_index, f'{value:.2f} JOD', 
                    va='center', fontweight='bold', color='#333')
            row_index = row_index + 1

        # 8. TYPOGRAPHY: Adding Title and Subtitle
        plt.title("Books & Electronics Lead the Market in Average Order Value", 
                  fontsize=18, fontweight='bold', pad=25, loc='left')

        # Descriptive subtitle explaining the high-value book impact
        plt.text(0, -0.6, "High-value items like 'Introduction to Algorithms' drive the Books category AOV.", 
                 fontsize=11, color='gray', style='italic')

        plt.xlabel("Average Order Value (JOD)", fontsize=12, fontweight='semibold')
        plt.ylabel("Product Category", fontsize=12, fontweight='semibold')

        # 9. FINAL POLISH: Removing borders and adding subtle gridlines
        sns.despine(left=True, bottom=True)
        ax.grid(axis='x', linestyle='--', alpha=0.3)

        # 10. EXPORTING: Saving the final image and closing the plot
        plt.savefig(output_image, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"\nSuccess! Professional chart saved at:\n'{output_image}'")

# Execute the main function
if __name__ == "__main__":
    generate_market_analysis_chart()