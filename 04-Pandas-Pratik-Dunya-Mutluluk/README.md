# Pandas Pratik: Dünya Mutluluk Raporu (2015–2019) 🌍

Bu klasör, **Pandas Eğitim** ve **Pandas ile Veri Temizleme** derslerinde öğrenilen konuların gerçek bir veri seti üzerinde uygulandığı **kişisel pratik çalışmalarımı** içerir.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `pandas_pratik_dunya_mutluluk.ipynb` | Pandas temellerinin uygulaması (filtreleme, groupby, merge, concat, Türkiye analizi) |
| `pandas_veri_temizleme_pratik.ipynb` | 5 dağınık dosyayı tek temiz veri setine dönüştürme çalışması |
| `2015.csv` … `2019.csv` | Ham veri: Dünya Mutluluk Raporu yıllık dosyaları |
| `mutluluk_2015_2019_temiz.csv` | Temizleme pratiğinin çıktısı: birleşik ve temiz veri seti (782 satır) |

## 📊 Veri Seti Hakkında

Dünya Mutluluk Raporu; ülkelerin mutluluk skorlarını ve bunu etkileyen faktörleri (kişi başı GSYH, sosyal destek, sağlıklı yaşam beklentisi, özgürlük, cömertlik, yolsuzluk algısı) içerir. Elimizde 2015–2019 arası 5 yıllık veri var (~155 ülke/yıl).

Bu veri seti pratik için özellikle uygun çünkü **gerçekten "kirli"**:
- Her yılın dosyasında **sütun isimleri farklı** yazılmış
- 2018'de **eksik değer** var
- Aynı ülke farklı yıllarda **farklı isimlerle** geçiyor (`Trinidad and Tobago` / `Trinidad & Tobago`)

## 🛠️ Notebook 1: Pandas Temelleri Pratiği

- `read_csv`, `head`, `info`, `describe` ile veri inceleme
- Series yapısı ve istatistikleri
- `loc` / `iloc` ve boolean filtreleme (skoru 7+ ülkeler, düşük GSYH'li ama mutlu ülkeler)
- `pd.cut` ile mutluluk kategorisi oluşturma
- `groupby` ile kategori ve bölge ortalamaları
- `merge` ile 2015'teki bölge bilgisini 2019 verisine ekleme
- `concat` ile yılları birleştirme
- **Uygulamalı analiz:** Türkiye'nin 5 yıllık mutluluk skoru ve sıralama trendi 🇹🇷

## 🧹 Notebook 2: Veri Temizleme Pratiği

| Adım | Uygulanan Teknik |
|---|---|
| Sütun standartlaştırma | Yıl bazlı eşleme sözlükleri + `rename()` |
| 5 dosyayı birleştirme | `concat()` + `Yil` sütunu |
| Eksik değer doldurma | Yıl medyanı ile `fillna()` |
| Duplicate kontrolü | `duplicated()` |
| Veri tipi düzeltme | `astype(int)` |
| Ülke ismi tutarlılığı | `value_counts()` ile tespit + `replace()` |
| İndeks düzenleme | `sort_values()` + `reset_index()` |
| Otomasyon | Uçtan uca temizleme fonksiyonu |

## 🔗 İlgili Dersler

Bu pratiklerin dayandığı ders notebook'ları için:
👉 [`03-Pandas-Ders`](../03-Pandas-Ders) klasörüne bakabilirsiniz.
