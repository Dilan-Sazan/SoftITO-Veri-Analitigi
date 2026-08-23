# CNN & YOLO Pratiği: Kedi mi, Köpek mi? 🐱🐶

Bu klasör, **CNN ve YOLO** dersindeki iş akışının kendi veri setime uygulandığı kişisel pratik çalışmamı içerir. Derste hazır CIFAR-10 veri seti kullanılmıştı; burada **kendi görüntü dosyalarımla** (500 kedi + 500 köpek fotoğrafı) sıfırdan bir ikili görüntü sınıflandırma problemi çözüyorum.

## ❓ Araştırma Sorusu

> 1.000 fotoğraflık küçük bir veri setiyle kedi/köpek ayırt eden bir model eğitilebilir mi? Sıfırdan kurulan bir CNN mi daha iyi sonuç verir, yoksa transfer öğrenme mi?

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `cnn_kedi_kopek_colab.ipynb` | Colab'da (T4 GPU) çalıştırılmış pratik — tüm çıktılar ve grafikler içinde |
| `kedi_kopek_veri.zip` | Veri seti: `cats_set/` (500 jpg) + `dogs_set/` (500 jpg), değişken boyutlu RGB fotoğraflar |

## ⚠️ Çalıştırma Notu

Derin öğrenme GPU gerektirir. Bu notebook Google Colab'da T4 GPU ile çalıştırıldı; çıktılar ve grafikler içinde.

Yeniden çalıştırmak için: `kedi_kopek_veri.zip` dosyasını Colab'a yükle (sol paneldeki dosya simgesinden) → **Çalışma zamanı → Türü değiştir → GPU (T4)** → hücreleri sırayla çalıştır.

## 🔄 Dersten Farkı

| | Ders (CIFAR-10) | Bu Pratik (Kedi/Köpek) |
|---|---|---|
| Veri kaynağı | `keras.datasets` ile tek satırda hazır | Kendi JPEG dosyalarım, klasör yapısından okunuyor |
| Görüntü boyutu | Sabit 32×32 | Değişken (~500×400), 160×160'a yeniden boyutlandırılıyor |
| Veri miktarı | 50.000 görüntü | 1.000 görüntü ⟵ transfer öğrenmenin neden var olduğunu gösteren senaryo |
| Sınıf sayısı | 10 (softmax, categorical_crossentropy) | 2 (sigmoid, binary_crossentropy) |
| Augmentasyon | `ImageDataGenerator` | Modern Keras augmentasyon **katmanları** (modelin içinde, GPU'da çalışır) |
| YOLO | Hazır örnek görüntüde | Kendi kedi/köpek fotoğraflarımda + 60 görüntüde başarı ölçümü |

## 🛠️ Notebook'un Adımları

**Hazırlık:** Kütüphaneler, GPU kontrolü, zip açma

**Bölüm 2 — Veri:** `image_dataset_from_directory` ile %80/%20 eğitim-doğrulama hattı, örnek görüntülerin gösterimi, sınıf dengesi kontrolü, `cache`/`prefetch` ile performans ayarı

**Bölüm 2.4 — Augmentasyon:** RandomFlip, RandomRotation, RandomZoom, RandomContrast katmanları — aynı görüntünün 8 farklı varyasyonu görselleştirilerek etkisi gösteriliyor

**Bölüm 3 — Sıfırdan CNN:** 4 adet Conv2D + MaxPooling bloğu, Dropout(0.5), sigmoid çıkış; EarlyStopping ile eğitim; accuracy/loss eğrileri; confusion matrix ve classification report

**Bölüm 4 — Transfer Learning:** ImageNet'te eğitilmiş MobileNetV2'nin dondurulmuş katmanları + GlobalAveragePooling + tek nöronlu sınıflandırıcı

**Bölüm 5 — Karşılaştırma:** İki modelin doğruluk/kayıp/epoch/parametre tablosu, bar grafik, **yanlış sınıflandırılan görüntülerin görselleştirilmesi** (modelin nerede zorlandığını görmek)

**Bölüm 6 — YOLO:** Ultralytics YOLOv8n ile kendi fotoğraflarımda nesne tespiti (kutu çizimi + güven skoru) ve 60 görüntülük başarı ölçümü

**Bölüm 7 — Kaydetme:** Modeli `.keras` formatında kaydetme

## 📌 Sonuçlar

| Model | Test Doğruluğu | Eğitim Süresi |
|---|---|---|
| Sıfırdan CNN (augmentasyonsuz) | **%52** | 11 sn |
| Sıfırdan CNN (augmentasyonlu) | **~%62** | 39 sn |
| **Transfer Learning (MobileNetV2)** | **%89** | 15 epoch |

### ⭐ Asıl Ders: Sıfırdan CNN Neden Çöktü?

Augmentasyonsuz CNN'in eğitim doğruluğu %84'e çıkarken doğrulama doğruluğu %48'de kaldı — yani model **ezberledi (overfitting)**, öğrenmedi. Sınıflandırma raporu bunu çok net gösteriyor:

- Kedi: recall %98 — neredeyse her şeye "kedi" diyor
- Köpek: recall %6 — köpeklerin %94'ünü kaçırıyor

Yani model gerçekte bir şey öğrenmemiş, çoğunluk tahminine kaçmış. %52'lik doğruluk yazı-tura atmakla aynı. Sebebi: **800 eğitim görüntüsü, 64×64 çözünürlükte, sıfırdan bir CNN'i eğitmek için çok az.**

Augmentasyon (döndürme, kaydırma, çevirme, yakınlaştırma) eklendiğinde doğruluk %62'ye çıktı — iyileşme var ama hâlâ yetersiz.

**Transfer öğrenme ise %89'a ulaştı.** ImageNet'in 1,4 milyon görüntüden öğrendiği görsel özellikler ödünç alınınca, aynı 800 görüntü yeterli hale geldi. Bu, "az veri varsa transfer öğrenme" ilkesinin en net kanıtı.

## 💡 Öğrenmeler

- **Az veri = transfer öğrenme:** 800 eğitim görüntüsüyle sıfırdan "kenar, doku, göz, kulak" öğrenmek zor; ImageNet'in 1,4 milyon görüntüden öğrendiği özellikleri ödünç almak çok daha etkili
- **Augmentasyon, veri çoğaltmanın bedava yolu:** her epoch'ta aynı fotoğraf farklı görünür
- **EarlyStopping** hem zaman kazandırır hem ezberlemeyi engeller
- **CNN vs YOLO farkı:** CNN "bu görüntüde ne var?" sorusunu yanıtlar, YOLO "nerede ve kaç tane var?" sorusunu da yanıtlar
- **Yanlış tahminlere bakmak**, tek bir doğruluk sayısından daha öğreticidir

## 🎯 Sonraki Adım Fikirleri

Fine-tuning (MobileNetV2'nin üst katmanlarını düşük öğrenme oranıyla açmak) • Grad-CAM ile modelin görüntünün neresine baktığını görselleştirmek • kendi verimle YOLO eğitmek (kutu etiketlemesi gerektirir)
