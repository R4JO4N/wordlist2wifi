#author: rajoan

#Please change 'rockyou.txt' to your file name if your file name is different.(for most cases it is)
           
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as infile, open('filtered.txt','w',encoding='utf-8', errors='ignore') as outfile:
    for line in infile:
        password=line.strip()
        if len(password)>=8:
            outfile.write(password+'\n')