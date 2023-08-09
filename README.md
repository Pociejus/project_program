# project_program
Pirmas projektas
Programa parašyta palengvinti ir pagreitinti darbą kuriant sporto programas. Iš esmės tai yra duomenų bazė pratimų su vizualiais pavyzdžiais kuri leidžia spausdinti sporto programos šabloną. 
Galima pildyti duomenų bazę pratimais ar naujais klientais, taip pat kaupiant informaciją ir apie klientus. Programa padaryta naudojantis Django karkasu, dėl jo patogumo naudotis. Nebuvo intencijos kurti interntetinę svetainę, bet šis projektas gali turi galimybę augti.
diegimas: 
1. Kopijuokite visus failus iš repozitorijos
2. Paleiskite komandą `pip install -r requirements.txt`, kad įdiegtumėte reikalingas bibliotekas
3. views.py faile 48 eilutėje reikės nurodyti absolute path iki Arial.ttf failo priklausomai nuo to, kuriame aplanke įsikelsite projektą.
Reikės susikurti savo superuser, nes programos kūrimas yra per admin panelę.
Pirmiausiai sukuriamas klientas pridedant naują userį per admin panelę. Ja pasiekiame prie pradinio adreso pridėje /admin. Useriui automatiškai priskiriamas profilis. Užpildžius duomenis apie klientą kuriama programa jai prisikiant tik klientą bet nepriskiriant programos dienos.
Tada kuriamos programos dienos pasirenkant jėgos pratimus bei tempimo pratimus taip pat per admin panelę. Išsaugojus duomenis galima keisti pratimų serijų bei pakartojimų skaičių.
Naują programą galima atsispausdinti nuėjus į pradinę puslapio direktoriją. Spaudžiame programos, pasirenkame norimą ir atsispausdiname paspaudę ant kiekvienos dienos atskirai.
Galime peržiūrėti informaciją apie klientus. Ten automatiškai suskaičiuojamas KMI ir pateikiamos rekomendacijos pagal šio indekso reikšmę bei paskaičiuojamas pulsas reikiamoms kardio treniruotėms pagal kliento amžių. 
