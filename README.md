


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
	- [Außenminister von Österreich](https://www.wikidata.org/wiki/Q5468294) (Q5468294)
	- [Staatssekretär (Österreich)](https://www.wikidata.org/wiki/Q2325273) (Q2325273)
	- [Bundesobmann der Österreichischen Volkspartei](https://www.wikidata.org/wiki/Q29941061) (Q29941061)
	- [Mitglied des österreichischen Bundesrates](https://www.wikidata.org/wiki/Q19360771) (Q19360771)
	- [Abgeordneter zum Nationalrat](https://www.wikidata.org/wiki/Q17535155) (Q17535155)
	- [Mitglied des Wiener Landtages und Gemeinderates](https://www.wikidata.org/wiki/Q23711521) (Q23711521)
	- [Bundesparteiobmann der FPÖ](https://www.wikidata.org/wiki/Q24256233) (Q24256233)
	- [Mitglied des Europäischen Parlaments](https://www.wikidata.org/wiki/Q27169) (Q27169)
	- [Mitglied des Wiener Landtages und Gemeinderates](https://www.wikidata.org/wiki/Q23711521) (Q23711521)
	- [Kategorie:Abgeordneter zum Nationalrat (Österreich)](https://www.wikidata.org/wiki/Q8620062) (Q8620062)
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
# Alle Mitglieder des Nationalrats
SELECT ?item ?itemLabel
WHERE {
	?item wdt:P39 wd:Q17535155.
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
- [Farbe](https://www.wikidata.org/wiki/Property:P462) (P462)
- [offizielle Website](https://www.wikidata.org/wiki/Property:P856) (P856)
- [Logo](https://www.wikidata.org/wiki/Property:P154) (P154)
- [Amt des Leiters](https://www.wikidata.org/wiki/Property:P2388) (P2388)
- [Vorsitzender](https://www.wikidata.org/wiki/Property:P488) (P488)

**Abfragen**

```
# Alle Mitglieder der ÖVP ever mit Profilbild
SELECT ?pic ?item ?itemLabel
WHERE {
  ?item wdt:P102 wd:Q186867.
  OPTIONAL {
    ?item wdt:P18 ?pic
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
```

## Wahlen

**Items und Properties**

- [Legislaturperiode](https://www.wikidata.org/wiki/Q15238777) (Q15238777)
- [Wahl](https://www.wikidata.org/wiki/Q40231) (Q40231)
- [Parlamentswahl](https://www.wikidata.org/wiki/Q1076105) (Q1076105)
- [Austrian legislative election](https://www.wikidata.org/wiki/Q22268901) (Q22268901)
	- [Nationalratswahl in Österreich 2013](https://www.wikidata.org/wiki/Q1386143) (Q1386143)
		- [Vorgänger](https://www.wikidata.org/wiki/Property:P155) (P155)
	- [Nationalratswahl in Österreich 2017](https://www.wikidata.org/wiki/Q19311231) (Q19311231)
- [zur Wahl stehendes Amt](https://www.wikidata.org/wiki/Property:P541) (P541)
- [Nationalrat](https://www.wikidata.org/wiki/Q871363) (Q871363)


**Abfragen**

```
ABFRAGE
```






