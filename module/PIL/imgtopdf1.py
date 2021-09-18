from PIL import Image
img=Image.open('shivamimg.jpg')
im=img.convert('RGB')
im.save('newpdf.pdf')