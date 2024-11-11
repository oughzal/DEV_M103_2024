# Polymorphisme

Le polymorphisme est un concept clé de la programmation orientée objet (POO). Il permet à des objets de différents types de répondre à des appels de méthodes de la même manière. En d'autres termes, une seule interface peut être utilisée pour représenter différentes implémentations.

## Types de polymorphisme

1. **Polymorphisme de sous-typage (ou d'inclusion)** : Il permet à une classe dérivée d'être traitée comme une classe de base. Par exemple, si `Chien` et `Chat` héritent de `Animal`, une méthode qui accepte un `Animal` peut accepter un `Chien` ou un `Chat`.

2. **Polymorphisme paramétrique** : Il permet aux méthodes de fonctionner avec des types génériques. Par exemple, une fonction qui peut accepter une liste de n'importe quel type d'objets.

3. **Polymorphisme ad hoc (ou surcharge)** : Il permet à des fonctions ou des opérateurs d'avoir différentes implémentations en fonction de leurs arguments. Par exemple, l'opérateur `+` peut être utilisé pour additionner des nombres ou concaténer des chaînes de caractères.

## Avantages du polymorphisme

- **Réutilisabilité** : Le code peut être réutilisé pour différents types d'objets.
- **Extensibilité** : Il est facile d'ajouter de nouveaux comportements sans modifier le code existant.
- **Maintenance** : Le code est plus facile à maintenir et à comprendre.

## Exemple en Python

```python
class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Woof!"

class Chat(Animal):
    def parler(self):
        return "Meow!"

def faire_parler(animal):
    print(animal.parler())

chien = Chien()
chat = Chat()

faire_parler(chien)  # Output: Woof!
faire_parler(chat)   # Output: Meow!
```

Dans cet exemple, la fonction `faire_parler` utilise le polymorphisme pour appeler la méthode `parler` sur des objets de types différents (`Chien` et `Chat`).
