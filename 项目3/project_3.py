from PIL import Image


def rorate_left(image):
    """
    image 是一个 Image 对象
    返回一个全新图像，它是 image 左转 90 度后的图像
    """
    h = image.height
    w = image.width
    # 创建一个 Image 对象
    result = Image.new("RGBA", (h, w))
    # 把 image 中的对应的像素点，放到 result 中
    for i in range(h):
        for j in range(w):
            img_position = (j, i)
            r, g, b, a = image.getpixel(img_position)
            result_postion = (i, w-1-j)
            result.putpixel(result_postion, (r, g, b, a))
    return result


def rorate_right(image):
    """
    image 是一个 Image 对象
    返回一个全新图像，它是 image 右转 90 度后的图像
    """
    h = image.height
    w = image.width
    # 创建一个 Image 对象
    result = Image.new("RGBA", (h, w))
    # 把 image 中的对应的像素点，放到 result 中
    for i in range(h):
        for j in range(w):
            img_position = (j, i)
            r, g, b, a = image.getpixel(img_position)
            result_postion = (h - 1 - i, j)
            result.putpixel(result_postion, (r, g, b, a))
    return result


def rorate_180(image):
    """
    image 是一个 Image 对象
    返回一个全新图像，它是 image 旋转 180 度后的图像
    """
    image = rorate_right(image)
    result = rorate_right(image)
    return result

if __name__ == '__main__':
    # 打开图像文件
    img = Image.open("a.jpg")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')
    #
    img = rorate_180(img)
    img.save('img_rorate_180.png')
