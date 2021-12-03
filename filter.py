from PIL import Image
import numpy as np

def editPicture(arrPixels,mozaicSize):
    return  np.array(arrPixels[:len(arrPixels) - len(arrPixels) % mozaicSize, :len(arrPixels[0]) - len(arrPixels[0]) % mozaicSize])

def setShadeOfGray(arrPixels,x,y,mozaicSize,gradation):
    curentShade =np.concatenate(arrPixels[x:x+mozaicSize,y:y+mozaicSize]).sum()/3
    return (curentShade// mozaicSize ** 2// gradation) * gradation

def setColor(arrPixels,color,row,col,mozaicSize):
    arrPixels[row:row + mozaicSize, col:col + mozaicSize] = [color,color,color]
    return arrPixels

def convert_image_to_mosaic(img_in='img2.jpg',img_out='res.jpg',block_size=10,gradation_step=50):
    arrPixels=np.array(Image.open(f"{img_in}"))
    arrPixels = editPicture(np.array(Image.open(f"img2.jpg")),block_size)
    for row in range(0, len(arrPixels), block_size):
        for col in range(0, len(arrPixels[1]), block_size):
            color = setShadeOfGray(arrPixels,row,col,block_size,gradation_step)
            arrPixels = setColor(arrPixels,color,row,col,block_size)
    res = Image.fromarray(arrPixels)
    res.save(f'{img_out}')


convert_image_to_mosaic(img_in='img2.jpg',img_out='res.jpg',block_size=10,gradation_step=50)
convert_image_to_mosaic(img_in='img2.jpg',img_out='res2.jpg',block_size=15,gradation_step=63)
convert_image_to_mosaic(img_in='img2.jpg',img_out='res3.jpg',block_size=1,gradation_step=1)


# i = 0
# while i < a:
#     j = 0
#     while j < a1:
#         s = 0
#         for n in range(i, i + 10):
#             for n1 in range(j, j + 10):
#                 num1 = int(arr[n][n1][0])
#                 num2 = int(arr[n][n1][1])
#                 num3 = int(arr[n][n1][2])
#                 M = (num1 + num2 + num3)/3
#                 s += M
#         s = int(s // 100)
#         for n in range(i, i + 10):
#             for n1 in range(j, j + 10):
#                 arr[n][n1][0] = int(s // 50) * 50
#                 arr[n][n1][1] = int(s // 50) * 50
#                 arr[n][n1][2] = int(s // 50) * 50
#         j = j + 10
#     i = i + 10
