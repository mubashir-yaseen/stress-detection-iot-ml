# 🧠 Real-Time Stress Detection System Using IoT & Machine Learning

This project presents a real-time stress detection system that uses physiological signals from biosensors (ECG, EEG, GSR, PPG) connected via IoT (ESP32/ESP8266), processed using machine learning models to classify stress levels.


## 🔬 Project Highlights

- 🧪 Collected real biosensor data (GSR, PPG, ECG) for live stress monitoring
- 📡 Streamed data over Wi-Fi using ESP32/ESP8266 microcontroller
- ⚙️ Used machine learning models to classify stress levels in real time
- 🎯 Achieved up to **92% classification accuracy**
- 📊 Visualized live stress levels on web interface using Streamlit


## 🛠️ Technologies Used

- ⚡ ESP32/ESP8266 (IoT Microcontroller)
- 📶 Arduino IDE + Serial Communication
- 🐍 Python, Scikit-learn
- 📈 Streamlit for dashboard
- 📚 Dataset: Kaggle Stress Dataset / Custom Collected Data


## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/mubashir-yaseen/stress-detection-iot-ml.git
cd stress-detection-iot-ml

# Install dependencies
pip install -r requirements.txt

# Generate Pickle file
Run model_training.py to train and generate stress_model.pkl.

# Start Streamlit dashboard (ensure serial device is connected)
streamlit run app.py

# (Optional) Test serial port reading
python serial_reader.py

````


## 📁 Project Structure

```
├── app.py                 # Streamlit Dashboard
├── model_training.py      # ML model training & evaluation
├── serial_reader.py       # Reads sensor data via COM port
├── utils/                 # Preprocessing, visualization functions
├── models/                # Saved ML model (e.g., stress_model.pkl)
├── data/                  # Dataset CSV files
└── README.md
```


## 💡 How It Works

1. **Sensors** (e.g., GSR, ECG, PPG) send analog signals to ESP32/ESP8266.
2. Data is streamed via serial to Python using `pyserial`.
3. Python app receives data, processes it, and classifies stress level.
4. Dashboard displays live status (e.g., "Relaxed", "Moderate", "Stressed").


## ✅ Results

* Accuracy: **92%**
* Model: Random Forest / SVM / XGBoost (can compare multiple)
* Real-time classification latency: \~1s


## 🔄 Future Improvements

* Integrate with wearable devices (e.g., smartwatches)
* Use deep learning (LSTM) for time-series classification
* Cloud-based dashboard (Azure or Firebase)


## 👨‍💻 Author

Muhammad Mubashir
📧 [mubashiryaseen@hotmail.com](mailto:mubashiryaseen@hotmail.com)
🔗 [GitHub](https://github.com/mubashir-yaseen)


## 📄 License

MIT License

