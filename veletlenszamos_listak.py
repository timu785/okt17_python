'''
készíts függvényt, mely az érmedobást szimulálja és legenerál 10 db fej
vagy írást és az eredményt eltárolja egy listában. A függvény térjen vissza a listával

A továbbiakban ezzel a listával dolgozz az alábbi függvényekben:
számold meg hány fej dobás van a listában


készíts függvényt, mely a kockadobást szimulálja és legenerál 200 db véletlen kockadobást
és az eredményt eltárolja egy listában. A függvény térjen vissza a listával

A továbbiakban ezzel a listával dolgozz az alábbi függvényekben:
számold meg hányszor dobtunk egyest, kettest, ... hatost!

Készíts 'cinkelt' kockát! A hatost nagyobb valószínűséggel dobja!
A cinkelt kockával is futtasd le a fenti függvényeidet! Kiderül a csalás?
'''
import vel_met
erme_lista=vel_met.ermedobas()
print(erme_lista)
print(vel_met.fejdb(erme_lista))

kocka_lista=vel_met.kockadobas()
print(kocka_lista)
print(vel_met.dobasdb(kocka_lista))
print(vel_met.dobasdb2(kocka_lista))

""" cinkelt_lista=vel_met.cinkelt()
print(cinkelt_lista)
print(vel_met.dobasdb2(cinkelt_lista)) """

