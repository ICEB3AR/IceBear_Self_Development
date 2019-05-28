import Image
 
def bitSolve(img):
    img = Image.open(file)
    width, height = img.size
 
    for x in range(width):
        for y in range(height):
            curr_color = img.getpixel( (x,y) )
            r,g,b = curr_color
 
            if r&4 != 0:
                r,g,b = (0xFF, 0xFF, 0xFF)
            else:
                r,g,b = (0, 0, 0)
 
            img.putpixel( (x,y), (r,g,b) )
 
    img.save("solved.png","png")
 
if __name__ == '__main__':
    file = "pic.png"
    bitSolve(file)
