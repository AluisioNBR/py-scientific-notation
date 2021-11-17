def notationTOnumber(notation = ""):
    notation = notation.strip()
    err = ""
    
    try :
        if notation == "":
            err = "A notação está vazia, não posso prosseguir!"
            raise Exception(err)

        
        if "*" in notation:
            notation.split("*")
        elif "x" in notation:
            notation.split("x")
        elif "X" in notation:
            notation.split("X")
        else:
            err = "A notação não possui sinal de multiplicação, não posso prosseguir!"
            raise Exception(err)
    
    except:
        print(err)
