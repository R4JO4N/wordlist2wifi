This is a simple python script to filter large wordlist files(like rockyou.txt and others).
I wrote it to get common passwords of my given length from a wordlist, basically for
wifi. it is unnecessary to check all the rockyou.txt passwords while using aircrack-ng or hashcat
as they contain a huge number of less than 8 character passwords. You can use this script to filter any word-
list, or wordlists generated by social engineering wordlist generator like cupp.py/other tools.
Commands:
git clone https://github.com/R4JO4N/wordlist2wifi
cd wordlist2wifi
ls
python3 customfilter.py <full path of input.txt> output.txt

example: (for Kali linux users)
python3 customfilter.py /usr/share/wordlists/rockyou.txt output.txt
