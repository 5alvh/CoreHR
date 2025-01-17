import re;
class validar:
    def __init__(self):
        self.letraPorResto={'0': 'T',
        '1': 'R',
        '2': 'W',
        '3': 'A',
        '4': 'G',
        '5': 'M',
        '6': 'Y',
        '7': 'F',
        '8': 'P',
        '9': 'D',
        '10': 'X',
        '11': 'B',
        '12': 'N',
        '13': 'J',
        '14': 'Z',
        '15': 'S',
        '16': 'Q',
        '17': 'V',
        '18': 'H',
        '19': 'L',
        '20': 'C',
        '21': 'K',
        '22': 'E'}
        self.letrasNie={"X":"0",
                "Y":"1",
                "Z":"2"}

    ####################|NIF|####################
    def validarFormaNif(self, nif):
        if re.fullmatch(r'\d{8}[A-Za-z]', nif):
            return True
        else:
            return False
        
    def validarNIF(self,nif):
        if self.validarFormaNif(nif):
            digitos8 = int(nif[0:8])
            operacion = digitos8 - (int(digitos8 / 23) * 23)
            if self.letraPorResto[str(operacion)] == nif[-1].upper():
                return True
            else:
                return False
        return False

    #print(validarNIF("09408901S")) #VALIDO
    #print(validarNIF("12345678Z")) #VALIDO
    #print(validarNIF("00000023T")) #VALIDO
    #print(validarNIF("87654321A")) #NO VALIDO

    ####################|NIE|####################
    def validarFormaNie(self,nie):
        if not re.fullmatch(r'[XYZ]\d{7}[A-Za-z]', nie):
            return False
        return True

    def validarNIE(self,nie):
        if self.validarFormaNie(nie):
            digitos8 = str(self.letrasNie[nie[0].upper()])+str(nie[1:8])
            intDigitos8 = int(digitos8)
            operacion = intDigitos8 - (int(intDigitos8 / 23) * 23)
            if self.letraPorResto[str(operacion)] == nie[-1].upper():
                return True
        return False

    #print(validarNIE("X9408901S")) #VALIDO
    #print(validarNIE("Y2345678Z")) #VALIDO
    #print(validarNIE("X0000023T")) #VALIDO
    #print(validarNIE("A0000023T")) #NO VALIDO
    #print(validarNIE("Y9408905X")) #VALIDO


    ####################|NAF|####################
    def validarNAF(self,naf):
        partesNAF = naf.split('/')

        if len(partesNAF) != 3:
            return False
        
        A, B, C = partesNAF
        
        if not (A.isdigit() and B.isdigit() and C.isdigit()):
            return False

        A = int(A)
        B = int(B)
        C = int(C)

        if B < 10000000:
            operacion = B + A * 10000000
            cod_control = operacion % 97
        else:
            cod_control = (int(str(A) + str(B))) % 97 

        if cod_control == C:
            return True
        
        return False


    #print(validarNAF("28/12345678/40"))  # 40
    #print(validarNAF("12/9000000/40"))   # NO VALIDO


    #####################IBAN######################################

    def validar_iban(self, iban):
        # Step 1: Remove spaces and check length
        iban = iban.replace(" ", "").upper()
        if len(iban) != 24:
            return False 

        iban_rearranged = iban[4:] + iban[:4]
        
        iban_numerico = ""
        for char in iban_rearranged:
            if char.isdigit():
                iban_numerico += char
            elif char.isalpha():
                iban_numerico += str(ord(char) - ord('A') + 10)

        if int(iban_numerico) % 97 == 1:
            return True  
        else:
            return False 

