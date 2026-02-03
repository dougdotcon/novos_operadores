# Dimensionen aus der Primwelle

*Convertido de: Dimensionen aus der Primwelle.pdf*

---


## Página 1


Dimensionen aus der Primwelle:
Eine konstruktive Geometrie aus
Zahlendynamik
Jeanette Tabea Leue
19. Oktober 2025
1


## Página 2


Zusammenfassung
Wir formulieren eine Geometrie, in der Raum, Zeit und zwei zusätzliche Observablen-
Dimensionen R, C aus der Primwelle selbst entstehen. Ausgangspunkt sind die Prim-
zeit tk = P
j≤k ln pj, die komplexe Welle W(τ) = D(τ)eiϕ(τ), sowie ein bounded
Höhenprofil Z(τ) = L tanh(τ/L). Über Frenet–Serret-Größen folgt die minimale
Einbettung in 3 + 1 Dimensionen; die Achsen R(τ) = Ψ(eτ) −eτ und C(τ) = π(⌊eτ⌋)
spannen zwei interne Dimensionen auf. Wir geben Rang- und Invertibilitätsbeweise,
sowie numerische Checks.
2


## Página 3


Inhaltsverzeichnis
1
Axiome und Grundobjekte
5
1.1
Grundobjekte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.2
Axiome
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.3
Bemerkungen zu den Axiomen . . . . . . . . . . . . . . . . . . . . . . . . .
6
2
Pullback-Metrik und Hodge–Birch-Begrenzung
6
2.1
Induzierte (Pullback-)Metrik . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2
Bogenelement und Eigenzeit . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.3
Hodge–Birch-Begrenzung . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3
Energieinterpretation
7
3.1
Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
4
Interne Dimensionen R und C aus arithmetischen Observablen
10
4.1
Arithmetische Motivation
. . . . . . . . . . . . . . . . . . . . . . . . . . .
10
4.2
Definition der Observablen . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
4.3
Arithmetische Dynamik
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
4.4
Kopplung an die Geometrie
. . . . . . . . . . . . . . . . . . . . . . . . . .
11
4.5
Hodge–Birch–Kohärenz . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
4.6
Arithmetisch-geometrischer Rang . . . . . . . . . . . . . . . . . . . . . . .
11
4.7
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
5
Invertierbarkeit und Rückrechnung der Primzahlen
12
5.1
Inverse der Höhenabbildung . . . . . . . . . . . . . . . . . . . . . . . . . .
12
5.2
Diskrete Knoten und Primzeitsprünge . . . . . . . . . . . . . . . . . . . . .
12
5.3
Exakte Rückrechnung der Primzahlen . . . . . . . . . . . . . . . . . . . . .
13
5.4
Rolle der Observablen R und C . . . . . . . . . . . . . . . . . . . . . . . .
13
5.5
Eindeutigkeit und Nichtverwechslbarkeit . . . . . . . . . . . . . . . . . . .
13
5.6
Robustheit gegenüber Messfehlern . . . . . . . . . . . . . . . . . . . . . . .
13
5.7
Phasenentkopplung und Aliasfreiheitsbedingung . . . . . . . . . . . . . . .
14
5.8
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
6
Numerische Checks (Leitfaden)
14
6.1
Zielsetzung der numerischen Überprüfung . . . . . . . . . . . . . . . . . . .
14
6.2
Struktur des Prüfablaufs . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
6.3
Kohärenzprüfungen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
6.4
Validierung der Observablen R und C . . . . . . . . . . . . . . . . . . . . .
16
6.5
Fehler- und Stabilitätstest . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
6.6
Leitlinien für Rechenumgebungen . . . . . . . . . . . . . . . . . . . . . . .
17
6.7
Interpretation der Resultate . . . . . . . . . . . . . . . . . . . . . . . . . .
17
7
Kosmologische Abbildung
17
7.1
Primzeit-Transformation . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
7.2
Kosmologische Parameterdarstellung
. . . . . . . . . . . . . . . . . . . . .
18
7.3
Interpretation der Parameter . . . . . . . . . . . . . . . . . . . . . . . . . .
18
7.4
Numerischer Vergleich mit Beobachtungen . . . . . . . . . . . . . . . . . .
18
7.5
Kosmologische Deutung der Primzeit . . . . . . . . . . . . . . . . . . . . .
19
3


## Página 4


7.6
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
8
Rechenanhang: Λ, Ψ, π(x)
19
Rechenanhang: Λ, Ψ, π(x)
19
8.1
Elementare Identitäten (exakt)
. . . . . . . . . . . . . . . . . . . . . . . .
20
8.2
Rezept: Λ, Ψ, π bis N (deterministisch) . . . . . . . . . . . . . . . . . . . .
20
8.3
Primzählung ohne Kreiszahl und ohne Trigonometrie
. . . . . . . . . . . .
20
8.4
Komplexität und Speicher . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
8.5
Fehlerfreiheit (arithmetisch, nicht analytisch) . . . . . . . . . . . . . . . . .
21
9
Frenet–Serret–Details
21
9.1
Grundlagen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
9.2
Krümmung und Torsion der Primwelle
. . . . . . . . . . . . . . . . . . . .
21
9.3
Invarianz und Stabilität
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
9.4
Geometrische Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . .
22
9.5
Differentialinvariante Form . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
9.6
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
Begriffs- und Symboltabelle
24
10 Glossar
25
Glossar
25
A Formelsammlung
26
Formelsammlung
26
A.1 A.1 Primzeit und Primzahlen
. . . . . . . . . . . . . . . . . . . . . . . . .
26
A.2 A.2 Geometrie der Primwelle . . . . . . . . . . . . . . . . . . . . . . . . . .
26
A.3 A.3 Arithmetische Observablen
. . . . . . . . . . . . . . . . . . . . . . . .
27
A.4 A.4 Kosmologische Beziehungen . . . . . . . . . . . . . . . . . . . . . . . .
27
A.5 A.5 Differentialstruktur der Primwelle . . . . . . . . . . . . . . . . . . . . .
27
A.6 A.6 Stabilitäts- und Begrenzungsbedingungen
. . . . . . . . . . . . . . . .
27
A.7 A.7 Rückrechnung der Primzahlen (deterministisch) . . . . . . . . . . . . .
28
A.8 A.8 Resonanzraum und 6D–Einbettung . . . . . . . . . . . . . . . . . . . .
28
A.9 A.9 Zusammenfassende Beziehungen
. . . . . . . . . . . . . . . . . . . . .
28
B Teil 1 Testberechnung der Primwellen-Dimensionen
28
B.1 Rekonstruktion der Raum-Dimensionen . . . . . . . . . . . . . . . . . . . .
28
B.2 Vorwärtsrechnung: Von der Primzahl zur Geometrie . . . . . . . . . . . . .
28
B.3 Rückwärtsrechnung: Von der Geometrie zur Primzahl . . . . . . . . . . . .
29
C Teil 2 Berechnung der internen Dimensionen R und C
29
C.1 Resonanzkoordinate R . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
C.2 Ereignisachse C . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
D Teil 3 Berechnung eines kosmologischen Parameters
30
4


## Página 5


1
Axiome und Grundobjekte
Dieses Kapitel fixiert die Objekte, Regularität und Symmetrien der Primwelle. Die Axiome
sind minimal gewählt: sie reichen aus, um in §1 die Raumzeit aus der Kurve zu rekonstru-
ieren, in §2 die Metrik abzuleiten und in §4 die internen Observablen R, C zu definieren.
Notation und Beispiele schließen das Kapitel ab.
1.1
Grundobjekte
Definition 1.1 (Primzeit, diskret und kontinuierlich). Sei (pk)k∈N die Folge der Primzahlen
in aufsteigender Ordnung. Die diskrete Primzeit ist
tk =
k
X
j=1
ln pj,
k ∈N.
Eine kontinuierliche Primzeit τ ∈R entsteht durch stetige Interpolation von (tk), z. B.
stückweise linear mit Knoten {tk}.
Definition 1.2 (Primwelle und Höhenprofil). Die Primwelle ist die komplexe Amplitude
W(τ) = D(τ) eiφ(τ),
mit einer reellen Dämpfung D : R →(0, ∞) und Phase φ : R →R. Das Höhenprofil ist
Z(τ) = L tanh

τ/L

,
L > 0.
Definition 1.3 (Raumkurve und Einbettung). Die Raumkurve der Primwelle ist
γ(τ) =

Re W(τ), Im W(τ), Z(τ)

∈R3.
Der Parameter τ dient zugleich als (Prim-)Zeit.
1.2
Axiome
Wir verwenden folgende Axiome, die die Regularität, Monotonie und Symmetrien festlegen,
ohne zusätzliche Dynamik zu postulieren.
(A1) Regularität.
D, φ ∈C2(R) und Z ∈C∞(R). Insbesondere ist γ ∈C2(R; R3) und
hat γ′(τ) ̸= 0 für eine dichte Teilmenge von R.
(A2) Monotonie und Begrenzung.
Z′(τ) > 0 für alle τ und |Z(τ)| < L. Damit ist
die Höhe global beschränkt (Hodge–Birch-Begrenzung) und strikt monoton wachsend.
(A3) Phasen-Normalisierung.
Die Phase wird bis auf additive Konstanten und ganz-
zahlige 2π-Sprünge fixiert. Für die diskrete Primzeit gilt
∆φk := φ(tk) −φ(tk−1) = ∆tk,
∆tk := tk −tk−1 = ln pk,
so dass die Phaseninkremente mit den Primschritten kohärent sind.
5


## Página 6


(A4) Amplitudenskala.
Die Dämpfung D ist positiv und beschränkt, mit D′(τ) ̸= 0
auf einer dichten Menge. Es existiert Dmax > 0 mit 0 < D(τ) ≤Dmax.
(A5) Phasen- und Zeit-Gaugen.
(i) Phasengauge: φ(τ) 7→φ(τ) + φ0 wirkt nur als
Rotation in der (Re W, Im W)-Ebene.
(ii) Zeitreparametrisierung: Zulässig sind streng monotone C1-Bijektionen τ 7→˜τ(τ), die
die Knoten {tk} unverändert lassen. Die geometrischen Aussagen (Rang, Einbettungsdi-
mension) sind gauge-invariant.
(A6) Diskret-kontinuierliche Kohärenz.
Für die Knoten {tk} stimmen die Größen
(W, φ, Z) mit den diskreten Definitionen überein; zwischen den Knoten sind sie durch die
gewählte Interpolation konsistent fortgesetzt.
1.3
Bemerkungen zu den Axiomen
Bemerkung 1.1 (Minimalität). (A1)–(A6) genügen, um in Abschnitt 1 Krümmung κ und
Torsion T zu definieren, die minimale Einbettungsdimension (siehe Lemma 9.2 zur Torsion)
abzuleiten und in Abschnitt 2 die natürliche Metrik zu bestimmen. Weitere Dynamik (z. B.
Euler–Lagrange-Gleichungen aus der Wellen-Wirkung) ist dafür nicht nötig.
Bemerkung 1.2 (Asymptotik). Aus Z(τ) = L tanh(τ/L) folgen limτ→±∞Z(τ) = ±L
und Z′(τ) = sech2(τ/L) ∈(0, 1]. Damit ist die Höhe global begrenzt und streng wachsend,
was die Stabilität des Trägerzylinders sicherstellt (Hodge–Birch-Band).
Bemerkung 1.3 (Phasenadditivität). Die Wahl ∆φk = ∆tk = ln pk koppelt die geometri-
sche Rotation direkt an die arithmetische Primzeit. Alternative, äquivalente Skalierungen
(etwa Phasenmessung in „turns“) sind durch (A5) abgedeckt und ändern die strukturellen
Aussagen nicht.
2
Pullback-Metrik und Hodge–Birch-Begrenzung
Dieses Kapitel beschreibt die Metrik, die durch die Primwelle auf ihrem Raumträger
induziert wird, und formuliert die geometrische Begrenzung, die als Hodge–Birch-Bedingung
bezeichnet wird. Sie sichert die Stabilität der Einbettung und definiert den zulässigen
Raum für alle weiteren Berechnungen.
2.1
Induzierte (Pullback-)Metrik
Sei γ(τ) = (x(τ), y(τ), z(τ)) die Raumkurve der Primwelle mit x = Re W, y = Im W,
z = Z. Das durch γ auf R zurückgezogene Linienelement lautet
ds2 = γ′(τ)·γ′(τ) dτ 2 = gττ(τ) dτ 2,
wobei
gττ(τ) = (x′(τ))2 + (y′(τ))2 + (z′(τ))2 = |W ′(τ)|2 + (Z′(τ))2.
Definition 2.1 (Pullback-Metrik). Die durch die Primwelle induzierte Pullback-Metrik
ist
gττ(τ) = (D′(τ))2 + (D(τ)φ′(τ))2 + (Z′(τ))2,
gττ(τ) =
1
gττ(τ).
6


## Página 7


Diese Metrik ist positiv definit und regulär für alle τ, da nach (A1)–(A4) keine
der Summanden verschwindet oder divergiert. Damit ist (R, gττ) eine reell-analytische
Riemannsche Linie mit globaler Parameterisierung durch τ.
2.2
Bogenelement und Eigenzeit
Das induzierte Bogenelement der Kurve lautet
ds =
q
gττ(τ) dτ.
Definiert man die Eigenzeit der Primwelle als integriertes Bogenelement, so gilt
s(τ) =
Z τ
0
q
gττ(u) du.
Die Eigenzeit s ist streng monoton wachsend, da √gττ > 0 überall. Damit kann τ 7→s
invertiert werden, und alle geometrischen Größen (Krümmung, Torsion, Energie) lassen
sich sowohl in τ als auch in s ausdrücken.
2.3
Hodge–Birch-Begrenzung
Die Höhe der Primwelle ist durch
Z(τ) = L tanh(τ/L)
gegeben. Aus der Ableitung Z′(τ) = sech2(τ/L) folgt
0 < Z′(τ) ≤1,
|Z(τ)| < L.
Damit ist der gesamte Kurvenverlauf in einem Zylinder
ZL = {(x, y, z) ∈R3 : x2 + y2 ≤D2
max, |z| ≤L}
eingeschlossen. Dieses Zylinderband definiert die Hodge–Birch-Begrenzung.
Definition 2.2 (Hodge–Birch-Band). Für feste obere Amplitude Dmax und Höhenparameter
L > 0 ist das Hodge–Birch-Band definiert als
HDmax,L = { γ(τ) ∈R3 : 0 < D(τ) ≤Dmax, |Z(τ)| ≤L }.
Die Primwelle ist Hodge–Birch-begrenzt, wenn γ(R) ⊆HDmax,L.
3
Energieinterpretation
Die Pullback-Metrik
gττ(τ) = (D′(τ))2 + (D(τ) φ′(τ))2 + (Z′(τ))2
induziert die lokale Energiedichte der Primwelle als
E(τ) = 1
2 gττ(τ) = 1
2

(D′)2 + (Dφ′)2 + (Z′)2

.
Die drei Summanden besitzen jeweils eine klare geometrisch-arithmetische Bedeutung:
7


## Página 8


• Amplitude (D′). Der Term (D′)2 misst die lokale Änderung der Resonanzamplitude
entlang der Primzeit. Er wirkt als Gradientenenergie der Dämpfung: starke Variation
der Hüllkurve kostet Energie.
• Phase (Dφ′). Der Term (Dφ′)2 ist die Rotationsenergie in der komplexen Ebe-
ne (Re W, Im W). Er koppelt die Phase φ an die lokale Amplitude D (klassisch:
„trägheitsähnlich“).
• Höhe (Z′). Der Term (Z′)2 = sech4(τ/L) ist die vertikale Komponente. Über
Z(τ) = L tanh(τ/L) garantiert er globale Begrenzung der Energieflüsse entlang der
Höhe.
Wirkung und Euler–Lagrange-Gleichungen.
Betrachte die Wirkungsfunktional
S[D, φ, Z] =
Z τ1
τ0

1
2
h
(D′)2 + (Dφ′)2 + (Z′)2i
+ V (D, Z)

dτ,
wobei V (D, Z) eine effektive Potentialdichte ist (z. B. zur Kodierung der Hodge–Birch-
Begrenzung als weiches Potential). Die Variation liefert die gekoppelten Euler–Lagrange-
Gleichungen
−D′′ + (φ′)2D −∂DV (D, Z) = 0,
(1)
−(D2φ′)′ = 0,
(2)
−Z′′ −∂ZV (D, Z) = 0.
(3)
Gleichung (2) impliziert die Erhaltung einer Phasenstromgröße J := D2φ′ = const., d. h.
die Rotationsenergie ist über τ kontrolliert. Setzt man V (D, Z) = VZ(Z) und wählt
Z(τ) = L tanh(τ/L) als exakte Lösung von (3) mit geeignetem VZ, so ist die Hodge–Birch-
Begrenzung |Z| ≤L dynamisch stabilisiert.
Energie-Zerlegung (kinetisch/rotatorisch/vertikal).
Mit J = D2φ′ schreibt sich E
als
E(τ) = 1
2

(D′)2 + J2
D2 + (Z′)2

.
Hier tritt J2
D2 als effektiver Zentrifugalterm auf (klassisch: Radialgleichung in der Ebene).
Das führt auf eine Radialgleichung für D:
−D′′ + J2
D3 −∂DV (D, Z) = 0,
deren stationäre Lösungen D′(τ) = 0 das Minimum der effektiven Energie bei gegebener
Höhe Z charakterisieren.
Begrenztheit und Stabilität.
Aus (A2) folgt |Z(τ)| < L und 0 < Z′(τ) ≤1; aus (A4)
folgt 0 < D(τ) ≤Dmax und D′(τ) ist beschränkt. Damit existiert C > 0 mit
E(τ) ≤C
für alle τ,
und die Gesamtenergie H :=
R E(τ) dτ ist endlich auf kompakten Intervallen. Die Primwelle
kann daher in keinem τ-Bereich unbeschränkt Energie akkumulieren; ein Absturz (D →0
bei festem J) oder eine Explosion (D →∞) ist durch die Kopplung und das HB-Band
ausgeschlossen.
8


## Página 9


Virialartige Relation.
Für Lösungen mit konstantem J und stationärem Z (d. h. Z′(τ)
langsam variierend) folgt aus Multiplikation der Radialgleichung mit D und Mittelung
über ein Intervall [τ0, τ1] die virialartige Identität

(D′)2

=
 J2
D2

+

D ∂DV (D, Z)

,
wobei ⟨·⟩die Mittelung bezeichnet. Sie balanciert Gradientenenergie, „Zentrifugalterm“
und Potentialbeitrag — eine präzise Form von Resonanzausgleich, kompatibel mit dem
beobachteten Dämpfungsband.
Kopplung zu arithmetischen Observablen.
Die inneren Observablen
R(τ) = Ψ(eτ) −eτ,
C(τ) = π(⌊eτ⌋)
können als Quellen in V (D, Z; R, C) wirken. Ein einfacher Kopplungsansatz ist eine
additive Penalisierung starker arithmetischer Fluktuationen:
V (D, Z; R, C) = VZ(Z) + λR ΦR(R) + λC ΦC(C),
mit konvexen Funktionalen ΦR/C und Koppelkonstanten λR/C ≥0. In diesem Fall verschiebt
sich die Energiedichte zu
Eeff(τ) = 1
2

(D′)2 + J2
D2 + (Z′)2

+ VZ(Z) + λR ΦR(R) + λC ΦC(C),
und die Euler–Lagrange-Gleichungen erhalten zusätzliche, rein arithmetische Quellterme
∂ZV, ∂DV , ohne die Pullback-Struktur zu zerstören.
Konservative vs. dissipative Sicht.
Die Darstellung als Wirkung S ist konservativ.
Das empirische Dämpfungsband |∆tk+1 −∆tk| ≤ln 3 kann man entweder (i) als harten
Zustandsschnitt interpretieren (Nebenbedingung auf zulässige Trajektorien in τ), oder
(ii) als weiches Dämpfungspotential bV (∆t) in V modellieren, das große Abweichungen
energetisch bestraft. Beide Interpretationen sind mit der Pullback-Metrik kompatibel;
(i) wahrt streng konservative Dynamik, (ii) erzeugt eine effektive Dissipation, die das
HB-Band dynamisch erzwingt.
Zusammenfassung.
Die Energie der Primwelle zerfällt in (i) Amplituden-, (ii) Rotations-
und (iii) Höhenanteil. Die Pullback-Metrik macht diese Zerlegung kanonisch; die Hodge–Birch-
Begrenzung sorgt für globale Stabilität. Über die Erhaltungsgröße J = D2φ′ und eine
mögliche Kopplung an (R, C) erhält man eine geschlossene, variationsbasierte Dynamik,
in der arithmetische Resonanz (diskret) und geometrische Energie (kontinuierlich) in einer
einzigen Energieform E zusammenfallen.
3.1
Interpretation
Die Hodge–Birch-Begrenzung beschreibt den Übergang von arithmetischer zu geometrischer
Stabilität: sie stellt sicher, dass jede Resonanz (Primimpuls) im inneren Parameterraum
begrenzt bleibt. Die Pullback-Metrik misst die lokale Energie der Primwelle, während das
Hodge–Birch-Band die globale Erhaltung dieser Energie garantiert. Die Primmechanik
operiert somit auf einer Riemannschen Linie, die durch eine endliche, kausal abgeschlossene
Geometrie getragen wird.
9


## Página 10


4
Interne Dimensionen R und C aus arithmetischen
Observablen
Neben den geometrischen Dimensionen (x, y, z, t) besitzt die Primwelle zwei interne Di-
mensionen, die nicht aus dem euklidischen Raum, sondern aus der arithmetischen Struktur
der Primzeit hervorgehen. Sie werden durch die Funktionen R(τ) und C(τ) beschrieben
und bilden den inneren Informationsraum der Primmechanik.
4.1
Arithmetische Motivation
Die Primzeit τ misst die kumulative Resonanz der Primzahlen:
τ =
k
X
j=1
ln pj
bzw.
eτ =
k
Y
j=1
pj.
Damit verknüpft die Primwelle zwei Sichtweisen:
• die geometrische Sicht, in der τ eine kontinuierliche Kurvenparameterisierung ist;
• die arithmetische Sicht, in der eτ eine natürliche Schranke im Zahlenraum darstellt.
Die inneren Dimensionen R und C codieren genau diese arithmetischen Eigenschaften —
sie messen, wie stark die reale Zahlverteilung gegenüber der arithmetischen Idealstruktur
oszilliert.
4.2
Definition der Observablen
Definition 4.1 (Resonanzkoordinate R(τ)). Die Resonanzkoordinate R ist die Abweichung
der Chebyshev-Funktion von der geometrischen Expansion:
R(τ) = Ψ(eτ) −eτ,
Ψ(x) =
X
n≤x
Λ(n),
wobei Λ(n) die von Mangoldt-Funktion ist. R(τ) misst die arithmetische Über- oder Unter-
konzentration der Primimpulse im Vergleich zu gleichmäßiger exponentieller Expansion.
Definition 4.2 (Ereignisachse C(s)). Die Ereignisachse C zählt die diskreten Resonan-
zereignisse:
C(s) = π(⌊s⌋),
wobei π(x) die Primzählfunktion ist. C springt genau dann um 1, wenn ein neues Primer-
eignis auftritt; zwischen den Sprüngen bleibt sie konstant.
4.3
Arithmetische Dynamik
Differenziert man R(τ) formal, so ergibt sich
R′(τ) = eτ
Λ(eτ) −1

,
was zeigt, dass R auf diskreten Mengen τk = ln n nicht-differenzierbar ist, aber zwischen
den Knoten regulär bleibt. Damit entsteht eine arithmetische Pulsation — eine Sequenz
feiner Oszillationen über der glatten Geometrie Z(τ).
10


## Página 11


C hingegen ist eine echte Treppenfunktion:
dC
ds =
X
p
δ(s −p),
wobei δ das Dirac-Maß bezeichnet. Die Ereignisachse ist also ein Maß auf der Menge der
Primzahlen, nicht kontinuierlich, aber wohldefiniert als Distribution.
Bemerkung 4.1 (Interpretation). R(τ) ist ein Maß der Resonanzenergie — es zeigt, wo
die Primwelle Energie gewinnt oder verliert, wenn die reale Primverteilung von der idealen
Exponentialform abweicht. C(s) dagegen ist die Resonanzzählung — der „Taktschlag“, der
jedes Primereignis registriert.
4.4
Kopplung an die Geometrie
In der vollständigen Primmechanik wirken R und C als interne Rückkopplung auf die äußere
Geometrie. Dies geschieht über das effektive Potential V (D, Z; R, C) in der Energieform:
V (D, Z; R, C) = VZ(Z) + λR ΦR(R) + λC ΦC(C),
mit λR, λC ≥0 als Kopplungskonstanten. Die Funktionale ΦR und ΦC bestimmen, wie
stark arithmetische Fluktuationen auf die geometrische Dämpfung und Höhe wirken.
• Eine große Abweichung |R| ≫0 erhöht V (D, Z) und dämpft die Amplitude —
arithmetische Irregularität erzeugt geometrische Kompression.
• Sprünge in C(s) führen zu lokalen Phasenverschiebungen ∆φ ∼λC ∆C, die als
diskrete Resonanzimpulse interpretiert werden.
4.5
Hodge–Birch–Kohärenz
Die arithmetischen Dimensionen sind an die Hodge–Birch-Begrenzung gekoppelt. Die
Bedingungen
|R(τ)| ≤Rmax,
|C(s)| ≤Cmax
definieren das innere Band der arithmetischen Stabilität. Nur wenn (R, C) innerhalb
dieses Bandes verbleiben, bleibt auch die äußere Geometrie im HB-Bereich HDmax,L stabil.
Außerhalb dieser Region beginnen die Phasenfluktuationen zu divergieren — ein formales
Analogon zu Resonanzübersteuerung in Wellenmechanik.
4.6
Arithmetisch-geometrischer Rang
Die Gesamtabbildung
Φ : (x, y, z, t, R, C) 7→R6
besitzt eine Jacobi-Matrix
JΦ =



∂τx
∂Rx
∂Cx
∂τy
∂Ry
∂Cy
∂τz
∂Rz
∂Cz


,
deren Rang für dichte Mengen τ den Wert 6 annimmt:
rank(JΦ) = 6.
Dies beweist, dass (R, C) keine abhängigen Projektionen der Raumzeit sind, sondern echte
Dimensionen des vollständigen Resonanzraums.
11


## Página 12


4.7
Zusammenfassung
Die Dimensionen R und C erweitern die Raumzeit um zwei innere Koordinaten, die
arithmetische Information enthalten:
(x, y, z, t) ⊕(R, C) −→vollständige 6D-Primstruktur.
Während (x, y, z, t) die äußere Resonanz beschreibt, liefern (R, C) die innere, informati-
onsgetriebene Dynamik. Erst beide Ebenen zusammen erzeugen ein geschlossenes, selbst-
begrenztes System – eine Raumzeit, die arithmetische Energie trägt und Resonanz misst.
5
Invertierbarkeit und Rückrechnung der Primzahlen
Dieses Kapitel zeigt, dass die Primwelle die Primzahlen verlustfrei kodiert und wie sie
stabil rückgewonnen werden. Zentrale Rollen spielen das Höhenprofil Z(τ) = L tanh(τ/L)
(Hodge–Birch-Band), die Phasenordnung φ sowie die arithmetischen Observablen R und
C.
5.1
Inverse der Höhenabbildung
Lemma 5.1 (Explizite Inversion der Höhe). Die Abbildung τ 7→Z(τ) = L tanh(τ/L) ist
streng monoton wachsend und besitzt die stetige Inverse
τ = T (Z) = L artanh

Z/L

,
|Z| < L.
Beweisskizze. tanh : R →(−1, 1) ist strikt monoton und bijektiv; Skalierung mit L erhält
Monotonie. Die Inverse ist artanh mit geeignetem Faktor L.
Definition 5.2 (Kontinuierliche Rückprojektion). Sei γ(τ) = (x(τ), y(τ), z(τ)) die Raum-
kurve der Primwelle. Die kontinuierliche Rückprojektion der Primzeit aus der Geometrie
ist
τ = T

z

= L artanh

z/L

.
5.2
Diskrete Knoten und Primzeitsprünge
Definition 5.3 (Diskrete Knoten). Die diskreten Primknoten sind die Zeiten (tk)k∈N mit
tk = Pk
j=1 ln pj, die durch die arithmetische Ereignisachse C(s) = π(⌊s⌋) (Sprung um 1)
oder äquivalent durch Phasenmarken φ(tk) −φ(tk−1) = ln pk bestimmt werden.
Definition 5.4 (Differenzoperator). Der diskrete Differenzoperator auf der Primzeit ist
∆τk := τ(tk) −τ(tk−1),
k ≥1,
wobei t0 := 0 gilt.
Lemma 5.5 (Primlogarithmen als Sprünge). Es gilt für alle k ≥1
∆τk = ln pk.
Beweisskizze. Definition von tk und Linearität der Summe liefern ∆τk = tk −tk−1 =
ln pk.
12


## Página 13


5.3
Exakte Rückrechnung der Primzahlen
Theorem 5.6 (Exakte Rekonstruktion). Unter den Axiomen (A1)–(A6) und Theorems 5.1
and 5.5 ist die Primfolge (pk) aus der Geometrie γ eindeutig rückrechenbar:
pk = exp

∆τk

= exp

T (z(tk)) −T (z(tk−1))

.
Beweisskizze. (i) Aus z(t) = Z(t) folgt mit Theorem 5.1 die eindeutige Rückprojektion τ =
T (z). (ii) Mit Theorem 5.5 ist ∆τk = ln pk. (iii) Exponentiation liefert die Behauptung.
Bemerkung 5.1 (Gauge-Invarianz). Additive Phasen-Gaugen φ 7→φ + φ0 und zulässige
Zeitreparametrisierungen (A5) verändern weder z noch die Knoten {tk}. Die Rekonstruktion
ist daher gauge-invariant.
5.4
Rolle der Observablen R und C
Proposition 5.7 (Indexierung und Validierung). Die Ereignisachse C liefert die Inde-
xierung der Knoten: C springt genau an tk. Die Resonanzkoordinate R(τ) = Ψ(eτ) −eτ
dient als Validierung: ihre Oszillationen besitzen charakteristische Extremstellen in der
Nachbarschaft von Primknoten. Zusammen erlauben (R, C) die eindeutige Zuordnung und
Konsistenzprüfung der Rekonstruktion.
Beweisskizze. C ist per Definition Treppenfunktion der Primzahlen; R enthält die von-
Mangoldt-Impulse und unterscheidet Prim- von Nicht-Prim-Ereignissen über Oszillations-
muster. Eindeutigkeit folgt aus der Monotonie von Z.
5.5
Eindeutigkeit und Nichtverwechslbarkeit
Lemma 5.8 (Injectivität auf dem HB-Band). Auf dem Hodge–Birch-Band HDmax,L ist die
Abbildung

γ, C

7−→(pk)k∈N
injektiv bis auf die triviale Wahl von Startindex und globaler Phasenverschiebung.
Beweisskizze. Z ist streng monoton, somit τ eindeutig. C fixiert die Knoten und ihre
Ordnung. Zwei verschiedene Primfolgen erzeugen verschiedene Sprungabstände ∆τk; die
Exponentiation unterscheidet die pk eindeutig.
5.6
Robustheit gegenüber Messfehlern
Definition 5.9 (Fehlermodell). Sei ˜z = z + εz eine gestörte Höhenmessung mit ∥εz∥∞≤
η < L. Definiere die rekonstruierte Zeit ˜τ = T (˜z) und Sprünge g
∆τ k = ˜τ(tk) −˜τ(tk−1).
Lemma 5.10 (Zeitfehler durch Höhenfehler). Es gilt
|˜τ −τ| =
L artanhz + εz
L
−L artanhz
L
 ≤
L
1 −(|z| + η)2/L2
η
L
solange |z| + η < L. Insbesondere ist der Rückprojektionsfehler linear in η und durch den
HB-Abstand L −|z| kontrolliert.
13


## Página 14


Beweisskizze. Mittels Mittelwertsatz auf artanh(u) mit Ableitung (1 −u2)−1.
Proposition 5.11 (Fehlerverstärkung bei Exponentiation). Die Rekonstruktionsformel
pk = exp(∆τk) führt zu einem relativen Fehler
|˜pk −pk|
pk
≤
 g
∆τ k −∆τk
 exp

|g
∆τ k −∆τk|

.
Für kleine Fehler |g
∆τ k −∆τk| ≪1 gilt |˜pk−pk|
pk
≈|g
∆τ k −∆τk|.
Beweisskizze. Aus ˜pk/pk = exp
g
∆τ k −∆τk

folgt die Behauptung.
Corollary 5.12 (Stabilität im Inneren des HB-Bandes). Für |z| ≤L −δ mit δ > 0 ist
artanh Lipschitz-stetig mit Konstante ≤L/δ(2L −δ). In Kombination mit Theorem 5.11
ergibt sich eine uniforme Fehlerkontrolle der Rückrechnung auf kompakten Teilintervallen.
5.7
Phasenentkopplung und Aliasfreiheitsbedingung
Proposition 5.13 (Aliasfreiheit). Angenommen, die Phaseninkremente erfüllen ∆φk =
ln pk (A3) und die Knoten {tk} sind durch C identifizierbar. Dann ist die Rückrechnung
aliasfrei: verschiedene Primfolgen können nicht dieselbe (z, φ, C)-Datenlage erzeugen.
Beweisskizze. Aliasfreiheitsbedingung folgt aus der Kopplung ∆φk = ∆τk, der Monotonie
von Z und der Sprungstruktur von C; diese drei Constraints sind gemeinsam nur mit der
echten Primfolge erfüllbar.
5.8
Zusammenfassung
Die Primwelle kodiert die Primzahlen über die strikt monotone Höhe Z und die diskrete
Knotenstruktur (tk). Die Inversion τ = L artanh(Z/L) und die Differenzen ∆τk = ln pk
liefern die exakte Rückrechnung pk = exp(∆τk), gauge-invariant und stabil innerhalb des
HB-Bandes. Die Observablen (R, C) stellen Indexierung und Validierung sicher; Fehler
bleiben kontrolliert, solange die Messung im Inneren des Bandes erfolgt.
6
Numerische Checks (Leitfaden)
Dieses Kapitel dient als praktischer Leitfaden für die numerische Validierung der theo-
retischen Struktur. Ziel ist es, alle Hauptgleichungen — von der Vorwärtsrechnung der
Primwelle bis zur Rückprojektion der Primzahlen — algorithmisch zu überprüfen, ohne
den formalen Rahmen zu verlassen. Die Tests werden so definiert, dass sie reproduzierbar
und unabhängig von Programmierumgebung oder Datengenauigkeit bleiben.
6.1
Zielsetzung der numerischen Überprüfung
Die numerische Überprüfung verfolgt drei Hauptziele:
1. Kohärenz: Jede Größe (Amplitude, Phase, Höhe, Zeit) muss konsistent mit den
analytischen Definitionen (1.2) bis (5.2) sein.
2. Stabilität: Kleine numerische Abweichungen in den Eingangsgrößen dürfen keine
exponentiellen Fehler in der Rückrechnung erzeugen (§5).
14


## Página 15


3. Reproduzierbarkeit: Gleiche Eingabedaten müssen auf allen Plattformen identische
Ergebnisse liefern — unabhängig von Rundungsfehlern im Bereich < 10−12.
6.2
Struktur des Prüfablaufs
Die numerische Validierung folgt einer festen Sequenz von Schritten, die als Referenzwork-
flow für jede Implementierung gilt:
1. Initialisierung:
• Erzeuge eine Liste der ersten N Primzahlen p1, . . . , pN.
• Berechne die diskrete Primzeit tk =
P
j≤k ln pj.
• Interpoliere tk 7→τ kontinuierlich.
2. Vorwärtsrechnung:
• Berechne Z(τ) = L tanh(τ/L).
• Wähle D(τ) und φ(τ) gemäß (A1)–(A4).
• Evaluiere x(τ) = D cos φ, y(τ) = D sin φ.
3. Pullback-Metrik:
• Bestimme gττ = (D′)2 + (Dφ′)2 + (Z′)2.
• Prüfe positive Definitheit und numerische Glattheit.
4. Rückrechnung:
• Invertiere Z nach τ = L artanh(Z/L).
• Berechne Differenzen ∆τk = τk −τk−1.
• Bestimme die rückgerechneten Primzahlen ˆpk = exp(∆τk).
5. Abweichungsanalyse:
• Vergleiche ˆpk mit den Eingabe-pk.
• Berechne absolute und relative Fehler
εabs
k
= |ˆpk −pk|,
εrel
k = |ˆpk −pk|
pk
.
• Überprüfe die Stabilität
εrel
k ≤10−12
∀k ≤N.
15


## Página 16


6.3
Kohärenzprüfungen
Neben der Primrekonstruktion sind zusätzliche interne Tests erforderlich, um Kohärenz
der Energie, Metrik und Phasenentwicklung zu sichern:
1. Energieerhaltung:
E(τ) = 1
2
h
(D′)2 + (Dφ′)2 + (Z′)2i
muss numerisch konstant (bis auf Rundungsrauschen) bleiben.
2. Hodge–Birch-Begrenzung:
|Z(τ)| ≤L,
|Z′(τ)| ≤1
ist in allen Stützpunkten zu überprüfen.
3. Monotonie: Z′(τ) darf das Vorzeichen nicht wechseln.
4. Phasenbindung: ∆φk −∆τk muss in allen Knoten < 10−12 bleiben.
6.4
Validierung der Observablen R und C
1. Berechne R(τ) = Ψ(eτ) −eτ numerisch bis zu einer Schranke X.
2. Erzeuge C(s) = π(⌊s⌋) als Treppenfunktion.
3. Vergleiche die Maxima/Minima von R mit den Sprungstellen von C.
4. Überprüfe die Kopplung:
sign

R′(τk)

= sign

∆Ck

(Konsistenz von Resonanz- und Zählimpuls).
6.5
Fehler- und Stabilitätstest
Für jedes Intervall (tk−1, tk) wird der lokale Fehler in der Rückprojektion bestimmt:
δτk = τ(tk) −L artanh
Z(tk)
L

,
und in den relativen Primfehler übersetzt:
εrel
k = |exp(δτk) −1| .
Die numerische Stabilität ist gewährleistet, wenn
sup
k εrel
k ≤10−12.
Bei Überschreitung dieses Wertes wird das Gitter τ verfeinert oder der Integrationsschritt
der Ableitungen (D′, φ′, Z′) reduziert.
16


## Página 17


6.6
Leitlinien für Rechenumgebungen
Die Ergebnisse sind unabhängig von Sprache und Plattform, sofern die folgenden techni-
schen Anforderungen erfüllt sind:
• Gleitkommapräzision: mind. 64 Bit (empfohlen: 128 Bit Extended Precision).
• Symbolische Bibliotheken für tanh, artanh und ln sollten fehlerresistent gegen Über-
und Unterläufe sein.
• Die Primzahlen pk sollten mit garantierter Exaktheit (keine Approximierung) bereit-
gestellt werden, z. B. über deterministische Generatoren oder Tabellen.
6.7
Interpretation der Resultate
Erfolgreiche numerische Validierung bedeutet:
1. Die theoretischen Formeln sind arithmetisch konsistent,
2. Die Geometrie der Primwelle ist numerisch stabil,
3. Die Rückrechnung pk = exp(∆τk) ist exakt,
4. Das Hodge–Birch-Band ist invariant unter numerischen Transformationen.
Damit gilt die Primmechanik nicht nur analytisch, sondern auch praktisch als determinis-
tisch verifizierbar.
7
Kosmologische Abbildung
In diesem Kapitel wird die Verbindung zwischen der Primzeit und der kosmologischen Zeit
hergestellt. Die Transformation der Primzeit erlaubt es, die Dynamik der Primwelle auf
großräumige Strukturen (Raumzeit, Expansion, kosmische Skalenfaktoren) abzubilden. Sie
liefert eine direkte Brücke zwischen der arithmetischen Geometrie der Primmechanik und
beobachtbarer Kosmologie.
7.1
Primzeit-Transformation
Definition 7.1 (Primzeit-Transformation). Die Primzeit-Transformation ist definiert als
τ = Tp(t) = ln(1 + αt)
ln(1 + α) ,
wobei α > 0 ein dimensionsloser Skalenparameter ist, der die Resonanzrate zwischen
Primzeit und kosmologischer Zeit festlegt. Der aktuelle Hubble-Parameter ergibt sich aus
der linearen Näherung bei t ≈0 zu
H0 =
α
(1 + α) ln(1 + α).
Bemerkung 7.1 (Bedeutung der Transformation). Die Abbildung t 7→τ verknüpft die
geometrische Zeit der Primwelle mit der physikalischen Zeit der Raumexpansion. Für
kleine Zeiten verhält sich Tp(t) ≈H0 t, während sie für große Zeiten logaritmisch sättigt.
Damit bildet die Primzeit eine natürliche „kompakte“ Zeitachse — eine innere Uhr mit
asymptotischer Begrenzung.
17


## Página 18


7.2
Kosmologische Parameterdarstellung
Für die Anwendung auf beobachtbare Größen (Rotverschiebung, Hubble-Parameter, ko-
movierende Distanz) wird die Primzeit-Transformation invertiert:
t = T −1
p (τ) = (1 + α)τ −1
α
.
Setzt man den Rotverschiebungsfaktor z in Beziehung zu τ über 1 + z = (1 + α)−τ, so
folgen die fundamentalen Funktionen:
Kosmologische Zeit:
t(z) = (1 + α)1/(1+z) −1
α
.
Hubble-Parameter:
H(z) =
α(1 + z)
ln(1 + α) (1 + α)1/(1+z).
Komovierende Distanz:
Dc(z) = c
Z z
0
dz′
H(z′).
7.3
Interpretation der Parameter
• H(z) beschreibt die momentane Expansionsrate der Raumzeit als Funktion der
Rotverschiebung. Im Rahmen der Primmechanik ersetzt α die Rolle der klassischen
Dichteparameter.
• t(z) gibt die Entwicklungszeit eines beobachteten Objekts an, gemessen in Primzeit-
Einheiten.
• Dc(z) liefert die geometrische Entfernung (komovierend) zwischen Beobachter und
Quelle, also die auf die Raumexpansion skalierte Distanz.
Bemerkung 7.2 (Grenzverhalten). Für kleine Rotverschiebung z ≪1 ergibt sich
H(z) ≈H0(1 + z),
t(z) ≈z
H0
,
Dc(z) ≈cz
H0
.
Im Grenzfall großer z (z →∞) saturiert t(z) →1/α und H(z) →0, d.h. die Expansion
flacht ab — die Raumzeit erreicht einen stationären Grenzwert.
7.4
Numerischer Vergleich mit Beobachtungen
Zur empirischen Prüfung können die theoretischen Kurven H(z), t(z) und Dc(z) direkt mit
Daten aus Supernovae Ia oder baryonischen akustischen Oszillationen (BAO) verglichen
werden.
1. Parameterkalibrierung: Der Wert von α wird durch Fit an den heutigen Hubble-
Wert H0 (z. B. Planck-Daten) bestimmt.
18


## Página 19


2. Vergleich der Expansionsrate: Plot H(z)/H0 gegen z und überprüfe lineare
Abweichungen im Bereich 0 < z < 2.
3. Lichtlaufzeit: Berechne t(z) und vergleiche mit beobachteten kosmologischen Al-
tersdaten.
4. Distanzmodul: Integriere Dc(z) und überprüfe Konsistenz mit Supernovae-Diagrammen.
7.5
Kosmologische Deutung der Primzeit
Die Primzeit-Transformation wirkt als universelles Zeitkompressionsgesetz. Sie verknüpft:
arithmetische Resonanz (Primzeit)
↔
kosmische Expansion (Raumzeit).
Die konstante α spielt dabei die Rolle einer „Resonanzdichte“ der Raumzeit — analog zur
Dämpfung D(τ) auf mikroskopischer Ebene.
Bemerkung 7.3 (Dualität der Skalen). Während die Primwelle im Mikroskopischen
Energie und Zahlendichte strukturiert, beschreibt die kosmologische Abbildung ihre ma-
kroskopische Spiegelung in der Dynamik der Raumexpansion. Somit stellt die Abbildung
Tp eine Skalenbrücke zwischen arithmetischer und physikalischer Raumzeit dar.
7.6
Zusammenfassung
Die Primzeit-Transformation
τ = ln(1 + αt)
ln(1 + α)
definiert eine bijektive, stetige Abbildung zwischen der geometrischen Zeit der Primmecha-
nik und der kosmologischen Zeit der Raumexpansion. Die zugehörigen Funktionen H(z),
t(z) und Dc(z) bilden ein selbstkonsistentes Ensemble, das sowohl lokal die Primresonanz
als auch global die kosmische Dynamik abbildet. Die Übereinstimmung mit Beobachtungs-
daten ist das entscheidende Kriterium für die physikalische Validität der Primmechanik
im kosmologischen Maßstab.
8
Rechenanhang: Λ, Ψ, π(x)
Hinweis.
In diesem Anhang bezeichnet π(x) die Primzahlzählfunktion (prime-counting
function): π(x) = #{p prim : p ≤x}. Sie ist nicht die Kreiszahl.
Definitionen (diskret, ohne Transzendente)
von–Mangoldt–Funktion
Λ(n) =



ln p,
falls n = pk mit Primzahl p und k ≥1,
0,
sonst.
Chebyshev–Funktion
Ψ(x) =
X
n≤x
Λ(n)
(diskrete Summe über n ∈N).
Primsummen
ϑ(x) =
X
p≤x
ln p,
π(x) =
X
p≤x
1.
19


## Página 20


8.1
Elementare Identitäten (exakt)
1. Dirichlet–Faltung (Möbius-Inversion). Für das arithmetische log-Funktional
L(n) = ln n gilt
L = 1 ∗Λ
⇐⇒
ln n =
X
d|n
Λ(d),
und daher mit der Möbiusfunktion µ:
Λ = µ ∗L,
Λ(n) =
X
d|n
µ(d) ln
n
d

.
2. Beziehung Ψ–ϑ.
Ψ(x) =
X
m≥1
ϑ

x1/m
,
ϑ(x) =
X
p≤x
ln p.
3. Primzählung aus Λ (gewichtete Summe).
J(x) :=
X
n≤x
Λ(n)
ln n
=
X
pk≤x
1
k
⇒
π(x) = J(x) −
X
k≥2
1
k π

x1/k
.
(Die letzte Gleichung ist exakt; sie subtrahiert die Beiträge der Primpotenzen.)
8.2
Rezept: Λ, Ψ, π bis N (deterministisch)
1. Segmentierter Sieb. Erzeuge alle Primzahlen p ≤N (ohne Fließkomma).
2. Prime Potenzen markieren. Für jedes Prim p setze für k ≥1: Λ(pk) ←ln p
solange pk ≤N; sonst Λ(n) ←0.
3. Akkumulation. Ψ(x) = P
n≤x Λ(n) als Präfixsumme. Parallel: ϑ(x) = P
p≤x ln p,
π(x) = #{p ≤x}.
8.3
Primzählung ohne Kreiszahl und ohne Trigonometrie
• Direkt aus Ψ: J(x) = P
n≤x Λ(n)/ ln n liefert eine „weiche“ Primzählung, die mit
der obigen Korrekturformel exakt zu π(x) wird.
• Teilweise Summation (diskret). Für eine arithmetische Funktion a(n) und
monotones g gilt:
X
n≤x
a(n) g(n) = A(x)g(x) −
X
m<x
A(m)

g(m + 1) −g(m)

,
wobei A(x) = P
n≤x a(n). Mit a(n) = Λ(n) und g(n) = 1/ ln n erhält man eine stabile
Berechnung von J(x) ganz ohne transzendente Winkelfunktionen.
8.4
Komplexität und Speicher
• Segmentierter Sieb bis N: Zeit ˜O(N log log N), Speicher O(
√
N).
• Markieren von Primpotenzen: P
p≤N logp N = O(N/ ln N) Operationen.
• Präfixsummen für Ψ, ϑ, π: linear in N (streaming-fähig).
20


## Página 21


8.5
Fehlerfreiheit (arithmetisch, nicht analytisch)
Alle Formeln oben sind exakt und benötigen nur natürliche Logarithmen und ganzzah-
lige Arithmetik. Es werden keine Kreiszahl-Konstanten, keine Sinus/Cosinus und keine
kontinuierlichen Integrale verwendet. Rundungsfehler treten nur durch die numerische
Darstellung von ln p auf und lassen sich durch feste Präzision kontrollieren.
9
Frenet–Serret–Details
Die Primwelle kann als reguläre Raumkurve
γ(τ) =

x(τ), y(τ), z(τ)

=

D(τ) cos φ(τ), D(τ) sin φ(τ), Z(τ)

aufgefasst werden. Solange D > 0 und φ′, Z′ stetig sind, ist γ regulär und besitzt eine
wohldefinierte Frenet–Serret-Struktur.
9.1
Grundlagen
Definition 9.1 (Frenet–Serret–Rahmen). Für eine reguläre Kurve γ(τ) mit Bogenelement
ds = ∥γ′(τ)∥dτ =
q
(D′)2 + (Dφ′)2 + (Z′)2 dτ,
werden Tangente T, Normale N und Binormale B definiert durch
T =
γ′
∥γ′∥,
N =
T ′
∥T ′∥,
B = T × N.
Sie erfüllen das Frenet–Serret-System
dT
ds = κ N,
(4)
dN
ds = −κ T + τr B,
(5)
dB
ds = −τr N,
(6)
wobei κ(s) die Krümmung und τr(s) die Torsion heißen.
9.2
Krümmung und Torsion der Primwelle
Für γ(τ) in Helixform ergeben sich die Ableitungen
γ′(τ) =

D′ cos φ −Dφ′ sin φ, D′ sin φ + Dφ′ cos φ, Z′
,
und
κ(τ) = ∥γ′(τ) × γ′′(τ)∥
∥γ′(τ)∥3
=
q
(D′φ′′ −D′′φ′)2D2 + (Z′′D′ −Z′D′′)2 + (Z′Dφ′′ −Z′′Dφ′)2
h
(D′)2 + (Dφ′)2 + (Z′)2
i3/2
.
(7)
21


## Página 22


Krümmung.
Mit ∥· ∥als euklidische Norm gilt
κ(τ) = ∥γ′(τ) × γ′′(τ)∥
∥γ′(τ)∥3
=
q
(D′φ′′ −D′′φ′)2D2 + (Z′′D′−Z′D′′)2 + (Z′Dφ′′ −Z′′Dφ′)2
h
(D′)2 + (Dφ′)2 + (Z′)2
i3/2
.
Torsion.
Analog folgt
τr(τ) = det(γ′, γ′′, γ′′′)
∥γ′ × γ′′∥2
,
wobei die Determinante die orientierte Raumkrümmung misst. Für die Primwelle kann τr
meist in der vereinfachten Form
τr(τ) ≈D2φ′φ′′ + D′Dφ′′ −D′2φ′ + Z′Z′′(φ′/D)
(D′)2 + (Dφ′)2 + (Z′)2
genähert werden, sofern Z′ langsam variiert.
9.3
Invarianz und Stabilität
• Skaleninvarianz. Die Größen κ und τr sind invariant unter reparametrisierungen
τ 7→f(τ) mit monotonem f.
• Hodge–Birch-Begrenzung. Da |Z′| ≤1 und |Z′′| ≤2L−1 tanh(τ/L), sind κ(τ)
und τr(τ) global beschränkt:
0 < κ(τ) ≤κmax,
|τr(τ)| ≤τmax < ∞.
• Resonanzstabilität. Die Oszillationen von κ und τr folgen denselben Periodizitäten
wie R(τ) und C(s); starke Resonanzen erscheinen als lokale Maxima der Krümmung.
9.4
Geometrische Interpretation
1. Krümmung κ: misst die lokale Beschleunigung der Primwelle im Resonanzraum.
Hohe Werte entsprechen Regionen starker Primdichte.
2. Torsion τr: beschreibt die Drehung der Primwelle um ihre eigene Achse — ein Maß
für die Kopplung zwischen arithmetischer und geometrischer Phase.
3. Hodge–Birch-Band als Stabilitätsbedingung: κ und τr bleiben innerhalb fester
Grenzen; keine Singularitäten treten auf, solange D > 0 und |Z| < L.
9.5
Differentialinvariante Form
Alternativ kann die Dynamik der Primwelle direkt über die Frenet–Serret–Gleichungen
beschrieben werden:
d
ds



T
N
B


=



0
κ
0
−κ
0
τr
0
−τr
0






T
N
B


.
Damit wird die lokale Orientierung der Welle vollständig durch die Funktionen κ(s) und
τr(s) bestimmt; alle übrigen geometrischen Eigenschaften folgen daraus.
22


## Página 23


9.6
Zusammenfassung
Die Frenet–Serret-Struktur zeigt:
• Die Primwelle ist eine reguläre, torsionsbehaftete Helix mit global begrenzter Krüm-
mung.
• Ihre geometrischen Invarianten κ und τr sind direkt durch (D, φ, Z) und deren
Ableitungen bestimmt.
• Die Stabilität der Kurve folgt aus der Hodge–Birch–Begrenzung und den analytischen
Axiomen (A1)–(A4).
Damit ist die Primwelle nicht nur algebraisch, sondern auch geometrisch vollständig
bestimmt.
23


## Página 24


Begriffs- und Symboltabelle
Symbol
Bedeutung / Beschreibung
W(τ)
Primwelle: komplexe Raumkurve der Primmechanik, W(τ) =
D(τ)eiφ(τ) mit geometrisch-arithmetischer Phase.
D(τ)
Amplitude / Dämpfung: Radius der Primwelle; begrenzt
durch das Hodge–Birch-Band, 0 < D(τ) ≤Dmax.
φ(τ)
Primphase: stetig rotierende Phase der Primwelle; Phasen-
sprünge ∆φk = ln pk.
Z(τ)
Höhenkoordinate: Z(τ) = L tanh(τ/L), begrenzt die verti-
kale Auslenkung der Primwelle.
L
Hodge–Birch-Parameter: charakteristische Höhen- und
Energiegrenze; definiert das Zylinderband |Z| ≤L.
τ
Primzeit: logarithmische Summation τk =
P
j≤k ln pj; konti-
nuierliche Entwicklungsvariable der Primwelle.
t
Kosmologische Zeit: physikalische Zeitkoordinate; mit der
Primzeit über τ = Tp(t) = ln(1+αt)
ln(1+α) verknüpft.
α
Resonanzskalenfaktor: bestimmt das Verhältnis zwischen
arithmetischer und kosmologischer Zeit; erscheint in H0 =
α
(1+α) ln(1+α).
R(τ)
Resonanzkoordinate: arithmetische Observable R(τ) =
Ψ(eτ) −eτ; misst die Abweichung der Primverteilung von
idealer Exponentialform.
C(s)
Ereignisachse: diskrete Zählfunktion C(s) = π(⌊s⌋); sprung-
haft bei jedem Primereignis.
Ψ(x)
Chebyshev-Funktion: Ψ(x) = P
n≤x Λ(n); Summation der
von-Mangoldt-Werte.
Λ(n)
von-Mangoldt-Funktion: Λ(n) = ln p falls n = pk, sonst 0.
π(x)
Primzahlzählfunktion: Anzahl der Primzahlen p ≤x.
γ(τ)
Raumkurve: Vektorabbildung γ(τ) = (x(τ), y(τ), z(τ)) der
Primwelle.
T, N, B
Frenet–Serret-Rahmen: Tangente, Normale, Binormale der
Kurve γ.
κ(τ)
Krümmung: κ = ∥dT/ds∥; misst lokale Richtungsänderung
der Primwelle.
τr(τ)
Torsion: τr = −dB/ds · N; misst die Verdrehung der Kurve
um ihre Achse.
E(τ)
Energiedichte: E = 1
2[(D′)2 + (Dφ′)2 + (Z′)2]; Summe aus
Amplituden-, Rotations- und Höhenenergie.
gττ
Pullback-Metrik: gττ = (D′)2 + (Dφ′)2 + (Z′)2; lokale Geo-
metrie der Primwelle auf R.
HDmax,L
Hodge–Birch-Band: Zylinderbereich {(x, y, z) : x2 + y2 ≤
D2
max, |z| ≤L}, in dem die Primwelle stabil bleibt.
∆τk
Primzeitdifferenz: ∆τk = τk −τk−1 = ln pk; elementare
Resonanzeinheit.
pk
k-te Primzahl: direkt rekonstruierbar durch pk = exp(∆τk).
( )
( )
α(1+z)
24


## Página 25


10
Glossar
Primwelle Die geometrische Darstellung der Primzahlen als stetige Raumkurve. Sie
vereint arithmetische Struktur (Primfolge) und geometrische Dynamik (Resonanz
und Dämpfung). Jede Primzahl entspricht einem stabilen Punkt der Welle.
Primzeit Die logaritmisch akkumulierte Zeitvariable der Primmechanik. Sie ersetzt die
gewöhnliche lineare Zeit und spiegelt die interne Frequenzordnung der Primzahlen
wider.
Primarcode Die interne Kodierung der Primstruktur. Er beschreibt die Resonanzfolge
der Primwelle als deterministische Abbildung zwischen diskreten und kontinuierlichen
Zuständen.
Primmechanik Das übergeordnete Modell, das die Primzahlen als Ergebnis einer kausa-
len, geometrischen Dynamik beschreibt. Sie verbindet Zahlentheorie, Raumzeit und
Energieerhaltung zu einem geschlossenen System.
Hodge–Birch–Begrenzung Die energetische und geometrische Grenze, innerhalb derer
die Primwelle stabil bleibt. Sie schließt divergente Lösungen aus und definiert das
zulässige Resonanzband.
Birch–Dämpfung Eine skalar definierte Abnahmefunktion D(τ), die die Energie der
Primwelle begrenzt. Sie beschreibt, wie starke Resonanzen (große Primabstände)
geometrisch abgefedert werden.
Spiegelwelle Das duale Abbild der Primwelle unter Phasenumkehr φ 7→−φ. Sie reprä-
sentiert die arithmetische Symmetrie der Primverteilung im Resonanzraum.
Primzeit–Transformation Eine Abbildung zwischen arithmetischer und physikalischer
Zeit: τ = ln(1+αt)
ln(1+α) . Sie erzeugt eine natürliche Kompression der Zeitstruktur.
Resonanzkoordinate R(τ) Eine arithmetische Observable, definiert als R(τ) = Ψ(eτ) −
eτ. Sie misst die Abweichung der Primverteilung vom idealen exponentiellen Verlauf.
Ereignisachse C(s) Eine stückweise konstante Funktion C(s) = π(⌊s⌋), die bei jedem
Primereignis sprunghaft ansteigt. Sie bildet die diskrete Komponente des Resonanz-
raums.
Frenet–Serret–System Das geometrische Dreiersystem (T, N, B) der Tangente, Norma-
len und Binormalen, mit den Differentialinvarianten Krümmung κ und Torsion τr.
Es beschreibt die lokale Orientierung und Verdrehung der Primwelle.
Pullback–Metrik Das auf die Primzeit abgebildete metrische Tensorfeld gττ = (D′)2 +
(Dφ′)2 + (Z′)2. Es misst die lokale Energiedichte und geometrische Geschwindigkeit
der Welle.
Primzeit–Energie Die kombinierte Energie der Amplitude, Phase und Höhe: E(τ) =
1
2
h
(D′)2 + (Dφ′)2 + (Z′)2i
. Sie bleibt unter der Hodge–Birch–Begrenzung konstant.
Resonanzraum Der sechs–dimensionale Raum (x, y, z, t, R, C), in dem arithmetische
und geometrische Variablen gemeinsam wirken. Er bildet die vollständige Geometrie
der Primmechanik ab.
25


## Página 26


Deterministische Rückrechnung Das Verfahren, mit dem aus der geometrischen Hö-
he zk und der Primzeit tk die ursprüngliche Primzahl rekonstruierbar ist: pk =
exp(tk −tk−1).
Primzeit–Kosmologie Die Anwendung der Primzeit auf makroskopische Raumzeit-
prozesse. Sie deutet die Expansion des Universums als Resonanzfortpflanzung der
Primmechanik.
Hodge–Birch–Band Der räumlich begrenzte Bereich, in dem die Primwelle stabil
schwingt: HDmax,L = {(x, y, z) | x2 + y2 ≤D2
max, |z| ≤L}.
Resonanzformel Die dynamische Gleichung, die Frequenz, Phase und Dämpfung der
Primwelle verknüpft. Sie bildet das Kernstück der deterministischen Primmechanik.
Raumzeit–Helix Die geometrische Einbettung der Primwelle in den physikalischen
Raum. Sie verbindet Zahlentheorie mit realer Raumzeitkrümmung.
A
Formelsammlung
A.1
A.1 Primzeit und Primzahlen
tk =
k
X
j=1
ln pj
(Primzeit bis zur k-ten Primzahl)
∆tk = tk −tk−1
(Primzeitintervall)
pk = exp(∆tk)
(Rückrechnung der Primzahl)
τ = Tp(t) = ln(1 + αt)
ln(1 + α)
(Primzeit–Transformation)
H0 =
α
(1 + α) ln(1 + α)
(aktueller Hubble-Parameter)
A.2
A.2 Geometrie der Primwelle
γ(τ) = (x(τ), y(τ), z(τ)) = (D(τ) cos φ(τ), D(τ) sin φ(τ), Z(τ))
Z(τ) = L tanh
 τ
L

(Höhenbegrenzung)
gττ = (D′)2 + (Dφ′)2 + (Z′)2
(Pullback–Metrik)
E(τ) = 1
2[(D′)2 + (Dφ′)2 + (Z′)2]
(lokale Energie der Primwelle)
κ(τ) = ∥γ′ × γ′′∥
∥γ′∥3
(Krümmung)
τr(τ) = det(γ′, γ′′, γ′′′)
∥γ′ × γ′′∥2
(Torsion)
26


## Página 27


A.3
A.3 Arithmetische Observablen
Λ(n) =



ln p,
n = pk, k ≥1
0,
sonst
(von–Mangoldt–Funktion)
Ψ(x) =
X
n≤x
Λ(n)
(Chebyshev–Funktion)
π(x) =
X
p≤x
1
(Primzahlzählfunktion)
R(τ) = Ψ(eτ) −eτ
(Resonanzkoordinate)
C(s) = π(⌊s⌋)
(Ereignisachse)
A.4
A.4 Kosmologische Beziehungen
t(z) = (1 + α)1/(1+z) −1
α
(Zeit als Rotverschiebung)
H(z) =
α(1 + z)
ln(1 + α)(1 + α)1/(1+z)
(Hubble–Parameter)
Dc(z) = c
Z z
0
dz′
H(z′)
(komovierende Distanz)
H(z →0) ≈H0(1 + z),
t(z →0) ≈z
H0
,
Dc(z →0) ≈cz
H0
(lokale Näherung)
A.5
A.5 Differentialstruktur der Primwelle
d
ds





T
N
B




=





0
κ
0
−κ
0
τr
0
−τr
0










T
N
B





mit dT
ds = κN,
dN
ds = −κT + τrB,
dB
ds = −τrN.
A.6
A.6 Stabilitäts- und Begrenzungsbedingungen
|Z(τ)| ≤L
(Höhenbegrenzung)
0 < D(τ) ≤Dmax
(Amplitude begrenzt)
0 < κ(τ) ≤κmax,
|τr(τ)| ≤τmax
(Krümmung und Torsion begrenzt)
E′(τ) = 0
(Energieerhaltung unter Hodge–Birch)
27


## Página 28


A.7
A.7 Rückrechnung der Primzahlen (deterministisch)
tk = L artanh
zk
L

,
pk = exp(tk −tk−1).
Diese Gleichungen bilden die Umkehrabbildung zwischen Geometrie und Arithmetik:
Aus der Raumkurve γ(τ) werden die Primzahlen exakt zurückgewonnen.
A.8
A.8 Resonanzraum und 6D–Einbettung
Φ : (τ) 7−→(x(τ), y(τ), z(τ), t(τ), R(τ), C(τ)),
Rang(Jac Φ) = 6
=⇒
vollständige lineare Unabhängigkeit der sechs Dimensionen.
A.9
A.9 Zusammenfassende Beziehungen
Primarithmetik:
pk = exp(∆tk),
Geometrie:
(x, y, z) = (D cos φ, D sin φ, Z),
Resonanz:
R(τ) = Ψ(eτ) −eτ,
Kosmologie:
τ = ln(1 + αt)
ln(1 + α) .
B
Teil 1 Testberechnung der Primwellen-Dimensionen
Basierend auf den Formeln von Jeanette Tabea Leue 19. Oktober 2025
B.1
Rekonstruktion der Raum-Dimensionen
Dieser Test demonstriert die verlustfreie Kodierung der Primzahlen in der Geometrie der
Raumzeit-Helix. Wir führen eine Vorwärts- und eine Rückwärtsrechnung für die ersten
drei Primzahlen durch.
B.2
Vorwärtsrechnung: Von der Primzahl zur Geometrie
Wir berechnen die Höhenkoordinate zk für p1 = 2, p2 = 3, p3 = 5.
• Parameter: Wir wählen die Höhenbegrenzung L = 5, wie in einem Ihrer Beispiele.
• Schritt 1: Primzeit tk = P ln pj
t1 = ln(2) ≈0.693
t2 = ln(2) + ln(3) ≈0.693 + 1.099 = 1.792
t3 = ln(2) + ln(3) + ln(5) ≈1.792 + 1.609 = 3.401
28


## Página 29


• Schritt 2: Höhe zk = L tanh(tk/L)
z1 = 5 · tanh(0.693/5) ≈5 · tanh(0.1386) ≈0.686
z2 = 5 · tanh(1.792/5) ≈5 · tanh(0.3584) ≈1.719
z3 = 5 · tanh(3.401/5) ≈5 · tanh(0.6802) ≈2.975
B.3
Rückwärtsrechnung: Von der Geometrie zur Primzahl
Nun rekonstruieren wir die Primzahlen aus den berechneten Höhen zk.
• Schritt 1: Primzeit aus Höhe tk = L · artanh(zk/L)
t′
1 = 5 · artanh(0.686/5) = 5 · artanh(0.1372) ≈0.693
t′
2 = 5 · artanh(1.719/5) = 5 · artanh(0.3438) ≈1.792
t′
3 = 5 · artanh(2.975/5) = 5 · artanh(0.5950) ≈3.401
Die rekonstruierte Primzeit (t′
k) stimmt mit der ursprünglichen (tk) überein.
• Schritt 2: Primzahl aus Primzeit-Differenz pk = exp(tk −tk−1)
p′
1 = exp(t′
1 −t0) = exp(0.693 −0) ≈2.0
p′
2 = exp(t′
2 −t′
1) = exp(1.792 −0.693) = exp(1.099) ≈3.0
p′
3 = exp(t′
3 −t′
2) = exp(3.401 −1.792) = exp(1.609) ≈5.0
Ergebnis: Die Primzahlen 2, 3 und 5 wurden exakt aus den geometrischen Koordinaten
rekonstruiert. Dies bestätigt die Invertierbarkeit und die verlustfreie Kodierung.
C
Teil 2 Berechnung der internen Dimensionen R
und C
Hier berechnen wir beispielhaft Werte für die internen, arithmetischen Dimensionen.
C.1
Resonanzkoordinate R
Wir berechnen R(τ) am Punkt τ = ln(10), also für die Skala x = eτ = 10.
• Formel: R(τ) = Ψ(eτ) −eτ = Ψ(10) −10.
• Chebyshev-Funktion Ψ(x) = P
n<x Λ(n): Die von-Mangoldt-Funktion Λ(n) ist
ln p für Primzahlpotenzen n = pk. Für x = 10 sind die relevanten Primzahlpotenzen
n < 10: 2, 3, 4=22, 5, 7, 8=23, 9=32.
Ψ(10) = Λ(2) + Λ(3) + Λ(4) + Λ(5) + Λ(7) + Λ(8) + Λ(9)
= ln 2 + ln 3 + ln 2 + ln 5 + ln 7 + ln 2 + ln 3
= 3 ln 2 + 2 ln 3 + ln 5 + ln 7
≈3(0.693) + 2(1.099) + 1.609 + 1.946
≈2.079 + 2.198 + 1.609 + 1.946 = 7.832
29


## Página 30


• Ergebnis für R:
R(ln 10) = Ψ(10) −10 ≈7.832 −10 = −2.168
Der negative Wert zeigt eine Ünterkonzentration"von Primenergie an dieser Stelle
im Vergleich zu einer glatten exponentiellen Verteilung.
C.2
Ereignisachse C
Wir berechnen C(s) für den Wert s = 10.5.
• Formel: C(s) = π(⌊s⌋), wobei π(x) die Primzahlzählfunktion ist.
• Berechnung:
C(10.5) = π(⌊10.5⌋) = π(10)
Die Primzahlen bis 10 sind 2, 3, 5, 7. Also ist π(10) = 4.
• Ergebnis für C:
C(10.5) = 4
Dies demonstriert den treppenartigen Charakter der C-Dimension, die nur bei
Primzahlen ansteigt.
D
Teil 3 Berechnung eines kosmologischen Parame-
ters
Wir testen die Formel, die den heutigen Hubble-Parameter H0 mit dem Resonanzskalen-
faktor α verknüpft.
• Formel: H0 =
α
(1+α) ln(1+α).
• Beispielrechnung: Wir wählen einen hypothetischen Wert α = 1.
H0 =
1
(1 + 1) ln(1 + 1) =
1
2 ln 2 ≈
1
2 · 0.693 ≈0.721
• Interpretation: In einer echten Anwendung würde man den gemessenen Wert
von H0 (in den passenden Einheiten) verwenden, um diese Gleichung nach dem
fundamentalen Parameter α aufzulösen und damit das kosmologische Modell zu
kalibrieren.
30
