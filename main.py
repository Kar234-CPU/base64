#Build by Karlo Perković. (KAKA development)
#25.2.2025.
#ver 0.2

import base64

#Functions for cli
def decode():          
    print(" _DECODE_")
    global encript_
    global scbit
    txt = input(" Your base64 text -> ")
    fsbit = txt.encode("ascii")
    loc = base64.b64decode(fsbit)
    scbit = loc.decode("ascii")
    print()
    encript_ = "decoded_"
    load()
def encode():
    print(" _ENCODE_")
    global encript_
    global scbit
    txt = input(" Your ascii text -> ")
    fsbit = txt.encode("ascii")
    scbit = base64.b64encode(fsbit)
    print()
    encript_ = "encoded_"
    load()
def load():
    if encript_ == "encoded_":
        print(" status -", encript_)
        print(" b' _your encoded text_ '")
        print()
        print(" OUT -", scbit)
        print()
    if encript_ == "decoded_":
        print(" status -", encript_)
        print()
        print(" OUT -", scbit)
        print()
def help():
    print("HELP:")
    print(" List of commands:")
    print("  help - brings help dialog")
    print("  exit - exits the program")
    print("  encode - encoding function for base64")
    print("  decode - decoding function for base64")
    print(" INFO:")
    print("  Build by Karlo Perković, (KAKA decvelopment).")
    print("  ver: 0.2")
    print("  25.2.2025.")
    print()

print()
print("    BASE64 encoder/decoder")
print("By KAKA dev. All rights reserved.")
print("tipe 'help' command for a help")
print("tipe 'exit' to exit")
print()
while True:  #loop
    comn = input("__>")
    comm = comn.lower()
    if comm == "exit":
        break
    if comm == "decode":
        decode()
    if comm == "encode":
        encode()
    if comm == "help":
        help()

