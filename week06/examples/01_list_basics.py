# # products = ["Notebook", "Pen", "Folder"]

# # print(products[0])
# # print(products[1])
# # print(products[2])

# # products.append("Marker")

# # print(products)

# # products[0] = "Blue Notebook"
# # products[1] = "Blue pen"
# # products[2] = "Blue Folder"
# # products[3] = "Blue Marker"

# # print(products)

# # count_of_products = len(products)

# # print("Count:", count_of_products)

# # alisveris_listesi = ["Elma", "Armut", "Muz", "Portakal", "Karpuz"]

# # print(alisveris_listesi[1])
# # print(alisveris_listesi[3])

# # alisveris_listesi.append("Pide")

# # print(alisveris_listesi)

# # alisveris_listesi.insert(2, "Kivi")

# # print(alisveris_listesi)

# # alisveris_listesi.remove("Elma")

# # print(alisveris_listesi)

# # silinen_remove = alisveris_listesi.remove("Armut")
# # print("Silinen eleman:", silinen_remove)
# # print(alisveris_listesi)


# # alisveris_listesi.pop(1)
# # print(alisveris_listesi)

# # silinen_pop = alisveris_listesi.pop(1)
# # print("Silinen eleman:", silinen_pop)
# # print(alisveris_listesi)


# # # Özellik	                                     pop()	                                                        remove()
# # # Neye Göre Siler?	                İndeks (Sıra) numarasına göre siler.	                    Değerin (Elemanın) kendisine göre siler.
# # # Varsayılan Davranış	            İndeks yazmazsanız en sondaki elemanı siler.	            Değer yazmak zorunludur, boş bırakılamaz.
# # # Elemanı Geri Döndürür mü?	        Evet. Sildiği elemanı koparıp size verir.               	Hayır. Elemanı tamamen yok eder, geriye bir şey dönmez.
# # # Eleman Bulunamazsa?	            Olmayan bir indeks girilirse IndexError verir.	            Olmayan bir değer girilirse ValueError verir.

# sayilar = [5, 2, 9, 1, 7, 3, 8, 4, 6]

# # sayilar.sort()
# # print(sayilar)

# # sayilar.reverse()
# # print(sayilar)

# # yeni_sayilar = sorted(sayilar)
# # print(yeni_sayilar)

# # sayilar.sort(reverse=True)
# # print(sayilar)

# # sayilar.reverse()
# # print(sayilar)

# count_5 = sayilar.count(5)

# print("5 sayısı listede", count_5, "kez geçiyor.")


# print(sayilar)

# sayilar2 = [1, 2, 3]
# sayilar3= [4, 5, 6]


# sayilar2.append(sayilar3)

# print(sayilar2)  

# print(sayilar2[3][1])  # This will print the entire sayilar3 list as a single element

# # sayilar.extend(sayilar2)
# # print(sayilar)

# # notlar = [
# #           [50, 60],
# #           [55, 65]
# #           ]

# # notlar_names = ["Ali", "Veli"]

# # print(notlar_names[0])
# # print(notlar[0][0])


sayilar = [1, 2, 3, [4, 5, 6, [7,8]]]

print(sayilar[0])
print(sayilar[1])
print(sayilar[2])
print(sayilar[3])

print(sayilar[3][0])
print(sayilar[3][1])
print(sayilar[3][2])
print(sayilar[3][3])

print(sayilar[3][3][0])
print(sayilar[3][3][1])