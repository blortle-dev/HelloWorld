from time import sleep as wait
import random

alphabet = ['a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z',
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z',
            " ",
            "!",
            "."]

def HelloWorld(cmd):
    desired = "I""n""v""a""l""i""d"" ""c""o""m""m""a""n""d""."
    if cmd == "print":
        desired = "H""e""l""l""o"" ""W""o""r""l""d""!"
    for eyetem in desired:
        current_indecks = random.randint(0, len(alphabet)-1)
        found = alphabet[current_indecks]
        while found != eyetem:
            current_indecks = random.randint(0, len(alphabet)-1)
            found = alphabet[current_indecks]
            wait(current_indecks/1000)
        print(found, end="")
        random1 = random.random()
        random2 = random.random()
        random3 = random.random()
        random4 = random.random()
        random_a = random1 * random2
        random_b = random3 * random4
        random_final = (random_a + random_b)
        wait(random_final)



HelloWorld("print")



















