from PIL import Image
import streamlit as st
from io import BytesIO


# function to paste the image
def paste_image_to_center(image1, image2):
    # make image2 to be transparent
    image2 = image2.convert("RGBA")
    opacity = 0.2
    image2.putalpha(int(255 * opacity))
    # get the size of image1
    width1, height1 = image1.size
    # get the size of image2
    width2, height2 = image2.size

    if width1 > height1:
        # resize image2 to be the same height as image1
        image2 = image2.resize((int(width2 * height1 / height2), height1))
    else:
        # resize image2 to be the same width as image1
        image2 = image2.resize((width1, int(height2 * width1 / width2)))

    # get the size of image2 after resizing
    width2, height2 = image2.size
    # paste image2 to the center of image1
    image1.paste(image2, (int((width1 - width2) / 2),
                 int((height1 - height2) / 2)), image2)
    return image1


flag_image = Image.open('bayrak.jpg')


back_file = st.file_uploader("Fotoğraf")

if back_file is not None:
    # check if it is not an image
    if not back_file.type.startswith('image/'):
        st.error('Lütfen bir resim dosyası seçin.')
    else:
        back_image = Image.open(back_file)

        # prepare red image with size of your_image and opacity of 0.5
        red_image = Image.new("RGBA", back_image.size, (228, 0, 0, 128))

        # paste the your_image to red_image
        back_image.paste(red_image, (0, 0), red_image)

        new_image = paste_image_to_center(back_image, flag_image)

        # new_image to bytes
        new_image_bytes = BytesIO()
        new_image.save(new_image_bytes, format='PNG')

        st.download_button(
            label="İndir",
            data=new_image_bytes,
            file_name="29ekim.png",
            mime="image/png",
        )

        st.image(new_image, use_column_width=True)
