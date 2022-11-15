import cv2
from PIL import Image, ImageDraw, ImageFont

original_konjiki_img = "images/konjikido_01.jpg"


def paste_img():

    # Pillowで画像を開く
    konjiki_img = Image.open(original_konjiki_img)
    # 顔に合ったサイズに画像をリサイズしてフォルダに保存
    new_konjiki_img = konjiki_img.resize((800, 400))
    draw = ImageDraw.Draw(new_konjiki_img)
    font = ImageFont.truetype(
        "C:/Windows/Fonts/msgothic.ttc",
        100,
    )
    draw.text((400, 200), "平泉 最高", "red", font=font, anchor="mm")
    new_konjiki_img.save("images/resized_konjiki_img.jpg")

    konjiki_list = new_konjiki_img
    return konjiki_list


print(paste_img())
