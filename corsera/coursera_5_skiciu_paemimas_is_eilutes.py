text = "X-DSPAM-Confidence:    0.8475"
pirmas = text.find('0')
antras = text[pirmas:]
ats = float(antras)
print(antras)