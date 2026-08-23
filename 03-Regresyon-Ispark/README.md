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

---

## 📓 Notebook Adım Adım — `ispark_regresyon_pratik.ipynb`

Notebook'un kendisinde yalnızca kod bulunur; her adımın açıklaması burada.

#### 1. Veriyi Yükleme ve Temizleme

Derste öğrendiğimiz kritik noktayı unutmuyoruz: bu veri setinde eksik koordinatlar NaN değil,
**-99 sentinel değeriyle** gizlenmiş durumda. Regresyondan önce temizliyoruz.

#### 2. Hipotez 1: 7/24 Açık Parklar Daha mı Büyük?

**Mantık:** 7/24 hizmet veren parklar genelde büyük yatırımlı otoparklardır; yol üstü parklar ise
çoğunlukla gündüz saatleriyle sınırlıdır. O halde çalışma süresi ile kapasite arasında ilişki bekleriz.

`WORKING_TIME` kategorik bir sütun → derste öğrendiğimiz gibi **dummy (0/1) değişkene** çeviriyoruz.

**Hipotez 1'in yorumu:**

- **b0** → kısıtlı saatlerde çalışan parkların ortalama kapasitesi (~b0 araç)
- **b1** → park 7/24 açıksa kapasite ortalama b1 araç daha fazla
- **p-değeri** çok küçük → ilişki tesadüf değil, istatistiksel olarak anlamlı ✓
- Ama **R² düşük** → derste öğrendiğimiz kritik ayrım burada da geçerli: *anlamlı olmak ≠ güçlü tahminci olmak*.
  Çalışma saati tek başına kapasite farklılığının küçük bir kısmını açıklıyor.

#### 3. Hipotez 2: İlçedeki Park Sayısı → İlçenin Toplam Kapasitesi

Şimdi dersten bir adım öteye gidiyoruz. Dersteki x değişkeni sadece 0/1 alabiliyordu;
burada x **gerçek bir sürekli sayı**: ilçedeki park noktası sayısı.

**Mantık:** Bir ilçede ne kadar çok İSPARK noktası varsa, toplam araç kapasitesi de o kadar
yüksek olmalı. Peki her ek park noktası, ilçe kapasitesine ortalama kaç araç ekliyor?
Regresyonun b1 katsayısı tam olarak bu soruyu cevaplar!

**Hipotez 2'nin yorumu:**

- **b1 ≈ her ek park noktasının ilçe kapasitesine ortalama kattığı araç sayısı**
- **R² ≈ 0.37** → park sayısı, ilçeler arası kapasite farklılığının yaklaşık %37'sini açıklıyor.
  H1'in R²'sinden (≈0.08) 4-5 kat güçlü bir model; yine de varyansın çoğu başka faktörlerde
  (ilçenin yüzölçümü, otopark tiplerinin dağılımı, ticari yoğunluk gibi)
- Dersteki 0/1 regresyonu "iki grup ortalaması karşılaştırması" idi; burada gerçek bir
  **doğru uydurma** görüyoruz — regresyonun asıl klasik kullanımı budur.

#### 4. Görselleştirme

Her iki modeli de dersteki gibi görselleştiriyoruz: solda regresyon doğrusu, sağda artık (residual) grafiği.

**Grafiklerin okunması:**

- **Solda:** İlçeler kırmızı doğrunun etrafında toplanmış — doğrusal ilişki net şekilde görülüyor.
  Fatih gibi park sayısı çok yüksek ilçeler doğrunun üzerinde: beklenenden bile fazla kapasiteye sahip.
- **Sağda:** Artıklar 0 çizgisinin etrafına dağılmış; ancak tahmin büyüdükçe artıkların saçılımının
  da büyüdüğü görülüyor. Bu, ileride öğreneceğimiz "değişen varyans (heteroskedastisite)" konusuna
  bir ön bakış — basit regresyonun her zaman yeterli olmadığının işareti.

#### 5. İki Modelin Karşılaştırması

#### Özet — Bu Pratikte Öğrendiklerim

1. **Sentinel değer temizliği:** -99 koordinatlar ve 0 kapasite gibi "gizli" hatalar regresyondan önce ayıklandı
2. **Dummy değişken tekniği** yeni bir hipoteze uygulandı (7/24 açık olma → kapasite)
3. **Sürekli değişkenli regresyon** ilk kez uygulandı (park sayısı → toplam kapasite) — dersteki 0/1
   örneğinden bir adım öteye geçildi
4. Her iki modelde katsayılar **elle hesaplanıp scipy ile doğrulandı** ✓
5. **R² ile p-değerinin farkı** somut olarak görüldü: her iki model de istatistiksel olarak anlamlı (p çok küçük), ama açıklama gücü çok farklı (R²: 0.08 vs 0.37)
6. Artık grafiğinde **saçılımın büyümesi** gözlemlendi → çoklu regresyon ve varsayım kontrollerine geçiş için motivasyon

**Bir sonraki adım:** İlçeye ek olarak park tipini de modele katmak → **çoklu doğrusal regresyon**
