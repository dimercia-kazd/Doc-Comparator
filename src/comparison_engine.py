def compare_lines(text1: str, text2: str) -> dict:
    """
    Compare deux textes ligne par ligne.
    Retourne un dictionnaire contenant :
    - 'common': lignes identiques
    - 'diff': paires de lignes différentes (sous forme de tuples)
    - 'unique_to_text1': lignes uniquement dans le texte 1
    - 'unique_to_text2': lignes uniquement dans le texte 2
    """
    # On divise chaque texte en lignes individuelles
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    common = []
    diff = []
    unique_to_text1 = []
    unique_to_text2 = []

    # On compare les lignes position par position 
    for l1, l2 in zip(lines1, lines2):
        if l1 == l2:
            common.append(l1)
        else:
            diff.append((l1, l2))  # On garde les deux versions différentes

    # On regarde s’il reste des lignes non comparées (si l’un est plus long que l’autre)
    if len(lines1) > len(lines2):
        unique_to_text1.extend(lines1[len(lines2):])
    elif len(lines2) > len(lines1):
        unique_to_text2.extend(lines2[len(lines1):])

    return {
        'common': common,
        'diff': diff,
        'unique_to_text1': unique_to_text1,
        'unique_to_text2': unique_to_text2
    }

def compare_words_in_line(line1: str, line2: str) -> dict:
    """
    Compare deux lignes mot à mot.

    :param line1: Première ligne à comparer.
    :param line2: Deuxième ligne à comparer.
    :return: Dictionnaire contenant :
        - 'common': liste des mots communs,
        - 'only_in_line1': liste des mots présents uniquement dans line1,
        - 'only_in_line2': liste des mots présents uniquement dans line2,
        - 'differences': liste des couples (mot1, mot2) pour les mots différents à la même position.
    """
    words1 = line1.strip().split()
    words2 = line2.strip().split()

    set1 = set(words1)
    set2 = set(words2)

    common = list(set1 & set2)
    only_in_line1 = list(set1 - set2)
    only_in_line2 = list(set2 - set1)

    # Comparaison positionnelle (mots à la même place mais différents)
    differences = []
    for w1, w2 in zip(words1, words2):
        if w1 != w2:
            differences.append((w1, w2))

    return {
        "common": common,
        "only_in_line1": only_in_line1,
        "only_in_line2": only_in_line2,
        "differences": differences
    }

def calculate_similarity_rate(text1: str, text2: str) -> float:
    """
    Calcule le pourcentage de similarité entre deux textes en fonction des lignes communes.

    :param text1: Premier texte.
    :param text2: Deuxième texte.
    :return: Taux de similarité (entre 0.0 et 100.0).
    """
    result = compare_lines(text1, text2)
    nb_communes = len(result['common'])

    # Nombre total moyen de lignes dans les deux textes
    nb_total = (len(text1.splitlines()) + len(text2.splitlines())) / 2

    if nb_total == 0:
        return 100.0  # Deux textes vides = 100% similaires

    taux = (nb_communes / nb_total) * 100
    return round(taux, 2)

def identify_unique_words(text1: str, text2: str) -> dict:
    """
    Identifie les mots présents uniquement dans l'un des deux textes.

    :param text1: Contenu du premier document.
    :param text2: Contenu du deuxième document.
    :return: Dictionnaire avec :
        - 'only_in_text1': liste des mots uniques au texte 1
        - 'only_in_text2': liste des mots uniques au texte 2
    """
    # On découpe les textes en mots (en ignorant la casse)
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    # On utilise les ensembles pour détecter les mots uniques
    set1 = set(words1)
    set2 = set(words2)

    only_in_text1 = list(set1 - set2)
    only_in_text2 = list(set2 - set1)

    return {
        "only_in_text1": only_in_text1,
        "only_in_text2": only_in_text2
    }

if __name__ == "__main__":
    t1 = "Le chat mange une souris"
    t2 = "Le chien mange une pomme"
    uniques = identify_unique_words(t1, t2)
    print("Mots uniques :", uniques)