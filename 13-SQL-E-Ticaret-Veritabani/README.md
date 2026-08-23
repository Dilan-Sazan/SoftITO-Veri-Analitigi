# SQL: E-Ticaret Veritabanı ve Sorgu Ödevi 🗄️

Bu klasör, SoftİTO Veri Analistliği eğitiminin **SQL** bölümünde hazırladığım ödevi içerir: sıfırdan bir e-ticaret veritabanı tasarımı, örnek verilerle doldurulması ve **38 analiz sorusunun** sorgularla cevaplanması.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `eticaret_veritabani.sql` | Tam betik: tablo tanımları + örnek veriler + 38 soru ve çözümleri |

**Veritabanı:** PostgreSQL (`SERIAL`, `::date` cast, `INTERVAL` gibi PostgreSQL sözdizimi kullanılmış)

Çalıştırmak için: PostgreSQL'de boş bir veritabanı oluşturup dosyayı baştan sona çalıştırmak yeterli — tablolar kurulur, veriler yüklenir, ardından sorgular sırayla incelenebilir.

## 🗂️ Veritabanı Şeması — 13 Tablo

| Tablo | İçerik |
|---|---|
| `kategoriler` | Ürün kategorileri |
| `saticilar` | Satıcı bilgileri, şehir, puan, durum |
| `musteriler` | Müşteri bilgileri, üyelik tipi, toplam harcama |
| `urunler` | Ürün kataloğu, fiyat, stok, puan |
| `siparisler` | Sipariş başlıkları, tutar, durum |
| `siparis_detaylari` | Sipariş satırları (hangi üründen kaç adet) |
| `odemeler` | Ödeme kayıtları |
| `kargo_sirketleri` | Kargo firmaları |
| `kargo_tracking` | Kargo takip kayıtları |
| `yorumlar` | Ürün yorumları ve puanları |
| `promosyonlar` | Promosyon kodları |
| `favoriler` | Müşteri favori listeleri |
| `indirimler` | Ürün bazlı indirim kayıtları |

### Tasarımda Kullanılan Kısıtlar

- **PRIMARY KEY / FOREIGN KEY** ile tablolar arası bütünlük (ör. `siparis_detaylari` hem `siparisler` hem `urunler`e bağlı)
- **CHECK** kısıtları ile geçerli değer kümesi zorlaması (`durum IN ('Aktif','Pasif','Beklemede')`, üyelik tipleri, kargo durumları)
- **UNIQUE** kısıtları (e-posta, takip numarası)
- **DEFAULT** değerler ve `ON DELETE CASCADE` davranışı
- `DECIMAL(15,2)` ile para alanlarında hassasiyet

## 📝 38 Soru — Zorluk Sırasına Göre

**Temel sorgular (1–10):** `SELECT`, `WHERE`, `ORDER BY`, `IN`, karşılaştırma operatörleri
> Örnek: 50.000 TL üzeri ürünler, belirli tarihten sonraki siparişler, puanı 4.5+ olan ürünler

**Toplulaştırma ve gruplama (11–22):** `COUNT`, `SUM`, `AVG`, `GROUP BY`, `LIMIT`
> Örnek: her kategorideki ürün sayısı, en çok satan 5 ürün, her satıcının sattığı toplam adet

**JOIN'ler (23–32):** `INNER JOIN`, `LEFT JOIN`, çoklu tablo birleştirme
> Örnek: bir müşterinin aldığı ürünler + kargo durumu + harcama (4 tablo birleştirme), en yüksek cirolu 5 satıcı

**İleri seviye (33–38):** alt sorgular (subquery), korelasyonlu alt sorgu, tarih aralığı hesapları
> Örnek: kendi kategorisinin ortalamasından pahalı ürünler (korelasyonlu subquery), son 3 aydaki sipariş ortalaması (`INTERVAL '3 months'`), en çok harcayan 3 müşterinin aldığı ürünler

## 💡 Bu Ödevde Öğrendiklerim

- **Veritabanı tasarımı**, sorgu yazmaktan önce gelir: doğru kurulmuş foreign key'ler sayesinde 4 tablolu JOIN'ler tek satırda yazılabiliyor
- **CHECK kısıtları**, hatalı verinin daha tabloya girmesini engelliyor — Python tarafında `dropna()` ile uğraştığımız kirli verilerin kaynağında çözümü bu
- **Korelasyonlu alt sorgu** (her ürünü kendi kategorisinin ortalamasıyla karşılaştırma) en çok zorlandığım ama en öğretici kısım oldu
- `siparis_tarihi::date` gibi PostgreSQL cast'leri ve `INTERVAL` ile tarih aritmetiği

## 🔍 Gözden Geçirme Notları

Kendi ödevimi tekrar okuduğumda fark ettiğim iki nokta (öğrenme kaydı olarak burada tutuyorum):

1. **`kargo_tracking` tablosu iki kez tanımlanmış** (satır 108 ve 120) — betiği baştan çalıştırırken ikinci `CREATE TABLE` "already exists" hatası verir. Tekrarlanan bloğun silinmesi gerekiyor.
2. **29. sorunun cevabı soruyla eşleşmiyor:** soru müşteri bazlı sipariş sayısı ve harcamayı istiyor, ancak yazılan sorgu kategori bazlı ürün istatistiği döndürüyor (30. sorunun cevabına benziyor). Doğrusu `musteriler` ve `siparisler` tablolarını birleştirip `GROUP BY m.ad_soyad` ile toplam harcamaya göre sıralamak olurdu.
