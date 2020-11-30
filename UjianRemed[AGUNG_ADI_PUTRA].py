
#########################################################
''''''''''''''''''''''Nomor 1''''''''''''''''''''''''''' 
#########################################################

def pendek(kalimat) :
    x=""
    x=list(kalimat.split())
    c=min(x, key=len)
    print ("The Shortest word has" ,len(c), "char(s)")

# pendek("Many people get up early in the morning")
# pendek("Every office would getting newest monitro")
pendek("Create new file after this morning")

#########################################################
''''''''''''''''''''''Nomor 2''''''''''''''''''''''''''' 
#########################################################


def pisah(angka) :
    kali = []
    while angka > 0 : 
        kali.append(angka%10)   
        angka = angka//10
    if angka == 0 :
        # print(kali)
        return kali
# print("Test pisah ",pisah(39)) 

def kalikan(kali) :
    herself = 1
    while len(kali) > 0 :
        herself = herself * kali.pop(0)
    if len(kali) == 0 :
        return herself    
# print("Test kalikan ",kalikan(pisah(39)))

def persistence(angka) :
    i= 0
    while angka >= 10 :
        angka = kalikan(pisah(angka))
        # print(angka)
        i+=1
    if angka < 10 : 
        return i
# print("Test persistence ",persistence(39))

angka=int(input("Masukkan angka : "))

if angka <0  :
    print ("Please input positive number only")
else : 
    print(f'So it take(s) {persistence(angka)} multipication until we get a single digit' )







