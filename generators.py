
def all_variants(text):


    for i in range(len(text)):
        for x in range(i + 1, len(text)+ 1):

            yield text[i:x]

wor = all_variants(text='abc')
print(wor)
for val in wor:
    print(val)



