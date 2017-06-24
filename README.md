


## PolitikerInnen

**Items und Properties**

- [Vorname](https://www.wikidata.org/wiki/Property:P735) (P735)
- [Geschlecht](https://www.wikidata.org/wiki/Property:P21) (P21)
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
- [Parteizugehörigkeit](https://www.wikidata.org/wiki/Property:P102) (P102)
	- [Die Grünen – Die grüne Alternative](https://www.wikidata.org/wiki/Q193178) (Q193178)
	- [Freiheitliche Partei Österreichs](https://www.wikidata.org/wiki/Q131692) (Q131692)
	- [NEOS – Das Neue Österreich und Liberales Forum](https://www.wikidata.org/wiki/Q13564543) (Q13564543)
	- [Österreichische Volkspartei](https://www.wikidata.org/wiki/Q186867) (Q186867)
	- [Sozialdemokratische Partei Österreichs](https://www.wikidata.org/wiki/Q179111) (Q179111)
	- [Team Stronach](https://www.wikidata.org/wiki/Q103748) (Q103748)
	- [Parteiloser](https://www.wikidata.org/wiki/Q327591) (Q327591)
- [Zugehörigkeit zu](https://www.wikidata.org/wiki/Property:P1416) (P1416)
- [Tätigkeit](https://www.wikidata.org/wiki/Property:P106) (P106)
	- [Politiker](https://www.wikidata.org/wiki/Q82955) (Q82955)
- [Parlaments-ID Österreich](https://www.wikidata.org/wiki/Property:P2280) (P2280): ID in der Datenbank "Wer ist Wer", geführt vom Österreichischen Parlament
- [kandidiert(e) für](https://www.wikidata.org/wiki/Property:P3602) (P3602)
- Wikipedia Seite mit Link (de)

**Beispiele**

- [Alexander van der Bellen](https://www.wikidata.org/wiki/Q78869)
- [Christian Kern](https://www.wikidata.org/wiki/Q18135060)
- [Sebastian Kurz](https://www.wikidata.org/wiki/Q2262885)
- [Angela Merkel](https://www.wikidata.org/wiki/Q567)


**[Wikidata:EveryPolitician](https://www.wikidata.org/w/index.php?title=Wikidata:EveryPolitician)**
- [Wikidata:EveryPolitician/Report:P6](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Report:P6)
- [Wikidata:EveryPolitician/Report:P1313/P1308](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Report:P1313/P1308)
- [Wikidata:EveryPolitician/Report:P39/Q2285706](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Report:P39/Q2285706)
- [Wikidata:EveryPolitician/Contrast Report:Head of Government](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Contrast_Report:Head_of_Government)
- [Wikidata:EveryPolitician/Report:P1313/P39](https://www.wikidata.org/wiki/Wikidata:EveryPolitician/Report:P1313/P39)

**Daten**

- [Offenes Parlament: Personen](https://offenesparlament.at/personen/XXV/)
- [Meine Abgeordneten](https://www.meineabgeordneten.at/)	

**Abfragen**

```
# Alle Politiker mit österr. Staatsbürgerschaft
SELECT ?item ?itemLabel WHERE {
  ?item wdt:P106 wd:Q82955;
        wdt:P27 wd:Q40.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```

```
# Alle Mitglieder des Nationalrates die es je gab
SELECT ?item ?itemLabel
WHERE {
  ?item wdt:P39 wd:Q17535155;
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
```

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
- Wikipedia Seite mit Link (de)

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

## Wahlen

**Items und Properties**

- [Wahl](https://www.wikidata.org/wiki/Q40231) (Q40231)
	- [Parlamentswahl](https://www.wikidata.org/wiki/Q1076105) (Q1076105)
		- [Austrian legislative election](https://www.wikidata.org/wiki/Q22268901) (Q22268901)
			- [Nationalratswahl in Österreich 2013](https://www.wikidata.org/wiki/Q1386143) (Q1386143)
				- [Vorgänger](https://www.wikidata.org/wiki/Property:P155) (P155)
			- [Nationalratswahl in Österreich 2017](https://www.wikidata.org/wiki/Q19311231) (Q19311231)
	- [Präsidentschaftswahl](https://www.wikidata.org/wiki/Q858439) (Q858439)
		- [Bundespräsidentenwahl](https://www.wikidata.org/wiki/Q23498202) (Q23498202)
			- [Bundespräsidentenwahl in Österreich 2016]() (Q19276001) - [zur Wahl stehendes Amt](https://www.wikidata.org/wiki/Property:P541) (P541)
- [Nationalrat](https://www.wikidata.org/wiki/Q871363) (Q871363)
- [Legislaturperiode](https://www.wikidata.org/wiki/Q15238777) (Q15238777)
- Wikipedia Seite mit Link (de)


**Abfragen**

```
ABFRAGE
```






