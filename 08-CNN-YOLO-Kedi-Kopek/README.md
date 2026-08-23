# CNN & YOLO Pratiği: Kedi mi, Köpek mi? 🐱🐶

Bu klasör, **CNN ve YOLO** dersindeki iş akışının kendi veri setime uygulandığı kişisel pratik çalışmamı içerir. Derste hazır CIFAR-10 veri seti kullanılmıştı; burada **kendi görüntü dosyalarımla** (500 kedi + 500 köpek fotoğrafı) sıfırdan bir ikili görüntü sınıflandırma problemi çözüyorum.

## ❓ Araştırma Sorusu

> 1.000 fotoğraflık küçük bir veri setiyle kedi/köpek ayırt eden bir model eğitilebilir mi? Sıfırdan kurulan bir CNN mi daha iyi sonuç verir, yoksa transfer öğrenme mi?

## 📄 Dosyalar

| Dosya | Açıklama |
|---|---|
| `cnn_kedi_kopek_pratik.ipynb` | Uçtan uca pratik: veri hattı → augmentasyon → CNN → transfer learning → YOLO |
| `kedi_kopek_veri.zip` | Veri seti: `cats_set/` (500 jpg) + `dogs_set/` (500 jpg), değişken boyutlu RGB fotoğraflar |

## ⚠️ Çalıştırma Notu (Önemli)

Bu notebook **Google Colab için** yazıldı ve GPU gerektirir — önceki pratiklerden farklı olarak çıktıları içine gömülü değil, çünkü derin öğrenme modellerinin eğitimi CPU'da saatler sürer.

Çalıştırmak için:
1. `kedi_kopek_veri.zip` dosyasını Colab'a yükle (sol paneldeki dosya simgesinden)
2. Notebook'u Colab'da aç → **Çalışma zamanı → Çalışma zamanı türünü değiştir → GPU (T4)**
3. Hücreleri sırayla çalıştır

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

## 💡 Beklenen Öğrenmeler

- **Az veri = transfer öğrenme:** 800 eğitim görüntüsüyle sıfırdan "kenar, doku, göz, kulak" öğrenmek zor; ImageNet'in 1,4 milyon görüntüden öğrendiği özellikleri ödünç almak çok daha etkili
- **Augmentasyon, veri çoğaltmanın bedava yolu:** her epoch'ta aynı fotoğraf farklı görünür
- **EarlyStopping** hem zaman kazandırır hem ezberlemeyi engeller
- **CNN vs YOLO farkı:** CNN "bu görüntüde ne var?" sorusunu yanıtlar, YOLO "nerede ve kaç tane var?" sorusunu da yanıtlar
- **Yanlış tahminlere bakmak**, tek bir doğruluk sayısından daha öğreticidir

## 🎯 Sonraki Adım Fikirleri

Fine-tuning (MobileNetV2'nin üst katmanlarını düşük öğrenme oranıyla açmak) • Grad-CAM ile modelin görüntünün neresine baktığını görselleştirmek • kendi verimle YOLO eğitmek (kutu etiketlemesi gerektirir)
