def citireLista():
    list = []
    n = int(input("Dati numarul de elem din lista: "))
    for i in range(n):
        list.append(int(input("list[" + str(i) + "]= ")))
    return list


def isPrime(nr):
    """
  Determina daca un numar este prim.
  :param x: nr intreg
  :return: True daca numarul este prim sau False in caz contrar.
  """
    if nr < 2:
        return False
    else:
        for i in range(2,nr):
            if nr % i == 0:
                return False
    return True


def testPrimeFunction():
    assert isPrime(7) == True
    assert isPrime(9) == False
    assert isPrime(2) == True


def noneArePrimes(list):
    """
  Determina daca toate numerele dintr-o lista sunt prime
  :param l: O lista de numere intregi
  :return: True daca toate numerele dintr-o lista sunt prime sau False, in caz contar.
  """
    for i in list:
        if isPrime(i):
            return False
    return True


def testNonePrimesFunction():
    assert noneArePrimes([]) == True
    assert noneArePrimes([1, 2, 3]) == False


def get_longest_all_not_primes(list):
    """
    Determina cea mai lunga subsecventa de numere neprime.
    :param list: O lista de numere intregi
    :return: Afiseaza cea mai lunga subsecventa de numere neprime dintr-o lista.
    """
    secvMax = []

    for i in range(len(list)):
        for j in range(i, len(list)):
            if noneArePrimes(list[i: j + 1]) and len(list[i: j + 1]) > len(secvMax):
                secvMax = list[i: j + 1]
    return secvMax


def testLongestNotPrimesFunction():
    assert get_longest_all_not_primes([]) == []
    assert get_longest_all_not_primes([1, 2, 3, 4, 6, 8, 12, 14, 5, 7, 2, 8, 10, 26]) == [4, 6, 8,  12, 14]
    assert get_longest_all_not_primes([2, 3, 5, 8, 6, 7]) == [8, 6]


def MediaElementelor(list):
    """
    Calculeaza media aritmetica a tuturor elementelor din lista
    :param list: lista de nr. intregi
    :return: media aritmetica a elementelor listei
    """
    suma = 0
    for i in list:
        suma = suma + i
    media = suma/len(list)
    return media

def TestMediaElementelor():
    assert MediaElementelor([1, 4, 4]) == 3
    assert MediaElementelor([12]) == 12
    assert MediaElementelor([10, 4]) == 7

def get_longest_average_below(list, average):
    """
    Determina cea mai lunga subsecventa in care toate elementele au media mai mica decat valoarea citita
    :param list: lista de nr. intregi
    :param average: valoarea citita (un numar intreg) cu care comparam media
    :return: Cea mai lunga subsecventa in care toate elementele din lista au media mai mica decat o valoare citita
    """
    subsecventaMax = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if MediaElementelor(list[i:j + 1]) < average and len(subsecventaMax) < len(list[i:j + 1]):
                subsecventaMax = list[i:j + 1]
    return subsecventaMax

def testgetlongestaveragebelow():
    assert get_longest_average_below([2, 4, 3, 55, 23], 5) == [2, 4, 3]
    assert get_longest_average_below([1, 2, 6, 12], 5) == [1, 2, 6]
    assert get_longest_average_below([5, 3, 22, 23], 10) == [5,3]

def ToateElementeleSuntPare(list):
    """
    Determina daca o lista are toate elementele nr. pare
    :param list: lista de nr. intregi
    :return: True, daca toate elementele din lista sunt nr. pare sau False, in caz contrar
    """
    for i in list:
        if i%2!=0:
            return False
    return True

def testToateElementeleSuntPare():
    assert ToateElementeleSuntPare([1, 5, 5]) == False
    assert ToateElementeleSuntPare([2, 4, 9]) == False
    assert ToateElementeleSuntPare([2, 12, 6]) == True

def get_longest_all_even(list):
    """
    Determina cea mai lunga subsecventa de elemente pare
    :param list: Lista de numere intregi
    :return: Cea mai lunga subsecventa de elemnte pare
    """
    subsecventaMax = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if ToateElementeleSuntPare(list[i:j+1]) and len(subsecventaMax) < len(list[i:j+1]):
                subsecventaMax = list[i:j+1]
    return subsecventaMax

def test_get_longest_all_even():
    assert get_longest_all_even([]) == []
    assert get_longest_all_even([1, 3, 15, 21]) == []
    assert get_longest_all_even([1, 2, 4, 3,5 ,8]) == [2,4]


def main():

    list = []

    while True:
        print("1. Citire date")
        print("2. Determinati cea mai lunga subsecventa de numere neprime dintr-o lista")
        print("3. Determinare cea mai lungă subsecvență in care media numerelor nu depășește o valoare citită")
        print("4. Determinare cea mai lungă subsecvență in care toate numerele sunt pare")
        print("5. Iesire")

        optiune = input("Selectati optiune: ")

        if optiune == "1":
            list = citireLista()
        elif optiune == "2":
            print(get_longest_all_not_primes(list))
        elif optiune == "3":
            average = int(input("Dati valoarea cu care sa se compare media:"))
            print(get_longest_average_below(list, average))
        elif optiune == "4":
            print(get_longest_all_even(list))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Selectati alta optiune.")


if __name__ == '__main__':
    testPrimeFunction()
    testNonePrimesFunction()
    testLongestNotPrimesFunction()
    testgetlongestaveragebelow()
    test_get_longest_all_even()
    main()