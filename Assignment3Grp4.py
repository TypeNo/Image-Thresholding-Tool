import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog

processed_image = None  # Variable to save the processed image

# Grayscale Global Thresholding
def Grayscale_global_thresholding(threshold_value):
    global processed_image
    threshold_slider.pack(pady=(0, 10))
    threshold_value = int(threshold_value)
    
    ret, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

    # Create a subplot with 1 row and 2 columns to display original and processed image
    plt.subplot(1, 2, 1)
    plt.imshow(img, 'gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(thresh, 'gray')
    plt.title(f'Grayscale Global Thresholding (Threshold: {threshold_value})')

    # Set the window size (width, height) in inches
    plt.gcf().set_size_inches(10, 5)
    plt.show(block=False)

    # Save the processed image
    processed_image = thresh
    save_button.pack(pady=(0, 20))

# Color Global Thresholding
def Color_global_thresholding(threshold_value):
    global processed_image
    threshold_slider.pack(pady=(0, 10))
    threshold_value = int(threshold_value)

    # Separate color channels
    b, g, r = cv2.split(img)

    # Apply thresholding to each channel
    ret, thresh_b = cv2.threshold(b, threshold_value, 255, cv2.THRESH_BINARY)
    ret, thresh_g = cv2.threshold(g, threshold_value, 255, cv2.THRESH_BINARY)
    ret, thresh_r = cv2.threshold(r, threshold_value, 255, cv2.THRESH_BINARY)

    # Merge thresholded channels back to color
    thresh_color = cv2.merge((thresh_b, thresh_g, thresh_r))

    # Create a subplot with 1 row and 2 columns to display original and processed image
    plt.subplot(1, 2, 1)
    plt.imshow(img, 'gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(thresh_color, 'gray')
    plt.title(f'Color Global Thresholding (Threshold: {threshold_value})')

    # Set the window size (width, height) in inches
    plt.gcf().set_size_inches(10, 5)
    plt.show(block=False)

    # Save the processed image
    processed_image = thresh_color
    save_button.pack(pady=(0, 20))

# Grayscale Adaptive Gaussian Thresholding with median blur
def Grayscale_adaptive_Gaussian_thresholding():
    threshold_slider.pack_forget()
    global processed_image
    blur = cv2.medianBlur(img, 7)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Create a subplot with 1 row and 2 columns to display original and processed image
    plt.subplot(1, 2, 1)
    plt.imshow(img, 'gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(thresh, 'gray')
    plt.title('Grayscale Adaptive Gaussian Thresholding with Median Blur')

    # Set the window size (width, height) in inches
    plt.gcf().set_size_inches(10, 5)
    plt.show(block=False)

    # Save the processed image
    processed_image = thresh
    save_button.pack(pady=(0, 20))

# Color Adaptive Gaussian Thresholding with median blur
def Color_adaptive_Gaussian_thresholding():
    global processed_image
    threshold_slider.pack_forget()

    # Separate color channels
    b, g, r = cv2.split(img)

    # Apply median blur to each channel
    blur_b = cv2.medianBlur(b, 9)
    blur_g = cv2.medianBlur(g, 9)
    blur_r = cv2.medianBlur(r, 9)

    # Apply adaptive Gaussian thresholding to each channel
    thresh_b = cv2.adaptiveThreshold(blur_b, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh_g = cv2.adaptiveThreshold(blur_g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh_r = cv2.adaptiveThreshold(blur_r, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Merge thresholded channels back to color
    thresh_color = cv2.merge((thresh_b, thresh_g, thresh_r))
    
    # Create a subplot with 1 row and 2 columns to display original and processed image
    plt.subplot(1, 2, 1)
    plt.imshow(img, 'gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(thresh_color, 'gray')
    plt.title('Color Adaptive Gaussian Thresholding with Median Blur')

    # Set the window size (width, height) in inches
    plt.gcf().set_size_inches(10, 5)
    plt.show(block=False)

    # Save the processed image
    processed_image = thresh_color
    save_button.pack(pady=(0, 20))

# Grayscale Otsu Thresholding with Gaussian Blur
def Grayscale_otsu_thresholding():
    global processed_image
    threshold_slider.pack_forget()

    blur = cv2.GaussianBlur(img,(5,5),0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Create a subplot with 1 row and 2 columns to display original and processed image
    plt.subplot(1, 2, 1)
    plt.imshow(img, 'gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(thresh, 'gray')
    plt.title('Grayscale Otsu Thresholding with Gaussian Blur')

    # Set the window size (width, height) in inches
    plt.gcf().set_size_inches(10, 5)
    plt.show(block=False)

    # Save the processed image
    processed_image = thresh
    save_button.pack(pady=(0, 20))

# Color Otsu Thresholding with Gaussian Blur
def Color_otsu_thresholding():
    threshold_slider.pack_forget()
    global processed_image

    # Separate color channels
    b, g, r = cv2.split(img)

     # Apply Gaussian Blur to each channel
    blur_b = cv2.GaussianBlur(b, (5, 5), 0)
    blur_g = cv2.GaussianBlur(g, (5, 5), 0)
    blur_r = cv2.GaussianBlur(r, (5, 5), 0)

    # Apply Otsu Thresholding to each channel
    ret, thresh_b = cv2.threshold(blur_b, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret, thresh_g = cv2.threshold(blur_g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret, thresh_r = cv2.threshold(blur_r, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Merge thresholded channels back to color
    thresh_color = cv2.merge([thresh_b, thresh_g, thresh_r])

    # Create a subplot with 1 row and 2 columns to display original and processed image
    plt.subplot(1, 2, 1)
    plt.imshow(img, 'gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(thresh_color, 'gray')
    plt.title('Color Otsu Thresholding with Gaussian Blur')

    # Set the window size (width, height) in inches
    plt.gcf().set_size_inches(10, 5)
    plt.show(block=False)

    # Save the processed image
    processed_image = thresh_color
    save_button.pack(pady=(0, 20))

# Function to save the processed image
def save_processed_image():
    global processed_image
    if processed_image is not None:
        filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if filepath:
            processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
            cv2.imwrite(filepath, processed_image)
            print("Processed image saved successfully.")

# when slider is slided, update the value to Grayscale_global_thresholding
def on_threshold_slider_change(value):
    Grayscale_global_thresholding(value)

# Function to open and process the Grayscale image
def Grayscale_threshold():
    save_button.pack_forget()
    global img, Grayscale_global_button, Grayscale_adaptive_button, Grayscale_otsu_button, Color_global_button
    filepath = filedialog.askopenfilename()
    if filepath:
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

        # Hide Color buttons and slider after successfully loading an image
        threshold_slider.pack_forget()
        Color_global_button.pack_forget()
        Color_adaptive_button.pack_forget()
        Color_otsu_button.pack_forget()
        # Show thresholding buttons after successfully loading an image
        Grayscale_global_button.pack(pady=(0, 10))
        Grayscale_adaptive_button.pack(pady=(0, 10))
        Grayscale_otsu_button.pack(pady=(0, 10))

# Function to open and process the Color image
def Color_threshold():
    save_button.pack_forget()
    global img, Grayscale_global_button, Grayscale_adaptive_button, Grayscale_otsu_button, Color_global_button
    filepath = filedialog.askopenfilename()
    if filepath:
        img = cv2.imread(filepath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Hide Grayscale buttons and slider after successfully loading an image
        threshold_slider.pack_forget()
        Grayscale_global_button.pack_forget()
        Grayscale_adaptive_button.pack_forget()
        Grayscale_otsu_button.pack_forget()
        # Show buttons after successfully loading an image
        Color_global_button.pack(pady=(0, 10))
        Color_adaptive_button.pack(pady=(0, 10))
        Color_otsu_button.pack(pady=(0, 10))

# Create the main window
root = tk.Tk()
root.title("Image Thresholding")
root.geometry("400x550") 

# Create buttons for thresholding methods
Grayscale_threshold_button = tk.Button(root, text="Thresholding in Grayscale", width=20, height=3, fg="White", bg="Black", command=Grayscale_threshold)
Color_threshold_button = tk.Button(root, text="Thresholding in Color", width=20, height=3, fg="Yellow", bg="Red", command=Color_threshold)
Grayscale_global_button = tk.Button(root, text="Grayscale Global Thresholding", command=lambda: [Grayscale_global_thresholding(threshold_slider.get())])
Grayscale_adaptive_button = tk.Button(root, text="Grayscale Adaptive Gaussian Thresholding", command=Grayscale_adaptive_Gaussian_thresholding)
Grayscale_otsu_button = tk.Button(root, text="Grayscale Otsu Thresholding", command=Grayscale_otsu_thresholding)
Color_global_button = tk.Button(root, text="Color Global Thresholding",  command=lambda: [Color_global_thresholding(threshold_slider.get())])
Color_adaptive_button = tk.Button(root, text="Color Adaptive Gaussian Thresholding", command=Color_adaptive_Gaussian_thresholding)
Color_otsu_button = tk.Button(root, text="Color Otsu Thresholding", command=Color_otsu_thresholding)
save_button = tk.Button(root, text="Save Processed Image", command=save_processed_image)
threshold_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Threshold Value", command=on_threshold_slider_change)

# Display Group information
title_style = ("", "13", "bold")
group_label = tk.Label(root, text="Assignment 3 Group 4", font=title_style)
group_label2 = tk.Label(root, text="Muhammad Akashah Bin Bahar")
group_label3 = tk.Label(root, text="Lew Chin Hong")
group_label4 = tk.Label(root, text="Yeo Chun Teck")
group_label.pack(pady=(20, 5))
group_label2.pack()
group_label3.pack()
group_label4.pack()

# Arrange buttons in the window
Grayscale_threshold_button.pack(pady=(20, 20))
Color_threshold_button.pack(pady=(0, 20))

# Run the main loop
root.mainloop()
