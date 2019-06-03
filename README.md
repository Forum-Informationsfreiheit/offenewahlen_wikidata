[Well structured political data for the whole world: impossible utopia, or Wikidata at its best?](https://media.ccc.de/v/wikidatacon2017-10035-well_structured_political_data_for_the_whole_world_impossible_utopia_or_wikidata_at_its_best)

# Wikidata und Wahldaten

Wikidata bietet sich als die idealle Datenbank für Informationen zu österreichischen Parteien, Wahlen und PolitikerInnen an - um diese zu sammeln und so auch wieder allen zur verfügung zu stellen. Als ersten Schritt dazu, muss die Datenbasis in Wikidata möglichst gut und komplett sein. Daher sind die meisten Aktivitäten zu Beginn rund um das Eintragen von Daten in Wikidata.

* [Wikidata.org](http://wikidata.org/)
* [SPARQL Query Service](https://query.wikidata.org/)
* [Project Page on Wikidata for Austrian politics](https://www.wikidata.org/wiki/Wikidata:WikiProject_Politics_Austria)

**[http://offenewahlen.at/](http://offenewahlen.at/)**

![Offene Wahlen](https://github.com/OKFNat/offenewahlen-at/blob/master/images/logos/ow-at.png)

## Mitmachen

* [Daten importieren](#daten-importieren)
  * Übersichten erstellen, um den Stand der Daten mitsamt Datenqualität überprüfen zu können
* Sammeln von Tools
* Entwickeln von Anwendungen und Tools
* Dokumentation verbessern: vor allem wichtige Tipps für EinsteigerInnen
* Tutorials schreiben
* [Wikidata Abfragen](https://query.wikidata.org) schreiben
* die Daten nutzen:
  * Visualisierungen nutzen
  * mit anderen Daten kombinieren
  * Analysen machen

## Bisherige Aktivitäten

### Sammeln von Informationen

In dieser Datei wurden die relevanten Informationen rund um Wikidata und österreichische PolitikerInnen, Parteien und Wahlen gesammelt (siehe weiter unten). Wir empfehlen, sich das mal anzusehen, um ein Gefühl für die aktuelle Datenstruktur zu den Items zu bekommen.

### Österr. Nationalrats-Abgeordnete aus EveryPolitician eintragen

**Liste an österr. Nationalratsabgeordneten**

Es gibt aktuell 183 Sitze im österr. Nationalrat. Die Sitzverteilung ist aktuell (27. 5. 2019) wie folgt:
- ﻿ÖVP 61
- ﻿SPÖ 52
- ﻿FPÖ 51
- ﻿NEOS 10
- ﻿JETZT 7
- ﻿Fraktionslos 2

Um die Informationslage zu österr. Nationalratsabgeordneten in Wikidata zu verbessern, wurden die Daten von [EveryPolitician](http://everypolitician.org/) mittels dem Python Tool [wikidataintegrator](https://github.com/SuLab/WikidataIntegrator) importiert. Die dabei verwendeten Daten sind in etwas zwei Jahre alt (Stand 25. Juni 2017). Das dazu verwendete Script findet sich unter `code/everypolitician2wikidata.py`.

Folgende Datenfelder wurden importiert:
- `given_name`: Vorname
- `gender`: Geschlecht
- `birth_date`: Geburtsdatum
- `contact_details` vom Typ Twitter

Folgende Daten wären noch wichtig:
- Parteizugehörigkeit

Zum Ausführen des Scripts wird im `code/`-Ordner eine `include.py`-Datei mit folgendem Inhalt benötigt (USERNAME und PASSWORD sind durch die eigenen Werte zu ersetzen).
```json
data = {
	'wikidata': {
		'user': 'USERNAME',
		'password': 'PASSWORD'
	}
}
```

## Österreich

Generell lassen sich einige Informationen auf [offenewahlen.at](http://offenewahlen.at) finden.

Der Nationalrat besteht in Österreich aus 183 Nationalratsabgeordneten.

was ist der NR?
was macht der NR?
WIKIPEDIA PAGES !!!


## Wikidata und Wahldaten

Wikidata ist der zentrale Ort, um Daten zu PolitikerInnen, Parteien und Wahlen zu sammeln und zu verknüpfen. Ins besondere das Verbinden von verschiedenen "Unique Identifiers" aus verschiedenen anderen Datenbanken ist hierbei zu nennen. So soll es einfach gemacht werden, Daten von verschiedensten Quellen miteinander zu verknüpfen.

### PolitikerInnen

Sammlung an Wikidata Items und Properties rund um PolitikerInnen.

**Items und Properties**

- [Vorname](https://www.wikidata.org/wiki/Property:P735) (P735)
- [Geschlecht](https://www.wikidata.org/wiki/Property:P21) (P21)
	- [männlich](https://www.wikidata.org/wiki/Q6581097) (Q6581097)
	- [weiblich](https://www.wikidata.org/wiki/Q6581072) (Q6581072)
	- [Intersexualität](https://www.wikidata.org/wiki/Q1097630) (Q1097630)
	- [Transfrau](https://www.wikidata.org/wiki/Q1052281) (Q1052281)
	- [Transmann](https://www.wikidata.org/wiki/Q2449503) (Q2449503)
	- [Genderqueer](https://www.wikidata.org/wiki/Q48270) (Q48270);
- [Geburtsdatum](https://www.wikidata.org/wiki/Property:P569) (P569)
- [Geburtsort](https://www.wikidata.org/wiki/Property:P19) (P19
- [Twitter Benutzername](https://www.wikidata.org/wiki/Property:P2002) (P2002)
- [Gewählt in](https://www.wikidata.org/wiki/Property:P2715) (P2715)
- [Land der Staatsangehörigkeit](https://www.wikidata.org/wiki/Property:P27) (P27)
	- [Österreich](https://www.wikidata.org/wiki/Q40) (Q40)
- [öffentliches Amt oder Stellung](https://www.wikidata.org/wiki/Property:P39) (P39)
	- [Bundeskanzler](https://www.wikidata.org/wiki/Q1006398) (Q1006398)
	- [Bundesminister](https://www.wikidata.org/wiki/Q1006360) (Q1006360)
	- [Bundespräsident](https://www.wikidata.org/wiki/Q475658) (Q475658)
		- [Amtsinhaber](https://www.wikidata.org/wiki/Property:P1308) (P1308)
	- [Außenminister von Österreich](https://www.wikidata.org/wiki/Q5468294) (Q5468294)
	- [Bundesminister für Gesundheit](https://www.wikidata.org/wiki/Q24256358) (Q24256358)
	- [Bundesminister für Inneres](https://www.wikidata.org/wiki/Q23938055) (Q23938055)
	- [Bundesminister für Forschung und Wissenschaft](https://www.wikidata.org/wiki/Q24256102) (Q24256102)
	- [Staatssekretär](https://www.wikidata.org/wiki/Q736559) (Q736559)
	- [Staatssekretär (Österreich)](https://www.wikidata.org/wiki/Q2325273) (Q2325273)
	- [Bundesobmann der Österreichischen Volkspartei](https://www.wikidata.org/wiki/Q29941061) (Q29941061)
	- [Bundesparteiobmann der FPÖ](https://www.wikidata.org/wiki/Q24256233) (Q24256233)
	- [Abgeordneter zum Nationalrat](https://www.wikidata.org/wiki/Q17535155) (Q17535155)
	- [Kategorie:Abgeordneter zum Nationalrat (Österreich)](https://www.wikidata.org/wiki/Q8620062) (Q8620062)
	- [Mitglied des österreichischen Bundesrates](https://www.wikidata.org/wiki/Q19360771) (Q19360771)
	- [Mitglied des Wiener Landtages und Gemeinderates](https://www.wikidata.org/wiki/Q23711521) (Q23711521)
	- [Mitglied des Europäischen Parlaments](https://www.wikidata.org/wiki/Q27169) (Q27169)
	- -> [Startzeitpunkt](https://www.wikidata.org/wiki/Property:P580) (P580)
	- -> [Endzeitpunkt](https://www.wikidata.org/wiki/Property:P582) (P582)
- [Parteizugehörigkeit](https://www.wikidata.org/wiki/Property:P102) (P102): Liste der relevantesten Parteien siehe unter Parteien
- [Zugehörigkeit zu](https://www.wikidata.org/wiki/Property:P1416) (P1416)
- [Tätigkeit](https://www.wikidata.org/wiki/Property:P106) (P106)
	- [Politiker](https://www.wikidata.org/wiki/Q82955) (Q82955)
- [Parlaments-ID Österreich](https://www.wikidata.org/wiki/Property:P2280) (P2280): ID in der Datenbank "Wer ist Wer", geführt vom Österreichischen Parlament
- [kandidiert(e) für](https://www.wikidata.org/wiki/Property:P3602) (P3602)
- [Amtsbezeichnung des Staatsoberhaupts](https://www.wikidata.org/wiki/Property:P1906) (P1906)
- [Amtsinhaber](https://www.wikidata.org/wiki/Property:P1308) (P1308)
- [Leiter der Regierung oder Verwaltung](https://www.wikidata.org/wiki/Property:P6) (P6)
- [berufliche Position](https://www.wikidata.org/wiki/Q4164871) (Q4164871)
- [Mensch](https://www.wikidata.org/wiki/Q5) (Q5)
- Wikipedia Seite mit Link (de)

**Beispiele**

- [Alexander van der Bellen](https://www.wikidata.org/wiki/Q78869)
- [Christian Kern](https://www.wikidata.org/wiki/Q18135060)
- [Sebastian Kurz](https://www.wikidata.org/wiki/Q2262885)
- [Angela Merkel](https://www.wikidata.org/wiki/Q567)


**Projekte**
- [Wikidata:WikiProject Politics infoboxes](https://www.wikidata.org/wiki/Wikidata:WikiProject_Politics_infoboxes)
- [Wikidata:WikiProject Heads of state and government](https://www.wikidata.org/wiki/Wikidata:WikiProject_Heads_of_state_and_government)
- [Wikidata:EveryPolitician](https://www.wikidata.org/w/index.php?title=Wikidata:EveryPolitician)
	- [Wikidata:EveryPolitician/Report:P6](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Report:P6): Heads of Government Report
	- [Wikidata:EveryPolitician/Report:P1313/P1308](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Report:P1313/P1308): Officeholders Report
	- [Wikidata:EveryPolitician/Report:P39/Q2285706](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Report:P39/Q2285706): Position held Report
	- [Wikidata:EveryPolitician/Contrast Report:Head of Government](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Contrast_Report:Head_of_Government): Head of Government Contrast Report. Vergleicht verschiedene Eintragungen auf Konsistenz.
	- [Wikidata:EveryPolitician/Report:P1313/P39](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Report:P1313/P39): Officeholders Report.


**Abfragen**

```
# Alle Politiker mit österr. Staatsbürgerschaft
SELECT ?item ?itemLabel WHERE {
  ?item wdt:P106 wd:Q82955;
        wdt:P27 wd:Q40.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }
}
```
[Link](http://tinyurl.com/yczz44u9)

```
# Alle Mitglieder des Nationalrates die es je gab mit allen deren Bildern
SELECT ?item ?itemLabel
WHERE {
  ?item wdt:P39 wd:Q17535155;
  FILTER NOT EXISTS {?statement pq:P582 ?endtime} # ... but no end time
  SERVICE wikibase:label { bd:serviceParam wikibase:language "de" }
}
```
[Link](http://tinyurl.com/yamh7md4)

```
# Alle aktuellen Mitglieder des Nationalrates
SELECT ?person ?personLabel
WHERE {
  ?person p:P39 ?statement. # person holds position <statement>
  ?statement ps:P39 wd:Q17535155. # the position is being member of the European Parliament
  ?statement pq:P580 ?starttime. # the position has a start time...
  FILTER NOT EXISTS {?statement pq:P582 ?endtime} # ... but no end time
  SERVICE wikibase:label { bd:serviceParam wikibase:language "de" }
}
```
[Link](http://tinyurl.com/y7k7fh3q)

```
# zeige geburtsorte von aktuellen mitgliedern des nationalrates auf einer Karte
#defaultView:Map
SELECT ?place ?placeLabel ?personLabel ?coords WHERE {
  ?person p:P39 ?statement. # person holds position <statement>
  ?statement ps:P39 wd:Q17535155. # the position is being member of the austrian national council
  ?statement pq:P580 ?starttime. # the position has a start time...
  FILTER NOT EXISTS {?statement pq:P582 ?endtime} # ... but no end time
  ?person wdt:P19 ?place. # person is born in place
  ?place wdt:P625 ?coords. # the place's coordinates
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }
}
```
[Link](http://tinyurl.com/y7lheoby)

```
# visualisiere die Geschlechter von österr. BürgermeisterInnen auf einer Karte
#defaultView:Map
SELECT ?cityLabel ?coords ?headLabel (?genderLabel as ?layer)
WHERE {
  ?city wdt:P6 ?head. # head of government of city
  ?city wdt:P17 wd:Q40. # city in Austria
  ?city wdt:P625 ?coords. # city's coordinates
  ?head wdt:P21 ?gender. # head's gender

  # tell the labelling service explicitly which labels to apply
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de".
    ?city rdfs:label ?cityLabel.
    ?head rdfs:label ?headLabel.
    ?gender rdfs:label ?genderLabel.
  }
}
```
[Link](http://tinyurl.com/ybq28naf)

### Parteien

Sammlung an Wikidata Items und Properties rund um Parteien.

**Items und Properties**

- [politische Partei](https://www.wikidata.org/wiki/Q7278) (Q7278)
- [politische Ideologie](https://www.wikidata.org/wiki/Property:P1142) (P1142)
- [Name in Amts- oder Originalsprache](https://www.wikidata.org/wiki/Property:P1705) (P1705)
- [Vorsitzender](https://www.wikidata.org/wiki/Property:P488) (P488)
- [Mitglied von](https://www.wikidata.org/wiki/Property:P463) (P463)
	- [Allianz der Liberalen und Demokraten für Europa](https://www.wikidata.org/wiki/Q25079) (Q25079)
	- [Sozialdemokratische Partei Europas](https://www.wikidata.org/wiki/Q220945) (Q220945)
	- [Europäische Linke](https://www.wikidata.org/wiki/Q202649) (Q202649)
	- [Europäische Volkspartei](https://www.wikidata.org/wiki/Q208242) (Q208242)
	- [Allianz der Europäischen nationalen Bewegungen](https://www.wikidata.org/wiki/Q368067) (Q368067)
	- [Europäische Freie Allianz](https://www.wikidata.org/wiki/Q639383) (Q639383)
	- [Europäische Nationale Front](https://www.wikidata.org/wiki/Q653566) (Q653566)
	- [Europäische Demokratische Partei](https://www.wikidata.org/wiki/Q734792) (Q734792)
	- [Bewegung für ein Europa der Freiheit und der Demokratie](https://www.wikidata.org/wiki/Q852329) (Q852329)
	- [Bewegung für ein Europa der Nationen und der Freiheit](https://www.wikidata.org/wiki/Q18907386) (Q18907386)
	- [Europäische Grüne Partei](https://www.wikidata.org/wiki/Q950179) (Q950179)
	- [Europeans United for Democracy](https://www.wikidata.org/wiki/Q1276239) (Q1276239)
	- [Europäische Allianz für Freiheit](https://www.wikidata.org/wiki/Q1377195) (Q1377195)
	- [Europäische Christliche Politische Bewegung](https://www.wikidata.org/wiki/Q1377279) (Q1377279)
	- [Allianz der Konservativen und Reformer in Europa](https://www.wikidata.org/wiki/Q1577483) (Q1577483)
	- [Pirate Parties International](https://www.wikidata.org/wiki/Q170) (Q170)
- [Farbe](https://www.wikidata.org/wiki/Property:P462) (P462)
- [offizielle Website](https://www.wikidata.org/wiki/Property:P856) (P856)
- [Logo](https://www.wikidata.org/wiki/Property:P154) (P154)
- [Amt des Leiters](https://www.wikidata.org/wiki/Property:P2388) (P2388)
- [Vorsitzender](https://www.wikidata.org/wiki/Property:P488) (P488)
- [Mitgliederzahl](https://www.wikidata.org/wiki/Property:P2124) (P2124)
- Wikipedia Seite mit Link (de)

**Parteien**

- [Die Grünen – Die grüne Alternative](https://www.wikidata.org/wiki/Q193178) (Q193178)
- [Freiheitliche Partei Österreichs](https://www.wikidata.org/wiki/Q131692) (Q131692)
- [NEOS – Das Neue Österreich und Liberales Forum](https://www.wikidata.org/wiki/Q13564543) (Q13564543)
- [Österreichische Volkspartei](https://www.wikidata.org/wiki/Q186867) (Q186867)
- [Sozialdemokratische Partei Österreichs](https://www.wikidata.org/wiki/Q179111) (Q179111)
- [Team Stronach](https://www.wikidata.org/wiki/Q103748) (Q103748)
- [Parteiloser](https://www.wikidata.org/wiki/Q327591) (Q327591)
- [Piratenpartei Österreichs](https://www.wikidata.org/wiki/Q695270) (Q695270)
- [Christliche Partei Österreichs](https://www.wikidata.org/wiki/Q578350) (Q578350)
- [Christliche Wählergemeinschaft](https://www.wikidata.org/wiki/Q876085) (Q876085)
- [EU-Austrittspartei für Österreich](https://www.wikidata.org/wiki/Q33697797) (Q33697797)
- [Kommunistische Partei Österreichs](https://www.wikidata.org/wiki/Q161118) (Q161118)
- [Bündnis Zukunft Österreich](https://www.wikidata.org/wiki/Q653833) (Q653833)
- [Der Wandel](https://www.wikidata.org/wiki/Q15805222) (Q15805222)

**Abfragen**

```
# Alle Parteien in Österreich
SELECT ?item ?itemLabel
WHERE {
  ?item wdt:P31 wd:Q7278;
        wdt:P17 wd:Q40.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "de" }
}
```
[Link](http://tinyurl.com/y92a7r9v)

```
# Alle aktiven Parteien in Österreich
SELECT ?item ?itemLabel
WHERE {
  ?item wdt:P31 wd:Q7278;
        wdt:P17 wd:Q40.
  OPTIONAL {
    ?item wdt:P576 ?abolished
  }
  FILTER (!bound(?abolished)).
  SERVICE wikibase:label { bd:serviceParam wikibase:language "de" }
}
```
[Link](http://tinyurl.com/ybkx6g8z)

### Wahlen

Sammlung an Wikidata Items und Properties rund um Wahlen.

**Items und Properties**

- [Wahl](https://www.wikidata.org/wiki/Q40231) (Q40231)
	- [Wahlgang](https://www.wikidata.org/wiki/Q24097670) (Q24097670)
	- [Parlamentswahl](https://www.wikidata.org/wiki/Q1076105) (Q1076105)
		- [Austrian legislative election](https://www.wikidata.org/wiki/Q22268901) (Q22268901)
			- [Nationalratswahl in Österreich 2013](https://www.wikidata.org/wiki/Q1386143) (Q1386143)
			- [Nationalratswahl in Österreich 2017](https://www.wikidata.org/wiki/Q19311231) (Q19311231)
			- Generell:
				- [Vorgänger](https://www.wikidata.org/wiki/Property:P155) (P155)
				- [Nachfolger](https://www.wikidata.org/wiki/Property:P156) (P156)
	- [Präsidentschaftswahl](https://www.wikidata.org/wiki/Q858439) (Q858439)
		- [Bundespräsidentenwahl](https://www.wikidata.org/wiki/Q23498202) (Q23498202)
			- [Bundespräsidentenwahl in Österreich 2016]() (Q19276001) - [zur Wahl stehendes Amt](https://www.wikidata.org/wiki/Property:P541) (P541)
	- [Kandidat](https://www.wikidata.org/wiki/Property:P726)
	- [Ergebnisse der Wahlen zum Europäischen Parlament in Österreich](https://www.wikidata.org/wiki/Q4825411) (Q4825411)
- [Nationalrat](https://www.wikidata.org/wiki/Q871363) (Q871363)
- [Bundesrat](https://www.wikidata.org/wiki/Q557150) (Q557150)
- [Legislaturperiode](https://www.wikidata.org/wiki/Q15238777) (Q15238777)
- [Anzahl der Sitze](https://www.wikidata.org/wiki/Property:P1342) (P1342)
- [Wählerschaft](https://www.wikidata.org/wiki/Property:P1831) (P1831)
- [abgegebene Stimme](https://www.wikidata.org/wiki/Property:P1868) (P1868)
- [Anzahl gültiger Stimmen](https://www.wikidata.org/wiki/Property:P1697) (P1697)
- [Anzahl der Sitze in gesetzgebendem Organ](https://www.wikidata.org/wiki/Property:P1410) (P1410)
- [Stimmen](https://www.wikidata.org/wiki/Property:P1111) (P1111)
- [erfolgreicher Kandidat](https://www.wikidata.org/wiki/Property:P991) (P991)
- Wikipedia Seite mit Link (de)

```
# Alle "Austrian legislative elections"
SELECT ?item ?itemLabel
WHERE {
  ?item wdt:P31 wd:Q22268901;
        wdt:P17 wd:Q40.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "de" }
}
```
[Link](http://tinyurl.com/y9w3evhl)

## Daten importieren

Als aller ersten Schritt sollen möglichst viele frei zugängliche Daten in Wikidata importiert werden. Wir haben vor wie folgt anzufangen:

1. Nationalratsabgeordete von EveryPolitician: Stefan dabei
2. KandidatInnen NRW17
3. Parteienregister

Unter [Wiki: Daten](https://github.com/OKFNat/offenewahlen-at/wiki/Daten) sind diverse Datensets zu finden. Wenn du bei den Imports mithelfen möchtest, [meld dich bitte](http://offenewahlen.at/kontakt).

**Limitations:** Account with at least 4 days of age and at least 50 edits

## Resources

### Wikidata

* [wikidata.org](https://www.wikidata.org/)
* [Wikidata API](https://www.wikidata.org/w/api.php)
* [Hilfe](https://www.wikidata.org/wiki/Wikidata:Introduction/de)
* [Template:Infobox officeholder](https://en.wikipedia.org/wiki/Template:Infobox_officeholder)
* [A Gentle Introduction to Wikidata for Absolute Beginners - including non-techies!](https://www.youtube.com/watch?v=eVrAx3AmUvA)
* [Wikidata Game](https://tools.wmflabs.org/wikidata-game/#)

### SPARQL

* [Wikidata Query Service](http://query.wikidata.org/)
* [SPARQL Hilfe](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help)
* [Examples](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples)
* [List of Properties](https://www.wikidata.org/wiki/Wikidata:List_of_properties)
* [SPARQL for absolute beginners](https://commons.wikimedia.org/wiki/File:SPARQL_for_absolute_beginners_-_CEE_conference_2017_Warsaw.pdf)

### Tools

* [WikidataQueryServiceR](https://github.com/bearloga/WikidataQueryServiceR): R wrapper for the Wikidata Query Service.
* [WikidataR](https://github.com/Ironholds/WikidataR): R wrapper for the Wikidata API.
* [WikidataIntegrator](https://github.com/SuLab/WikidataIntegrator): Python tool for the API
* [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot)
* [QuickStatement](https://tools.wmflabs.org/wikidata-todo/quick_statements.php)
* [External tools](https://www.wikidata.org/wiki/Wikidata:Tools/External_tools/de)
* [Tools Directory](https://tools.wmflabs.org/hay/directory/#/search/wikidata)
