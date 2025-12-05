import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_images(images, titles, rows=2, cols=3, figsize=(15, 10)):
    """Helper function to display multiple images"""
    plt.figure(figsize=figsize)
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(rows, cols, i + 1)
        if len(img.shape) == 2:  # Grayscale
            plt.imshow(img, cmap='gray')
        else:  # Color
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

def separate_channels(image):
    """Separate RGB channels"""
    B, G, R = cv2.split(image)
    return R, G, B

def visualize_individual_channels(image, R, G, B):
    """Create colored visualizations of individual channels"""
    # Create zero channels
    zeros = np.zeros(R.shape, dtype=np.uint8)
    
    # Create individual channel images with color
    red_channel = cv2.merge([zeros, zeros, R])
    green_channel = cv2.merge([zeros, G, zeros])
    blue_channel = cv2.merge([B, zeros, zeros])
    
    return red_channel, green_channel, blue_channel

def channel_complement(image):
    """Compute negative/complement of each channel"""
    return 255 - image

def swap_channels(image, mode='RB'):
    """Swap color channels
    mode: 'RB' (Red-Blue), 'RG' (Red-Green), 'GB' (Green-Blue)
    """
    B, G, R = cv2.split(image)
    
    if mode == 'RB':
        return cv2.merge([R, G, B])  # Swap R and B
    elif mode == 'RG':
        return cv2.merge([B, R, G])  # Swap R and G
    elif mode == 'GB':
        return cv2.merge([G, B, R])  # Swap G and B
    else:
        return image

def remove_channel(image, channel='R'):
    """Remove a specific channel (set to zero)"""
    B, G, R = cv2.split(image)
    zeros = np.zeros(R.shape, dtype=np.uint8)
    
    if channel == 'R':
        return cv2.merge([B, G, zeros])
    elif channel == 'G':
        return cv2.merge([B, zeros, R])
    elif channel == 'B':
        return cv2.merge([zeros, G, R])
    else:
        return image

def enhance_channel(image, channel='R', factor=1.5):
    """Enhance a specific channel by multiplication factor"""
    B, G, R = cv2.split(image)
    
    if channel == 'R':
        R = np.clip(R * factor, 0, 255).astype(np.uint8)
    elif channel == 'G':
        G = np.clip(G * factor, 0, 255).astype(np.uint8)
    elif channel == 'B':
        B = np.clip(B * factor, 0, 255).astype(np.uint8)
    
    return cv2.merge([B, G, R])

def main():
    # Read the image
    image_path = 'Test Flower.jpg'  # Change to your image path
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return
    
    print("Color Image Channel Manipulation")
    print("=" * 50)
    
    # 1. Separate and display individual channels
    print("\n1. Separating RGB channels...")
    R, G, B = separate_channels(image)
    
    # Visualize grayscale channels
    images = [image, R, G, B]
    titles = ['Original Image', 'Red Channel', 'Green Channel', 'Blue Channel']
    display_images(images, titles, rows=2, cols=2)
    
    # 2. Visualize colored individual channels
    print("\n2. Visualizing individual channels in color...")
    red_img, green_img, blue_img = visualize_individual_channels(image, R, G, B)
    
    images = [image, red_img, green_img, blue_img]
    titles = ['Original Image', 'Red Channel (Colored)', 'Green Channel (Colored)', 'Blue Channel (Colored)']
    display_images(images, titles, rows=2, cols=2)
    
    # 3. Channel complement (negative)
    print("\n3. Computing channel complement...")
    complement_img = channel_complement(image)
    
    images = [image, complement_img]
    titles = ['Original Image', 'Color Negative (All Channels)']
    display_images(images, titles, rows=1, cols=2, figsize=(12, 5))
    
    # 4. Channel swapping
    print("\n4. Swapping channels...")
    swap_rb = swap_channels(image, 'RB')
    swap_rg = swap_channels(image, 'RG')
    swap_gb = swap_channels(image, 'GB')
    
    images = [image, swap_rb, swap_rg, swap_gb]
    titles = ['Original', 'R-B Swapped', 'R-G Swapped', 'G-B Swapped']
    display_images(images, titles, rows=2, cols=2)
    
    # 5. Channel removal
    print("\n5. Removing individual channels...")
    remove_r = remove_channel(image, 'R')
    remove_g = remove_channel(image, 'G')
    remove_b = remove_channel(image, 'B')
    
    images = [image, remove_r, remove_g, remove_b]
    titles = ['Original', 'Red Removed', 'Green Removed', 'Blue Removed']
    display_images(images, titles, rows=2, cols=2)
    
    # 6. Channel enhancement
    print("\n6. Enhancing individual channels...")
    enhance_r = enhance_channel(image, 'R', 1.5)
    enhance_g = enhance_channel(image, 'G', 1.5)
    enhance_b = enhance_channel(image, 'B', 1.5)
    
    images = [image, enhance_r, enhance_g, enhance_b]
    titles = ['Original', 'Red Enhanced', 'Green Enhanced', 'Blue Enhanced']
    display_images(images, titles, rows=2, cols=2)
    
    # 7. Save results
    print("\n7. Saving results...")
    cv2.imwrite('red_channel.jpg', R)
    cv2.imwrite('green_channel.jpg', G)
    cv2.imwrite('blue_channel.jpg', B)
    cv2.imwrite('color_negative.jpg', complement_img)
    cv2.imwrite('rb_swapped.jpg', swap_rb)
    cv2.imwrite('red_removed.jpg', remove_r)
    cv2.imwrite('red_enhanced.jpg', enhance_r)
    
    print("\nAll operations completed successfully!")
    print("Results saved to current directory.")

if __name__ == "__main__":
    main()    


    