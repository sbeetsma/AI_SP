import random

# lijst van kleuren die de pionnen in het spel kunnen hebben
# Red, Blue, Green, Yellow, Orange, Purple
kleuren_lst = ['R','B','G','Y','O','P']

### bot
def bot_code_random(code_lengte=4):
    """"functie om een random kleur code te genereren"""
    random_code = []
    for i in range(code_lengte):
        random_code.append(random.choice(kleuren_lst))
    return random_code
###
### functie om kleurcode te raden en te maken voor player
def kleur_code_player(code_lengte=4):
    """Functie om een gok te ontvangen en te controleren of de gegeven input wel de juiste input is voor een kleurcode.
    Ook wordt deze functie gebruikt als de speler zelf een kleurcode maakt
    args:
    -code_lengte, argument voor de lengte van de kleurcode standaard 4"""
    valid = False
    while not valid:
        code = list(input("input een kleurcode bijv 'RRBB'").upper())
        # als code niet de juist lengte is start while loop opnieuw
        if len(code) != code_lengte:
            continue
        for kleur in code:
            if kleur not in kleuren_lst:
                continue
            return code

def bot_feedback(geheime_code, poging_code, poging):
    """geeft feedback in vorm van een dictionary"""
    def zwart(geheime_code, poging_code):
        """functie die controleert hoeveel kleuren uit de poging voorkomen in de geheime code en op dezelfde positie zijn als in de geheime code"""
        # aantal zwart
        aantal = 0
        # i staat voor index
        for i in range(len(poging_code)):
            if poging_code[i] == geheime_code[i]:
                aantal += 1
        return aantal

    def wit(geheime_code, poging_code):
        """functie die controleert hoeveel kleuren uit de poging voorkomen in de geheime code"""
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
        return aantal - zwart(geheime_code, poging_code)

    zwart_wit = {'zwart':0, 'wit':0}
    zwart_wit['zwart'], zwart_wit['wit'] = zwart(geheime_code, poging_code), wit(geheime_code, poging_code)
    print(zwart_wit)
    return(zwart_wit)

def player_vs_PC(game_length = 10):
    poging = 1
    geheime_code = bot_code_random()
    print(geheime_code)
    while True:
        print('poging {}'.format(poging))
        ### vraagG
        poging_code = kleur_code_player()
        poging += 1
        ### feedback
        feedback = bot_feedback(geheime_code, poging_code, poging)

player_vs_PC()

def mainloop():

def start_game():
