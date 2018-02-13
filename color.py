from math import floor
from random import randint

def newColor(own = None, target = None):
    gen = {
        "r": floor(randint(0,255)),
        "g": floor(randint(0,255)),
        "b": floor(randint(0,255))
    }
    if own and target:
        gen["r"] = closeColor(own["r"], target["r"])
        gen["g"] = closeColor(own["g"], target["g"])
        gen["b"] = closeColor(own["b"], target["b"])

    return gen

def closeColor(own, target):
    if own > target:
        return floor(randint(0, own))
    elif own < target:
        return floor(randint(own, 255))
    else:
        return own
