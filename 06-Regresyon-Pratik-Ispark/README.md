# Regresyon Pratiği: İSPARK Verisiyle İki Yeni Hipotez 🚗

Bu klasör, **Basit Doğrusal Regresyon** dersinde öğrenilen yöntemlerin **kendi kurduğum iki yeni hipoteze** uygulandığı kişisel pratik çalışmamı içerir. Dersteki soruyu tekrarlamak yerine, aynı teknikleri farklı sorulara uygulayarak pekiştirdim — üstelik ikinci hipotezde dersin bir adım ötesine geçip **sürekli değişkenli** regresyon denedim.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `ispark_regresyon_pratik.ipynb` | İki hipotezin sıfırdan regresyonla test edildiği pratik notebook (tüm çıktı ve grafiklerle) |
| `ispark_parking.csv` | İSPARK otopark verisi (708 park noktası, 9 sütun) |

## 📊 Veri Seti Hakkında

İstanbul Büyükşehir Belediyesi'ne bağlı İSPARK otoparklarının verisi. Her satır bir park noktasıdır:
park adı, tipi (yol üstü / açık otopark / kapalı otopark / taksi / minibüs), kapasitesi, çalışma saatleri, ilçesi ve koordinatları.

⚠️ Veride **gizli hatalar** vardır (derste öğrendiğimiz gibi): 4 satırda koordinatlar -99 sentinel değeriyle doldurulmuş, 1 satırda kapasite 0. Pratik bu temizlikle başlar.

## 🔬 Test Edilen Hipotezler

### Hipotez 1: "7/24 açık parklar daha mı büyük?" *(dummy değişkenli — dersteki teknik)*
`WORKING_TIME` sütunundan `IS_24H` (0/1) dummy değişkeni türetildi.

**Sonuç:** ŷ = 104.2 + 304.2·x → 7/24 açık parklar ortalama **304 araç daha büyük**. p-değeri ≈ 10⁻¹⁴ (kesinlikle anlamlı) ama **R² ≈ 0.08** (zayıf tahminci). Dersteki "anlamlılık ≠ tahmin gücü" mesajının kendi hipotezimde birebir tekrarı!

### Hipotez 2: "İlçedeki park sayısı, ilçenin toplam kapasitesini tahmin eder mi?" *(sürekli değişkenli — dersin bir adım ötesi)*
`groupby` ile 34 ilçelik özet tablo kuruldu; x = ilçedeki park noktası sayısı, y = ilçenin toplam kapasitesi.

**Sonuç:** Toplam_Kapasite = 1785 + **101.8**·Park_Sayısı → her yeni park noktası ilçe kapasitesine ortalama ~102 araç ekliyor. **R² ≈ 0.37** — H1'den 4-5 kat güçlü bir model, ama varyansın çoğu hâlâ modelde olmayan faktörlerde (ilçe büyüklüğü, ticari yoğunluk vb.).

## 🛠️ Uygulanan Teknikler

| Teknik | Nerede |
|---|---|
| Sentinel değer (-99) ve mantıksal hata (kapasite=0) temizliği | Bölüm 1 |
| Dummy (0/1) değişken oluşturma | Hipotez 1 |
| b0 ve b1'i en küçük kareler formülüyle **elle** hesaplama | Her iki hipotez |
| R²'yi elle hesaplama (ss_res / ss_tot) | Her iki hipotez |
| `scipy.stats.linregress` ile doğrulama ✓ | Her iki hipotez |
| `groupby` + `agg` ile gözlem birimi dönüştürme (park → ilçe) | Hipotez 2 |
| Regresyon doğrusu + artık (residual) grafiği | Bölüm 4 |
| İki modelin tablo halinde karşılaştırılması | Bölüm 5 |

## 📌 Öne Çıkan Bulgular ve Dersler

- Her iki hipotez de **istatistiksel olarak anlamlı**, ama açıklama güçleri çok farklı (R²: 0.08 vs 0.37) — p-değeri ile R²'nin neden ayrı ayrı rapor edilmesi gerektiğini kendi analizimde gördüm
- Fatih, hem park sayısında hem toplam kapasitede açık ara lider; regresyon doğrusunun bile üzerinde
- Artık grafiğinde tahminler büyüdükçe saçılımın arttığı gözlendi (heteroskedastisite ön izlemesi) → basit regresyonun sınırları
- **Sonraki hedef:** ilçe + park tipini birlikte modele katan çoklu doğrusal regresyon

## 🔗 İlgili Ders

Bu pratiğin dayandığı ders notebook'u için:
👉 [`05-Regresyon-Ders`](../05-Regresyon-Ders) klasörüne bakabilirsiniz.
