import cv2
import image, ImageEnhance
def main():
    filename = 'cat.png'
    image = Image.open(filename)
    size = width, height = image.size

    enchancer = ImageEnhance.Bightness(image)
    image = enchancer.enchance( 0.5 )
    image.save("modified_" + filename)
    del image

if (__name__ == "__main__"):
    main()