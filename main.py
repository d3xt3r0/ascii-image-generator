from PIL import Image

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
            avg = value[0] + value[1] + value[2] / 3
            temp.append(avg)
        intensity_matrix.append(temp)

    return intensity_matrix




if __name__ == "__main__":
    print("Welcome to ascii-art-generator!\n")
    pixel_matrix = read_image("res/ascii-pineapple.jpg")
    intensity_matrix = get_intensity_matrix(pixel_matrix)