import pandas as pd

# Load the CSV file
df = pd.read_csv('data/raw/irrigation.csv')

# Filter and clean the data for harvested and irrigated areas
harvested_area_df = df[df['Data Item'] == 'SOYBEANS - ACRES HARVESTED'].copy()
harvested_area_df['Value'] = harvested_area_df['Value'].str.replace(',', '').astype(int)
harvested_area_df.rename(columns={'Value': 'harvested_area', 'Year': 'year', 'State': 'state_name'}, inplace=True)

irrigated_area_df = df[df['Data Item'] == 'SOYBEANS, IRRIGATED - ACRES HARVESTED'].copy()
irrigated_area_df['Value'] = irrigated_area_df['Value'].str.replace(',', '').astype(int)
irrigated_area_df.rename(columns={'Value': 'irrigated_harvested_area', 'Year': 'year', 'State': 'state_name'}, inplace=True)

# Merge the two DataFrames
merged_df = pd.merge(
    harvested_area_df[['year', 'state_name', 'harvested_area']],
    irrigated_area_df[['year', 'state_name', 'irrigated_harvested_area']],
    on=['year', 'state_name']
)

# Calculate the irrigation proportion
merged_df['irrigation_proportion'] = (100 * (merged_df['irrigated_harvested_area'] / merged_df['harvested_area'])).round(1)

# Select the required columns
result_df = merged_df[['year', 'state_name', 'harvested_area', 'irrigated_harvested_area', 'irrigation_proportion']]

# Display the resulting DataFrame
print(result_df.head())
result_df.to_csv('data/intermediate/processed_irrigation.csv', index=False)