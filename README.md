# Img-to-ASCII
Written in Python using PILLOW library
## Converts an image into a ASCII art
1. Clone the repository:

```
$ git clone git@github.com:OliverKTK/Img-to-ASCII.git
```

2. Change variables:
	Change `path` and `fontPath`. Can also change spacing between letters and the scale in relation to the original image 

``` 
charWidth = 11
charHeight = 13
scale = 0.1 # where 1 is a 1:1 scale
path = 'image.jpg'
fontPath = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
nameOutput = 'output'
```

3. Run the code
	An image output will be created in the code directory

![alt text](https://github.com/OliverKTK/Img-to-ASCII/blob/main/monalisa_ascii.png?raw=true)