'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
word = 'Pig latin is cool'
arr = word.split(" ")
output = ""
for i in arr:
    letter = i[0]
    i = i[1:] + letter+"ay"
    output =output+" "+ i
output = output.strip();
    