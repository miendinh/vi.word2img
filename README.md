# vi.word2img

A tool to generate text image dataset for Deeplearning OCR project.

![](images/rang.jpg) ![](images/tram.jpg) ![](images/nam.jpg)![](images/cung.jpg) ![](images/tu.jpg)  ![](images/day.jpg)

![](images/cua.jpg) ![](images/tin.jpg) ![](images/con2.jpg) ![](images/mot.jpg) ![](images/chut.jpg) ![](images/nay.jpg) ![](images/lam.jpg) ![](images/nghi.jpg)

```
usage: word2img.py [-h] [--font_size FONT_SIZE] [--font_dir FONT_DIR]
                   [--font_color FONT_COLOR [FONT_COLOR ...]]
                   [--bg_color BG_COLOR [BG_COLOR ...]]
                   [--dictionary DICTIONARY] [--image_width IMAGE_WIDTH]
                   [--image_height IMAGE_HEIGHT] [--output_dir OUTPUT_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --font_size FONT_SIZE
                        Font size
  --font_dir FONT_DIR   Font dir
  --font_color FONT_COLOR [FONT_COLOR ...]
                        color of text in image RBG.
                        Ex: --font_color 255 255 255
  --bg_color BG_COLOR [BG_COLOR ...]
                        background color of output text image RBG.
                        Ex: --bg_color 0 0 0
  --dictionary DICTIONARY
                        List of vocabulary
  --image_width IMAGE_WIDTH
                        width of output image (pixel)
  --image_height IMAGE_HEIGHT
                        height of output image (pixel)
  --output_dir OUTPUT_DIR
                        output dir
```                        
