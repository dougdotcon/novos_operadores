# Anhang A Primwellen Operator

*Convertido de: Anhang A Primwellen Operator.PDF*

---


## Página 1


Der Primwellen-Operator
Jeanette Tabea Leue
03. Oktober 2025
Einleitung
Der Primwellen-Operator ist ein mathematisches Verfahren zur strukturellen
Analyse
von
Primzahlen.
Er
erzeugt
eine
Wellenfunktion,
die
durch
das
Auftreten von Primzahlen moduliert wird. Ziel ist es, Muster in der Verteilung
von Primzahlen sichtbar zu machen.
Deﬁnitionen
[label=(]
1.
Kandidatenmenge C
Es werden
nur
Zahlen
betrachtet,
die zu
einer bestimmten
Restklasse
modulo einer Primzahl P gehören:
C={n∈∣n≡rP, r∈RP}
Dabei ist RP eine deﬁnierte Menge von Resten, die als relevant gelten.
2.
Prim-Entscheidung δ(n)
Diese Funktion entscheidet, ob eine Zahl n sowohl zur Kandidatenmenge
gehört als auch eine Primzahl ist:
δ(n)=
3.
Spiegel-Wellenwert Δ(n)
Jeder
erkannte
Primzahl-Kandidat
erhält
ein
Vorzeichen,
das
sich
in
regelmäßigen Abständen spiegelt:
Δ(n)=δ(n)⋅(-1)
⌊n
P⌋
Die Spiegelung erfolgt über die ganzzahlige Division durch P, was eine
periodische Struktur erzeugt.
4.
Primwelle W(n)
Die
Wellenfunktion
entsteht
durch
rekursive
Aufsummierung
der
Spiegel-Wellenwerte:
1


## Página 2


W(0)=0,W(n)=W(n-1)+Δ(n)
Dadurch entsteht eine Wellenform, die durch das Auftreten von Primzahlen
moduliert wird.
Interpretation
Die Primwelle W(n) kann als Signal verstanden werden, das die Verteilung von
Primzahlen in einem bestimmten Zahlenraum reﬂektiert. Durch die alternierenden
Vorzeichen entsteht eine Art „Spiegelung“, die Muster und Symmetrien sichtbar
machen kann.
Beispiel
Für P=5 und RP={1,2} ergibt sich
eine Kandidatenmenge mit Zahlen wie
6,7,11,12,. Die Funktion
δ(n) erkennt
z. B. 7 und
11 als Primzahlen. Die
Wellenfunktion W(n) summiert die jeweiligen Δ(n)-Werte und erzeugt so ein
Wellenmuster.
Ausblick
Der
Primwellen-Operator
kann
als
Grundlage
für
Visualisierungen,
algorithmische Primzahlsuche oder zur Analyse von Primzahlverteilungen dienen.
Erweiterungen sind denkbar durch Variation von P, dynamische Restmengen RP
oder alternative Spiegelungsfunktionen.
2
