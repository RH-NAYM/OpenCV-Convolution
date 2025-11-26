# 🖼️ Image Filtering Using Convolution in OpenCV :: main branch
<p align="center">
  <a href="https://opencv.org/" target="_blank">
    <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv&logoColor=white">
  </a>
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white">
  </a>
  <a href="https://jupyter.org/" target="_blank">
    <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white">
  </a>
  <a href="https://numpy.org/" target="_blank">
    <img src="https://img.shields.io/badge/Numpy-Numerical-lightblue?logo=numpy&logoColor=white">
  </a>
  <a href="https://matplotlib.org/" target="_blank">
    <img src="https://img.shields.io/badge/Matplotlib-Visualization-yellow?logo=plotly&logoColor=white">
  </a>
</p>


# 📁 Project Structure
```bash
.
├── 📓 Image_Filtering.ipynb            # Main Computer Vision course notebook
├── 📘 README.md                        # Documentation & module overview
├── 📦 requirements.txt                 # Python dependencies
├── 🖼️ testImage.jpg                    # Sample input image
├── 🧪 test.py                          # Quick testing / experiments
└── 🛠️ tools                            # Utility functions
    └── 🧩 tools.py                     # Helper methods for filtering & visualization
```

# 📌 Overview
This project demonstrates image filtering using convolution kernels in OpenCV.
It explains how kernels work, how images are processed pixel-by-pixel, and how different filters affect image quality.

All examples are implemented in a Jupyter Notebook with side-by-side visual comparisons using Matplotlib.


# 🧠 What You’ll Learn
```bash
:: What convolution kernels are
:: How cv2.filter2D() works
:: Identity filtering
:: Custom kernel blurring
:: Built-in OpenCV filters:
:: Average Blur (cv2.blur)
:: Gaussian Blur
:: Median Blur
:: Bilateral Filtering
:: Image sharpening using custom kernels
:: Visual comparison of filters
```
# 🛠️ Technologies Used
```bash
:: Python
:: OpenCV
:: NumPy
:: Matplotlib
:: Jupyter Notebook
```
# 📦 Installation
## 1️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
```
```bash
source venv/bin/activate    # Linux / macOS
```
```bash
venv\Scripts\activate       # Windows
```
## 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

# 🚀 How to Run
### Option 1: Jupyter Notebook (Local)
```bash
jupyter notebook
```
open
```bash
Image_Filtering.ipynb
```
### Option 2: Google Colab
```bash
Upload the .ipynb file to Google Colab and run all cells
```

# ✅ Summary
```bash
:: Convolution kernels are the foundation of image filtering
:: Custom kernels offer flexibility and control
:: OpenCV built-in filters are optimized and efficient
:: Bilateral filtering preserves edges while reducing noise
:: Visualization helps understand real filtering effects
```
This project is ideal for students, CV beginners, and AI practitioners.
