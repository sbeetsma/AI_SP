# imports random, itertools
# ramdom voor het genereren van een random geheime code en random kiezen uit een lijst combinaties
# itertools om itertools.product te gebruiken voor het maken van een iterable die over alle mogelijke combinaties itereert.
import random
from itertools import *

# bronnen (staan ook bij de betreffende functies):
    # leerbron uitrekenen witte pinnen https://stackoverflow.com/questions/47773412/mastermind-check-result-python
    # leerbronnen itertools product  # https://www.youtube.com/watch?v=QXT_aCFYYDA https://www.hackerrank.com/challenges/itertools-product/problem

    # YET ANOTHER MASTERMIND STRATEGY, Barteld Kooi, Department of Philosophy, University of Groningen, The Netherlands

    # Shapiro, E. (1983). Playing Mastermind Logically. SIGART Newsletter, Vol. 85, pp. 28 – 29.
    # Knuth, D. (1976-1977). The Computer as Master Mind. Journal of Recreational Mathematics, Vol. 9, No. 1, pp. 1–6.


### PC/bot functies die bij het spel zelf horen
def bot_geheime_code(code_lengte=4):
    """"functie om een random (geheime) kleur code te genereren
    args:
        code_lengte, de lengte van de kleurcode standaard 4"""

    random_code = []
    # for lengte van de geheime code
    for i in range(code_lengte):
        # voeg een random kleur toe aan de geheime code
        random_code.append(random.choice(kleuren_lst))
    return random_code

def bot_feedback(geheime_code, poging_code):
    """geeft feedback in vorm van een dictionary bijv {zwart:2,wit:2}
    zwart == aantal op de juiste positie en juiste kleur
    wit == aantal juiste kleur maar niet juiste positie
    args:
        geheime_code, de geheime code uit het spel
        poging_code, de vraag over de geheime code"""

    def zwart():
        """nested functie om de zwarte pinnen te berekenen"""

        # aantal zwart
        aantal = 0
        # i staat voor index
        for i in range(len(poging_code)):
            if poging_code[i] == geheime_code[i]:
                aantal += 1
        return aantal

    def wit():
        """nested functie om de witte pinnen te berekenen
        hulpbron voor uitrekenen witte pinnen https://stackoverflow.com/questions/47773412/mastermind-check-result-python"""

        # copy lijst
        temp_geheime_code = geheime_code.copy()
        # aantal wit
        aantal = 0
        # i staat voor index
        for i in range(len(poging_code)):
            if poging_code[i] in temp_geheime_code:
                # haal de kleur uit de temp lijst (1x ookal staat de kleur er meerdere keren in)
                temp_geheime_code.remove(poging_code[i])
                aantal += 1
        # wit is alleen van de pinnen die alleen de juiste kleur zijn niet positie, dus wit = wit - zwart
        return aantal - zwart()
    # zwart en wit is aan het begin 0, na de feedback past deze keys aan
    zwart_wit = {}
    zwart_wit['zwart'], zwart_wit['wit'] = zwart(), wit()
    return(zwart_wit)

### player functies (handmatig kleurcode voor poging/geheime poging en feedback)

def player_kleur_code(code_lengte=4, *arguments):
    """
    Functie om een kleurcode te ontvangen via input, deze input wordt gevalideerd.
    Deze functie wordt gebruikt als player een geheime code wilt maken of wanneer player een code poging maakt"
    args:
        code_lengte, de lengte van de kleurcode standaard 4
        *arguments zodat de gameloop deze functie of een bot functie kan aanroepen met dezelfde parameters """

    invalid = True
    while invalid:
        code = list(input("input een code bijv 'RRBB': ").upper())
        # als code niet de juist lengte is start while loop opnieuw
        if len(code) != code_lengte:
            print('je code is niet de juiste lengte de code moet {} lang zijn'.format(code_lengte))
            continue
        for kleur in code:
            # als een kleur niet een juiste kleur is break de for loop
            if kleur not in kleuren_lst:
                print('kies een code bestaande uit kleuren die beschikbaar zijn!')
                break
            # anders is de code valid dus invalid = false
            else:
                invalid = False
    return code

def player_feedback(geheime_code, poging_code):
    """"Functie waarmee player feedback kan geven op de vraag/poging van de code rader
    args:
        geheime_code, de geheime code uit het spel
        poging_code, de vraag over de geheime code"""

    zwart_wit = dict()
    code_lengte = len(poging_code)
    print('geheime code is {}'.format(geheime_code))
    print('de vraag is {}?'.format(poging_code))
    zwart, wit = -1, -1
    # zwarte en witte pinnen meer dan 0 en niet meer dan de lengte van de geheime code.
    while zwart < 0 or zwart > code_lengte or wit < 0 or  wit > code_lengte:
        try:
            zwart = int(input("Aantal zwarte pinnen: "))
            wit = int(input("Aantal witte pinnen: "))
        except ValueError:
            continue
    # values opslaan in dictionary
    zwart_wit['zwart'], zwart_wit['wit'] = zwart, wit
    return zwart_wit

### functies gebruikt door bots

def alle_combinaties(lengte, lst):
    """Genereert een lijst met alle mogelijk combinaties gegeven een lijst met elementen en hoelang een combinatie is
    bijv. (['a', 'b']['a', 'b'], 2) returned [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]
    args:
        lengte, integer die aanduid hoelang elke combinatie moet zijn in de lijst met alle combinaties
        lst, de lijst die alle elementen bevat waarvan je alle mogelijke combinaties wilt (kleurenlijst)"""

    # https://www.youtube.com/watch?v=QXT_aCFYYDA https://www.hackerrank.com/challenges/itertools-product/problem bronnen die gebruikt zijn bij het leren over itertools product
    # product om een iterable te maken waar elke mogelijke combinatie instaat van lengte repeat met list() een lijst maken van het resultaat van de iterable

    return sorted(list(product(lst, repeat=lengte)))

def feedback_consistente_combinaties(alle_combi_lst, old_feedback):
    """returned een lijst met combinaties die consistent is met de alle voorafgaande feedback.
    args:
        alle_combi_lst, een lijst van alle mogelijke combinaties (return van de functie alle_combinaties)
        old_feedback, lijst die dictionaries bevat met informatie over de oude pogingen/vragen en feedback"""
    # voor elk antwoord in de oude feedback
    for antwoord in old_feedback:
        # nieuwe lijst weer leeg maken per oude feedback( wordt de lijst met nieuwe mogelijke combinaties )
        mogelijke_antwoorden = []
        # voor elk mogelijk antwoord in alle mogelijke combinaties
        for mogelijk_antwoord in alle_combi_lst:
            # als de feedback op (mogelijk antwoord, antwoord) hetzelfde is als de feedback op het afgelopen antwoord
            # voeg dan het mogelijke antwoord toe aan de mogelijke antwoorden lijst
            if bot_feedback(antwoord['poging'], list(mogelijk_antwoord)) == antwoord['feedback']:
                mogelijke_antwoorden.append(mogelijk_antwoord)
        # alle mogelijke combinaties worden nu alle mogelijke antwoorden zo word de lijst mogelijke antwoorden steeds kleiner na elke feedback
        alle_combi_lst = mogelijke_antwoorden.copy()
    return mogelijke_antwoorden

def stap_voorruit(combinaties):
    """"Kijkt een stap voorruit, welke feedback elk mogelijk antwoord mogelijk zou kunnen krijgen
         hier komt een worst case uit per mogelijke antwoord de combinatie met de laagste worstcase is de vraag / poging.
         args:
            combinaties, een lijst met alle mogelijke combinaties die consistent zijn met de voorafgaande feedback (return van feedback_consistente_combinaties)"""
    # dictionary voor hoevaak elke mogelijke feedback kan voorkomen
    mogelijkheden = {}
    # dictionary voor de worst_case (=hoogste value in mogelijkheden) van alle combinaties
    worst_cases = {}
    # for loop om worstcase van elke mogelijke "poging"/antwoord aan dictionary toetevoegen
    for poging in combinaties:
        # for loop om mogelijke feedback bij te houden van elke mogelijke poging met elk mogelijk antwoord
        for antwoord in combinaties:
            # str van de feedback maken omdat dict geen key kan zijn
            fb = str(bot_feedback(list(antwoord), list(poging)))
            if fb in mogelijkheden:
                mogelijkheden[fb] += 1
            else:
                mogelijkheden[fb] = 1
        # elke mogelijke poging heeft een worst_case (de grooste waarde uit mogelijkheden) voeg deze toe aan de worst_cases dictionary
        worst_cases[(poging)] = (max(mogelijkheden.values()))
        # clear de mogelijkheden dict
        mogelijkheden = {}

    # return de key(=poging/vraag) van de laagste value(worst-case) in de worst_cases dictionary.
    # dit is de beste(laagste) worst-case.
    return list(min(worst_cases, key=worst_cases.get))

### AI bot functies/heuristieken

def simple_strategy(lengte_code, poging, old_feedback):
    """ Shapiro, E. (1983). Playing Mastermind Logically. SIGART Newsletter, Vol. 85, pp. 28 – 29.
    Kiest een random antwoord uit een lijst met alle mogelijke combinaties voor de eerste poging
    De volgende poging(en) zijn consistent met de gegeven feedback op voorafgaande poging(en) tot dat de geheime combinatie geraden is
    args:
        lengte_code lengte van de geheime code.
        poging, hoeveelste poging in het spel
        old_feedback, alle voorafgaande feedback/vragen uit het spel"""
    # lijst van alle mogelijke combinaties
    combinaties = alle_combinaties(lengte_code, kleuren_lst)
    if poging == 1:
        # random keuze uit lijst met alle code mogelijkheden
        return list(random.choice(combinaties))
    # Elke poging na de eerste
    else:
        # de lijst met combinaties inkorten op mogelijke antwoorden die consistent feedback geven met de vorige poging(en)
        combinaties = feedback_consistente_combinaties(combinaties, old_feedback)
        return list(random.choice(combinaties))

def worst_case_strategy(lengte_code, poging, old_feedback):
    """"Knuth, D. (1976-1977). The Computer as Master Mind. Journal of Recreational Mathematics, Vol. 9, No. 1,
    pp. 1–6.
    In het worst case algoritme wordt voor elke mogelijk poging (die consistent is met alle vorige feedback).
    Gekeken welke feedback deze mogelijke poging zou krijgen voor elk mogelijk antwoord.
    De poging met de laagste worst case (worst case van het aantal overgebleven mogelijke combinaties na het stellen/vragen van die poging), wordt de vraag die het algoritme stelt.
    args:
        lengte_code lengte van de geheime code.
        poging, hoeveelste poging in het spel
        old_feedback, alle voorafgaande feedback/vragen uit het spel"""
    def eerste_poging():
        """hardcoded eerste poging voor de worst case strategy returned een code waarvan de eerste helft een random kleur is en de andere helft een andere random kleur"""
        eerste_poging = []
        kleur = random.choice(kleuren_lst)
        # append eerste helft van de kleur code
        for i in range(lengte_code // 2):
            eerste_poging.append(kleur)
        # nieuwe random kleur die niet hetzelfde is als de eerste helft
        while kleur == eerste_poging[0]:
            kleur = random.choice(kleuren_lst)
        # append tweede helft van de kleur code
        for i in range(lengte_code - (lengte_code // 2)):
            eerste_poging.append(kleur)
        return eerste_poging
    if poging == 1:
        # hard code de eerste poging
        return eerste_poging()
    else:
        # alle mogelijke combinaties
        combinaties = alle_combinaties(lengte_code, kleuren_lst)
        # alle mogelijke combinaties consistent met alle feedback
        combinaties = feedback_consistente_combinaties(combinaties, old_feedback)\
        # functie stap_voorruit returned combinatie met laagste worst case
        return stap_voorruit(combinaties)

def sjoerd_strategy(lengte_code, poging, old_feedback):
    """" heuristiek verzonnen door Sjoerd Beetsma.
    Deze strategie stelt eerst voor elke mogelijke kleur de vraag die volledig uit 1 kleur bestaat bijv. code lengte = 4 en kleuren zijn alleen 'G' 'B' 'Y'
    Dan vraagt het algoritme eerst 'GGGG' als tweede vraag 'BBBB' etc..
    Na dat elke kleur gevraagd is werkt het algoritme als volgt:
    Elke kleur die feedback zwart = 0 en wit =  0 heeft gekregen komt niet voor in de geheime code. Elke combinatie die een van deze kleuren bevat wordt uitgesloten.
    Uit de overgebleven lijst van mogelijkheden wordt een willekeurig antwoord gekozen.

    args:
        lengte_code lengte van de geheime code.
        poging, hoeveelste poging in het spel
        old_feedback, alle voorafgaande feedback/vragen uit het spel"""
    combinaties = alle_combinaties(lengte_code, kleuren_lst)
    # eerste pogingen 4x dezelfde kleur als antwoord geven tot dat elke unieke kleur geweest is
    if poging <= len(kleuren_lst):
        kleur = kleuren_lst[poging-1]
        return [kleur,kleur,kleur,kleur]
    # elke mogelijke combinatie verwijderen die een kleur bevat waar de feedback 0 zwart en 0 wit op was
    else:
        for zet in old_feedback:
            # alle vorige pogingen uit de mogelijke combinatie lijst halen
            combinaties.remove(tuple(zet['poging']))
            # als de feedback  0 zwart en 0 wit is
            if zet['feedback']['zwart'] == 0 and zet['feedback']['wit'] == 0:
                for kleur in zet['poging']:
                    for combi in combinaties:
                        if kleur in list(combi):
                            combinaties.remove(combi)
        return list(random.choice(combinaties))

### mainloop van het spel en startup functie
# lijst van kleuren die de pionnen in het spel kunnen hebben
# Red, Blue, Green, Yellow, Orange, Purple (ook nog gesorteerd)
kleuren_lst = ['R','B','G','Y','O','P']
def mainloop(raad_functie, feedback_functie, geheime_code_functie, kleuren, game_length = 10):
    """"Mainloop van het spel Mastermind

    args:
        raad_functie, de functie waarmee de vraag gesteld gaat worden
        feedback_functie, de functie waarmee de feedback bepaald zal worden
        geheime_code_functie, de functie waarmee de geheime code bepaald wordt
        game_length, het maximaal aantal pogingen"""
    #list van dictionaries bijhouden van voorgaande moves en hun feedback
    old_feedback = []
    # counter voor aantal pogingen
    poging_nr = 1
    print("De kleuren in het spel zijn: {}, max pogingen is {}".format(kleuren_lst, game_length))
    # geheime code wordt aangemaakt
    print('Geheime code maken...')
    geheime_code = geheime_code_functie()
    print('Geheime code is klaar')
    code_lengte = len(geheime_code)
    # zolang poging kleiner of gelijk aan game lengte is
    while poging_nr <= game_length:
        print('poging {} uit de {}'.format(poging_nr, game_length))
        ### vraag / poging
        poging_code = raad_functie(code_lengte, poging_nr, old_feedback)
        ### antwoord / feedback
        feedback = feedback_functie(geheime_code, poging_code)
        # voeg dictiorynary van poging + feedback toe aan lijst van alle feedback
        old_feedback.append({'poging':poging_code, 'feedback':feedback})
        print('{} geeft feedback: {}'.format(poging_code, feedback))
        # win conditie
        if feedback['zwart'] == 4:
            print("WIN! WIN! WIN! :)")
            break
        # lose conditie
        elif poging_nr == game_length:
            print("GAME OVER! :(")
            print('de geheime code was {}'.format(geheime_code))
        # poging + 1
        poging_nr += 1

def start_up():
    """
    Functie voor het startmenu van het spel Mastermind, vanuit hier wordt het spel gestart met een bepaalde game mode bepaald door de gebruiker.
    Spel uitleg:
    Het spel mastermind heeft als doel om de geheime (kleur) code te kraken.
    Volgens de standaard regels zijn er 6 verschillende kleuren en is de geheime code 4 lang.
    Er is een codemaker en een codekraker.
    De codekraker maakt de code, vervolgens doet de codekraker een vraag en geeft de codekraker antwoord(feedback).
    Het antwoord bestaat uit witte en zwarte pinnen. Zwart = correcte positie & kleur. Wit = correcte kleur & niet correcte positie.
    Als de code wordt geraden in (standaard) 10 pogingen heeft de codekraker gewonnen.
    Anders heeft de codekraker verloren.
    """
    print("|-----------------------|")
    print("|                       |")
    print("|  M A S T E R M I N D  |")
    print("|                       |")
    print("|-----------------------|")
    print('\n(P = Player(/speler), PC = Computer, B1 = Simple Strategy, B2 = Worst case strategy, B3 = Sjoerd strategy)\n\n(Rader VS Kraker)game modes:')
    game_opties = ['PvP', 'PvPC', 'B1vP', 'B1vPC', 'B2vP', 'B2vPC', 'B3vP', 'B3vPC']
    for optie in game_opties:
        print(optie)
    print("")
    # input valideren voor gamemode keuze
    game_mode = ''
    while game_mode not in game_opties:
        game_mode = input('Voer een game mode in (hoofdletter gevoelig): ')
    # input valideren voor aantal max pogingen in het spel
    max_pogingen = 0
    while max_pogingen <= 0:
        try:
            max_pogingen = int(input('max aantal pogingen (standaard 10)? geef een heel getal boven de 0 of druk gelijk op enter voor standaard aantal pogingen: '))
        # als input geen (positieve) int is max pogingen = standaard aantal pogingen ( 10 )
        except ValueError:
                max_pogingen = 10
                break
    # player
    if game_mode == 'PvP':
        mainloop(player_kleur_code, player_feedback, player_kleur_code, kleuren_lst, max_pogingen)
    elif game_mode == 'PvPC':
        mainloop(player_kleur_code, bot_feedback, bot_geheime_code, kleuren_lst, max_pogingen)
    # simple strategy
    elif game_mode == 'B1vP':
        mainloop(simple_strategy, player_feedback, player_kleur_code, kleuren_lst, max_pogingen)
    elif game_mode == 'B1vPC':
        mainloop(simple_strategy, bot_feedback, bot_geheime_code, kleuren_lst,max_pogingen)
    # worst case strategy
    elif game_mode == 'B2vP':
        mainloop(worst_case_strategy, player_feedback, player_kleur_code, kleuren_lst,max_pogingen)
    elif game_mode == 'B2vPC':
        mainloop(worst_case_strategy, bot_feedback, bot_geheime_code, kleuren_lst,max_pogingen)
    # sjoerd strategy
    elif game_mode == 'B3vP':
        mainloop(sjoerd_strategy, player_feedback, player_kleur_code, kleuren_lst,max_pogingen)
    elif game_mode == 'B3vPC':
        mainloop(sjoerd_strategy, bot_feedback, bot_geheime_code, kleuren_lst,max_pogingen)

start_up()
