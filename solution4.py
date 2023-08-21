bcainfo="""BCA course information:
Bachelor of computer Application.
It is a three years undergraduate course."""

with open('BCA.txt','w') as bca:
    bca.write(bcainfo)

rows={'A':0,'B':0,'C':0}

with open('BCA.txt','r') as intro_file:
    lines=intro_file.readlines()
    for line in lines:
            f_char=line.strip()[0]
            if f_char in rows:
                rows[f_char]+=1

for char,count in rows.items():
    print(f"Number of rows start with '{char}':{count}")