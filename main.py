mode = input(
    "please insert the mode (please insert 'HELP' if there are any doubts) ")

Letters = [
    '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
Translation = []

if mode == "decodify":
    while True:
        valor = input("please insert a valid value ")

        if valor == "END":
            break

        Div_Var = int(valor)  #div_var /= 26
        Mod_Var = Div_Var % 27
        #---------------- while loop ------------
        while True:
            Div_Var = int(Div_Var / 27)
            Translation += Letters[Mod_Var]
            Mod_Var = int(Div_Var % 27)
            if Div_Var < 27:
                Translation += Letters[Mod_Var]
                break
        #------------- while loop end -----------
        Translation.reverse()
        var_trans = ""
        for char in Translation:
            var_trans += char
        print(var_trans)
        Translation = []

elif mode == "codify":
    while True:
        valor = input("please insert something to be codified ")
        powering_val = len(valor) - 1
        codification = 0

        if valor == "END":
            break

        for char in valor:

            if char in Letters:
                codification += Letters.index(char) * (27**powering_val)
                powering_val -= 1
            else:
                print("the char '", char, "' cannot be codified")

        print(codification)
#---------------- HELP ------------------
elif mode == "HELP":
    print(
        "\nthis code was created by JOÃO FERNANDO aka: Arcélius\n"
        "\nthe mode 'codify' codefies valid words to a system of numbers in base 27\n"
        "\nthe mode 'decodify' decodefies a valid number in base 27 into real words\n"
        "\nyou are using a limited program, it might occour a codification error if the code recive a large word\n"
        "\nto end the execution of the code please type 'END' as the value to be codified or decodified\n"
    )

    for char in Letters:
        print("the char is ", char, "and index value is ", Letters.index(char))
#----------------------------------------
else:
    print("please insert a valid mode")
