"""Module pour vérifier si une chaîne de caractères est un palindrome.

Ce module tient compte des accents et des caractères spéciaux.
"""

import re
import unicodedata

def enlever_accents(texte):
    """Supprime les accents d'une chaîne de caractères."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', texte)
        if unicodedata.category(c) != 'Mn'
    )

def ispalindrome(s):
    """Vérifie si une chaîne de caractères est un palindrome."""
    # Convertir en minuscules et enlever les accents
    s = enlever_accents(s.lower())
    # Supprimer tous les caractères non alphanumériques
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    # Vérifier si la chaîne est égale à son inversion
    return s == s[::-1]

#### Fonction principale

def main():
    """Fonction principale pour tester la fonction ispalindrome."""
    # Vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
