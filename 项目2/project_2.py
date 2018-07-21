from PIL import Image


"""
# 先介绍一个新函数, 原型如下
# Image.new(mode, size)
# mode 是字符串, 我们使用 'RGBA' 表示生成一个每个像素由 rgba 四字节组成的图片
# size 是一个 (w, h) 表示宽高的 tuple

# 具体例子如下
# 生成一个宽高都是 100 的 rgba 模式的 Image 对象
# img = Image.new("RGBA", (100, 100))
"""


def crop(image, frame):
    """
    image 是一个 Image 对象
    frame 是一个 tuple 如下 (x, y, w, h)
        用于表示一个矩形的左上角座标 x y 和 宽高 w h

    不修改原图像
    返回一个 Image 对象, 它是用 frame 把 image 裁剪出来的新图像
    """
    x, y, w, h = frame
    # 创建一个 Image 对象
    result = Image.new("RGBA", (w, h))
    # 把 image 中的对应的像素点，放到 result 中
    for i in range(h):
        for j in range(w):
            img_position = (x+j, y+i)
            r, g, b, a = image.getpixel(img_position)
            result_postion = (j, i)
            result.putpixel(result_postion, (r, g, b, a))
    return result


def flip(image):
    """
    image 是一个 Image 对象

    不修改原图像
    返回一个 Image 对象, 它是 image 上下镜像的图像
    """
    h = image.height
    w = image.width
    # 创建一个 Image 对象
    result = Image.new("RGBA", (w, h))
    # 把 image 中的对应的像素点，放到 result 中
    for i in range(h):
        for j in range(w):
            img_position = (j, i)
            r, g, b, a = image.getpixel(img_position)
            result_postion = (j, h-1-i)
            result.putpixel(result_postion, (r, g, b, a))
    return result


def flop(image):
    """
    image 是一个 Image 对象

    不修改原图像
    返回一个 Image 对象, 它是 image 左右镜像的图像
    """
    h = image.height
    w = image.width
    # 创建一个 Image 对象
    result = Image.new("RGBA", (w, h))
    # 把 image 中的对应的像素点，放到 result 中
    for i in range(h):
        for j in range(w):
            img_position = (j, i)
            r, g, b, a = image.getpixel(img_position)
            result_postion = (w-1-j, i)
            result.putpixel(result_postion, (r, g, b, a))
    return result

def main():
    """
    压缩包内有图片 a.jpg
    图片是面朝左的 doge 加下方的四个字
    要求生成一张图片 b.jpg, 狗头朝右但下方文字不变
    """
    # 打开图像文件
    img = Image.open("a.jpg")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')
    #
    img_top = crop(img, frame=(0, 0, 111, 95))
    img_top = flop(img_top)
    # 将 img_top 写入 img
    h = img_top.height
    w = img_top.width
    for i in range(h):
        for j in range(w):
            position = (j, i)
            r, g, b, a = img_top.getpixel(position)
            img.putpixel(position, (r, g, b, a))
    img.save('img_main.png')


if __name__ == '__main__':
    # # 打开图像文件
    # img = Image.open("a.jpg")
    # # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    # img = img.convert('RGBA')
    # 调用函数，对图片进行操作
    # img = flop(img)
    # 保存
    # img.save('img_flop.png')

    main()
