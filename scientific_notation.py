def notationTOnumber(notation = ""):
    notation = notation.strip()
    err = ""
    
    try :
        if notation == "":
            err = "A notação está vazia, não posso prosseguir!"
            raise Exception(err)

        if "+" in notation or "-" in notation or "/" in notation:
            err = "A notação não aceita adições, subtrações ou divisões, não posso prosseguir!"
            raise Exception(err)
        
        if "*" in notation:
            notation = notation.split("*")
        elif "∙" in notation:
            notation = notation.split("∙")
        elif "x" in notation:
            notation = notation.split("x")
        elif "X" in notation:
            notation = notation.split("X")
        else:
            err = "A notação não possui sinal de multiplicação, não posso prosseguir!"
            raise Exception(err)

        itens = 0
        for chunk in notation:
            itens = itens + 1

        if itens > 2 or itens < 0:
            err = "Tem mais de uma multiplicação na notação, não posso prosseguir!"
            raise Exception(err)

        notation[0] = notation[0].strip(); notation[1] = notation[1].strip()

        number = None; condition = None
        if "." in notation[0]:
            number = notation[0].split('.')
            if number[0].strip().isnumeric() and number[1].strip().isnumeric():
                notation[0] = float(number[0] + '.' + number[1])
            else :
                err = "O multiplicador não é um número, não posso prosseguir!"
                raise Exception(err)
        
        elif "," in notation[0]:
            number = notation[0].split(',')
            if number[0].strip().isnumeric() and number[1].strip().isnumeric():
                notation[0] = float(number[0] + '.' + number[1])
            else :
                err = "O multiplicador não é um número, não posso prosseguir!"
                raise Exception(err)

        else :
            number = notation[0]
            if number.strip().isnumeric():
                notation[0] = int(number)
            else :
                err = "O multiplicador não é um número, não posso prosseguir!"
                raise Exception(err)

        base, exp = "", ""; char = notation[1][1]
        if not char == "⁰" or char == "¹" or char == "²" or char == "³" or char == "⁴" or char == "⁵" or char == "⁶" or char == "⁷" or char == "⁸" or char == "⁹":
            for char in notation[1]:
                if char == "⁰":
                    exp = exp + '0'
                
                elif char == "¹":
                    exp = exp + '1'
                
                elif char == "²":
                    exp = exp + '2'
                
                elif char == "³":
                    exp = exp + '3'
                
                elif char == "⁴":
                    exp = exp + '4'
                
                elif char == "⁵":
                    exp = exp + '5'
                
                elif char == "⁶":
                    exp = exp + '6'
                
                elif char == "⁷":
                    exp = exp + '7'
                
                elif char == "⁸":
                    exp = exp + '8'
                
                elif char == "⁹":
                    exp = exp + '9'
                    
                else :
                    base = base + char
            
            base = base.strip()
            exp = int(exp.strip())
            
            if base.isnumeric():
                base = int(base)
            else :
                err = "A base não é um número, não posso prosseguir!"
                raise Exception(err)


        else :
            err = "Não existe base para exponenciação na notação, não posso prosseguir!"
            raise Exception(err)

        print(f"{base},{exp}")
        print(type(notation[1]))
        print(notation)
    
    except:
        print(err)

""
notationTOnumber('   2,7   *   10     ')