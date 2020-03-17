#
# from PIL import Image
from PIL import Image, ImageFilter

def main():
    image = Image.open('/Users/guanbinbin/IMG_9186的副本.JPG')
    # image.format, image.size, image.mode  ('JPG', (500, 750), 'RGB')
    # image.show()
    # rect = 80, 20, 310, 360
    # size = 128, 128
    # image.rotate(180).show()
    # image.transpose(Image.FLIP_LEFT_RIGHT).show()
    image.filter(ImageFilter.CONTOUR).show()
if __name__ == '__main__':
    main()
