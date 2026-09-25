# Traveling Salesperson Problem (TSP) Solver using Simulated Annealing 🌍

🇬🇧 **[English](#english)** | 🇹🇷 **[Türkçe](#türkçe)**

---

## English

This repository contains a Python-based solver for the **Traveling Salesperson Problem (TSP)** utilizing the **Simulated Annealing (SA)** algorithm. The project is designed to calculate the shortest possible route connecting a given set of 2D coordinates within a strict time limit.

### Core Mechanics
Unlike standard SA implementations that rely on fixed iteration-based cooling, this solver uses a **Time-Based Exponential Cooling** schedule. The temperature smoothly decays from the initial exploration phase down to the final exploitation phase, perfectly synced with the user-defined time limit. Neighborhood generation is handled via fast delta-cost **2-Opt** inversions to efficiently uncross route segments.

### Features
*   **Dynamic Cooling:** Temperature automatically adjusts based on elapsed execution time, preventing early stagnation (freezing).
*   **Robust Data Handling:** Automatically parses and cleans `.csv` or `.txt` coordinate files, ignoring headers or corrupted text rows.
*   **Optimized Performance:** Fast Euclidean distance matrix calculations and delta-evaluations using `numpy` and `pandas`.

### Installation
Ensure you have the required Python libraries installed:
```bash
pip install numpy pandas
```

### Usage
1. Place your city coordinates in a file named `coordinates.csv` in the root directory. The file should contain `ID`, `X`, and `Y` values (separated by commas, spaces, or tabs).
2. Run the optimization script:
```bash
python path.py
```
3. The script will output live temperature drops, intermediate best costs, and the final shortest route sequence to the terminal.

---

## Türkçe

Bu depo, **Gezgin Satıcı Problemi (TSP)** için **Benzetimli Tavlama (Simulated Annealing - SA)** algoritmasını kullanan Python tabanlı bir çözümleyici içerir. Proje, verilen 2 boyutlu koordinat setini birbirine bağlayan en kısa rotayı, belirlenen kesin süre sınırı içinde hesaplamak üzere tasarlanmıştır.

### Temel Çalışma Mantığı
Sabit iterasyona dayalı soğutma kullanan standart SA uygulamalarının aksine, bu çözümleyici **Zamana Bağlı Üstel Soğutma (Time-Based Exponential Cooling)** programı kullanır. Sıcaklık, kullanıcının belirlediği süre sınırı ile tam senkronize olarak, ilk keşif aşamasından son sömürü aşamasına kadar pürüzsüz bir şekilde düşer. Komşuluk üretimi (yeni rota denemeleri), kesişen yolları verimli bir şekilde açmak için hızlı delta-maliyet **2-Opt** ters çevirme hamleleriyle gerçekleştirilir.

### Özellikler
*   **Dinamik Soğutma:** Sıcaklık, geçen çalışma süresine göre otomatik olarak ayarlanarak algoritmanın erken donmasını (yerel çukurlara saplanmasını) engeller.
*   **Güçlü Veri İşleme:** `.csv` veya `.txt` koordinat dosyalarını başlıkları veya bozuk metin satırlarını yok sayarak otomatik olarak temizler ve işler.
*   **Optimize Edilmiş Performans:** `numpy` ve `pandas` kullanarak hızlı Öklid mesafe matrisi hesaplamaları ve delta değerlendirmeleri sunar.

### Kurulum
Gerekli Python kütüphanelerinin yüklü olduğundan emin olun:
```bash
pip install numpy pandas
```

### Kullanım
1. Şehir koordinatlarınızı ana dizindeki `coordinates.csv` adlı dosyaya yerleştirin. Dosya `ID`, `X` ve `Y` değerlerini içermelidir (virgül, boşluk veya sekme ile ayrılmış olabilir).
2. Optimizasyon kodunu çalıştırın:
```bash
python path.py
```
3. Program terminalde anlık sıcaklık düşüşlerini, ara iyileştirmeleri ve bulunan en kısa rotanın son şehir sıralamasını canlı olarak çıktı verecektir.
