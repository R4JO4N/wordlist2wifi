#author: rajoan

#Please change 'rockyou.txt' to your file name if your file name is different.(for most cases it is)

number=int(input("Enter your password length:"))
character=input("Do you want exact(E) or greater than or equal(G) or Less than or equal(L)?")
           
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as infile, open('filtered.txt','w',encoding='utf-8', errors='ignore') as outfile:
    for line in infile:
        password=line.strip()
        if(character=='E' or character=='e'):
            if len(password)==number:
                outfile.write(password+'\n')
        elif(character=='G' or character=='g'):
            if len(password)>=number:
                outfile.write(password+'\n')
        elif(character=='L' or character=='l'):
            if len(password)<=number:
                outfile.write(password+'\n')
        else:
            print("Wrong input, please run the program again.")
            break

        
