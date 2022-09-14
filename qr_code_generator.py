#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Wed Sep 14 2022
# version ='1.0'

# Import libraries
# Function to get text/URI and convert to QR Code
# Save QR Code as image

import qrcode


def generate_qrcode(text, filename):

    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{filename}.png")


qr_input = input(" Enter URI or text: ") # Text for QR Code
qr_name = input(" Name to save file as (*.png): ") # Filename for image
generate_qrcode(qr_input, qr_name) # Generate QR Code using user input
