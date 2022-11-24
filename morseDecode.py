morse = '  .... . -.--   .--- ..- -.. .'
dic = {"....": "H", ".": "E", "-.--": "Y", ".---": "J", "..-": "U", "-..": "D"}

sd = ""
# morse = morse.strip().replace("  "," ").split(" ")
arr = morse.strip().replace("  "," ").split(" ")
for i in arr:
    if i == "":
        sd += " "
    else:
        sd +=dic.get(i)
