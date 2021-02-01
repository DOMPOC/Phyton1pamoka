#  integer, string ,long, double, float, boolean

skaicius = float
sakinys = "stringas"
flag = False
skaiciu_list = [6, 2, 1, 6, 2, 78, 3, 2, 1]
counter = 0

list = ["Galaxy S20", "Iphone 12", "XiaomiMi10"]
tv_list = ["silelis", "samsungTV", "LGTV"]

#for i, v in enumerate(list):
 #   print(i, v)

#unikalus_zodziai = set(list)
#print(unikalus_zodziai)

kategorijos = {"mobile_phones": list, "TV": tv_list}

#print(kategorijos.items())

#while flag == False:
 #   counter += 1
  #  if counter== 100:
   #     flag=True
    # print(counter)

#def funkcija(sarasas, sarasas2):
 #   print(sarasas, sarasas2)

#funkcija(list, tv_list)


class Testas:
    def metodas(self, sarasas):
        print(sarasas)

#t = Testas()
#t.metodas(list)


pirmas_indeksas = list[1]
print(pirmas_indeksas)

if len(list) == 3:
    print(len(list))

if flag == True:
    print("Flag is false")
else:
    print("Flag was not true")

if list == tv_list:
    print(list + " and " + tv_list + "are the same list")
elif len(tv_list) == len(list):
    print("both lists have same amount of elements")
else:
    print("none of the criteria fits")

#bad logical statement example
#if list == tv_list:
 #   print(list + " and " + tv_list + "are the same list")
#if len(tv_list) == len(list):
 #   print("both lists have same amount of elements")
#else:
#    print("none of the criteria fits")









