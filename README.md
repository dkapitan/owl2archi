# owl2archi: conversie script om KIK-V objecten in Archi elementen te importeren

## Doel

Met dit script kan je eenmalig concepten (klasses) met bijbehorende attributen uit de KIK-V Ontologie exporteren t.b.v. import in Archi.

## Werkwijze

Exporteer in Protégé handmatig elke ontologie in een afzonderlijke csv:
- onz-org.csv
- onz-zorg.csv
- onz-pers.csv
- onz-g.csv
- onz-fin.csv

Selecteer hierbij:
- alle klasses (het script maakt nog een selectie)
- de attributen die informatie bevatten: rdfs:label, rdfs:definition, rdfs:isDefinedBy, rdfs:comment, skos:definition, definitionSource, editorNote
- `Include headers in first line` en `Include column with superclasses`

Run dit script, en importeer alle archi-imports in Archi. Voor het gemak is een roundtrip gemaakt en vanuit Archi een export van alle elementen gedaan.

Versie 0.1:
    - bevat alleen objecten, met daarin de object annotaties de gevuld zijn (rdfs:label etc.)
TO DO:
    - superclasses toevoegen, zodat in Archi concept hierarchie te zien is
    - andere relevante relaties toevoegen
