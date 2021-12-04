def im_changes():
    from PIL import Image

    try:
        image = Image.open("images/source/mustang.jpg")
        # image2 = Image.open("images/source/watermark.jpg")
        # image2 = Image.open("images/source/watermark3.png")
        # image2 = Image.open("images/source/watermark4.png")
        image2 = Image.open("images/source/watermark5.png")
    except FileNotFoundError:
        print("File is not found")
    image2.thumbnail((300, 300))

    def watermark(input_image, watermark_image, x_offset, y_offset):
        pixels = input_image.load()
        pixels_source = watermark_image.load()
        width, height = input_image.size[0], input_image.size[1]
        width_source, height_source = watermark_image.size[0], watermark_image.size[1]
        for x in range(0, width_source):
            for y in range(0, height_source):
                try:
                    if x <= width and y <= height:
                        if not pixels_source[x, y] == (0, 0, 0, 255):
                            pixels[x + x_offset, y + y_offset] = pixels_source[x, y]
                except IndexError:
                    return print("!!!!Inserted image is out of background image!!!!")
        input_image.show()
        input_image.save("images/image_with_watermark.jpg")

    watermark(image, image2, 500, 500)
