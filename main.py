from PIL import Image

def read_image(loc):
    '''
    Read image
    '''
    try:
        image = Image.open(loc)
        width, height = image.size
        print(f"Width = {width}\nHeight = {height}")
    except FileNotFoundError as error:
        print(error)


if __name__ == "__main__":
    print("Welcome to ascii-art-generator!")
    read_image("res/ascii-pineapple.jpg")