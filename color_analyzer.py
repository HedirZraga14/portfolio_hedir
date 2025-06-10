import cv2
import numpy as np
from sklearn.cluster import KMeans
import webcolors

def get_dominant_colors(image_path, num_colors=5):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not read image at {image_path}")
    
    # Convert to RGB (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Flatten the image
    pixels = image.reshape(-1, 3)
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    
    # Get the cluster centers (dominant colors)
    colors = kmeans.cluster_centers_.astype(int)
    
    # Get the percentage of each color
    labels = kmeans.labels_
    counts = np.bincount(labels)
    percentages = counts / len(pixels)
    
    # Sort colors by percentage
    sorted_indices = np.argsort(percentages)[::-1]
    colors = colors[sorted_indices]
    percentages = percentages[sorted_indices]
    
    return colors, percentages

def closest_color(rgb):
    try:
        return webcolors.rgb_to_name(rgb)
    except ValueError:
        return None

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

# Analyze the image
image_path = 'hedir.jpg'
try:
    colors, percentages = get_dominant_colors(image_path)
    print("\nDominant Colors in Image:")
    print("-" * 50)
    for i, (color, percentage) in enumerate(zip(colors, percentages)):
        color_name = closest_color(color)
        hex_color = rgb_to_hex(color)
        print(f"Color {i+1} ({percentage*100:.1f}%):")
        print(f"  RGB: {color}")
        print(f"  HEX: {hex_color}")
        if color_name:
            print(f"  Name: {color_name}")
        print("-" * 50)
        
        # Update CSS variables
        print("\nUpdate your CSS with these variables:")
        print(f"    --color-{i+1}: {hex_color};")
        
except Exception as e:
    print(f"Error analyzing image: {str(e)}")
