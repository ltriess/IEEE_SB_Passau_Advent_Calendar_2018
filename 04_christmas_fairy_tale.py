import sys

DEBUG = False


def translator(text, alphabet, key):
    trantab = str.maketrans(alphabet, key)
    return text.translate(trantab)


def caesar_decode(ciphertext, s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return translator(ciphertext, alpha, alpha[-s:] + alpha[:-s])


class FrequencyAnalysis:
    def __init__(self, ciphertext):
        cor = [0.0651, 0.0189, 0.0306, 0.0508, 0.1740, 0.0166, 0.0301, 0.0476, 0.0755,
               0.0027, 0.0121, 0.0344, 0.0253, 0.0978, 0.0251, 0.0079, 0.0002, 0.0700,
               0.0727, 0.0615, 0.0435, 0.0067, 0.0189, 0.0003, 0.0004, 0.0113]
        maxval = max(cor)
        self.cor = []
        for i, e in enumerate(cor):
            self.cor.append(e / maxval)

        self.ciphertext = ciphertext.lower()
        self.freq()
        self.min_error()
        self.key = self.minimum[0]
        self.solution = caesar_decode(self.ciphertext, self.minimum[0])

    def freq(self):
        self.arr = [0.0] * 26
        for l in self.ciphertext:
            x = ord(l)
            if x >= 97 and x <= 122:
                self.arr[x - 97] += 1.0
        maxval = max(self.arr)
        for i, e in enumerate(self.arr):
            self.arr[i] = e / maxval

    def error(self):
        e = 0
        for i in range(0, len(self.arr)):
            e += abs(self.arr[i] - self.cor[i]) ** 2
        return e

    def min_error(self):
        self.minimum = [0, 10000]
        for rot in range(0, 25):
            e = self.error()
            # print(rot, e)
            if e < self.minimum[1]:
                self.minimum[1] = e
                self.minimum[0] = rot
            x = self.arr[-1]
            del self.cor[-1]
            self.cor.insert(0, x)


def main():

    if DEBUG:
        sys.stdin = open("samples/04_input.txt")

    count = 0
    ciphertext = ''
    while count < 2:
        try:
            if count == 1:
                ciphertext += '\n\n'
            ciphertext += '{}\n'.format(input())

            count = 0
        except:
            count += 1

    fa = FrequencyAnalysis(ciphertext)
    decrypted = fa.solution

    output = ''
    for i, (encr, decr) in enumerate(zip(ciphertext, decrypted)):
        if encr.isupper():
            output += decr.upper()
        else:
            output += decr

    print(output[:-3])


if __name__ == "__main__":
    main()
