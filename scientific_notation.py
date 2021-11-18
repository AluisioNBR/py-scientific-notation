def notationTOnumber(notation = ""):
    notation = notation.strip()
    err = ""
    
    try :
        if notation == "":
            err = "A notação está vazia, não posso prosseguir!"
            raise Exception(err)

        if "+" in notation or "/" in notation:
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

        base, exp = "", ""
        if not notation[1][1] == "⁰" or not notation[1][1] == "¹" or not notation[1][1] == "²" or not notation[1][1] == "³" or not notation[1][1] == "⁴" or not notation[1][1] == "⁵" or not notation[1][1] == "⁶" or not notation[1][1] == "⁷" or not notation[1][1] == "⁸" or not notation[1][1] == "⁹":
            for i in range(len(notation[1])):
                char = notation[1][i]

                if char == '-':
                    if notation[1][i - 1] != "⁰" and notation[1][i - 1] != "¹" and notation[1][i - 1] != "²" and notation[1][i - 1] != "³" and notation[1][i - 1] != "⁴" and notation[1][i - 1] != "⁵" and notation[1][i - 1] != "⁶" and notation[1][i - 1] != "⁷" and notation[1][i - 1] != "⁸" and notation[1][i - 1] != "⁹":
                        exp = exp + '-'

                    elif notation[1][i + 1] != "⁰" and notation[1][i + 1] != "¹" and notation[1][i + 1] != "²" and notation[1][i + 1] != "³" and notation[1][i + 1] != "⁴" and notation[1][i + 1] != "⁵" and notation[1][i + 1] != "⁶" and notation[1][i + 1] != "⁷" and notation[1][i + 1] != "⁸" and notation[1][i + 1] != "⁹":
                        base = base + '-'

                else :
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
            exp = exp.strip()

            condition1, condition2 = None, None
            if base[0] == '-':
                condition1 = base[1:].isnumeric()
            else :
                condition1 = base.isnumeric()
            
            if exp[0] == '-':
                condition2 = exp[1:].isnumeric()
            else:
                condition2 = exp.isnumeric()

            if condition1 and exp != '' and condition2:
                base = float(base)
                exp = int(exp)
            else :
                err = "A base, ou o expoente, não é um número, não posso prosseguir!"
                raise Exception(err)

            notation[1] = base
            notation.append(exp)


        else :
            err = "Não existe base para exponenciação na notação, não posso prosseguir!"
            raise Exception(err)
    
        result = notation[0] * (notation[1] ** notation[2])
        return result

    except:
        print(err)

def numberTOnotation(number = ""):
    number = number.strip()
    err = ""

    try :
        if number == '' or number.isalpha():
            err = 'O número não existe, não posso prosseguir!'
            raise Exception(err)

        comma, exp, num = False, 0, ''
        for i in range(len(number)):
            char = number[i]

            if char == ' ':
                err = 'Existem espaços vazios no número, não posso prosseguir!'
                raise Exception(err)
            
            elif char.isalpha():
                err = 'Existem letras na expressão, não posso prosseguir!'
                raise Exception(err)
            
            elif char == '0' and i != 0:
                exp = exp + 1

            else :
                if num != '0' and num != '1' and num != '2' and num != '3' and num != '4' and num != '5' and num != '6' and num != '7' and num != '8' and num != '9' and not comma:
                    num = num + '.'
                    comma = True

                if comma:
                    exp = exp + 1

                num = num + char

        print(f"{num} x 10 > {exp}")
    except :
        print(err)

numberTOnotation('0.10')