from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter, ImageEnhance
import os

# TODO 1  : Buka gambar dengan pillow
background = Image.open("C:\\Kuliah\\Semester 5\\Fungsio\\Praktikum\\All Modules\\Modules\\Praktikum\\Modul 6\\praktikum\\assets\\bgUmm.jpg")
overlay = Image.open("C:\\Kuliah\\Semester 5\\Fungsio\\Praktikum\\All Modules\\Modules\\Praktikum\\Modul 6\\praktikum\\assets\\umm.jpg")
font_path = "C:\\Kuliah\\Semester 5\\Fungsio\\Praktikum\\All Modules\\Modules\\Praktikum\\Modul 6\\codelab\\assets\\font\\Montserrat-Italic-VariableFont_wght.ttf"

background = background.resize((1920, 1080))

# TODO 2 : Rotate 30 derajat & Grayscale
rotated_bg = ImageOps.grayscale(background.copy()).rotate(30)
final_bg = rotated_bg.filter(ImageFilter.BLUR)

# TODO 3 : Tingat kecerahan dan kontras to 1.51 (NIM 351)
brightness_factor = 1.51
contrast_factor = 1.51

enhancer = ImageEnhance.Brightness(overlay.copy())
brightened = enhancer.enhance(brightness_factor)

enhancer = ImageEnhance.Contrast(brightened)
contrast_enhanced = enhancer.enhance(contrast_factor)

# TODO 4: Menyisipkan Overlay
overlay = brightened.resize((600, 600))
overlay_position = (600, 300)

# TODO 5: Text Overlay
padding = 200
customFont = ImageFont.truetype(font_path, 24)
draw = ImageDraw.Draw(overlay)
text = "INFORMATIKA JOSSS!"
text_width = draw.textlength(text, font=customFont)
text_height = draw.textlength(text, font=customFont)


text_position = ((overlay.width - text_width) // 2, overlay.height - text_height + padding)
draw.text(text_position, text, font=customFont, fill="black")

final_result = final_bg.copy()
final_result.paste(overlay, overlay_position)

final_result.show()

# TODO 6 : Save image
save_path = os.path.join("C:\Kuliah\Semester 5\Fungsio\Praktikum\All Modules\Modules\Praktikum\Modul 6\praktikum/result", "tugas_praktikum_enam.png")
final_result.save(save_path)
