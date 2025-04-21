from PIL import Image
import sys

def apply_sharpen_filter(input_image_path, output_image_path):
    try:
        # Open the image from the file
        image = Image.open(input_image_path)
        width, height = image.size

        # Create an empty image for the result
        sharpened_image = Image.new('RGB', (width, height))

        # Sharpening filter kernel (3x3 matrix)
        kernel = [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ]

        for x in range(1, width - 1):
            for y in range(1, height - 1):
                new_pixel = [0, 0, 0]
                for i in range(3):
                    for j in range(3):
                        pixel = image.getpixel((x + i - 1, y + j - 1))
                        for k in range(3):
                            new_pixel[k] += pixel[k] * kernel[i][j]

                for k in range(3):
                    new_pixel[k] = max(0, min(255, new_pixel[k]))

                sharpened_image.putpixel((x, y), tuple(new_pixel))

        # Save the processed image
        sharpened_image.save(output_image_path)
        print(f"Sharpening filter applied and saved to {output_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sharpen_filter.py <input_image> <output_image>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    apply_sharpen_filter(input_image_path, output_image_path)
