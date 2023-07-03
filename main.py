import cv2

ASCII_CHARS = '@%#*+=-:.[]{};,<>/?\| '

def resize_image(image, new_width=100):
    """
    Resize the image while maintaining the aspect ratio.

    Args:
        image (numpy.ndarray): The input image.
        new_width (int): The desired width of the image (default: 100).

    Returns:
        numpy.ndarray: The resized image.
    """
    width = image.shape[1]
    height = image.shape[0]
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def convert_grayscale(image):
    """
    Convert the image to grayscale.

    Args:
        image (numpy.ndarray): The input image.

    Returns:
        numpy.ndarray: The grayscale image.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def map_pixels_to_ascii(image, range_width=25):
    """
    Map the pixel values of the image to ASCII characters.

    Args:
        image (numpy.ndarray): The input image.
        range_width (int): The range width for mapping pixel values to ASCII characters (default: 25).

    Returns:
        str: The ASCII art representation of the image.
    """
    pixels = image.flatten()
    ascii_str = ''
    for pixel_value in pixels:
        try:
            ascii_str += ASCII_CHARS[pixel_value // range_width]
        except IndexError as e:
            print(f"Error in map_pixels_to_ascii: {e}")
            print(f"pixel_value: {pixel_value}")
            print(f"range_width: {range_width}")
    return ascii_str

def convert_image_to_ascii(image):
    """
    Convert the image to ASCII art.

    Args:
        image (numpy.ndarray): The input image.

    Returns:
        str: The ASCII art representation of the image.
    """
    try:
        image = resize_image(image)
        image = convert_grayscale(image)
        ascii_str = map_pixels_to_ascii(image)
        img_width = image.shape[1]
        ascii_str_len = len(ascii_str)
        ascii_img = ''
        for i in range(0, ascii_str_len, img_width):
            ascii_img += ascii_str[i:i + img_width] + '\n'
        return ascii_img
    except Exception as e:
        print(f"Error in convert_image_to_ascii: {e}")
        return ''

def main(image_path):
    """
    Convert an image to ASCII art and print the result.

    Args:
        image_path (str): The path to the image file.
    """
    try:
        image = cv2.imread(image_path)
        ascii_img = convert_image_to_ascii(image)
        print(ascii_img)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
image_path = r'path/to/your/image.jpg'
main(image_path)
