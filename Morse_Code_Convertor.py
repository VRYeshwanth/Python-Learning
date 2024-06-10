import time
morse_code = {'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','0': '-----','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.','&': '.-...',"'": '.----.','@': '.--.-.',')': '-.--.-','(': '-.--.',':': '---...',',': '--..--','=': '-...-','!': '-.-.--','.': '.-.-.-','-': '-....-','%': '------..-.-----','+': '.-.-.','"': '.-..-.','?': '..--..','/': '-..-.'}

def convert(text):
    code = ""
    for ch in text.upper():
        if ch in morse_code:
            code += morse_code[ch]+ " "
        else:
            code += ' '
    return code

if __name__ == "__main__":
    paragraph = input("Enter a paragraph : \n")
    code = convert(paragraph)
    txt = "Converting"
    for i in range(6):
        dots = "." * i
        print(f"\r{txt}{dots}", end = "", flush=True)
        time.sleep(0.75)
    print("Successfully Converted")
    with open("Morse_Code_Output.txt", "w") as f:
        f.write(code)
