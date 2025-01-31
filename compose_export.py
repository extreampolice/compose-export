#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=nmb-0KcgXzI
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *
    
def layer_to_image(layer):
    buffer = pdb.gimp_edit_named_copy(layer, "LAYER")
    new_image = pdb.gimp_edit_named_paste_as_new_image(buffer)
    return new_image

def compose_export(image, drawable, filename):
    if len(image.layers) < 4:
        pdb.gimp_message("You currently have {} layers in your image. You need at least 4 layers to perform this action".format(len(image.layers)))
        return
    compose_type = "RGBA"
    image1 = layer_to_image(image.layers[0])
    image2 = layer_to_image(image.layers[1])
    image3 = layer_to_image(image.layers[2])
    image4 = layer_to_image(image.layers[3])
    new_image = pdb.plug_in_compose(image1, drawable, image2, image3, image4, compose_type)
    pdb.file_tga_save(new_image, new_image.layers[0], filename, filename, 0, 1)

register(
    "python-fu-compose-export",
    "Compose-export",
    "Composes the the current image and exports it",
    "extreampolice", "extreampolice", "2025",
    "compose-export",
    "GRAY*", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_FILENAME, "filename", "file name", "D:\SteamLibrary\steamapps\common\War Thunder\UserSkins")
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    compose_export, menu="<Image>")  # second item is menu location

main()