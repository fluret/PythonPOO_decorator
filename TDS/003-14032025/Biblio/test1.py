from livre import Livre

livre1 = Livre("Les Misérables", "Victor Hugo", 3)
livre2 = Livre("Les fleurs du mal", "Charles Baudelaire", 1)

print(livre1)
print('*'*10)
livre2.degrade()
print(livre2)