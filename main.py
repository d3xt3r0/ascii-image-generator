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
    image.thumbnail((300, 100))
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
            temp.append(ascii_chars[int(value * (len(ascii_chars) / 255) ) - 1])
        ascii_matrix.append(temp)

    return ascii_matrix


def print_ascii_matrix(ascii_matrix):
    '''
    you thought right, it prints the ascii matrix
    
    '''
    # print("\n")
    # for row in ascii_matrix:
    #     for pixel in row:
    #         print(pixel,end="")

    for row in ascii_matrix:
        line = [p+p for p in row]
        print("".join(line))





if __name__ == "__main__":
    print("Welcome to ascii-art-generator!\n")

    pixel_matrix = read_image("res/test.png")
    intensity_matrix = get_intensity_matrix(pixel_matrix)
    ascii_matrix = convert_to_ascii(intensity_matrix, ASCII_CHARS)
    print_ascii_matrix(ascii_matrix)