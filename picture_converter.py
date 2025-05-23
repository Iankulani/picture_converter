from PIL import Image

def create_icon():
    print("=== ICO Icon Generator ===")
    image_path = input("Enter the path to the image (e.g., picture.png):").strip()
    output_name = input("Enter the desired output file name (e.g., app_icon.ico): ").strip()
    
    # Ask for size and validate it
    try:
        size_input = input("Enter icon size (default is 256, just type a number like 256): ").strip()
        size = int(size_input) if size_input else 256
    except ValueError:
        print("Invalid size entered. Defaulting to 256x256.")
        size = 256

    try:
        img = Image.open(image_path)
        img.save(output_name, format='ICO', sizes=[(size, size)])
        print(f"Icon saved as '{output_name}' with size {size}x{size}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_icon()
