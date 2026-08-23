import pandas as pd
import numpy as np

print('='*80)
print('Basic Statistics')
print('='*80)

df = pd.read_excel('student_data.xlsx')

print(f"DataFrame Shape: {df.shape}, Columns: {df.columns.tolist()}, length: {len(df)}")

dersler = ['Matematik', 'Fizik', 'Kimya', 'Türkçe', 'İngilizce', 'Bilgisayar']

stats_data = []
for ders in dersler:
    notlar = df[ders].dropna()

    print(f"\n{ders} Notları İstatistikleri:")
    print(f"Minimum: {notlar.min()}")
    print(f"Maksimum: {notlar.max()}")
    print(f"Ortalama: {notlar.mean()}")
    print(f"Medyan: {notlar.median()}")
    print(f"Standard Sapma: {notlar.std()}")
    print(f"Varyans: {notlar.var()}")
    print(f"Çeyrekler: {notlar.quantile([0.25, 0.5, 0.75]).to_dict()}")

    stats_data.append({
        'Ders': ders,
        'Minimum': notlar.min(),
        'Maksimum': notlar.max(),
        'Ortalama': notlar.mean(),
        'Medyan': notlar.median(),
        'Standard Sapma': notlar.std(),
        'Varyans': notlar.var(),
        'Çeyrekler': str(notlar.quantile([0.25, 0.5, 0.75]).to_dict())
    })

stats_df = pd.DataFrame(stats_data)
stats_df.to_excel('ders_istatistikleri.xlsx', index=False)