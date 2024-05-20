from PIL import Image

def encrypt_image(image_path, key, output_path):
    """
    Encrypts an image by manipulating its pixel values.
    Args:
    - image_path (str): The path to the input image.
    - key (int): The encryption key (integer).
    - output_path (str): The path to save the encrypted image.
    """
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()  # Load the pixel data
    
    for i in range(img.size[0]):  # For every pixel in the width
        for j in range(img.size[1]):  # For every pixel in the height
            r, g, b = pixels[i, j]
            # Encrypt each pixel by adding the key (simple encryption)
            pixels[i, j] = (r + key) % 256, (g + key) % 256, (b + key) % 256
    
    # Save the encrypted image
    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    """
    Decrypts an image by reversing the pixel value manipulation.
    Args:
    - image_path (str): The path to the encrypted image.
    - key (int): The encryption key (integer).
    - output_path (str): The path to save the decrypted image.
    """
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = img.load()  # Load the pixel data
    
    for i in range(img.size[0]):  # For every pixel in the width
        for j in range(img.size[1]):  # For every pixel in the height
            r, g, b = pixels[i, j]
            # Decrypt each pixel by subtracting the key
            pixels[i, j] = (r - key) % 256, (g - key) % 256, (b - key) % 256
    
    # Save the decrypted image
    img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    key = 123  # Example key for encryption/decryption
    encrypt_image("input.jpg", key, "encrypted.png")
    decrypt_image("encrypted.png", key, "decrypted.png")
