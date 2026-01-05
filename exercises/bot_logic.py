import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
    
    return password

def gen_emodji():
    emodji = [":)", "^v^", "=-=", "XD"]
    return random.choice(emodji)

def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Cara"
    else:
        return "Cruz"


def chiste():
    return (
        "a: ¡POR FAVOR AYÚDAME!, ¡He perdido a mi hija!\n"
        "b: ¿Cómo se llama?\n"
        "a: Esperanza T-T\n"
        "b: ¡Imposible! La esperanza es lo último que se pierde XD jajajajaja..."
    )
