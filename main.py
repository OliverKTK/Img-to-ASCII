from PIL import Image, ImageDraw, ImageFont
import math


# Characters used for the ascii art
# chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`. "[::-1]
chars = "$B8W#ohbpwZ0LJYzvnrf/|){[?_~>!I:^. "[::-1]
# chars = " .:-=+*#%@"

# Maps the chars into an array and divedes it for their range
charArray = list(chars)
charLen = len(charArray)
interval = charLen/256

# The Height and Width of eacch character
charWidth = 11
charHeight = 13

# Gets the char for the value
def getChar(value):
    return charArray[math.floor(value*interval)]

# Resizes Image for delta as a scale
def imageResize(image, delta, charWidth, charHeight):
    width, height = image.size
    width = int(width*delta)
    height = int(height*delta*(charWidth/charHeight))
    return width, height


# Opens image/ gets font used and resizes it
im = Image.open("duck.jpg").convert("RGB")
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
width, height = imageResize(im, 0.1, charWidth, charHeight)
im = im.resize((width, height))
pix = im.load()

# Create canvas for the ascii art
outputImg = Image.new('RGB', (charWidth*width, charHeight*height), color = (0,0,0))
d = ImageDraw.Draw(outputImg)


print(width, height)

# Iterates for each pixxel in Image and writes the char in the canvas
for i in range(width):
    for j in range(height):
        r, g, b = pix[i,j]
        value = int((r+g+b)/3)
        d.text((i*charWidth, j*charHeight), getChar(value), font= font, fill = (r, g, b))

# Saves the result
outputImg.save('output.png')

