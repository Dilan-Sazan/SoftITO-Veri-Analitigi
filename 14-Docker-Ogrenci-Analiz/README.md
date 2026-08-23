# Docker ile Konteynerize Edilmiş Öğrenci Analizi 🐳

Bu klasör, SoftİTO Veri Analistliği eğitiminin **Docker** bölümünde yaptığım çalışmayı içerir. Amaç, Python analiz betiklerini konteyner içinde çalıştırmak — yani "benim bilgisayarımda çalışıyordu" probleminden kurtulmak.

## 🎯 Bu Proje Ne Yapıyor?

100 öğrencilik bir not tablosunu üç ayrı analizden geçiriyor. Her analiz **kendi Docker servisi** olarak tanımlı ve `docker-compose` ile tek komutla çalıştırılabiliyor.

| Servis | Betik | Görevi | Çıktısı |
|---|---|---|---|
| `basic_istatistic` | `basic_statistic.py` | Her dersin min/maks/ortalama/medyan/std/varyans/çeyrek değerleri | `ders_istatistikleri.xlsx` |
| `correlation_analysis` | `correlation_analysis.py` | Dersler arası ve ortalama-katılım-devamsızlık korelasyonları | ekrana yazdırır |
| `performance_segmentation` | `performance_segmentation.py` | Öğrencileri seviye ve duruma göre gruplama | `seviye_dagilimi.xlsx`, `durum_seviye_dagilimi.xlsx` |

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `Dockerfile` | Konteyner tarifi: Python 3.12-slim imajı, bağımlılık kurulumu, dosyaların kopyalanması |
| `docker-compose.yml` | Üç servisin tanımı — hepsi aynı imajı kullanır, farklı komut çalıştırır |
| `requirements.txt` | pandas, numpy, scikit-learn, openpyxl |
| `student_data.xlsx` | Girdi verisi: 100 öğrenci × 15 sütun |
| `*.py` | Üç analiz betiği |
| `ders_istatistikleri.xlsx`, `seviye_dagilimi.xlsx`, `durum_seviye_dagilimi.xlsx` | Betiklerin ürettiği çıktılar |

## 📊 Veri Seti

100 öğrenci, 15 sütun: Öğrenci ID, Ad, Sınıf, altı ders notu (Matematik, Fizik, Kimya, Türkçe, İngilizce, Bilgisayar), Katılım, Devamsızlık, Kayıt Tarihi, Ortalama, Durum (Başarılı/Yetersiz), Seviye (B/C/D/F).

### Çıkan Sonuçlar

**Ders istatistikleri:** En yüksek ortalama Bilgisayar'da (75.95), en düşük Matematik'te (69.07). Bilgisayar aynı zamanda en düşük standart sapmaya sahip (13.84) — yani öğrenciler bu derste birbirine en yakın notları almış.

**Seviye dağılımı:** C-İyi 49, D-Orta 37, B-Çok İyi 12, F-Zayıf 2 öğrenci.

**Durum × Seviye:** Başarılı sayılan 61 öğrencinin tamamı B veya C seviyesinde; Yetersiz olan 39 öğrencinin tamamı D veya F'te. Yani "Durum" alanı doğrudan seviyeden türetilmiş.

## 🐳 Docker Tarafı — Ne Öğrendim

**Dockerfile** bir tarif dosyası: hangi Python sürümü, hangi kütüphaneler, hangi dosyalar. Bu tarifle oluşan imaj her makinede aynı şekilde çalışır.

```dockerfile
FROM python:3.12-slim        # temel imaj
WORKDIR /app                 # konteyner içindeki çalışma klasörü
COPY requirements.txt .      # önce bağımlılıklar kopyalanır
RUN pip install -r requirements.txt
COPY *.xlsx .                # sonra veri ve kod
COPY *.py .
```

Bağımlılıkların koddan **önce** kopyalanması bilinçli: Docker katmanları önbelleğe alır, kod değişince kütüphaneler yeniden kurulmaz.

**docker-compose.yml** ise birden fazla servisi tek dosyada tanımlar. Üçü de aynı imajdan (`build: .`) doğar ama farklı `command` çalıştırır. `volumes: - .:/app` satırı klasörü konteynere bağlar — böylece üretilen Excel dosyaları konteyner kapandığında kaybolmaz, bilgisayarda kalır.

## ▶️ Çalıştırma

```bash
docker compose up --build              # üç servisi birden çalıştır
docker compose run basic_istatistic    # sadece birini çalıştır
```

## 🔍 Gözden Geçirme Notları

Çalışmayı tekrar incelediğimde fark ettiğim iki hata (öğrenme kaydı olarak burada tutuyorum):

**1. `performance_segmentation.py`, `basic_statistic.py`'nin birebir kopyası.**
Dosya adı segmentasyon diyor ama içerik istatistik hesaplıyor ve `ders_istatistikleri.xlsx`'i yeniden yazıyor. Klasördeki `seviye_dagilimi.xlsx` ve `durum_seviye_dagilimi.xlsx` dosyaları, betiğin özgün hâlinin bir zamanlar çalıştığını gösteriyor — sonradan üzerine yanlış içerik kopyalanmış. Doğru hâli şu iki satırı içermeliydi:

```python
df['Seviye'].value_counts()                    # -> seviye_dagilimi.xlsx
pd.crosstab(df['Durum'], df['Seviye'])         # -> durum_seviye_dagilimi.xlsx
```

**2. `correlation_analysis.py`'de girinti (indentation) hatası.**
`print` satırları ve `correlationS.append(...)` döngülerin **dışında** kaldığı için sadece son yineleme çalışıyor. Sonuç olarak 15 ders çifti yerine tek bir satır yazdırılıyor ve o da hatalı etiketleniyor ("Bilgisayar and Bilgisayar"). Python'da girintinin akışı belirlediğinin çok net bir örneği — bir seviye boşluk, tüm çıktıyı değiştiriyor.
