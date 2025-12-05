#  Color Image Channel Manipulation using OpenCV

###  A College Project for **Digital Image Processing (DIP)**

---

##  Project Overview

This project demonstrates various **color channel operations** on RGB images using **OpenCV, NumPy, and Matplotlib**.  
It explores how digital images are represented and manipulated across the Red, Green, and Blue (RGB) color channels — key concepts in **Digital Image Processing**.

The script performs:
- Channel separation
- Visualization of individual channels (in grayscale and color)
- Negative/complement transformation
- Channel swapping
- Channel removal
- Channel enhancement

Each operation helps build intuition about how colors blend and how modifying one channel affects the overall image.

---

##  Features & Functionality

| Operation | Description |
|------------|-------------|
| **Separate Channels** | Splits the image into individual R, G, B channels. |
| **Visualize Channels** | Displays each channel as grayscale and colored image maps. |
| **Color Negative (Complement)** | Creates image negative by subtracting from 255. |
| **Swap Channels** | Interchanges R-G, R-B, or G-B channels. |
| **Remove a Channel** | Sets a chosen channel (R/G/B) to zero. |
| **Enhance Channel** | Amplifies intensity of a specific color channel. |

All transformations are displayed using Matplotlib and saved locally using OpenCV.

---

##  Technologies Used

- **Python 3.x**
- **OpenCV (cv2)**
- **NumPy**
- **Matplotlib**

---

DIP-Color-Channel-Manipulation/
│
├──  main.py                    # Main Python script (your code)
├──   Test Flower.jpg           # Sample input image
│
├──  outputs/                   # Generated results folder
│   ├── red_channel.jpg
│   ├── green_channel.jpg
│   ├── blue_channel.jpg
│   ├── color_negative.jpg
│   ├── rb_swapped.jpg
│   ├── red_removed.jpg
│   └── red_enhanced.jpg
│
├──  README.md                  # Project documentation
├──  requirements.txt           # Python dependencies
├──  .gitignore                 # Git ignore file
└──  images/                    # Sample result images for README
    ├── original.jpg
    ├── red_channel_sample.jpg
    └── color_negative_sample.jpg


##  How to Run the Project

1. **Clone the repository:**
git clone https://github.com/yourusername/DIP-Color-Channel-Manipulation.git
cd DIP-Color-Channel-Manipulation

2. **Install dependencies:**
pip install opencv-python numpy matplotlib


3. **Place your input image** in the project folder and update the image filename in the script:
image_path = 'Test Flower.jpg'


4. **Run the program:**
python main.py


5. The processed images will display in popup windows and get saved in the current directory.

---

##  Learning Outcomes

- Understanding of RGB image representation in digital form.
- Fundamentals of color space manipulation.
- Practical exposure to OpenCV and NumPy image processing functions.
- Visualization of color-based transformations and their pixel-level impact.

---

##  Conclusion

This project emphasizes how **color channel manipulation** is a powerful foundation for more advanced image processing tasks such as:
- Color enhancement
- Object detection
- Image segmentation
- Computer vision preprocessing

---

⭐ **If you find this project useful, give it a star on GitHub!**
