#
from PIL import Image


def main():
    image = Image.open('/Users/guanbinbin/IMG_9186的副本.JPG')
    # image.format, image.size, image.mode  ('JPG', (500, 750), 'RGB')
    # image.show()
    # rect = 80, 20, 310, 360
    
    image.crop(rect).show()
if __name__ == '__main__':
    main()
