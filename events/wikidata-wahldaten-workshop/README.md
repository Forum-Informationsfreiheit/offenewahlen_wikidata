# Wikidata Wahldaten Workshop

Date: 30th of September 2017

Location: [Wikimedia Austria Office](http://wikimedia.at/) in Vienna.

Facilitators
* [Stefan Kasberger](http://www.stefankasberger.at/)
* Peter Grassberger
* Simeona Cruz
* Tobias Schönberg

## WORKSHOP

In the workshop, we will introduce to Wikidata through elections.

* [Workshop Page](http://offenewahlen.at/termine/wikidata-wahldaten-workshop/)
* [GitHub Repository](https://github.com/OKFNat/offenewahlen-wikidata)

### Timetable

| Timetable     | Agenda       |
|---------------|--------------|
| 14:00 - 14:25 | Welcome |
| 14:25 - 14:40 | Introduction Wikidata |
| 14:40 - 15:00 | Introduction Elections and Wikidata |
| 15:00 - 15:10 | Break |
| 15:10 - 16:35 | Workshop part I|
| 16:35 - 16:50 | Break |
| 16:50 - 17:50 | Workshop part II|
| 17:50 - 18:00 | Conclusion |

### Welcome

Stefan Kasberger and Sonja Fischbauer

* Welcome participants from Open Knowledge Austria and Wikimedia Austria. 
* Friendly space policy
* Short introduction round from participants

### Introduction Wikidata

Tobias Schönberg

Introduction into the world of Wikidata.

### Introduction Elections and Wikidata

Stefan Kasberger

Introduction into data around elections and the status quo of Wikidata in election related data. We will learn what kind of data is created around elections, how the status quo of election data in wikidata is and what we do at #OffeneWahlen AT.

**[Slides](slides_introduction-elections-wikidata.pdf)**

* Election data: [Meine Abgeordnete](http://meineabgeordneten.at/), [data.gv.at](http://data.gv.at/), [BMI](http://www.bmi.gv.at/412/), [Offenes Parlament](http://offenesparlament.at/), [Parteispende.at](http://parteispende.at/), [Neuwal](http://neuwal.com/), [EveryPolitician](http://everypolitician.org/), [weitere Resourcen](http://offenewahlen.at/ressourcen)
* Election data in Wikidata
  * [Bundespräsident Alexander Van der Bellen (Q78869)](https://www.wikidata.org/wiki/Q78869)
  * [All austrian parliament members](http://tinyurl.com/yamh7md4) 
  * [All actual austrian parliament members](http://tinyurl.com/y7k7fh3q) 
  * Map: [Birthplace of austrian mayors, labeled by gender](http://tinyurl.com/ybq28naf) 
* [offenewahlen.at](http://offenewahlen.at/)
  * [Forderungen](http://offenewahlen.at/forderungen-v1)
  * [Wahl-Daten-Party](http://offenewahlen.at/termine/wahl-daten-party/)
  * [Mitmachen](http://offenewahlen.at/mitmachen)
  * [#NRW17-Visualisierung](https://github.com/OKFNat/offenewahlen-nrw17/wiki)
  * [Newsletter](http://offenewahlen.at/newsletter)

### Workshop

#### Beginners

Tobias Schönberg and Simeona Cruz.

Fo beginners in both, Wikidata and election data.

#### Advanced

For beginners in Wikidata with some basic experience around elections and/or election data.

First we will do our first edit in Wikidata, as we look for informations about parties and add them. Then we will have a short look into SPARQL (the Wikidata query language) and the Wikidata API. In the second part we will discuss about problems and the possible future of wikidata around political entities.

* Register Wikidata account
* Add a party
  * Show status of austrian parties in wikidata ([SPARQL query](http://tinyurl.com/yaup9za9))
  * Show austrian party register ([Spreadsheet](https://docs.google.com/spreadsheets/d/1plpcBuIXYEYkjGxXZYkGq2gmsxD3-Hm3qyvnif1XzM8/edit#gid=1391613793))
  * Look if party already exists
  * Do online research about party: e. g. website, Twitter, name, short-name, creation data, color, wikipedia url, 
  * Document status with sources if available
  * Talk about experiences
  * Create/update entries
  * Show status of Austrian parties in Wikidata again ([SPARQL query](http://tinyurl.com/yaup9za9))
* Introduction into SPARQL
  * RDF
    * knowledge in subject–predicate–object triples
  * Queries
    * Items and Properties
  * Find more
    * [query.wikidata.org](https://query.wikidata.org/)
    * [Examples](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples)
    * [Find Properties](https://www.wikidata.org/wiki/Wikidata:List_of_properties)
    * [Help](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/Wikidata_Query_Help)
* Introduction to the API
  * General
    * What is an API
    * [Wikidata API](https://www.wikidata.org/w/api.php)
    * [Wikibase API](https://www.mediawiki.org/wiki/Wikibase/API)
    * Limitations: account with at least 4 days of age and at least 50 edits
    * Login: Username and password
  * [WikidataIntegrator](https://github.com/SuLab/WikidataIntegrator): Python tool for the API
    * developed by life-science researchers
    * 1. Login
    * 2. Prepare data: create an object for each entry
    * 3. Write all objects to the logged-in instance
  * [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot)
  * [QuickStatement](https://tools.wmflabs.org/wikidata-todo/quick_statements.php)
  * other Tools ([External tools](https://www.wikidata.org/wiki/Wikidata:Tools/External_tools/de), [Tools Directory](https://tools.wmflabs.org/hay/directory/#/search/wikidata))
* Discussion --> Document in [Etherpad](http://pad.okfn.org/p/OffeneWahlenAT-Wikidata)
  * Which Data should be in and which sources do you know?
  * Use-Cases for Wikidata around elections: ideas?
  * Unique Identifiers: Problems, chances, paths toward it?
  * What are you interested in?
  * What should be done next / most important data?

### Conclusion

* Feedback round
* Sum Up
* Join [NRW17-Visualisierung](https://github.com/OKFNat/offenewahlen-nrw17/wiki) and [Wahl-Daten-Party](http://offenewahlen.at/termine/wahl-daten-party/)
* Good Bye



