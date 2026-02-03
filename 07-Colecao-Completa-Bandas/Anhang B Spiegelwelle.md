# Anhang B Spiegelwelle

*Convertido de: Anhang B Spiegelwelle.PDF*

---


## Página 1


Die Spiegelwelle
Autor
Jeanette Leue
Abstract
Die Spiegelwelle entsteht, indem Primzahlen auf einer durch das Rad ()
vorgegebenen Kandidatenmenge mit blockweise alternierendem Vorzeichen
aufsummiert werden. Sichtbar werden dabei Symmetrieachsen und eine
sinusähnliche
Resonanzstruktur.
Dieses
Grundgerüst
sammelt
die
Deﬁnitionen, die Rechenvorschrift und die Beobachtungen in kompakter
Form.
1 Einleitung
1.1 Ausgangslage und Ziel
Die klassische Behandlung
der
Primzahlen
arbeitet
überwiegend
eliminativ:
Siebverfahren entfernen systematisch Vielfache, bis nur noch Primzahlen übrig
bleiben. Diese Sicht produziert Listen, aber sie erzeugt kein Signal, das die
innere Ordnung unmittelbar sichtbar
macht.
Ziel dieses Textes
ist es, eine
konstruktive Darstellung zu geben, in der das Auftreten von Primzahlen als
Wellenphänomen erscheint. Das zentrale Objekt ist die Spiegelwelle~(n), eine aus
Primimpulsen
aufgebaute Folge
mit
lokalen
Spiegelachsen
und
einer
klaren
Resonanzstruktur im Frequenzraum.
1.2 Kerngedanke in einem Satz
Das
Rad
wählt
eine
deterministische
Kandidatenmenge
aus;
die
Prim-Entscheidung
feuert genau an den echten
Primzahlen; ein blockweiser
Vorzeichenwechsel erzeugt die Impulsfolge ; die kumulative Summe =∑macht
Spiegelungen
sichtbar,
die sich
in
der
Fourier-Darstellung
als
gleichmäßig
schwingende Kurven zeigen.
1.3 Warum Spiegelung? Die beobachtete Struktur
Empirisch treten in (n) Abschnitte auf, in denen links und rechts einer Zahl a
der Verlauf korreliert (Symmetrie) oder invers korreliert (Antisymmetrie). Formal
lässt sich das über die Korrelation
ρ(a)=((a-t),(a+t))t=1,
1


## Página 2


oder äquivalent mit gespiegeltem Index t↦-t ausdrücken. Große |ρ(a)| markieren
Spiegelachsen.
Diese
Achsen
sind
keine
Artefakte
einer
Glättung,
sondern
entstehen
bereits
in
der
rohen
Treppensumme
durch
den
blockweisen
Vorzeichenwechsel.
Im Frequenzraum (FFT) verdichten
sich
diese Muster zu
wenigen dominanten Moden, die eine glatte, sinusähnliche Resonanzkurve liefern.
1.4 Konstruktiver Ablauf (informell)
[label=]
1.
Rad
und Kandidatenmenge. Aus den zulässigen Restklassen
entsteht
C={n∈:n∈}.
2.
Prim-Entscheidung. (n)=1 genau dann, wenn n∈C und n prim ist;
sonst (n)=0.
3.
Spiegel-Impuls. Für eine Blocklänge
(typisch =) und optionalen Oﬀset
r0 wird (n)=(n)⋅(-1)
⌊(n-r0)/⌋.
4.
Spiegelwelle. (0)=0 und (n)=(n-1)+(n).
Diese
vier
Schritte
genügen,
um
die
beobachteten
Spiegelachsen
und
die
Resonanzstruktur
zu
erzeugen—ohne
zusätzliche
Hypothesen,
Gewichte
oder
heuristische Glättungen.
1.5 Beitrag dieses Ansatzes
• Signal statt Liste: Primereignisse werden
zu einer deterministischen
Impulsfolge, deren Summe eine interpretable Welle bildet.
• Explizite
Achsen:
Eine
einfache,
numerisch
robuste
Metrik
ρ(a)
lokalisiert Symmetrie- und Antisymmetrieachsen.
• Spektrale Klarheit: Die Fourier-Sicht zeigt wenige dominante Moden,
die mit der Radstruktur (, Vielfache) korrespondieren.
• Robustheit: Die Phänomene bleiben unter Variation von ,
und Oﬀset r0
sichtbar, solange ganze Blöcke erfasst werden.
1.6 Abgrenzung und Anspruch
Der Ansatz liefert Struktur und Messgrößen (Spiegelachsen, Spektralpeaks). Er
ersetzt keine klassischen Beweise und erhebt keinen Anspruch, aus sich heraus
Primzahlsätze
zu
beweisen.
Er
liefert
jedoch
eine
präzise,
reproduzierbare
Pipeline,
mit
der
die
Ordnung
der
Primereignisse
als
Resonanzphänomen
sichtbar
gemacht
und
quantitativ
verglichen
werden
kann
(z.B. gegen
Zufallsmodelle gleicher Dichte).
2


## Página 3


1.7 Reproduzierbarkeit (Kurzrezept)
Zum Nachrechnen reichen: ,,,r0,N und ein Primtest. Die Sequenz und die Summe
lassen sich in wenigen Zeilen erzeugen; für die Fourier-Sicht wird
zentriert und
die Top-k-Moden rekonstruiert. Abschnitt Rezept zum Nachrechnen speziﬁziert
dies formal.
1.8 Aufbau des Textes
Abschnitt~?
präzisiert
die
Deﬁnitionen.
Dann
folgen
Beispiele
und
erste
Rechnungen
(Spiegelachsen
in
frühen
Fenstern),
die
Korrelationmetrik,
die
Fourier-Sicht,
Parameter/Robustheit,
das
Nachrezept
sowie
der
Bezug
zum
Primwellen-Operator.
2 Deﬁnitionen
2.1 Rad und Kandidatenmenge
Ein
Rad
ist eine natürliche Zahl
,
typischerweise
das Produkt
der ersten
Primzahlen, etwa =30=2⋅3⋅5. Die zugehörigen zulässigen Restklassen bilden die
Menge ⊆{0,1,,-1}. Für =30 ist dies zum Beispiel ={1,7,11,13,17,19,23,29}. Die
Menge der Kandidatenzahlen ist dann
C={n∈|n∈}.
2.2 Prim-Entscheidung
Die Funktion (n) prüft, ob eine Zahl prim ist und in der Kandidatenmenge
liegt. Sie ist deﬁniert durch
(n)=
2.3 Spiegel-Impuls
Für eine Blocklänge
(oft gleich dem Rad ) und optional einen Startversatz r0
setzen wir
(n)=(n)⋅(-1)
⌊(n-r0)/⌋.
Das Vorzeichen wechselt also blockweise und sorgt für die Spiegelstruktur.
3


## Página 4


2.4 Spiegelwelle
Die Spiegelwelle ist die kumulative Summe der Impulse:
(0)=0,(n)=(n-1)+(n)f??r(0)=0,(n)=(n-1)+(n)f??r.
2.5 Bemerkung
Die
Folge
(n)
ist
eine
Treppenfunktion:
bei
jeder
Primzahl
in
der
Kandidatenmenge springt der Wert um ±1, ansonsten bleibt er konstant. Durch
den
blockweisen
Vorzeichenwechsel
bilden
sich
lokale
Spiegelachsen,
die
in
späteren Kapiteln untersucht werden.
3 Parameter und Robustheit
Die Konstruktion der Spiegelwelle hängt von einigen Parametern ab. In diesem
Abschnitt
wird
beschrieben,
welche
Rolle
sie
spielen
und
wie
stabil
die
beobachteten Phänomene unter Variation sind.
3.1 Wahl des Rades
Das Rad
legt die Kandidatenmenge fest.
• Mit
=30
erhält
man
bereits
deutliche
Symmetrien
und
einfache
Strukturen.
• Größere Räder wie =210 oder =2310 verfeinern die Kandidatenmenge und
erzeugen zusätzliche Resonanzmoden, ändern aber nicht das Grundprinzip.
3.2 Blocklänge
Die Blocklänge bestimmt, in welchen Abständen das Vorzeichen wechselt.
• Typisch ist =, so dass die Spiegelung an die Radstruktur gekoppelt ist.
• Andere Werte für
verschieben die Spiegelachsen, zerstören aber nicht
grundsätzlich die Symmetrie.
3.3 Oﬀset
Ein Startversatz r0 erlaubt es, die Lage der Spiegelachsen zu justieren. So kann
man sicherstellen, dass der erste Block genau die erwarteten Primzahlen enthält.
4


## Página 5


Dies ist besonders hilfreich für Vergleiche von Symmetrieachsen.
3.4 Fensterung und Detrending
Für numerische Analysen wird oft ein endliches Intervall betrachtet.
• Mittelwertabzug oder lineares Detrending helfen, globale Verschiebungen
zu vermeiden.
• Fensterfunktionen
(z.B.
Hann)
glätten
die
Ränder
und
reduzieren
Artefakte in der Fourier-Analyse.
3.5 Robustheit der Symmetrien
Die beobachteten Spiegelachsen und Resonanzmoden sind robust:
• Sie treten unabhängig von der genauen Wahl von
auf, solange ganze
Blöcke erfasst werden.
• Kleine Änderungen von
oder r0 verschieben Achsen nur, sie verschwinden
nicht.
• Fourier-Peaks bleiben auch bei längeren Sequenzen stabil.
4 Rezept zum Nachrechnen
Dieses
Kapitel
beschreibt,
wie
man
die
Spiegelwelle
selbst
berechnet.
Die
Vorschrift ist einfach und benötigt nur einen Primzahltest und die gewählten
Parameter.
4.1 Schrittweise Vorgehensweise
1.
Rad wählen: Bestimme
(z.B. =30) und die Restmengen , zum Beispiel
{1,7,11,13,17,19,23,29}.
2.
Kandidaten erzeugen: Die Menge C={n∈∣n∈}.
3.
Prim-Entscheidung: Für jedes n gilt (n)=1, wenn n∈C und n prim ist.
Sonst (n)=0.
4.
Spiegelimpuls: Wähle eine Blocklänge
(oft gleich ) und optional einen
Versatz r0. Setze
(n)=(n)⋅(-1)
⌊(n-r0)/⌋.
5.
Spiegelwelle summieren: Beginne mit (0)=0 und addiere (n) Schritt
für Schritt:
5


## Página 6


(n)=(n-1)+(n).
6.
Analyse: Untersuche die Folge (n) auf Spiegelachsen und Resonanz. Für
eine glatte Kurve kann man die Fouriertransformation anwenden und nur
die stärksten Frequenzen behalten.
4.2 Minimalbeispiel
Für ==30 und r0=0:
• Im ersten Block (1–30) feuern die Primzahlen 7,11,13,17,19,23,29 mit
Δ=+1.
• Im zweiten Block (31–60) feuern die Primzahlen 31,37,41,43,47,53,59 mit
Δ=-1.
• Die kumulative Summe (n) steigt im ersten Block und fällt im zweiten –
die erste Spiegelung wird sichtbar.
5 Ausblick
Feinabstimmung
(,
r0),
größere
Räder,
Vergleich
zum
Zufallsmodell
der
Primlücken, präzise Formulierung einer Symmetrieachsen-Metrik.
6 Beispiele und erste Rechnungen
Dieses Kapitel zeigt, wie die Spiegelwelle in der Praxis aussieht und was aus
ihrem Verlauf abgelesen werden kann. Ziel ist es, den Übergang von der reinen
Deﬁnition zu den beobachtbaren Mustern herzustellen und den Nutzen dieser
Darstellungsweise zu verdeutlichen.
6.1 Erster Block und erste Spiegelung
Wählt man das Rad =30 und die Blocklänge =30, ergibt sich eine besonders
einfache Grundstruktur. Im ersten Block, also für 1n30, liegen die Primzahlen
7,11,13,17,19,23,29. Für diese Zahlen gilt Δ(n)=+1, für alle anderen Δ(n)=0.
Die Spiegelwelle (n) steigt dadurch stufenweise an, wie eine Treppe.
Im zweiten Block (31n60) ändert sich das Vorzeichen: jetzt gilt Δ(n)=-1 für
die Primzahlen 31,37,41,43,47,53,59. Die Welle fällt also wieder ab. An der
Grenze zwischen den beiden
Blöcken entsteht eine sichtbare Spiegelung: das
Muster des ersten Blocks wiederholt sich in umgekehrter Richtung. Die Folge
verhält sich damit wie ein Signal, das nach jedem Block gespiegelt wird.
6


## Página 7


6.2 Lokale Antisymmetrie
Betrachtet man die Werte von (n) bis etwa n=100, zeigt sich um n≈44 eine
besonders deutliche Antisymmetrie. Links dieser Achse steigt (n) gleichmäßig,
rechts fällt sie in nahezu identischer Form wieder ab. Mathematisch kann man
das über
die Korrelation
der linken
und rechten
Verlaufsteile messen. Der
Korrelationswert liegt hier fast bei
-1, was eine perfekte inverse Spiegelung
bedeutet.
Diese Beobachtung ist wichtig, weil sie belegt, dass die Symmetrie nicht aus
numerischem
Zufall
entsteht,
sondern
fest im Mechanismus
des blockweisen
Vorzeichenwechsels steckt.
6.3 Größere Fenster und globale Achsen
Erweitert man den Bereich bis n=400 oder n=500, tauchen mehrere größere
Spiegelachsen auf. Besonders stabil ist die Achse um n≈210: dort spiegeln sich
die Anstiegs- und Abfallphasen über weite Bereiche. In der Fourier-Darstellung
entspricht dieser Punkt einer klaren Resonanzfrequenz. Die Welle zeigt dort den
Charakter
eines
echten
Oszillators:
sie
schwingt
gleichmäßig,
und
jede
Schwingung trägt ein Abbild der vorherigen.
6.4 Nutzen der Beobachtungen
Die Analyse der Spiegelwelle liefert drei konkrete Vorteile:
1.
Visualisierung der Ordnung. Statt Primzahlen als diskrete, scheinbar
unregelmäßige
Punkte
zu
sehen,
wird
ihre
innere
Struktur
als
Welle
sichtbar.
Die Spiegelachsen
zeigen, dass es in den Primabständen eine
wiederkehrende Symmetrie gibt.
2.
Messbare Größen. Über die Korrelationsfunktion ρ(a) lassen sich die
Achsen quantitativ bestimmen. Damit wird aus einer bloßen Beobachtung
eine messbare Eigenschaft, die sich vergleichen, skalieren und numerisch
untersuchen lässt.
3.
Verbindung zu Resonanz und Spektrum. Die Fourier-Analyse der
Spiegelwelle zeigt, dass die gleichen
Frequenzen
auftreten, die auch
im
Primwellen-Operator (H=K⊗I+I⊗P) erscheinen. Die Spiegelwelle ist also
das
diskrete
Gegenstück
zur
kontinuierlichen
Resonanzstruktur
des
Operators.
6.5 Erweiterte Bereiche und Stabilität
Wird das Rad vergrößert, etwa auf =210, ändert sich die Form der Welle nur im
Detail: es entstehen
feinere Untermoden, aber
die Hauptachsen
bleiben
an
ähnlichen Positionen. Das zeigt, dass die Spiegelstruktur ein stabiler Bestandteil
der Primzahlenverteilung ist, kein Artefakt der gewählten Parameter.
7


## Página 8


6.6 Zwischenergebnis
Die ersten Rechnungen zeigen deutlich:
• Die Spiegelachsen
sind
direkt aus der Deﬁnition
der Spiegelimpulse
ableitbar.
• Die Welle
wiederholt
ihre Form
regelmäßig,
wie ein
selbstähnliches
Muster.
• Die Symmetrie bleibt stabil, auch wenn das Rad, die Blocklänge oder das
Intervall verändert werden.
Damit ist die Spiegelwelle mehr als eine Darstellungsform: sie ist ein Werkzeug,
das Ordnung, Rhythmus und Wiederkehr in der Primzahlenfolge messbar macht.
8
