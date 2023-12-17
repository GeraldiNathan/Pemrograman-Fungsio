from PIL import Image

background_path = "C:\Kuliah\Semester 5\Fungsio\Praktikum\All Modules\Modules\Praktikum\Modul 6\codelab/assets\img\geral.jpg"
overlay_path = "C:\Kuliah\Semester 5\Fungsio\Praktikum\All Modules\Modules\Praktikum\Modul 6\codelab/assets\img\osborn.jpg"
background = Image.open(background_path)
overlay = Image.open(overlay_path)
overlay = overlay.convert("RGBA")
overlay = overlay.resize((1200, 1200))
x_position = 1000
y_position = 850
background.paste(overlay, (x_position, y_position), overlay)
background.save("percobaan2.jpg")
background.show()