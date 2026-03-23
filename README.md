# Observability Intelligence System for Log Anomaly Detection

## 🚀 Overview
This project builds an end-to-end machine learning system to detect anomalies in distributed system logs and reduce alert fatigue. By combining structured log metadata with NLP-based feature extraction, the system identifies abnormal patterns and groups related failures into actionable incidents.

---

## 🎯 Problem Statement
Modern distributed systems generate massive volumes of logs, overwhelming SRE and DevOps teams with alerts. Most logs are normal, while only a small fraction represent failures or anomalies. This project addresses:

- Detecting rare anomalous events in highly imbalanced log data  
- Reducing alert noise while preserving critical signals  
- Grouping related anomalies into meaningful incidents for faster root cause analysis  

---

## 📊 Dataset
- **Source:** LogHub HDFS Dataset  
- **Type:** Semi-structured system logs  
- **Size:** ~2000 log entries  

### Features:
- Timestamp (Date, Time)  
- Log Level (INFO, WARN, etc.)  
- Component (system module)  
- EventId (log template identifier)  
- Content (log message text)  

---

## ⚙️ Tech Stack

### 🧠 Core Technologies
- Python  
- Pandas, NumPy  
- Scikit-learn  
- SciPy  

### 🤖 Machine Learning
- Isolation Forest (unsupervised anomaly detection)  
- Random Forest (supervised classification)  

### 🧾 NLP / Feature Engineering
- TF-IDF Vectorization  
- Label Encoding  
- Temporal Feature Extraction  
- Message Length Features  

### 📈 Visualization
- Matplotlib  

---

## 🧩 System Architecture

### 1. Data Processing
- Load structured log dataset  
- Extract temporal and textual features  

### 2. Feature Engineering
- Convert log messages → TF-IDF vectors  
- Encode categorical variables  
- Combine structured + unstructured features  

### 3. Modeling
- Train Isolation Forest for anomaly detection  
- Train Random Forest for supervised baseline  

### 4. Evaluation
- Precision, Recall, F1-score  
- Confusion matrix  
- Model comparison  

### 5. Incident Grouping
- Group anomalies using EventId  
- Reduce alert volume by clustering similar failures  

---

## 📊 Key Results

- Achieved **~99% recall** using Isolation Forest  
- Identified strong class imbalance (~4% anomalies)  
- Reduced ~98 anomalies into **4 root incident groups**  
- Demonstrated overfitting in supervised model due to heuristic labels  

---

## 📂 Project Structure

observability-intelligence-system/
│
├── data/ # Dataset
├── notebooks/ # Main ML pipeline
├── src/ # Visualization functions
├── results/ # HTML report
├── README.md
├── requirements.txt
└── .gitignore


---

## 🧠 Key Insights

- Log data is highly imbalanced  
- Few components dominate system activity  
- Unsupervised models generalize better for rare anomalies  
- Grouping anomalies significantly reduces alert fatigue  

---

## ⚠️ Limitations

- Labels are heuristically generated  
- Dataset is relatively small  
- TF-IDF does not capture deep semantic meaning  
- Supervised model shows overfitting  

---

## 🔮 Future Work

- Apply LSTM / Transformer-based models  
- Real-time log streaming (Kafka, Spark)  
- Improve labeling strategies  
- Extend to larger multi-system datasets  

---

## ▶️ How to Run

```bash
python -m venv .venv
source .venv/bin/activate   # (or Windows equivalent)
pip install -r requirements.txt
jupyter notebook notebooks/log-anomaly-detection-ml.ipynb
