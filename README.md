# 🐾 WildVision AI — Animal Species Prediction

🚀 A fast and lightweight Machine Learning web app built using **Streamlit** that predicts animal species based on physical and biological features.

LIVE LINK : https://animalspeciesprediction-em5icb5wmcujmqfztmazkt.streamlit.app/

---

## 📌 Project Overview

**WildVision AI** is an interactive ML-powered application that classifies animals into species such as:

* 🐦 Bird
* 🐟 Fish
* 🐍 Reptile
* 🐶 Mammal

The model uses features like weight, body length, number of legs, and biological traits to make predictions.

---

## ⚡ Features

* 🔮 Real-time prediction using trained ML model
* ⚡ Fast loading (optimized with caching)
* 🎯 High accuracy Random Forest model
* 📊 Probability visualization (confidence score)
* 🎨 Clean & modern UI with Streamlit
* 📁 Dataset preview option
* 🌐 Ready for deployment

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn**
* **Pandas**
* **NumPy**

---

## 📂 Project Structure

```
animal_species_prediction/
│── app.py
│── requirements.txt
│── models/
│   ├── animal_species_model.pkl
│   ├── model_columns.pkl
│   └── labels.pkl
│── data/
│   └── animal_species_dataset.csv
│── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/kailashd112/animal_species_prediction.git
cd animal_species_prediction
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

👉 App will open in your browser automatically.

---

## 📊 Model Details

* **Algorithm:** Random Forest Classifier

* **Input Features:**

  * Weight (kg)
  * Body Length (cm)
  * Number of Legs
  * Has Fur
  * Has Wings
  * Lays Eggs
  * Has Tail
  * Aquatic
  * Warm Blooded

* **Output:** Predicted Animal Species + Confidence Score

---

## ⚡ Performance Optimization

* ✅ Cached model loading using `@st.cache_resource`
* ✅ Lazy dataset loading
* ✅ Lightweight dependencies
* ✅ Reduced model size for faster predictions

---

## 🌐 Deployment

You can deploy this project easily on:

* **Streamlit Cloud (Recommended)**
* **Render**
* **Railway**

---

## 🖼️ UI Preview

> *(Add screenshot here after deployment)*

---

## 🔥 Future Improvements

* 📸 Image-based animal detection (CNN model)
* 🎨 Advanced UI animations
* 📊 Model evaluation dashboard
* 🌍 Real-world dataset integration

---

## 👨‍💻 Author

**Kailash Dake**
🔗 GitHub: https://github.com/kailashd112

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share with others

---

## 📜 License

This project is open-source and available under the **MIT License**.
