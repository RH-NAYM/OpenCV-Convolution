# 🖼️ Comprehensive Image Filtering Using Convolution in OpenCV
[![main branch](https://img.shields.io/badge/branch-dev-blue?style=flat&logo=git&logoColor=white)](https://github.com/RH-NAYM/OpenCV-Convolution/tree/main)
#

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
├── 📓 Image_Filtering.ipynb            # Comprehensive Jupyter Notebook on image filtering
├── 📘 README.md                        # Detailed documentation & project overview
├── 📦 requirements.txt                 # Python dependencies (OpenCV, NumPy, Matplotlib)
├── 🖼️ testImage.jpg                    # Sample input image for demonstrations
├── 🧪 test.py                          # Quick testing scripts and experiments
└── 🛠️ tools                            # Utility module for helpers
    └── 🧩 tools.py                     # Functions for image loading, visualization, and utilities
```
# 📌 Overview
This project provides a deep dive into image filtering techniques using convolution in OpenCV. Inspired by resources like LearnOpenCV, it covers foundational concepts to advanced topics, including theoretical explanations, mathematical derivations, practical code implementations, and performance optimizations.

The Jupyter Notebook includes step-by-step examples with visual comparisons using Matplotlib subplots, making it easy to understand how different filters impact image quality. Topics range from basic blurring and sharpening to frequency domain filtering, noise handling, and real-world applications.

Whether you're a beginner in computer vision or an experienced practitioner, this repository serves as a complete reference for mastering convolution-based image processing in OpenCV.


# 📋 Table of Contents (Notebook Sections)
```bash
1. Introduction to Convolution in Image Processing
2. Mathematical Foundations of Convolution
3. Kernel Design Principles
4. Border Handling and Padding in Convolution
5. Applying Identity Kernel
6. Low-Pass Filters: Blurring Techniques
        - Custom Box Blur
        - Built-in Box Blur
        - Gaussian Blur
        - Median Blur
        - Bilateral Filter
7. High-Pass Filters: Sharpening and Edge Enhancement
        - Basic Sharpening Kernel
        - Unsharp Masking
        - Laplacian Filter for Edge Detection
        - Sobel Operators
8. Directional and Advanced Kernels
        - Emboss Filter
        - Prewitt Operator
        - Scharr Operator
        - Gabor Filters
9. Frequency Domain Filtering
        - Fourier Transform Basics
        - High-Pass and Low-Pass in Frequency Domain

10. Noise in Images: Addition and Removal
11. Performance Considerations and Optimization
12. Real-World Applications and Case Studies
13. Summary and Best Practices
```
# 🧠 What You’ll Learn
- Core concepts of convolution kernels and how they process images pixel-by-pixel.
- Mathematical foundations, including 1D/2D convolution, normalization, and cross-correlation.
- Kernel design principles: size, symmetry, and sum properties for different effects.
- Border handling techniques to manage edge artifacts during filtering.
- Basic filters: Identity kernel and custom box blurring.
- Built-in OpenCV blurring methods: Average (cv2.blur), Gaussian, Median, and Bilateral.
- Sharpening techniques: Custom kernels, unsharp masking, and high-pass filters.
- Edge detection: Laplacian, Sobel, Prewitt, and Scharr operators.
- Advanced kernels: Emboss for 3D effects and Gabor for texture analysis.
- Frequency domain filtering using Fourier transforms for efficient low/high-pass operations.
- Handling image noise: Adding Gaussian/salt-and-pepper noise and removal strategies.
- Performance optimizations: Separable kernels, built-in functions, and benchmarking.
- Real-world applications in medical imaging, autonomous vehicles, photography, and more.
- Best practices for combining filters, parameter tuning, and visualization.


# 🛠️ Technologies Used
- Python 3.x
- OpenCV (cv2) for core image processing and filtering.
- NumPy for array manipulations and kernel creation.
- Matplotlib for visual comparisons and plotting (e.g., subplots, frequency spectra).
- Jupyter Notebook for interactive execution and documentation.

# 📦 Installation
## 1️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```
## 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

# 🚀 How to Run
## Option 1: Jupyter Notebook (Local)
```bash
1. Install Jupyter if needed: pip install notebook.
2. Launch Jupyter: jupyter notebook.
3. Open Image_Filtering.ipynb and run cells sequentially.
        - The notebook automatically downloads a sample image if testImage.jpg is missing.
```
## Option 2: Google Colab
```bash
1. Upload Image_Filtering.ipynb to Google Colab.
2. Install dependencies in a cell: !pip install opencv-python numpy matplotlib.
3. Run all cells for interactive demonstrations.
```
```bash
# Note: Ensure the sample image is available or let the notebook fetch it from the provided URL.
```
# ✅ Summary
- Convolution kernels form the backbone of image filtering, enabling custom effects like blurring, sharpening, and edge detection.
- Custom implementations with cv2.filter2D() offer flexibility, while OpenCV's built-in functions provide optimized performance.
- Advanced topics like frequency domain filtering and noise handling extend practical utility.
- Visualizations and code examples make complex concepts accessible.
- Experiment with parameters (e.g., kernel size, sigma) to see real-time effects.
```bash
# This repository is perfect for computer vision students, AI enthusiasts, and professionals seeking a thorough understanding of OpenCV filtering techniques.
```

# 🍴 Real-World Applications and Case Studies
- Medical Imaging: Use median or bilateral filters for noise reduction in MRI/CT scans while preserving edges.
- Autonomous Vehicles: Apply Sobel/Laplacian for real-time edge detection in lane finding and obstacle avoidance.
- Photography & Editing: Sharpen images with unsharp masking or apply Gaussian blur for bokeh effects.
- Security & Surveillance: Employ Gabor filters for texture-based recognition in facial or fingerprint analysis.
- Industrial Inspection: Frequency domain filtering to detect defects in manufacturing lines.
- Case Study: OCR Preprocessing - Combine Gaussian blur to remove noise, followed by sharpening and edge enhancement to improve text recognition accuracy in scanned documents.
- Case Study: Satellite Imagery - Bilateral filtering for atmospheric noise reduction, combined with high-pass filters for feature extraction in remote sensing.

```bash
# For contributions or issues, feel free to open a pull request or issue on the repository!
```
