import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_laplacian_variance(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    
    # Apply Laplacian filter
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    variance = laplacian.var()
    
    # Display images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(laplacian, cmap="gray")
    axes[1].set_title(f"Laplacian Variance: {variance:.2f}")
    axes[1].axis("off")

    plt.show()

    return variance

# Run the function with your image
image_path = "blurry.jpg"  # Replace with your image path
variance = show_laplacian_variance(image_path)

# Print if the image is blurry
threshold = 200
if variance < threshold:
    print(f"Blurry Image (Variance: {variance:.2f})")
else:
    print(f"Sharp Image (Variance: {variance:.2f})")



# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# def create_sample_images():
#     # Create a blank white image
#     image = np.full((300, 300, 3), 255, dtype=np.uint8)

#     # Draw sharp black rectangles (edges)
#     cv2.rectangle(image, (50, 50), (250, 250), (0, 0, 0), 5)
#     cv2.line(image, (50, 150), (250, 150), (0, 0, 0), 5)
#     cv2.line(image, (150, 50), (150, 250), (0, 0, 0), 5)

#     # Save the sharp image
#     sharp_image_path = "sharp.jpg"
#     cv2.imwrite(sharp_image_path, image)

#     # Create a blurry version by applying Gaussian blur
#     blurry_image = cv2.GaussianBlur(image, (21, 21), 0)

#     # Save the blurry image
#     blurry_image_path = "blurry.jpg"
#     cv2.imwrite(blurry_image_path, blurry_image)

#     # Display the images
#     fig, axes = plt.subplots(1, 2, figsize=(10, 5))
#     axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     axes[0].set_title("Sharp Image")
#     axes[0].axis("off")

#     axes[1].imshow(cv2.cvtColor(blurry_image, cv2.COLOR_BGR2RGB))
#     axes[1].set_title("Blurry Image")
#     axes[1].axis("off")

#     plt.show()

#     print(f"Images saved: {sharp_image_path}, {blurry_image_path}")

# # Run the function to generate and save images
# create_sample_images()
