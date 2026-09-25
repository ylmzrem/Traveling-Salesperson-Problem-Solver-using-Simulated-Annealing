<div align="center">

# 🌍 Traveling Salesperson Problem (TSP) Solver

### Gezgin Satıcı Problemi Çözümleyici

![Language](https://img.shields.io/badge/Language-Python-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Simulated_Annealing-brightgreen)

*A dynamic, time-based exponential cooling Simulated Annealing optimizer for the Traveling Salesperson Problem.*<br>
*Zaman bazlı üstel soğutma kullanan, dinamik Benzetimli Tavlama tabanlı Gezgin Satıcı Problemi çözümleyicisi.*

[English](#english) | [Türkçe](#türkçe)

</div>

---

## <a id="english"></a> 🇬🇧 English

This repository contains a Python-based solver for the **Traveling Salesperson Problem (TSP)** utilizing the **Simulated Annealing (SA)** algorithm. Unlike standard SA implementations, this solver uses a **Time-Based Exponential Cooling** schedule perfectly synced with a user-defined time limit.

### 🚀 Requirements & Installation
Ensure you have Python installed on your system. Then, install the required libraries:
```bash
pip install numpy pandas
```

### 📁 Data Format
Place your city coordinates in a file named `coordinates.csv` in the root directory. The file should contain `ID`, `X`, and `Y` values (separated by commas, spaces, or tabs). The program automatically ignores headers and corrupted text rows.
```text
ID  X       Y
1   510.27  319.67
2   125.47  178.93
3   8279.73 195.27
```

### ⚙️ Settings
You can easily modify the algorithm parameters at the top of the `path.py` file:
```python
FILE_NAME = 'coordinates.csv'
TIME_LIMIT = 100            # Execution time in seconds
INITIAL_TEMPERATURE = 50.0  # Starting temperature for exploration
FINAL_TEMPERATURE = 0.01    # Temperature at the final second
```

### ▶️ Usage
Run the optimization script using the following command. The script will output live temperature drops and the final shortest route sequence to the terminal.
```bash
python path.py
```

---

## <a id="türkçe"></a> 🇹🇷 Türkçe

Bu depo, **Gezgin Satıcı Problemi (TSP)** için **Benzetimli Tavlama (Simulated Annealing - SA)** algoritmasını kullanan Python tabanlı bir çözümleyici içerir. Standart SA uygulamalarının aksine, bu çözümleyici kullanıcının belirlediği süre sınırı ile tam senkronize çalışan **Zamana Bağlı Üstel Soğutma** kullanır.

### 🚀 Gereksinimler & Kurulum
Sisteminizde Python'un yüklü olduğundan emin olun. Ardından projenin çalışması için gerekli kütüphaneleri yükleyin:
```bash
pip install numpy pandas
```

### 📁 Veri Formatı
Şehir koordinatlarınızı ana dizindeki `coordinates.csv` adlı dosyaya yerleştirin. Dosya `ID`, `X` ve `Y` değerlerini içermelidir (virgül, boşluk veya sekme ile ayrılmış olabilir). Program başlık satırlarını ve bozuk verileri otomatik olarak temizler.
```text
ID  X       Y
1   510.27  319.67
2   125.47  178.93
3   8279.73 195.27
```

### ⚙️ Ayarlar
Kodu çalıştırmadan önce `path.py` dosyasının en üstündeki parametreleri kendi hedeflerinize göre özelleştirebilirsiniz:
```python
DOSYA_ADI = 'coordinates.csv'
ZAMAN_SINIRI = 100           # Saniye cinsinden maksimum çalışma süresi
BASLANGIC_SICAKLIK = 50.0    # Keşif aşaması başlangıç sıcaklığı
BITIS_SICAKLIK = 0.01        # Algoritmanın duracağı son saniye sıcaklığı
```

### ▶️ Kullanım
Kodu başlatmak için terminalde aşağıdaki komutu çalıştırın. Program anlık sıcaklık düşüşlerini ve bulunan en kısa rotayı canlı olarak gösterecektir.
```bash
python path.py
```
