import random
def pyramide_for(len):
    "Functie om pyramide te printen van len lengte op zijn middelpunt met een for loop"
    for i in range(0, len, 1):
        print('*'*i)
    for i in range(len, 0, -1):
        print('*'*i)

def pyramide_while(len):
    "Functie om pyramide te printen van len lengte op zijn middelpunt met een while loop"

    counter = 0
    # while de counter kleiner is dan de gegeven lengte
    while counter < len:
        print('*'*counter)
        counter += 1
    # while de counter groter is dan 0
    while counter > 0:
        print('*'*counter)
        counter -= 1
def count(lst):
    """functie om te tellen hoevaak een int in een lijst voor komt"""
    freqs = dict()
    # voor elk getal in de lijst
    for getal in lst:
        # als het getal nog niet bestaan de dict
        if int(getal) not in freqs:
            # huidig getal komt 1 keer voor
            freqs[int(getal)] = 1
        # anders is het getal al eerder voor gekomen
        else:
            # huidig aantal komt +1 keer voor
            freqs[int(getal)] += 1
    return freqs

def grootste_verschil(lst):
    """functie om het grootste verschil tussen opvolgende getallen te berekenen"""
    grootste = 0
    # voor elke index in de lijst behalve de laatste
    for i in range(len(lst)-1):
        # controleer of het volgende getal min het huidige getal een groter verschil heeft dan het huidige grootste verschil
        if lst[i+1] - lst[i] > grootste:
            grootste = lst[i+1] - lst[i]
    return(grootste)

def zero_one(lst):
    """zero one functie"""
    freq = count(lst)
    if freq[0] > 12 or freq[0] > freq[1]:
        return False
    return True

def tekst_check():
    """functie die om 2 strings vraagt en de index terug geeft waar het eerste verschil is"""
    # inputs voor versS
    string_1 = input("Eerste tekst voor vergelijking")
    string_2 = input("Tweede tekst voor vergelijking")
    if string_1 == string_2:
        print('Je eerste en tweede tekst zijn hetzelfde')
        return
    i = 0
    while i < len(string_1) and i < len(string_2):
        if string_1[i] != string_2[i]:
            print('strings hebben een verschil vanaf index {}'.format(i))
            # stop zodra het verschil gevonden is
            return
        i += 1
    # de strings deels hetzelfde maar eentje is langer, print vanaf welke index dit is
    print('strings hebben een verschil vanaf index {}'.format(i))

def palindroom(tekst):
    """functie die controleert of een gegeven tekst een palindroom is"""
    # als de tekst het zelfde is als zichzelf omgekeerd
    if tekst == tekst[::-1]:
        print('woord is palindroom')
    else:
        print('woord is geen palindroom')

def sorteren(lst):
    """functie om een gegeven lijst te sorteren"""
    # copy van de lijst
    lst_sorted = lst.copy()
    # while conditie
    controleren = True
    while controleren:
        # controleren = false tot dat een getal geswapt wordt
        controleren = False
        for i in range(len(lst_sorted) - 1):
            # Als lijst index i groter is dan lijst index i + 1 dan verwissel je de 2 getallen.
            if lst_sorted[i] > lst_sorted[i + 1]:
                lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                # als een getal geswapt is blijf dan doorgaan met controleren/sorteren
                controleren = True
    return lst_sorted

def gemiddelde(lst):
    """functie om het gemiddelde van een gegeven lijst te berekenen en te returnen als een lijst"""
    return sum(lst) / len(lst)

def gemiddelde_lijst(lst):
    """functie om het gemiddelde van een gegeven lijst te berekenen en te returnen als een lijst"""
    lijst_gemiddelde = []
    for lijst in lst:
        lijst_gemiddelde.append(gemiddelde(lijst))
    return lijst_gemiddelde

def getal_raden():
    """functie om de gebruiker een getal te laten raden tussen de 1 en 10"""

    gok = 0
    # antwoord is een random number
    antwoord = random.randrange(1, 10, 1)
    # zolang de gok niet het antwoord is vraag om een gok
    while int(gok) != antwoord:
        gok = input("Welk getal gok je? ")
    print("Je hebt het getal geraden")

def text_comp(directory = 'test.txt', new_directory = 'testcomp.txt'):
    """functie die een directiory van een text file mee krijgt en deze compiled naar een aangegeven directory( bijv 'text.txt')"""
    # open de meegekregen directory (txt file)
    with open(directory, 'r') as f:
        # voor elke line in het bestand
        for lines in f:
            # strip whitespaces
            x = lines.strip()
            # als een line leeg is wordt deze niet toegevoegd aan het nieuwe bestand
            if x == '':
                continue
            else:
                # append de line aan de meegegeven directory (txt file)
                with open(new_directory, 'a') as f2:
                    f2.write(x)
                    f2.write('\n')

def bits_verschuiven(ch, n):
    """functie die alle bitjes naar rechts verplaatst bij een positief meegegeven getal en naar links bij een negatief meegegeven getal"""
    # alle bitjes aan een lijst toevoegen
    bit_lst = [bits for bits in str(ch)]
    # voor elk bitje in de lijst
    # verschuif de list met indices en maak er weer een string van
    return "".join(bit_lst[n:] + bit_lst[:n])

def fib(getal, index0=0, index1=1):
    """Functie om fib nummer uit te rekenen gegeven zijn index"""
    # base case
    if getal <= 1:
        # [i] ipv [0] zodat bij fib(0) 0 wordt returned en niet 1
        return (index0, index1)[getal]
    # blijft fib recursief aanroepen tot basecase bereikt is.
    return fib(getal - 1, index1, index0 + index1)


def caesar():
    """functie die een string vraagt en de een rotatie om een caesar encrypte string te returnen"""
    # vraag in de tekst en rotatie
    tekst = input("Input een tekst: ")
    rotatie = int(input("Geef een rotatie: "))
    # wordt de uiteindelijk encrypte string (placeholder)
    tekst_caesar = ''
    # alfabet
    abc = 'abcdefghijklmnopqrstuvwxyz'
    # voor elke character in de string
    for char in tekst:
        # spaties worden niet encrypt maar blijven spaties
        if char == " ":
            tekst_caesar += char
        # positie van het character vinden in het alfabet
        positie = abc.find(char)
        # nieuwe positie volgens caesar encryptie is (positie + rotatie) modulo 26
        positie_nieuw = (positie + rotatie) % 26
        # nieuwe character a.d.h.v de nieuwe positie
        char_nieuw = abc[positie_nieuw]
        # nieuwe character aan de tekst_caesar string toevoegen
        tekst_caesar += char_nieuw
    return tekst_caesar


def fizz_buzz():
    """functie die reeks cijfers print maar ipv cijfers die deelbaar zijn door 3 en of 5 wordt een string geprint"""
    for i in range(1, 101):
        # als het getal / 3 en het getal / 5 beide 0 als rest heeft. fizzbuzz
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # deelbaar door 3 met rest 0. print fizz
        elif i % 3 == 0:
            print("Fizz")
        # deelbaar door 5 met rest 0. print buzz
        elif i % 5 == 0:
            print("Buzz")
        # anders niet deelbaar door 3 of 5. print getal
        else:
            print(i)
