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
scale = 0.1 # Where 1 is a 1:1 scale
name = 'imageName'
path = name+ '.jpg' # Change '.jpg' if using another file extension
fontPath = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
```

3. Run the code
	An image output will be created in the code directory with the name `name`_ascii.png

![alt text](https://github.com/OliverKTK/Img-to-ASCII/blob/main/monalisa_ascii.png?raw=true)