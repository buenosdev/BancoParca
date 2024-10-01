
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pywinstyles

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\DaviBueno\Downloads\TkInter\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#F8F9FC")


canvas = Canvas(
    window,
    bg = "#F8F9FC",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    1080.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1.0,
    0.0,
    304.0,
    1080.0,
    fill="#B6CAE2",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    background='#cccccc',
    activebackground='#cccccc'
)
pywinstyles.set_opacity(button_1, color='#cccccc')
button_1.place(
    x=39.0,
    y=279.0,
    width=225.0,
    height=74.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    background='#cccccc',
    activebackground='#cccccc'
)
pywinstyles.set_opacity(button_2, color='#cccccc')
button_2.place(
    x=39.0,
    y=180.0,
    width=225.0,
    height=74.0
)

canvas.create_rectangle(
    47.0,
    927.0,
    245.0,
    928.0,
    fill="#ECECEE",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    158.0,
    102.0,
    image=image_image_1
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    background='#cccccc',
    activebackground='#cccccc'
)
pywinstyles.set_opacity(button_3, color='#cccccc')
button_3.place(
    x=39.0,
    y=938.0,
    width=225.0,
    height=73.0
)

canvas.create_rectangle(
    365.0,
    41.0,
    902.0,
    1027.0,
    fill="#B6CAE2",
    outline="")

canvas.create_rectangle(
    924.439453125,
    44.093994140625,
    1864.348388671875,
    1027.0,
    fill="#F3F3F3",
    outline="")

canvas.create_rectangle(
    924.0,
    44.0,
    1864.0,
    181.0,
    fill="#B6CAE2",
    outline="")

canvas.create_text(
    1473.0,
    100.80584716796875,
    anchor="nw",
    text="*******",
    fill="#4978B0",
    font=("SourceSansPro Bold", 50 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    background='#cccccc',
    activebackground='#cccccc'
)
pywinstyles.set_opacity(button_4, color='#cccccc')
button_4.place(
    x=1727.3583984375,
    y=95.53799438476562,
    width=48.0802001953125,
    height=35.384002685546875
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    background='#cccccc',
    activebackground='#cccccc'
)
pywinstyles.set_opacity(button_5, color='#cccccc')
button_5.place(
    x=656.609375,
    y=461.7156982421875,
    width=188.390869140625,
    height=188.390869140625
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    background='#cccccc',
    activebackground='#cccccc'
)
pywinstyles.set_opacity(button_6, color='#cccccc')
button_6.place(
    x=656.609375,
    y=713.609130859375,
    width=188.390869140625,
    height=188.390869140625
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    background='#cccccc',
    activebackground='#cccccc'
)
pywinstyles.set_opacity(button_7, color='#cccccc')
button_7.place(
    x=428.0,
    y=713.4923706054688,
    width=188.390869140625,
    height=188.390869140625
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    background='#cccccc',
    activebackground='#cccccc'
)
pywinstyles.set_opacity(button_8, color='#cccccc')
button_8.place(
    x=428.0,
    y=461.5989990234375,
    width=188.390869140625,
    height=188.390869140625
)

canvas.create_text(
    439.0,
    315.0,
    anchor="nw",
    text="Bem vindo, Fulano!",
    fill="#4978B0",
    font=("Heebo Regular", 48 * -1)
)

canvas.create_text(
    957.0,
    81.0,
    anchor="nw",
    text="Saldo em conta:",
    fill="#4978B0",
    font=("SourceSansPro SemiBold", 48 * -1)
)

canvas.create_text(
    519.0,
    120.0,
    anchor="nw",
    text="Banco Parça",
    fill="#4978B0",
    font=("Heebo Regular", 48 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    474.0,
    160.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
