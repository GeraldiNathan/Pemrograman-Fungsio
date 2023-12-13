from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance

image = Image.open("C:\Kuliah\Semester 5\Fungsio\Praktikum\All Modules\Modules\Praktikum\Modul 6/assets\img\calvin_selfie.jpg")

enhancer = ImageEnhance.Brightness(image)
brightened = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened)
final = enhancer.enhance(1.2)

# final.save("gyjawaw.jpg")
final.show()