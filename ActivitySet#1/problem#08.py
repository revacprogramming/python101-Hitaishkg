text = "X-DSPAM-Confidence:    0.8475"
start=text.find(":")
piece=text[start+1:]
end=float(piece)
print(end)