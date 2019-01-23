"""
Used to quickly tag image data
"""
import json
from os import listdir, remove

import pyglet

###
# CONST
###
HEIGHT = 1080
WIDTH = 1920
FONT_SIZE = 36
IMAGE_DIR = 'images'

HORNS = 1
NO_HORNS = 0


###
# Manifest/Images
###
class State(object):
    manifest = {}
    images = []
    current_image = None
    num_yes = 0
    num_no = 0

    image_obj = None
    label_obj = None
    yes_obj = None
    no_obj = None

    def __init__(self):
        with open('manifest.json', 'rb') as manifest_file:
            self.manifest = json.loads(manifest_file.read())

        for m in self.manifest:
            if self.manifest[m] == HORNS:
                self.num_yes += 1
            else:
                self.num_no += 1

        self.images = [f for f in listdir(IMAGE_DIR) if f not in self.manifest]
        self.next()

    def save(self):
        with open('manifest.json', 'wb') as outfile:
            outfile.write(json.dumps(self.manifest))

    def tag(self, value):
        if value == HORNS:
            self.num_yes += 1
        else:
            self.num_no += 1

        self.manifest[self.current_image] = value

    def next(self):
        self.current_image = self.images.pop()
        try:
            self.image_obj = pyglet.resource.image("{0}/{1}".format(IMAGE_DIR, self.current_image))
            self.image_obj.scale = (
                min(self.image_obj.height, HEIGHT) / max(self.image_obj.height, HEIGHT),
                min(self.image_obj.width, WIDTH) / max(self.image_obj.width, WIDTH)
            )
            self.image_obj.width = WIDTH
            self.image_obj.height = HEIGHT
            self.image_obj.texture.width = WIDTH
            self.image_obj.texture.height = HEIGHT
        except pyglet.image.codecs.ImageDecodeException:
            print("ERROR LOADING FILE '{0}/{1}'".format(IMAGE_DIR, self.current_image))
            remove("{0}/{1}".format(IMAGE_DIR, self.current_image))
            self.next()
            return

        self.label_obj = pyglet.text.Label(
            "{0} new, {1} done".format(len(self.images), len(self.manifest)),
            font_name="Times New Roman",
            font_size=FONT_SIZE,
            x=WIDTH/2,
            y=FONT_SIZE,
            anchor_x='center'
        )

        self.yes_obj = pyglet.text.Label(
            "({0}) Yes Horns >".format(self.num_yes),
            font_name="Times New Roman",
            font_size=FONT_SIZE,
            x=WIDTH-FONT_SIZE,
            y=FONT_SIZE,
            anchor_x='right'
        )
        self.no_obj = pyglet.text.Label(
            "< No Horns ({0})".format(self.num_no),
            font_name="Times New Roman",
            font_size=FONT_SIZE,
            x=FONT_SIZE,
            y=FONT_SIZE,
        )


STATE = State()


###
# pyglet Objects/Helpers
###
window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption="Deer Tinder - Feeling Horny?")


@window.event
def on_draw():
    window.clear()
    if STATE.image_obj:
        STATE.image_obj.blit(0, 0)
    if STATE.label_obj:
        STATE.label_obj.draw()
    if STATE.yes_obj:
        STATE.yes_obj.draw()
    if STATE.no_obj:
        STATE.no_obj.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        STATE.tag(NO_HORNS)
        print("no")
        STATE.next()
    elif symbol == pyglet.window.key.RIGHT:
        STATE.tag(HORNS)
        print("HELL YEAH")
        STATE.next()
    elif symbol == pyglet.window.key.S:
        print("Saving...")
        STATE.save()


###
# State
###
pyglet.app.run()
