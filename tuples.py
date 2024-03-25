one_element_tuple_2 = 1.,2.5,
print(one_element_tuple_2)
print(type(one_element_tuple_2))

afro_beats_singers = ("Davido", "Wizkid", "Tiwa Svage", "Flavour", "Phyno")
print(afro_beats_singers[3])
print(afro_beats_singers[3])
print(afro_beats_singers[0 : 2])
print(afro_beats_singers[2:3])

y = list(afro_beats_singers)
y.append("Omah Lay")
afro_beats_singers = tuple(y)
print(afro_beats_singers)

# another_afro_beats_singers = ("Odumodu Black")
# afro_beats_singers += another_afro_beats_singers
# print(afro_beats_singers)

# del  another_afro_beats_singers

a1, a2, a3, a4, a5, a6 = afro_beats_singers
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

for i in afro_beats_singers:
    print(range(len(i)))
    
for m in range(len(afro_beats_singers)):
    print(afro_beats_singers[m])    

# a = 0
# while a < len(afro_beats_singers):
#     print(afro_beats_singers[a])
# a += 1

afro_beats_singers *= 3
print(afro_beats_singers)





