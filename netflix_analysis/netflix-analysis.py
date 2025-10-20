import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# adjust path to your actual CSV filename/location
df = pd.read_csv("netflix_titles.csv")

# 2. Clean data
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')

# Extract year from date_added
df["year_added"] = df["date_added"].dt.year

# Create a numeric duration column (only for movies)
df["duration_min"] = df['duration'].apply(
    lambda x: int(str(x).split()[0]) if 'min' in str(x) else np.nan
)

# 3. Basic Stats
print('Total Titles:', len(df))
print('Movies:', (df['type'] == 'Movie').sum())
print('Tv shows:', (df['type'] == 'TV Show').sum())
print('Unique Countries:', df["country"].unique())

# 4. Top 10 Countries
top_countries = (df['country'].str.split(',')
                 .explode()
                 .str.strip()
                 .value_counts()
                 .head(10)
)
print('\nTop 10 Countries:\n', top_countries)

# 5. Titles Added by Year
titles_by_year = df.groupby('year_added').size().dropna()

# 6. Visualization Section
plt.figure(figsize=(6,6))
plt.pie([(df['type'] == 'Movie').sum(), (df["type"] == 'TV Show').sum()],
        labels=['Movie', 'TV Show'], autopct='%1.1f%%', startangle=90
)
plt.title('Movies Vs Tv Shows on Netflix')
plt.show()

plt.figure(figsize=(10,6))
top_countries.plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries By Number Of Titles')
plt.xlabel('Countries')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()

# 7. Optional — Save summary
summary = {
    'total_titles': len(df),
    'movies': int((df['type'] == 'Movie').sum()),
    'tv_shows': int((df['type'] == 'TV Show').sum()),
    'unique_countries': int(df['country'].nunique())
}

pd.DataFrame([summary]).to_csv('summary_stats.csv', index=False)
print("\n✅ Analysis complete. Charts displayed and summary saved to summary_stats.csv")