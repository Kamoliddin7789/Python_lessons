#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#ismlar=["ravshan","feruz","jamshid","ikrom","hayot"]
#for ism in ismlar:
#    print(f"salom {ism}")
#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#print(f"kod {len(ismlar)} martta takrorlandi")
#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#toq_sonlar=list(range(9,100,2))
#for son in toq_sonlar:
 #   print(son)
#kinolar=[]
#print(" 5 ta eng yoqtirgan kinoyingiz qaysi?")
#for kino in range(5):
 #   kinolar.append(input(f"kinoni nomini kiriting\n>>"))
#print(kinolar)
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
x=int(input("bugun necha kishi bilan uchrashdinggiz?>>"))
suhbatdoshlar=[]
for n in range(x):
    suhbatdoshlar.append(input(f"{n+1}-suhbatdoshinggiz?\n>>").title())
print(suhbatdoshlar)

 
    




