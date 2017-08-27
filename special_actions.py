#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wand.image import Image
from wand.drawing import Drawing

class SpecialActions():

    def __init__(self):
        pass

    @staticmethod
    def create_image_search(image_name, text):
        """creates an image with the given string"""
        with Image(filename=image_name) as img:
            with img.clone() as cloned:
                cloned.format = 'png'
                with Drawing() as draw:
                    draw.font_family = 'italic'
                    draw.font_size = 40
                    text = SpecialActions.simplifying(text)
                    draw.text(148, 800, text)
                    draw(cloned)
                    cloned.save(filename="generated_meme_search.png")

    @staticmethod
    def simplifying(text):
        """Tokenizes the text by fragments of 20 chars"""
        str(text)
        size = len(text) / 20
        i = 0
        while i < (size - 1):
            text += text[size*0:size*1] + "\n"
            i += 1
        return text
