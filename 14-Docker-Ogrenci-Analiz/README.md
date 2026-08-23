# Docker ile Konteynerize Edilmiş Öğrenci Analizi 🐳

Bu klasör, SoftİTO Veri Analistliği eğitiminin **Docker** bölümünde yazdığım analiz projesini içerir. Amaç, Python analiz betiklerini konteyner içinde çalıştırmak — yani "benim bilgisayarımda çalışıyordu" probleminden kurtulmak.

## 🎯 Proje Ne Yapıyor?

100 öğrencilik bir not tablosunu üç ayrı analizden geçiriyor. Her analiz **kendi Docker servisi** olarak tanımlı ve `docker compose` ile tek komutla çalıştırılabiliyor.

| Servis | Betik | Görevi | Çıktısı |
|---|---|---|---|
| `basic_istatistic` | `basic_statistic.py` | Her dersin min / maks / ortalama / medyan / std / varyans / çeyrek değerleri | `ders_istatistikleri.xlsx` |
| `correlation_analysis` | `correlation_analysis.py` | Dersler arası ve ortalama–katılım–devamsızlık korelasyonları | ekrana yazdırır |
| `performance_segmentation` | `performance_segmentation.py` | Öğrencileri seviye ve duruma göre gruplama | `seviye_dagilimi.xlsx`, `durum_seviye_dagilimi.xlsx` |

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `Dockerfile` | Konteyner tarifi: Python 3.12-slim, bağımlılık kurulumu, dosyaların kopyalanması |
| `docker-compose.yml` | Üç servisin tanımı — hepsi aynı imajı kullanır, farklı komut çalıştırır |
| `requirements.txt` | pandas, numpy, scikit-learn, openpyxl |
| `basic_statistic.py` | Ders bazlı betimleyici istatistikler |
| `correlation_analysis.py` | Korelasyon analizi |
| `performance_segmentation.py` | Seviye ve durum segmentasyonu |

> **Not:** Girdi verisi `student_data.xlsx` (100 öğrenci × 15 sütun: altı ders notu, katılım, devamsızlık, ortalama, durum, seviye) eğitim kapsamında sağlandığı için bu repoda yer almıyor. Betikleri çalıştırmak için bu dosyanın aynı klasörde bulunması gerekir. Betiklerin ürettiği Excel çıktıları da repoya dahil edilmedi — çalıştırıldığında yeniden oluşurlar.

## 🐳 Docker Tarafı — Ne Öğrendim

**Dockerfile** bir tarif dosyası: hangi Python sürümü, hangi kütüphaneler, hangi dosyalar. Bu tarifle oluşan imaj her makinede aynı şekilde çalışır.

```dockerfile
FROM python:3.12-slim        # temel imaj
WORKDIR /app                 # konteyner içindeki çalışma klasörü
COPY requirements.txt .      # önce bağımlılıklar
RUN pip install --no-cache-dir -r requirements.txt
COPY *.xlsx .                # sonra veri ve kod
COPY *.py .
```

Bağımlılıkların koddan **önce** kopyalanması bilinçli: Docker her adımı katman olarak önbelleğe alır, böylece kod değiştiğinde kütüphaneler yeniden kurulmaz, imaj çok daha hızlı yeniden inşa edilir.

**docker-compose.yml** birden fazla servisi tek dosyada tanımlar. Üç servis de aynı imajdan (`build: .`) doğar ama farklı `command` çalıştırır. `volumes: - .:/app` satırı klasörü konteynere bağlar — böylece üretilen Excel dosyaları konteyner kapandığında kaybolmaz, bilgisayarda kalır.

## ▶️ Çalıştırma

```bash
docker compose up --build              # üç servisi birden çalıştır
docker compose run basic_istatistic    # sadece birini çalıştır
```

## 📊 Analizlerden Çıkan Sonuçlar

**Ders istatistikleri:** En yüksek ortalama Bilgisayar'da (75.95), en düşük Matematik'te (69.07). Bilgisayar aynı zamanda en düşük standart sapmaya sahip (13.84) — öğrenciler bu derste birbirine en yakın notları almış.

**Korelasyonlar:** Dersler arası korelasyonların tamamı ±0.12 aralığında, yani neredeyse sıfır. Bir dersten iyi not almak diğerini yordamıyor — veri rastgele üretildiği için beklenen bir sonuç.

**Segmentasyon:** C-İyi 49, D-Orta 37, B-Çok İyi 12, F-Zayıf 2 öğrenci. Çapraz tablo, "Durum" alanının doğrudan seviyeden türetildiğini gösteriyor: Başarılı sayılan 61 öğrencinin tamamı B veya C'de, Yetersiz olan 39'unun tamamı D veya F'te.

Seviye ortalamaları da tutarlı bir örüntü çiziyor: F seviyesindeki öğrencilerin katılımı belirgin şekilde düşük (47.5, diğer gruplarda ~70) ve devamsızlığı yüksek (14.5, diğerlerinde ~9).

## 🔧 Düzeltilen Hatalar

Çalışmayı gözden geçirirken bulduğum ve düzelttiğim iki hata:

**1. `performance_segmentation.py`, `basic_statistic.py`'nin kopyasıydı.** Dosya adı segmentasyon diyordu ama içerik istatistik hesaplıyor ve `ders_istatistikleri.xlsx`'i yeniden yazıyordu. Yeniden yazıldı: artık `value_counts()` ile seviye dağılımını, `pd.crosstab()` ile durum–seviye çapraz tablosunu ve `groupby()` ile seviye bazlı ortalamaları hesaplıyor.

**2. `correlation_analysis.py`'de girinti hatası vardı.** `print` satırları ve `correlationS.append(...)` döngülerin **dışında** kalmıştı, bu yüzden sadece son yineleme çalışıyor, 15 ders çifti yerine tek satır yazdırılıyor ve o da hatalı etiketleniyordu ("Bilgisayar and Bilgisayar"). Girintiler düzeltildi; artık tüm çiftler korelasyon büyüklüğüne göre sıralı listeleniyor. Python'da bir seviye boşluğun tüm çıktıyı değiştirebileceğinin iyi bir örneği.
