from PIL import Image, ImageOps, ImageDraw, ImageFont

img = Image.open("C:\Kuliah\Semester 5\Fungsio\Praktikum\All Modules\Modules\Praktikum\Modul 6/assets\img\calvin_selfie.jpg")

fontPath = "C:\Kuliah\Semester 5\Fungsio\Praktikum\All Modules\Modules\Praktikum\Modul 6/assets/font\Montserrat-Italic-VariableFont_wght.ttf"
customFont = ImageFont.truetype(fontPath, 30)


# change color into dust
imgAfter = ImageOps.grayscale(img.copy())
draw = ImageDraw.Draw(imgAfter)
text = "DIS IS MY PREN FROM LUMAJANG KELPIN SANTOSO"
image_width, image_height = img.size
# text_width, text_height = draw.textsize(text, font=customFont)

bbox = draw.textbbox((8, 8), text, font=customFont)
text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

text_position = (
    (image_width - text_width) // 2,
    (image_height - text_height) // 3,
    )
draw.text(text_position, text, font=customFont, fill="black")


imgAfter.save("output_image.jpg")
imgAfter.show()