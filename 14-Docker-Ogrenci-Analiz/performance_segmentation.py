import pandas as pd
import numpy as np

print('='*80)
print('Performans Segmentasyonu')
print('='*80)

df = pd.read_excel('student_data.xlsx')

print(f"DataFrame Shape: {df.shape}, Columns: {df.columns.tolist()}, length: {len(df)}")

# ── Seviye dağılımı ─────────────────────────────────────────────────────────
seviye_dagilimi = df['Seviye'].value_counts()

print('\n' + '='*80)
print('Seviye Dağılımı:')
print('='*80)
for seviye, adet in seviye_dagilimi.items():
    yuzde = adet / len(df) * 100
    print(f'{seviye}: {adet} öğrenci (%{yuzde:.1f})')

# ── Durum dağılımı ──────────────────────────────────────────────────────────
durum_dagilimi = df['Durum'].value_counts()

print('\n' + '='*80)
print('Durum Dağılımı:')
print('='*80)
for durum, adet in durum_dagilimi.items():
    yuzde = adet / len(df) * 100
    print(f'{durum}: {adet} öğrenci (%{yuzde:.1f})')

# ── Durum × Seviye çapraz tablosu ───────────────────────────────────────────
durum_seviye = pd.crosstab(df['Durum'], df['Seviye'])

print('\n' + '='*80)
print('Durum - Seviye Çapraz Tablosu:')
print('='*80)
print(durum_seviye)

# ── Seviyelere göre ortalama not, katılım ve devamsızlık ────────────────────
print('\n' + '='*80)
print('Seviyelere Göre Ortalamalar:')
print('='*80)
seviye_ozet = df.groupby('Seviye')[['Ortalama', 'Katılım', 'Devamsızlık']].mean().round(2)
print(seviye_ozet)

# ── Sonuçları Excel'e kaydet ────────────────────────────────────────────────
seviye_dagilimi.reset_index().to_excel('seviye_dagilimi.xlsx', index=False)
durum_seviye.reset_index().to_excel('durum_seviye_dagilimi.xlsx', index=False)

print('\n' + '='*80)
print('Sonuçlar kaydedildi: seviye_dagilimi.xlsx, durum_seviye_dagilimi.xlsx')
print('='*80)
