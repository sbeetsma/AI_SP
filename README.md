SPEL UITLEG:
Het spel mastermind heeft als doel om de geheime (kleur) code te kraken.
    Volgens de standaard regels zijn er 6 verschillende kleuren en is de geheime code 4 lang.
    Er is een codemaker en een codekraker.
    De codekraker maakt de code, vervolgens doet de codekraker een vraag en geeft de codekraker antwoord(feedback).
    Het antwoord bestaat uit witte en zwarte pinnen. Zwart = correcte positie & kleur. Wit = correcte kleur & niet correcte positie.
    Als de code wordt geraden in (standaard) 10 pogingen heeft de codekraker gewonnen.
    Anders heeft de codekraker verloren.
    
Instructies progamma starten:
1. download de respository https://github.com/sbeetsma/mastermind
2. unzip alle bestanden
3. open de map mastermind
4. open het bestand mastermind.py

Let op: 
    bij het maken van het game mode keuze (eerste stap na het starten progamma).
    Input moet een van de volgende strings zijn 'PvP', 'PvPC', 'B1vP', 'B1vPC', 'B2vP', 'B2vPC', 'B3vP', 'B3vPC'
    
    P = Player / Echte speler
    PC = PC (automatisch feedback geven en automatisch geheime coden genereren)
    
    B1 = simple strategy
    B2 = worst case strategy
    B3 = sjoerd strategy (eigen heuristiek)
    
    
leerbronnen (staan ook bij de betreffende functies):
    leerbron uitrekenen witte pinnen https://stackoverflow.com/questions/47773412/mastermind-check-result-python
    leerbronnen itertools product https://www.youtube.com/watch?v=QXT_aCFYYDA https://www.hackerrank.com/challenges/itertools-product/problem
bronnen algoritmes/heuristieken
YET ANOTHER MASTERMIND STRATEGY, Barteld Kooi, Department of Philosophy, University of Groningen, The Netherlands
    Shapiro, E. (1983). Playing Mastermind Logically. SIGART Newsletter, Vol. 85, pp. 28 – 29.
    Knuth, D. (1976-1977). The Computer as Master Mind. Journal of Recreational Mathematics, Vol. 9, No. 1, pp. 1–6.
