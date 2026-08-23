import pandas as pd
import numpy as np

print('='*80)
print('Korelasyon Analizi')
print('='*80)

df = pd.read_excel('student_data.xlsx')

print(f'DataFrame Shape: {df.shape}, Columns: {df.columns.tolist()}, length: {len(df)}')

numeric_columns = ['Matematik', 'Fizik', 'Kimya', 'Türkçe', 'İngilizce', 'Bilgisayar',
                   'Ortalama', 'Katılım', 'Devamsızlık']
correlation_matrix = df[numeric_columns].corr()

print('='*80)
print('\nCorrelation Matrix:')
print('='*80)

dersler = ['Matematik', 'Fizik', 'Kimya', 'Türkçe', 'İngilizce', 'Bilgisayar']

for i in dersler:
    for j in dersler:
        if i != j:
            correlation = correlation_matrix.loc[i, j]
            print(f'Correlation between {i} and {j}: {correlation:.4f}')

print('\n' + '='*80)
print('Ortalama ile Diğer Dersler Arasındaki Korelasyonlar:')
print('='*80)
for ders in dersler:
    correlation = correlation_matrix.loc['Ortalama', ders]
    print(f'Correlation between Ortalama and {ders}: {correlation:.4f}')

katilim_correlation = correlation_matrix.loc['Ortalama', 'Katılım']
devamsizlik_correlation = correlation_matrix.loc['Ortalama', 'Devamsızlık']

print(f'\n Katılım <-> Ortalama: {katilim_correlation:.4f}')
artar_azalir = 'artar' if katilim_correlation > 0 else 'azalır'
print(f' -> Katılım arttıkça Ortalama {artar_azalir}')

print(f'\n Devamsızlık <-> Ortalama: {devamsizlik_correlation:.4f}')
artar_azalir = 'artar' if devamsizlik_correlation > 0 else 'azalır'
print(f' -> Devamsızlık arttıkça Ortalama {artar_azalir}')

print('\n' + '='*80)
print('Yüksek korele çiftler:')
print('='*80)

correlationS = []
for i, ders1 in enumerate(dersler):
    for j, ders2 in enumerate(dersler):
        if i < j:
            correlation = correlation_matrix.loc[ders1, ders2]
            correlationS.append((ders1, ders2, correlation))

correlationS.sort(key=lambda x: abs(x[2]), reverse=True)
for ders1, ders2, correlation in correlationS:
    print(f'Correlation between {ders1} and {ders2}: {correlation:.4f}')
