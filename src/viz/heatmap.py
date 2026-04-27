import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist

def plot_clustered_heatmap(df, col, freq='M', agg_func='sum'):
    """
    Plot a clustered heatmap for a numeric column aggregated at a given frequency.

    Parameters:
    - df: DataFrame containing the data.
    - col: Name of the column to aggregate (e.g., 'total precipitation').
    - freq: Frequency for aggregation ('D' for daily, 'M' for monthly, 'Y' for yearly).
    - agg_func: Aggregation function to apply ('sum', 'min', 'max', 'mean', etc.). Default is 'sum'.

    Returns:
    - Displays a clustered heatmap.
    """
    # Ensure 'date' is in datetime format (assuming 'date' column exists)
    if 'date' not in df.columns:
        raise ValueError("DataFrame must contain a 'date' column.")
    df['date'] = pd.to_datetime(df['date'])

    # Aggregate data at the specified frequency
    aggregated = df.groupby(
        ['state_name', pd.Grouper(key='date', freq=freq)]
    )[col].agg(agg_func).reset_index()

    # Extract year from the date for cleaner labels
    aggregated['year'] = aggregated['date'].dt.year

    # Pivot to a heatmap format
    pivot_df = aggregated.pivot_table(
        index='state_name',
        columns='year',
        values=col
    )

    # Compute pairwise distances and linkage for clustering
    row_linkage = linkage(pdist(pivot_df, metric='euclidean'), method='ward')
    col_linkage = linkage(pdist(pivot_df.T, metric='euclidean'), method='ward')

    # Plot clustered heatmap
    sns.clustermap(
        pivot_df,
        cmap='viridis',
        row_linkage=row_linkage,
        col_linkage=col_linkage,
        figsize=(12, 8),
        cbar_kws={'label': f'{col} (mm)'}
    )
    plt.title(f'{col} Heatmap (Clustered)')
    plt.tight_layout()
    plt.show()

# Example usage:
# plot_clustered_heatmap(weather_df, 'total precipitation', freq='M')