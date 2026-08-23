# Power BI: Satış Analizi Dashboard'u 📊

Bu klasör, SoftİTO Veri Analitiği eğitiminin **Power BI** bölümünde hazırladığım satış analizi raporunu içerir. Önceki klasörlerdeki Python çalışmalarından farklı olarak burada iş zekâsı (BI) tarafı var: veri modelleme, DAX ölçüleri ve etkileşimli görselleştirme.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `satis_dashboard.pbix` | Power BI Desktop rapor dosyası (veri modeli + ölçüler + görseller) |

> Açmak için **Power BI Desktop** gerekir ([ücretsiz indirme](https://powerbi.microsoft.com/desktop/)). Dosya veriyi içinde barındırır, ayrıca bir kaynağa bağlanmaya gerek yoktur.

## 🗂️ Veri Modeli

Yıldız şeması (star schema) mantığıyla kurulmuş 7 tablo:

| Tablo | Rolü |
|---|---|
| `Satislar` | **Fact tablosu** — işlem kayıtları |
| `Musteriler` | Boyut — müşteri bilgileri ve segment |
| `Urunler` | Boyut — ürün kataloğu |
| `Magazalar` | Boyut — mağaza bilgileri |
| `Takvim` | Tarih boyutu — zaman bazlı analizler için |
| `Hedefler` | Hedef ciro değerleri |
| `_Olculer` | DAX ölçülerinin toplandığı ayrı tablo |

Ölçülerin `_Olculer` adında ayrı bir tabloda toplanması, model büyüdükçe ölçüleri tek yerden yönetmeyi sağlayan yaygın bir Power BI pratiğidir.

## 📐 Oluşturulan DAX Ölçüleri

- **Toplam Ciro** — temel satış metriği
- **Hedef Ciro** — KPI karşılaştırması için hedef değer
- **Sipariş Sayısı** — işlem adedi
- **Kümülatif Ciro %** — ürünlerin ciroya kümülatif katkısı (ABC analizinin temeli)
- **ABC Sınıfı** — ürünleri ciro katkısına göre A/B/C gruplarına ayıran sınıflandırma

## 📈 Rapor Sayfası — 4 Görsel

**1. Çizgi Grafik — Aylık Ciro Trendi**
`Takvim.YilAy` ekseninde toplam cironun zaman içindeki seyri. Mevsimsellik ve büyüme eğilimini gösterir.

**2. KPI Kartı — Ciro vs Hedef**
Toplam ciroyu hedefle karşılaştırır, arka planda trend çizgisi gösterir. Tek bakışta "hedefin neresindeyiz?" sorusunu yanıtlar.

**3. Tablo — ABC Analizi**
Ürün adı, toplam ciro, kümülatif ciro yüzdesi ve ABC sınıfı. **Pareto (80/20) prensibinin** uygulanmış hali: cironun büyük kısmını üreten az sayıdaki A grubu ürünü ortaya çıkarır. Stok ve satın alma kararlarında kullanılan klasik bir perakende analizidir.

**4. Dağılım Grafiği — Müşteri Segmentasyonu**
X ekseninde sipariş sayısı, Y ekseninde toplam ciro; her nokta bir müşteri, renkler segmenti gösterir. Sağ üst köşedeki müşteriler hem sık alışveriş yapan hem çok harcayan en değerli grup; sağ altta ise sık gelip az harcayanlar görünür.

## 💡 Bu Çalışmada Öğrendiklerim

- **Yıldız şeması kurmak:** fact ve dimension tablolarını ayırıp ilişkilerle bağlamak
- **Ayrı takvim tablosu:** zaman bazlı analizler için Power BI'ın beklediği standart yapı
- **DAX ile hesaplanan ölçüler** — kümülatif yüzde gibi sıralamaya bağlı hesaplar özellikle öğretici
- **ABC analizi**, iş dünyasında en çok kullanılan segmentasyon yöntemlerinden biri
- Aynı analizleri Python'la da yapmak mümkün, ama Power BI'ın farkı **etkileşim**: görsellerden birine tıklayınca diğerleri otomatik filtreleniyor
