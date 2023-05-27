"""
Zadanie: mamy daną tablicę liczb całkowitych "a"; chcemy potencjalnie stworzyć inną tablicę
tej samej długości, "b", gdzie
b[i] = a[i] lub a[i] - a[j],
przy czym "j" może być inne dla każdego "i".

Chcemy by ostatecznie wszystkie elementy tablicy "b" miały tą samą parzystość... czyli by były wszystkie
parzyste, lub wszystkie nieparzyste. Dodatkowo wszystkie liczby tablicy "a" i "b" mają być > 0.

Przykład:

a = [1, 5, 6]
można wykorzystać do budowy
b = [1, 5, 5]  (wszystkie są nieparzyste, przy czym a[0]=b[0], a[1]=b[1], b[2] = a[2] - a[0])
lub
b = [1, 5, 1]  (teraz na ostatniej pozycji odjęliśmy 5, czyli a[1])



"""


def equalize_parity(a: list[int]) -> bool:
    a = sorted(a)
    n = len(a)
    parity_list = []
    for i in a:
        x = i % 2
        parity_list.append(x)
        if sum(parity_list) == 0 or sum(parity_list) == n:
            return True
        elif a[0] % 2 == 1:
            return True
        else: 
            return False
    return True



