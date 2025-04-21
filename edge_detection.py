from PIL import Image
import sys

def apply_sobel_filter(input_image_path, output_image_path):
    try:
        # Open the image from the file
        image = Image.open(input_image_path)

        # Convert the image to grayscale
        gray_image = image.convert('L')

        # Get the dimensions of the image
        width, height = gray_image.size

        # Create an empty image for the result
        edge_image = Image.new('L', (width, height))

        # Sobel operators for detecting horizontal and vertical edges
        sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

        for x in range(1, width - 1):
            for y in range(1, height - 1):
                pixel_x = sum(gray_image.getpixel((i, j)) * sobel_x[i - x + 1][j - y + 1] for i in range(x - 1, x + 2) for j in range(y - 1, y + 2))
                pixel_y = sum(gray_image.getpixel((i, j)) * sobel_y[i - x + 1][j - y + 1] for i in range(x - 1, x + 2) for j in range(y - 1, y + 2))
                edge_image.putpixel((x, y), int((pixel_x ** 2 + pixel_y ** 2) ** 0.5))

        # Save the processed image
        edge_image.save(output_image_path)
        print(f"Sobel filter applied and saved to {output_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sobel_filter.py <input_image> <output_image>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    apply_sobel_filter(input_image_path, output_image_path)
