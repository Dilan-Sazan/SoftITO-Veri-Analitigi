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

---

## 📓 Notebook Adım Adım — `pandas_pratik_dunya_mutluluk.ipynb`

Notebook'un kendisinde yalnızca kod bulunur; her adımın açıklaması burada.

#### 1. Veri Okuma ve İnceleme

2019 yılı verisiyle başlıyoruz.

#### 2. Series Yapısı

DataFrame'in tek bir sütunu aslında bir **Series**'tir.

#### 3. Veri Seçme: loc ve iloc

- `iloc` → konuma (pozisyona) göre seçim
- `loc` → etikete/koşula göre seçim

#### 4. Filtreleme

Koşullara uyan satırları seçiyoruz (derste gördüğümüz boolean filtreleme).

#### 5. Yeni Sütun Ekleme

Skora göre kategori sütunu oluşturalım.

#### 6. Sıralama ve Gruplama

**Yorum:** Mutluluk kategorisi yükseldikçe GSYH, sosyal destek ve sağlık ortalamalarının da arttığı net şekilde görülüyor.

#### 7. Merge: Bölge Bilgisini Ekleme

2019 verisinde bölge (Region) sütunu yok, ama 2015 verisinde var. Derste öğrendiğimiz `merge` ile iki tabloyu birleştirip 2019 verisine bölge bilgisi ekleyelim.

#### 8. Concat: Yılları Alt Alta Birleştirme

2018 ve 2019 dosyalarının sütunları aynı; `concat` ile alt alta ekleyelim.

#### 9. Uygulamalı Analiz: Türkiye'nin 5 Yıllık Trendi

Her yılın dosyasında sütun isimleri farklı olduğu için, döngüyle her dosyayı okuyup Türkiye'nin skorunu ve sırasını çekiyoruz.

#### Özet

Bu pratikte Pandas Eğitim dersindeki konuları Dünya Mutluluk Raporu verisine uyguladık:

- `read_csv`, `head`, `info`, `describe` ile **veriyi tanıdık**
- **Series** yapısını ve temel istatistiklerini gördük
- `loc`/`iloc` ve **boolean filtreleme** ile ülke seçtik (Türkiye, skoru 7+ ülkeler...)
- `pd.cut` ile **kategori sütunu** oluşturduk
- `sort_values` ve `groupby` ile **sıralama ve gruplama** yaptık
- `merge` ile 2015'teki **bölge bilgisini 2019 verisine ekledik**, bölge ortalamaları çıkardık
- `concat` ile **yılları alt alta birleştirdik**
- Uygulamalı analizde **Türkiye'nin 5 yıllık mutluluk trendini** çıkardık

📌 Dikkat çeken nokta: Her yılın dosyasında sütun isimleri farklıydı — bu sorunun kalıcı çözümü **veri temizleme** pratiğinde! 👉 `pandas_veri_temizleme_pratik.ipynb`

---

## 📓 Notebook Adım Adım — `pandas_veri_temizleme_pratik.ipynb`

Notebook'un kendisinde yalnızca kod bulunur; her adımın açıklaması burada.

#### 1. Veriyi Yükleme ve İlk Bakış

#### 2. Sütun İsimlerini Standartlaştırma

Her yıl için ayrı bir "çeviri sözlüğü" (rename map) tanımlayıp `rename()` ile ortak Türkçe isimlere geçiyoruz.

#### 3. Genel Veri Sağlığı Kontrolü

#### 4. Eksik Değerlerin Tespiti ve Giderilmesi

`Yolsuzluk_Algisi` sütununda 1 eksik değer var. Önce hangi satır olduğunu bulalım, sonra dolduralım.

#### 5. Yinelenen (Duplicate) Kayıt Kontrolü

Aynı ülke aynı yılda iki kez geçiyor mu?

#### 6. Veri Tiplerinin Düzeltilmesi

#### 7. Kategori Tutarlılığı: Ülke İsimleri

En sinsi sorun! Her ülke 5 yılda da varsa 5 kez görünmeli. 5'ten az görünen ülkeler ya rapora bazı yıllar girmemiş ya da **ismi farklı yazılmış**.

**Not:** Hâlâ 5'ten az görünen ülkeler var (Oman, Puerto Rico, Suriname...) ama bunlar yazım hatası değil — o ülkeler bazı yıllarda rapora gerçekten dahil edilmemiş. Bu normaldir ve düzeltilecek bir hata değildir. Veri temizlemede **her farklılık hata değildir**, ayrımı yapmak analistin işidir!

#### 8. İndeks Düzenleme

#### 9. Temizlenmiş Veriyi Kaydetme

#### 10. Uçtan Uca Temizleme Fonksiyonu

Derste öğrendiğimiz gibi, tüm adımları tek bir fonksiyonda topluyoruz — böylece yeni yıl verisi geldiğinde tek satırla temizlik yapılabilir.

#### Bonus: Temiz Verinin Meyvesi 🍎

Temizlik bitti — artık 5 yılı tek tabloda analiz edebiliriz. Ham dosyalarla bu tek satırda yapılamazdı!

#### Özet

Bu pratikte, Veri Temizleme dersindeki tüm adımları gerçek bir soruna uyguladık:

| Adım | Sorun | Çözüm |
|---|---|---|
| Sütun standartlaştırma | Her yılda farklı sütun isimleri | `rename()` + yıl bazlı eşleme sözlüğü |
| Birleştirme | 5 ayrı dosya | `concat()` + `Yil` sütunu |
| Eksik değer | 2018 BAE yolsuzluk algısı boş | Yıl medyanı ile `fillna()` |
| Duplicate | (kontrol edildi, yoktu) | `duplicated()` / `drop_duplicates()` |
| Veri tipi | Sira float görünüyordu | `astype(int)` |
| Kategori tutarlılığı | Aynı ülke farklı isimlerle | `replace()` + `value_counts()` ile tespit |
| İndeks | Karışık sıra | `sort_values()` + `reset_index()` |
| Kaydetme | — | `to_csv()` |
| Otomasyon | Tekrarlanabilirlik | Uçtan uca temizleme fonksiyonu |

Çıktı: **`mutluluk_2015_2019_temiz.csv`** — 782 satırlık, eksiksiz, tutarlı, analiz edilmeye hazır veri seti. ✅
