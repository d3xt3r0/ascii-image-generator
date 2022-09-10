from PIL import Image


ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def read_image(loc):
    '''
    Read image
    '''
    try:
        image = Image.open(loc)
        width, height = image.size
        print(f"Successfully loaded the image!\nImage Size: {width} x {height}\n")

    except FileNotFoundError as error:
        print(error)

    # convert the image as a 2D array

    pixel_data = list(image.getdata())

    pixel_matrix = []
    
    for i in range(0,len(pixel_data),image.width):
        pixel_matrix.append(pixel_data[i : i + image.width])

    return pixel_matrix


def get_intensity_matrix(pixel_matrix):

    '''
    Convert the RGB values of each pixel to a single brightenss value.

    '''

    intensity_matrix = []

    for row in pixel_matrix:
        temp = []
        for value in row:
            avg = (value[0] + value[1] + value[2])/ 3
            temp.append(avg)
        intensity_matrix.append(temp)

    return intensity_matrix


def convert_to_ascii(intensity_matrix, ascii_chars):
    '''
    map each intensity value to appropriate ascii character
    
    '''

    ascii_matrix = []

    for row in intensity_matrix:
        temp = []
        for value in row:
            temp.append(ascii_chars[int(value/255 * len(ascii_chars))])
        ascii_matrix.append(temp)

    return ascii_matrix




if __name__ == "__main__":
    print("Welcome to ascii-art-generator!\n")

    pixel_matrix = read_image("res/ascii-pineapple.jpg")
    intensity_matrix = get_intensity_matrix(pixel_matrix)
    ascii_matrix = convert_to_ascii(intensity_matrix, ASCII_CHARS)

    print(ascii_matrix[-1])