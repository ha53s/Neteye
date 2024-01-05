import pyfiglet
from termcolor import colored
from pyfiglet import figlet_format


def toolScreen():
    text = "Net Eye"
    ascii_art = pyfiglet.figlet_format(text)
    font = colored(ascii_art, color='blue')
    print(font)
    print("\033[91m" + "   ~~ Welcome to Net Eye ~~" + "\033[0m")
    print("\033[94m" + "---------------------------------------" + "\033[0m")
    print("\033[94m" + " [!] Version :1.0 " + "\033[0m")
    print("\033[94m" + " [!] Copyrights : Students Final Project at IAU " + "\033[0m")
    print("\033[94m" + " [!] Course : CYS 403 Programming for Cybersecurity " + "\033[0m")
    print("\033[94m" + " [!] Instructor : Ms. Reem Alassaf " + "\033[0m")
    print("\033[94m" + "---------------------------------------" + "\033[0m")
    print("\033[91m" + "   Written by: Group[5]" + "\033[0m")
    print("\033[94m" + "---------------------------------------" + "\033[0m")

    print("\033[94m" + " [+] Zahrah Aljanabi " + "\033[0m")
    print("\033[94m" + " [+] Hams Almansori" + "\033[0m")
    print("\033[94m" + " [+] Reiman Almohana " + "\033[0m")
    print("\033[94m" + " [+] Sara Khalid Almulla " + "\033[0m")
    print("\033[94m" + " [+] Reem Majed Alotaibi " + "\033[0m")
    print("\033[94m" + "---------------------------------------" + "\033[0m")

def options():
    print("\033[91m" + " Options: " + "\033[0m")
    print("\033[94m" + "---------------------------------------" + "\033[0m")
    print("\033[94m" + " [1] IP Look Up " + "\033[0m")
    print("\033[94m" + " [2] MAC Look Up " + "\033[0m")
    print("\033[94m" + " [3] Scan IP for open ports " + "\033[0m")
    print("\033[94m" + " [4] Filtered IP Search" + "\033[0m")
    print("\033[94m" + " [5] Quit " + "\033[0m")


if __name__ == "__main__":
    toolScreen()
