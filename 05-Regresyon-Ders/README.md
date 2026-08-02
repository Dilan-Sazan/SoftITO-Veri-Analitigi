# Basit Doğrusal Regresyon — İSPARK Verisiyle (Ders Çalışması) 📘

Bu klasör, SoftİTO Veri Analistliği eğitiminde **derste işlenen** regresyon notebook'unu içerir. Notebook, eğitmenimiz tarafından hazırlanmış olup İstanbul'daki İSPARK otoparklarının gerçek verisi üzerinden basit doğrusal regresyonu **hiçbir hazır regresyon kütüphanesi kullanmadan, formülünden başlayarak** anlatır.

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `ispark_regresyon_analizi.ipynb` | Basit doğrusal regresyonu sıfırdan anlatan ders notebook'u |
| `ispark_parking.csv` | İSPARK otopark verisi (708 park noktası) — notebook'un çalışması için gereklidir |

## ❓ Dersin Araştırma Sorusu

> Bir park noktasının "gerçek otopark alanı" (açık/kapalı otopark) olması ile "yol üstü / taksi / minibüs parkı" olması, park **kapasitesini** ne kadar açıklar?

## 📚 İçindekiler ve Öğretilen Kavramlar

1. **Regresyonun temel mantığı** — ŷ = b0 + b1·x denklemi; b0 (sabit) ve b1 (eğim) katsayılarının anlamı
2. **En Küçük Kareler (Least Squares) yöntemi** — en iyi uyan doğruyu bulan formüllerin matematiği
3. **Veri keşfi ve gizli hata temizliği** — `isnull()` sıfır gösterse bile verinin temiz olmayabileceği; koordinatlardaki **-99 sentinel (yer tutucu) değerlerinin** tespiti ve temizlenmesi
4. **Dummy (gösterge) değişken** — kategorik bir sütunu (park tipi) 0/1 koduyla regresyona sokma tekniği
5. **Katsayıları elle hesaplama** — b0 ve b1'in NumPy ile formülden hesaplanması ve yorumlanması
6. **R² (belirlilik katsayısı)** — modelin açıklama gücünün ölçülmesi (derste R² ≈ 0.13 çıkar ve bunun *neden düşük olduğu* tartışılır)
7. **scipy ile doğrulama** — elle hesaplanan sonuçların `stats.linregress` ile birebir örtüştüğünün gösterilmesi
8. **p-değeri vs R² ayrımı** — ⭐ dersin en önemli mesajı: *ilişkinin istatistiksel olarak anlamlı olması (p ≈ 10⁻²³), modelin güçlü bir tahminci olduğu anlamına gelmez*
9. **Görselleştirme** — regresyon doğrusu grafiği ve artık (residual) grafiği; artıkların geniş saçılımının düşük R²'nin görsel karşılığı olduğu

## 💡 Dersten Akılda Kalması Gerekenler

- Kategorik değişkenler dummy kodlanmadan regresyona giremez
- x'in yalnızca 0/1 aldığı regresyon, aslında iki grubun ortalamasını karşılaştırır
- **Anlamlılık ≠ tahmin gücü** — p-değeri ve R² farklı soruları cevaplar
- Gerçek veride tek değişken genelde yetmez → sonraki konu: **çoklu regresyon**

## 🔗 İlgili Pratik

Bu derste öğrenilen yöntemlerin iki yeni hipoteze uygulandığı pratik çalışma için:
👉 [`06-Regresyon-Pratik-Ispark`](../06-Regresyon-Pratik-Ispark) klasörüne bakabilirsiniz.
