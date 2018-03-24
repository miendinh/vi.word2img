from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
import os
import random
import argparse
import shutil


def load_vocab(args):
    vocab = {}
    reverse_vocab = {}
    with open(args.dictionary) as viet_dict:
        for idx, word in enumerate(viet_dict):
            vocab[idx] = word.strip()

    reverse_vocab = dict(zip(vocab.values(), vocab.keys()))
    return (vocab, reverse_vocab)

def load_fonts(path):
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


def word2image(word, ttf, name, args):
    image = Image.new(
        "RGB", (args.image_width, args.image_height), args.bg_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(ttf, args.font_size)
    w, h = draw.textsize(word, font=font)
    draw.text(((args.image_width - w) // 2, (args.image_height - h) //
               2), word, args.font_color, font=font)
    print(name)
    image.save(args.output_dir +'/'+ name + '.jpg')


def clean(args):
    if os.path.exists(args.output_dir):
        if args.output_clean:
            shutil.rmtree(args.output_dir)
            while os.path.exists(args.output_dir):
                pass

    os.makedirs(args.output_dir)


def main(args):
    vocab, reverse_vocab = load_vocab(args)
    fonts = list(load_fonts(args.font_dir))
    clean(args)
    count = 0
    print(vocab.values())
    for word in vocab.values():
        for font in fonts:
            print('font:', font)
            name = '{:08d}-{:05d}'.format(count, reverse_vocab[word])
            word2image(word, font, name, args)
            count += 1
    print('Done. Let\'s check your output folder: ', args.output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--font_size', type=int, help='Font size', default=18)
    parser.add_argument('--font_dir', type=str,
                        help='Font dir', default='fonts/test/')
    parser.add_argument('--font_color', nargs='+', type=int,
                        help='Color of text in image RBG. Ex: --font_color 255 255 255', default=[255, 255, 255])
    parser.add_argument('--bg_color', nargs='+', type=int,
                        help='Background color of output text image RBG. Ex: --bg_color 0 0 0', default=[0, 0, 0])
    parser.add_argument('--dictionary', type=str,
                        help='List of vocabulary in txt file', default='dict/test.dic')
    parser.add_argument('--image_width', type=int,
                        help='Width of output image (pixel)', default=100)
    parser.add_argument('--image_height', type=int,
                        help='Height of output image (pixel)', default=32)
    parser.add_argument('--output_dir', type=str,
                        help='Output dir', default='data/train/test/')
    parser.add_argument('--output_clean', type=bool,
                        help='Clean output folder', default=False)

    args = parser.parse_args()
    args.bg_color = tuple(args.bg_color)
    args.font_color = tuple(args.font_color)

    main(args)
