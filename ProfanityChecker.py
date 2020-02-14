lines = []
while True:
    line = input()
    if line == 'q' or line =="Q":
        break
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)



profanity_words = ['something','dog','other','example'] # Your creativity goes in this list.

if any(word in text for word in profanity_words):
    print('Your paragraph contains profanity.')
else:
    print("Clear. Go ahead.")