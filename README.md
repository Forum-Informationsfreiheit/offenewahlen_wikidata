# Wikidata und Wahldaten

Wikidata soll die zentrale Datenbank für Parteien, Wahlen und PolitikerInnen aufgebaut werden. Gemeinsam sollen so die Daten eingetragen, gepflegt und genutzt werden, so dass alle mit einem möglichst guten Datenset arbeiten können.

## Erstes Ziel

Gemeinsam sollen die wichtigsten Daten zu allen aktuellen 183 Nationalratsabgeordneten gesammelt und in Wikidata übertragen werden. Dies wären:
- Name
- Vorname
- Nachname
- Wikidata ID
- Geburtsort (Wikidata Item)
- Geburtsdatum
- Geschlecht (Wikidata Item)
- parteizugehörigkeit (Wikidata Item)

Dazu werden die Daten zuerst im Spreadsheet [data/nr-abgeordnete_20170623.csv](data/nr-abgeordnete_20170623.csv) gesammelt. Am besten dazu die Abfrage nach allen Mitgliedern des Nationalrates ausführen und dann in der Suche nach den Nachnamen suchen, um auf die passende Person zu kommen.


Danach werden die Daten mittels eines Python Scripts automatisch in Wikidata importiert.

## PolitikerInnen

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
- [Geburtsort](https://www.wikidata.org/wiki/Property:P19) (P19)
- [Gewählt in](https://www.wikidata.org/wiki/Property:P2715) (P2715)
- [Land der Staatsangehörigkeit](https://www.wikidata.org/wiki/Property:P27) (P27)
	- [Österreich](https://www.wikidata.org/wiki/Q40) (Q40)
- [öffentliches Amt oder Stellung](https://www.wikidata.org/wiki/Property:P39) (P39)
	- [Bundeskanzler](https://www.wikidata.org/wiki/Q1006398) (Q1006398)
	- [Bundespräsident](https://www.wikidata.org/wiki/Q475658) (Q475658)
		- [Amtsinhaber](https://www.wikidata.org/wiki/Property:P1308) (P1308)
	- [Außenminister von Österreich](https://www.wikidata.org/wiki/Q5468294) (Q5468294)
	- [Staatssekretär (Österreich)](https://www.wikidata.org/wiki/Q2325273) (Q2325273)
	- [Bundesobmann der Österreichischen Volkspartei](https://www.wikidata.org/wiki/Q29941061) (Q29941061)
	- [Bundesparteiobmann der FPÖ](https://www.wikidata.org/wiki/Q24256233) (Q24256233)
	- [Abgeordneter zum Nationalrat](https://www.wikidata.org/wiki/Q17535155) (Q17535155)
	- [Kategorie:Abgeordneter zum Nationalrat (Österreich)](https://www.wikidata.org/wiki/Q8620062) (Q8620062)
	- [Mitglied des österreichischen Bundesrates](https://www.wikidata.org/wiki/Q19360771) (Q19360771)
	- [Mitglied des Wiener Landtages und Gemeinderates](https://www.wikidata.org/wiki/Q23711521) (Q23711521)
	- [Mitglied des Europäischen Parlaments](https://www.wikidata.org/wiki/Q27169) (Q27169)
- [Parteizugehörigkeit](https://www.wikidata.org/wiki/Property:P102) (P102): Liste der relevantesten Parteien siehe unter Parteien
- [Zugehörigkeit zu](https://www.wikidata.org/wiki/Property:P1416) (P1416)
- [Tätigkeit](https://www.wikidata.org/wiki/Property:P106) (P106)
	- [Politiker](https://www.wikidata.org/wiki/Q82955) (Q82955)
- [Parlaments-ID Österreich](https://www.wikidata.org/wiki/Property:P2280) (P2280): ID in der Datenbank "Wer ist Wer", geführt vom Österreichischen Parlament
- [kandidiert(e) für](https://www.wikidata.org/wiki/Property:P3602) (P3602)
- [Amtsbezeichnung des Staatsoberhaupts](https://www.wikidata.org/wiki/Property:P1906) (P1906)
- [Amtsinhaber](https://www.wikidata.org/wiki/Property:P1308) (P1308)
- [Leiter der Regierung oder Verwaltung](https://www.wikidata.org/wiki/Property:P6) (P6)
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
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
[Link](http://tinyurl.com/yczz44u9)

```
# Alle Mitglieder des Nationalrates die es je gab
SELECT ?item ?itemLabel
WHERE {
  ?item wdt:P39 wd:Q17535155;
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
```
[Link](http://tinyurl.com/yamh7md4)

```
# show birthplaces of current members of the austrian national council on a map
#defaultView:Map
SELECT ?place ?placeLabel ?personLabel ?coords WHERE {
  ?person p:P39 ?statement. # person holds position <statement>
  ?statement ps:P39 wd:Q17535155. # the position is being member of the European Parliament
  ?statement pq:P580 ?starttime. # the position has a start time...
  FILTER NOT EXISTS {?statement pq:P582 ?endtime} # ... but no end time
  ?person wdt:P19 ?place. # person is born in place
  ?place wdt:P625 ?coords. # the place's coordinates
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
[Link](http://tinyurl.com/y7lheoby)

```
# visualize the genders of Austrian mayors on a map
#defaultView:Map
SELECT ?cityLabel ?coords ?headLabel (?genderLabel as ?layer)
WHERE {
  ?city wdt:P6 ?head. # head of government of city
  ?city wdt:P17 wd:Q40. # city in Austria
  ?city wdt:P625 ?coords. # city's coordinates
  ?head wdt:P21 ?gender. # head's gender
  
  # tell the labelling service explicitly which labels to apply
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".
    ?city rdfs:label ?cityLabel.
    ?head rdfs:label ?headLabel.
    ?gender rdfs:label ?genderLabel.
  }
}
```
[Link](http://tinyurl.com/ybq28naf)

## Parteien

**Items und Properties**

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
	- [Europäische Grüne Partei](https://www.wikidata.org/wiki/Q950179) (Q950179)
	- [Europeans United for Democracy](https://www.wikidata.org/wiki/Q1276239) (Q1276239)
	- [Europäische Allianz für Freiheit](https://www.wikidata.org/wiki/Q1377195) (Q1377195)
	- [Europäische Christliche Politische Bewegung](https://www.wikidata.org/wiki/Q1377279) (Q1377279)
	- [Allianz der Konservativen und Reformer in Europa](https://www.wikidata.org/wiki/Q1577483) (Q1577483)
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

**Abfragen**

```
# Alle Mitglieder des Nationalrates mit allen deren Bildern
SELECT ?item ?itemLabel ?pic
WHERE {
  ?item wdt:P39 wd:Q17535155;
  OPTIONAL {
    ?item wdt:P18 ?pic.
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
```
[Link](http://tinyurl.com/y7sw88tf)

```
# Alle Parteien in Österreich
SELECT ?item ?itemLabel
WHERE {
  ?item wdt:P31 wd:Q7278;
        wdt:P17 wd:Q40.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
```
[Link](http://tinyurl.com/y92a7r9v)

## Wahlen

**Items und Properties**

- [Wahl](https://www.wikidata.org/wiki/Q40231) (Q40231)
	- [Wahlgang](https://www.wikidata.org/wiki/Q24097670) (Q24097670)
	- [Parlamentswahl](https://www.wikidata.org/wiki/Q1076105) (Q1076105)
		- [Austrian legislative election](https://www.wikidata.org/wiki/Q22268901) (Q22268901)
			- [Nationalratswahl in Österreich 2013](https://www.wikidata.org/wiki/Q1386143) (Q1386143)
				- [Vorgänger](https://www.wikidata.org/wiki/Property:P155) (P155)
				- [Nachfolger](https://www.wikidata.org/wiki/Property:P156) (P156)
			- [Nationalratswahl in Österreich 2017](https://www.wikidata.org/wiki/Q19311231) (Q19311231)
	- [Präsidentschaftswahl](https://www.wikidata.org/wiki/Q858439) (Q858439)
		- [Bundespräsidentenwahl](https://www.wikidata.org/wiki/Q23498202) (Q23498202)
			- [Bundespräsidentenwahl in Österreich 2016]() (Q19276001) - [zur Wahl stehendes Amt](https://www.wikidata.org/wiki/Property:P541) (P541)
	- [Kandidat](https://www.wikidata.org/wiki/Property:P726)
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
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
```
[Link](http://tinyurl.com/y9w3evhl)

## Infoboxes

- [Template:Infobox officeholder](https://en.wikipedia.org/wiki/Template:Infobox_officeholder)

## Daten

- [EveryPolitician](http://everypolitician.org/)
- [Parlament](https://www.parlament.gv.at/WWER/NR/)
- [Offenes Parlament: Personen](https://offenesparlament.at/personen/XXV/)
- [Meine Abgeordneten](https://www.meineabgeordneten.at/)




