# 📊 ML Evaluation Dashboard

**ML Evaluation Dashboard** is a Python-based Streamlit component designed to **visualize**, **compare**, and **interpret** machine learning model performance. It helps data scientists and ML engineers explore evaluation metrics interactively and share results efficiently.

---

## 🚀 Features

1. 📈 Visual comparison of multiple ML models  
2. 🧮 Displays key evaluation metrics (e.g., Accuracy, F1-score, ROC-AUC)  
3. 📊 Interactive plots for classification and regression tasks  
4. 🔌 Easy integration with existing ML pipelines  
5. ⚡ Lightweight, customizable, and ready for production use  

---

## 📦 Installation

### Option 1: Install via pip (recommended)

```bash
pip install ml-eval-dashboard
```

### Option 2: Install from source (for contributors)

```bash
git clone https://github.com/M-Tariq-Butt/ml_eval_dashboard.git
cd ml_eval_dashboard
pip install -e .
```

### (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

## 🧑‍💻 Usage

### 🔹 Method 1: Run with command-line (streamlit launch)

Once installed via `pip`, simply run the following in your terminal:

```bash
ml-eval-dashboard
```

This will start the Streamlit app in your browser where you can upload CSV files and explore visualizations and reports.

---

### 🔹 Method 2: Run from Python Script

Import and run the dashboard manually in a Python script:

```python
from ml_eval_dashboard import dashboard

dashboard.run_dashboard()
```

---

## 📄 Input Format

Each uploaded CSV file should contain at least the following columns:

- `y_true`: Ground truth labels  
- `y_pred`: Model predictions  

Optional for classification:
- `y_prob`: Probabilities for binary classification  
- `y_prob_classX`: Probabilities for each class in multiclass classification  

---

## 📁 Project Structure

```
ml_eval_dashboard/             # Core dashboard logic and modules
├── evaluator.py               # Metric evaluation functions
├── visualizer.py              # Plotting utilities
├── dashboard.py               # Main Streamlit app
├── report_generator.py        # PDF report generation

outputs/                       # Store model evaluation result files

requirements.txt               # Dependencies list
setup.py                       # Packaging and entry point
LICENSE                        # License info
README.md                      # You are here!
```

---

## 📘 Documentation

Detailed usage instructions and API documentation will be available soon in the `docs/` folder or the GitHub Wiki.

---

## ⚙️ Dependencies

Listed in `requirements.txt`. Key dependencies include:

- `streamlit`
- `scikit-learn`
- `pandas`
- `matplotlib`
- `seaborn`

---

## 💻 Deployment Requirements

- Python 3.7+
- Platform independent (tested on Windows, macOS, and Linux)

---

## 🪪 License

This project is licensed under the **MIT License**.  
See the [LICENSE](./LICENSE) file for full details.
