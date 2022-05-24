import os, math
from PIL import Image

'''
这个世界需要更多的英雄!
'''


def merge(list_image):
    '''
    图片拼接，制作大图
    :param list_image: 传入一个列表，列表中包含所有图片对象
    :return: 返回大图
    '''
    long_image = len(list_image)
    n = int(math.sqrt(long_image))
    im = Image.new('RGB', (256 * n, 256 * (n+1)))
    list = iter(list_image)
    num=0
    for i in range(0, n):
        a = i * 256
        for j in range(0, n):
            b = j * 256
            im.paste(next(list), (a, b))
            num+=1
    if num!=long_image:
        b=im.size[0]
        a=0
        for j in list:
            im.paste(j, (a, b))
            a += 256
    else:
        im = im.crop((0,0,256*n,256*n))
    return im


def modify_resolution(im, size=(256, 256)):
    '''
        格式化图片处理
    :param im: 传入一个图片对象
    :param size: 格式化图片像素大小
    :return: 格式化图片对象
    '''
    size1 = im.size
    min_size = min(size1)
    im = im.crop((0, 0, min_size, min_size))
    im = im.resize(size)
    return im


Add_image = '/Users/liujiacheng/Documents/image processing/image'
os.chdir(Add_image)
list_image = os.listdir()
list_im = []
for i in list_image:
    a = os.path.join(Add_image, i)
    im = Image.open(a)
    im = modify_resolution(im)
    list_im.append(im)
im = merge(list_im)
im.show()
os.chdir(Add_image)
im.save('test1.JPEG.JPEG', 'JPEG')
im.close()
