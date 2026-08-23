# SoftİTO Veri Analistliği — Pratik Çalışmalarım 📊

Bu repo, SoftİTO Veri Analistliği eğitimi boyunca öğrendiğim konuları **kendi seçtiğim veri setleri üzerinde uyguladığım pratik çalışmaları** içerir. Her çalışma kendi klasöründe; kendi README dosyası, notebook'u ve veri setiyle birlikte durur.

Notebook'lar çalıştırılmış haldedir — GitHub'da açtığınızda çıktıları ve grafikleri doğrudan görebilirsiniz. (`08` klasöründeki derin öğrenme notebook'u Google Colab'da T4 GPU ile çalıştırılmıştır.)

## 📁 Çalışmalar

| Klasör | Konu | Veri Seti |
|---|---|---|
| [`01-NumPy-Ogrenci-Performans`](01-NumPy-Ogrenci-Performans) | NumPy: array işlemleri, boolean filtreleme, broadcasting, istatistikler | 5.000 öğrencilik performans verisi |
| [`02-Pandas-Dunya-Mutluluk`](02-Pandas-Dunya-Mutluluk) | Pandas temelleri + veri temizleme (5 dağınık dosyanın birleştirilmesi) | Dünya Mutluluk Raporu 2015–2019 |
| [`03-Regresyon-Ispark`](03-Regresyon-Ispark) | Basit doğrusal regresyon: en küçük kareler, dummy değişken, R² vs p-değeri | İSPARK otopark verisi (708 nokta) |
| [`04-Coklu-Regresyon-Mutluluk`](04-Coklu-Regresyon-Mutluluk) | Çoklu regresyon: basit vs çoklu model karşılaştırması (R² 0.62 → 0.72) | Mutluluk verisi (02'nin temiz çıktısı) |
| [`05-Polinom-Regresyon-Ogrenci`](05-Polinom-Regresyon-Ogrenci) | Polinom regresyon: ters-U ilişkisinin yakalanması, K-Fold ile derece seçimi | 1.020 öğrencilik performans verisi |
| [`06-Lojistik-Regresyon-Diyabet`](06-Lojistik-Regresyon-Diyabet) | Sınıflandırma: doğruluk yanılsaması ve sınıf dengesizliğiyle mücadele | CDC BRFSS 2015 (253.680 kişi) |
| [`07-SVM-AI-Isleri`](07-SVM-AI-Isleri) | SVM: kernel karşılaştırması, GridSearchCV, veri sızıntısı tespiti | 90.000 küresel AI iş ilanı |
| [`08-CNN-YOLO-Kedi-Kopek`](08-CNN-YOLO-Kedi-Kopek) | Derin öğrenme: sıfırdan CNN vs transfer learning (MobileNetV2) — %52'ye karşı %89 | 1.000 kedi/köpek fotoğrafı |
| [`09-Random-Forest-Elmas`](09-Random-Forest-Elmas) | Random Forest: aynı veriyle hem regresyon (R² 0.98) hem sınıflandırma (%79), özellik önemleri | 53.940 elmas |
| [`10-Isolation-Forest-Dolandiricilik`](10-Isolation-Forest-Dolandiricilik) | Denetimsiz anomali tespiti: etiketsiz dolandırıcılık yakalama (ROC-AUC 0.92), contamination etkisi | 60.000 kredi kartı işlemi |
| [`11-AdaBoost-XGBoost-Gelir`](11-AdaBoost-XGBoost-Gelir) | Boosting karşılaştırması: XGBoost hem daha doğru (AUC 0.93 vs 0.91) hem 4.5 kat hızlı | 45.000 kişilik nüfus sayımı |
| [`12-PowerBI-Satis-Dashboard`](12-PowerBI-Satis-Dashboard) | Power BI: yıldız şeması, DAX ölçüleri, ABC analizi ve müşteri segmentasyonu dashboard'u | Satış verisi (pbix içinde) |
| [`13-SQL-E-Ticaret-Veritabani`](13-SQL-E-Ticaret-Veritabani) | SQL: 13 tablolu e-ticaret veritabanı tasarımı ve 38 analiz sorgusu (JOIN, GROUP BY, subquery) | Kendi oluşturduğum örnek veri |

## 🔗 Çalışmalar Arası Bağlantı

`02` klasöründe 5 ayrı yıllık dosyayı temizleyip tek veri setine dönüştürdüm; `04` klasöründeki çoklu regresyon modeli tam olarak bu temiz veriyi kullanıyor. Yani repo içinde gerçek bir analist iş akışı zinciri var: **temizle → keşfet → modelle**.

## 🛠️ Kullanılan Araçlar

Python • SQL (PostgreSQL) • Power BI (DAX) • NumPy • pandas • matplotlib • seaborn • scipy • scikit-learn • XGBoost • TensorFlow/Keras • Ultralytics YOLO • Jupyter Notebook / Google Colab

## 💡 Öne Çıkan Öğrenmeler

- **Veri sızıntısı (data leakage):** hedeften türetilmiş sütunları modele koymamak (`Sira`, `experience_years`)
- **Anlamlılık ≠ tahmin gücü:** p-değeri çok küçük olabilir ama R² düşük kalabilir
- **Doğruluk yanılsaması:** dengesiz veride %85 accuracy'li model, riskli hastaların %81'ini kaçırabilir
- **Her aykırı değer hata değildir:** IQR'ın işaretlediği uç değerler bazen tam da aradığımız sinyaldir
- **Karmaşık olan her zaman kazanmaz:** linear kernel, RBF ve polinomu geçebilir
- **Az veri varsa transfer öğrenme:** sıfırdan CNN %52'de kalırken MobileNetV2 %89'a ulaştı
- **Karıştırıcı değişken (confounding):** en iyi kesim elmaslar en ucuz çıktı — çünkü daha küçüklerdi
- **Denetimsiz öğrenme de iş görür:** hiç etiket görmeden dolandırıcılık tespitinde ROC-AUC 0.92
- **Özellik önemi modele göre değişir:** AdaBoost ve XGBoost aynı veride farklı değişkenleri öne çıkardı

---
*SoftİTO Veri Analistliği Eğitimi — 2026*
