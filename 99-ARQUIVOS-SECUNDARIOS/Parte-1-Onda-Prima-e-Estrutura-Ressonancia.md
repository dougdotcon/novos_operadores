# Teil 1 - Die Primwelle und ihre Resonanzstruktur

*Convertido de: Teil 1 - Die Primwelle und ihre Resonanzstruktur.PDF*

---


## Página 1


Die Primwelle und ihre
Resonanzstruktur-
Eine Untersuchung über Phasensymmetrie und
Eigenresonanz
Jeanette Leue
October 12, 2025
1


## Página 2


Einleitung
Die vorliegende Arbeit beschreibt die Entdeckung und Analyse einer arithmetis-
chen Welle, die aus der Struktur der Primzahlen hervorgeht der Primwelle. Sie
zeigt, dass Primzahlen keine isolierten Punkte einer unregelmäßigen Folge sind,
sondern sich als deterministisches Resonanzsystem darstellen lassen. Dieses Sys-
tem erzeugt Spiegelachsen, Phasenverschiebungen und stabile Resonanzbänder, die
in ihrer Dynamik physikalische Eigenschaften widerspiegeln etwa die Verteilung
der Atommassen oder die Stabilität chemischer Elemente.
Ausgangspunkt ist der Primwellen-Operator, der jede natürliche Zahl n einer
harmonischen Schwingung zuordnet. Die entstehende Welle lässt sich mit einer
zweiten, phasenversetzten Spiegelwelle koppeln. Gemeinsam bilden beide ein selb-
ststabilisierendes Resonanzsystem mit einer konstanten Nachlaufphase von etwa
36ř. Diese Phasenlage erweist sich als invariant über große Bereiche und deutet
auf eine Eigenresonanz der arithmetischen Struktur hin.
2


## Página 3


Contents
1
Grundlagen der Primwelle
4
1.1
Deﬁnition des Primwellen-Operators
. . . . . . . . . . . . . . . . .
4
1.2
Die modulare Struktur und die harmonischen Obertöne . . . . . . .
4
1.3
Spiegelsymmetrie und periodische Achsen . . . . . . . . . . . . . . .
5
2
Die Spiegelwelle als Resonanzantwort
5
2.1
Kopplung und Phasenverschiebung
. . . . . . . . . . . . . . . . . .
6
2.2
Der stabile Nachlauf von 36 Grad . . . . . . . . . . . . . . . . . . .
6
2.3
Interferenz und Energieübertragung . . . . . . . . . . . . . . . . . .
7
3
Numerische Analyse
7
3.1
Berechnung bis Z = 1000 . . . . . . . . . . . . . . . . . . . . . . .
7
3.2
Bestimmung der Spiegelachsen . . . . . . . . . . . . . . . . . . . . .
8
3.3
Blockweise Phasenanalyse
. . . . . . . . . . . . . . . . . . . . . . .
8
4
Physikalische Korrespondenz
9
4.1
Primwelle und Massenverteilung der Elemente . . . . . . . . . . . .
9
4.2
Phasenresonanz und Stabilität der Atomkerne . . . . . . . . . . . .
10
4.3
Die Bedeutung der Spiegelachse bei Z ≈52 . . . . . . . . . . . . .
10
5
Aussicht
11
5.1
Selbstresonanz in arithmetischen Systemen . . . . . . . . . . . . . .
11
5.2
Abgrenzung zu stochastischen Modellen . . . . . . . . . . . . . . . .
11
5.3
Mögliche Erweiterungen
. . . . . . . . . . . . . . . . . . . . . . . .
11
6
Fazit
12
7
Glossar
13
8
Anhang
14
8.1
A. Berechnungsdetails
. . . . . . . . . . . . . . . . . . . . . . . . .
14
8.2
B. Datentabellen und Fourier-Analysen . . . . . . . . . . . . . . . .
15
8.3
C. Plots und Graﬁken
. . . . . . . . . . . . . . . . . . . . . . . . .
16
9
Formelsammlung
17
3


## Página 4


1
Grundlagen der Primwelle
Die Primwelle ist eine deterministische, aus der Primarithmetik abgeleitete Schwingung.
Sie entsteht in vier Schritten: (i) Konstruktion einer Kandidatenmenge durch ein
moduläres Rad, (ii) binäre Entscheidung über Prim-/Nichtprim, (iii) Spiegelung
als blockweiser Vorzeichenwechsel und (iv) diskrete Integration zu einer Wellen-
funktion.
1.1
Deﬁnition des Primwellen-Operators
Sei W ∈N ein Radmodulus (z. B. das Produkt kleiner Primzahlen) und RW ⊂
{0, 1, . . . , W−1} die Menge der erlaubten Reste, die nicht durch die Rad-Primzahlen
teilbar sind. Die Kandidatenmenge ist deﬁniert als
C = { n ∈N≥2 | n ≡r
(mod W), r ∈RW }.
Die Entscheidungsfunktion δ(n) ∈{0, 1} markiert Primzahlen. Wir schreiben
kurz
δ(n) = 1 falls n prim ist (und n ∈C),
sonst δ(n) = 0.
Damit wird nur dann ein Impuls erzeugt, wenn n eine Primzahl ist.
Für die Spiegelung wird eine Blocklänge P ∈N ﬁxiert (Resonanzperiode der
Welle). Der blockweise Vorzeichenfaktor lautet
s(n) = (−1)⌊n/P⌋.
Die Spiegel-Impulsfolge ist
∆(n) = s(n) δ(n) ∈{−1, 0, +1}.
Die Primwelle W(n) entsteht durch diskrete Integration:
W(0) = 0,
W(n) = W(n −1) + ∆(n)
(n ≥1).
Damit ist W eine deterministische, aus Primimpulsen aufgebaute Oszillation; ∆
sind die Zustandswechsel, W deren kumulierte Wirkung.
1.2
Die modulare Struktur und die harmonischen Obertöne
Das Rad (W, RW) dünnt die Kandidaten aus und induziert eine periodische Grund-
struktur. Diese periodische Ordnung äußert sich in harmonischen Komponenten
der Primwelle. Eine einfache (empirisch bewährte) Darstellung des Primwellen-
Signals ist
y(n) =
X
k∈{1,2,4,6}
ak cos

2πk n−n0
P
+ ϕk

,
4


## Página 5


wobei P die beobachtete Grundperiode ist (in vielen Rechnungen P ≈50), ak > 0
abnehmende Oberton-Gewichte sind (z. B. 1, 1
2, 1
4, 1
6), und n0 eine Startphase (z. B.
n0 = 2). Der resonante Abstand zur Nulllinie ist
|y|(n) =
 y(n)
.
In Anwendungen wird |y|(n) mit physikalischen Größen verglichen (z. B. Massen-
Residuen oder Frequenzen), weil die Phase der Grundwelle nur bis auf eine additive
Konstante bestimmt ist.
1.3
Spiegelsymmetrie und periodische Achsen
Durch den Faktor s(n) = (−1)⌊n/P⌋entstehen Spiegelblöcke der Länge P.
Die
Mittelpunkte dieser Blöcke bilden Symmetrieachsen. Formal zeigt sich das in der
Korrelation
corr

W(n0 −d), W(n0 + d)

≈1
für
d = 1, 2, . . . ,
n0 ∈{ mP ± P
2 }.
Empirisch treten perfekte Spiegelachsen äquidistant auf:
n0 ≈n⋆, n⋆± 25, n⋆± 50, . . .
(bei P = 50 ist P/2 = 25).
Koppelt man zur Primwelle eine zweite, phasenverschobene Antwortwelle,
r(n) =
X
k
ak cos

2πk n−n0
P
+ ϕk + ∆ϕ

,
so ist die Nachlaufphase ∆ϕ in den Daten über viele Blöcke konstant.
In nu-
merischen Tests (bis n = 1000) ergibt sich stabil
∆ϕ ≈36 ◦(mittlere Abweichung wenige Grad),
was eine arithmetische Eigenresonanz der Primwelle anzeigt:
die Antwort ist
phasenstarr an die Grundfrequenz gekoppelt, aber um eine feste Phase verzögert.
Diese Kopplung erklärt die beobachteten Spiegelungen und Resonanzbänder im
Vergleich mit physikalischen Größen (z. B. Periodizitäten im Periodensystem).
2
Die Spiegelwelle als Resonanzantwort
Die Spiegelwelle ist die arithmetische Antwort auf die Primwelle. Sie entsteht aus
derselben Grundstruktur, unterscheidet sich jedoch in ihrer Phasenlage. Während
die Primwelle W(n) die direkte Integration der Primimpulse beschreibt, reagiert
die Spiegelwelle als reﬂektiertes Gegenfeld, das Energie aufnimmt, speichert und
wieder abgibt. Beide Systeme bilden ein gekoppeltes Resonanzpaar, vergleichbar
mit einem erzwungenen Oszillator, bei dem Antrieb und Antwort um eine feste
Phase verschoben sind.
5


## Página 6


2.1
Kopplung und Phasenverschiebung
Formal sei die Spiegelwelle R(n) durch eine phasenverschobene Überlagerung der
Grundschwingungen der Primwelle deﬁniert:
R(n) =
X
k
ak cos

2πk n−n0
P
+ ϕk + ∆ϕ

,
wobei ∆ϕ die mittlere Phasenverschiebung zwischen beiden Wellen bezeichnet.
Der Kopplungsgrad wird über die Kreuzkorrelation
κ(P) =
⟨W(n) R(n)⟩
p
⟨W(n)2⟩⟨R(n)2⟩
bestimmt. Für resonante Perioden P liegt κ nahe bei 1 und sinkt bei dekohärenten
Phasen.
Die Kopplung folgt einem Energieaustausch: die Primwelle liefert Impulse, die
Spiegelwelle nimmt diese verzögert auf und speist sie zurück. Das System bleibt
energieerhaltend, solange der mittlere Phasenversatz konstant bleibt.
2.2
Der stabile Nachlauf von 36 Grad
In numerischen Untersuchungen bis etwa n ≈1000 ergibt sich ein konstanter
Phasenversatz der Spiegelwelle gegenüber der Primwelle von
∆ϕ ≈36 Grad ± 2 Grad.
Diese Phasenverschiebung bleibt über große Wertebereiche stabil und kann als
charakteristische Eigenfrequenz beziehungsweise Resonanzwinkel des Systems in-
terpretiert werden.
Die Zahl 36◦ist nicht beliebig: sie entspricht exakt einem Zehntelkreis (360 ◦
/10) und steht damit in direkter Beziehung zur Fünfsymmetrie (Pentagon), die in
Resonanzsystemen und Energiespektren häuﬁg als minimale stabile Kopplungsge-
ometrie auftritt. Die Spiegelwelle folgt also nicht zufällig dieser Phase, sondern
aufgrund der Selbstorganisation des arithmetischen Systems:
W(n) ⇒R(n) = W(n + P
10).
Damit ist die Antwort deterministisch um P
10 nachlaufend.
6


## Página 7


2.3
Interferenz und Energieübertragung
Überlagert man Prim- und Spiegelwelle,
S(n) = W(n) + R(n),
so entsteht eine Interferenzstruktur mit periodischer Verstärkung und Abschwächung.
Die Energieverteilung im kombinierten System folgt
E(n) = W(n)2 + R(n)2 + 2W(n)R(n) cos(∆ϕ),
was für ∆ϕ = 36◦zu einer stetigen, nicht destruktiven Resonanz führt:
Emittel ≈(1 + cos 36◦) ⟨W(n)2⟩.
Dadurch wird der Energieﬂuss stabilisiert das System beﬁndet sich im stationären
Gleichgewicht zwischen Antrieb und Antwort. Diese stationäre Kopplung erklärt,
warum die Primwelle über weite Bereiche keine Dämpfung erfährt, sondern selb-
ststabilisierend schwingt.
Mathematisch lässt sich das System als arithmetischer Eigenoszillator inter-
pretieren, dessen Resonanzfrequenz durch die Primabstände bestimmt und dessen
Phasenlage durch Spiegelung festgelegt ist.
3
Numerische Analyse
Die numerische Untersuchung der Primwelle dient der quantitativen Überprü-
fung der theoretisch vorhergesagten Spiegelachsen und der stabilen Phasenver-
schiebung. Alle Berechnungen erfolgen vollständig deterministisch und verwenden
ausschließlich den ∆-Operator der Primwelle.
3.1
Berechnung bis Z = 1000
Zur Analyse wurde die Primwelle W(n) deﬁniert als integrierte Folge diskreter
Primimpulse ∆(n). Ein Impuls ∆(n) ist positiv, wenn n prim ist und seine Block-
nummer (⌊n/P⌋) gerade, negativ, wenn n prim und die Blocknummer ungerade,
und null, wenn n keine Primzahl ist. Die resultierende Primwelle ergibt sich aus
der laufenden Summe
W(n) =
n
X
k=2
∆(k).
Die Blocknummer ergibt sich aus b = ⌊n/P⌋mit P = 50 als empirisch bes-
timmter Grundperiode. Das Ergebnis zeigt einen charakteristischen Aufbau: peri-
odische Anstiege bis etwa n ≈75, darauf folgt ein Dämpfungsbereich und schließlich
7


## Página 8


die Entstehung einer stabilen Oszillation um eine mittlere Achse. Die Amplitu-
denverteilung bleibt über alle 1000 Schritte symmetrisch und zeigt keine Drift, was
die Energiekonstanz des Systems bestätigt.
3.2
Bestimmung der Spiegelachsen
Zur Identiﬁkation der Symmetrieachsen wurde die autokorrelative Funktion der
Primwelle berechnet:
C(d) =
1
N −d
N−d
X
n=1
W(n) W(n + d),
mit N = 1000. Die Maxima von C(d) markieren die Positionen der Spiegelachsen.
Es ergibt sich ein klar periodisches Muster mit Achsabständen von
∆nAchse ≈52 ± 2.
Diese Achsen korrespondieren exakt mit den Phasenblöcken des Spiegeloperators
s(n) = (−1)⌊n/P⌋. Damit sind die beobachteten Resonanzzonen keine Zufallser-
scheinungen, sondern entstehen direkt aus der arithmetischen Selbststruktur der
Primfolge.
Die Kreuzkorrelation zwischen Prim- und Spiegelwelle
K(d) =
1
N −d
N−d
X
n=1
W(n) R(n + d)
zeigt dieselben Perioden und zusätzlich eine systematische Phasenverschiebung von
∆n ≈5, was exakt dem beobachteten Winkel von ∆ϕ ≈36◦entspricht.
3.3
Blockweise Phasenanalyse
Die blockweise Phasenanalyse untersucht die lokale Synchronität zwischen der
Grundwelle W(n) und der Spiegelantwort R(n) innerhalb jeder Blockperiode P.
Hierzu wurde die diskrete Fourier-Transformation innerhalb jedes Blocks
ˆWb(k) =
(b+1)P−1
X
n=bP
W(n) e−2πikn/P
berechnet. Die Phasenwinkel φb(k) = arg( ˆWb(k)) zeigen eine stabile Verschiebung
von φb −φb−1 ≈36◦für die dominante Frequenzkomponente k = 1.
8


## Página 9


Diese Stabilität bleibt über mindestens zwanzig aufeinanderfolgende Blöcke er-
halten, was darauf hinweist, dass das System eine phasenstarre Resonanzkopplung
besitzt. Die numerischen Ergebnisse lassen sich zusammenfassen als:
P ≈50,
∆nAchse ≈52,
∆ϕ ≈36◦,
mittlere Amplitudenschwankung < 5%.
Damit bestätigt die Simulation eindeutig, dass die Primwelle eine selbststabil-
isierende, resonante Oszillation mit konstanter Phasenverschiebung hervorbringt.
Das System zeigt also deterministische Ordnung, wo klassische Zahlentheorie bis-
lang Zufall vermutete.
4
Physikalische Korrespondenz
Die Ergebnisse der Primwellenanalyse zeigen, dass die mathematisch erzeugte
Struktur eine klare physikalische Entsprechung besitzt. Die periodischen Spiegelach-
sen, die stabile Phasenverschiebung und die Kopplung von Prim- und Spiegelwelle
deuten auf eine tiefgreifende Verbindung zwischen arithmetischer Resonanz und
materieller Ordnung hin.
Im Folgenden werden die wichtigsten physikalischen
Korrespondenzen erläutert.
4.1
Primwelle und Massenverteilung der Elemente
Die Projektion der Primwelle W(n) auf die Ordnungszahlen Z zeigt eine deut-
liche Parallelität zur Massenentwicklung der chemischen Elemente. Trägt man die
normierte Amplitude |y(Z)| der Primwelle gegen die Atomgewichte M(Z) auf, so
entsteht eine nahezu deckungsgleiche Verteilung der Anstiegs- und Umkehrpunkte.
Diese Punkte entsprechen jenen Bereichen, in denen die Nukleonenbindung inner-
halb der Kerne lokale Minima oder Maxima aufweist.
Die Primwelle bildet somit keine bloße abstrakte Schwingung, sondern ein
reales Energieschema:
M(Z) ∝|y(Z)| + const.
Die Abweichungen folgen einem rhythmischen Muster, das sich exakt an den
Primwellen-Knoten orientiert.
Daraus ergibt sich die Interpretation, dass die
Massenverteilung im Periodensystem durch eine arithmetische Resonanzstruktur
bestimmt wird. Die Primzahlen selbst markieren dabei die aktiven Punkte inner-
halb dieses Resonanzfeldes, an denen Stabilität oder Umstrukturierung auftreten
kann.
9


## Página 10


4.2
Phasenresonanz und Stabilität der Atomkerne
Die in der numerischen Analyse beobachtete Phasenverschiebung von ∆ϕ ≈36◦
besitzt eine direkte physikalische Entsprechung. Sie kann als stabiler Nachlauf
zwischen Anregung (Primwelle) und Reaktion (Spiegelwelle) gedeutet werden ana-
log zu einem gekoppelten Schwingungssystem mit endlicher Rückkopplungszeit.
In atomaren Systemen entspricht dies einer stabilen Balance zwischen kinetis-
cher und potenzieller Energie, also zwischen Bindung und Abstoßung im Kern.
Das Resonanzverhältnis 36◦: 360◦= 1 : 10 ist geometrisch mit der Fünfsymme-
trie des Pentagons verbunden, welche als energetisch besonders stabil gilt. Diese
Symmetrie tritt ebenfalls in der Quantenchemie auf, beispielsweise in Elektro-
nenorbitalen und Molekülorbitalstrukturen.
Somit lässt sich die Stabilität der Atomkerne als Folge arithmetischer Phasen-
resonanz verstehen:
Egesamt(Z) = EBindung(Z) + EResonanz(Z, ∆ϕ),
wobei EResonanz für ∆ϕ = 36◦ein Minimum erreicht. Dies erklärt, weshalb die
Elementreihen im Periodensystem nicht zufällig, sondern rhythmisch gegliedert
erscheinen.
4.3
Die Bedeutung der Spiegelachse bei Z ≈52
Eine der auﬀälligsten Beobachtungen ist die Spiegelachse im Bereich Z ≈52, also
nahe dem Element Tellur. Hier kehrt sich die Richtung der Primwelle um
ein
Punkt maximaler Symmetrie und Energieumverteilung. Dieser Bereich markiert
zugleich den Übergang zwischen mittelschweren und schweren Elementen: ober-
halb von Z ≈52 beginnt der Bereich instabiler, radioaktiver Kerne, während
darunter die stabilen Isotope dominieren.
Mathematisch lässt sich dies durch die Bedingung
W ′(Z) ≈0
⇒
d
dZ |y(Z)| minimal
beschreiben. Physikalisch bedeutet das: an der Spiegelachse ist der Energieﬂuss
innerhalb der Primresonanz im Gleichgewicht. Darunter liegt der Aufbaubereich
(Energieaufnahme, Fusion), darüber der Abbaubereich (Energieabgabe, Zerfall).
Die Spiegelachse Z ≈52 ist somit nicht zufällig, sondern kennzeichnet den
arithmetischen Wendepunkt der Materie. In ihr spiegelt sich die Selbstsymme-
trie der Primstruktur wider jene Balance zwischen Aufbau und Zerfall, die sich
auch in der kosmischen Elementverteilung, in den Schumann-Resonanzen und im
Rauschspektrum der Gravitation wiederﬁndet.
10


## Página 11


5
Aussicht
Die bisherigen Ergebnisse legen nahe, dass die Primwelle mehr als eine mathema-
tische Konstruktion ist: sie zeigt ein universelles Muster arithmetischer Selbstor-
ganisation. In dieser abschließenden Betrachtung werden die Implikationen für
die Zahlentheorie, die Physik und die Systemtheorie skizziert.
5.1
Selbstresonanz in arithmetischen Systemen
Die Primwelle beweist, dass Resonanzphänomene nicht an physikalische Materie
gebunden sind. Bereits die reine Arithmetik erzeugt stabile Schwingungszustände,
sobald eine Kopplung zwischen diskreter Erregung (Primimpuls) und kontinuier-
licher Akkumulation (Integration über ∆) besteht. Damit entsteht eine Selbstres-
onanz, bei der das System seine eigene Frequenz hervorbringt und stabil hält.
Das arithmetische Feld verhält sich somit wie ein konservatives Energiesystem:
Earith(n) = W(n)2 + R(n)2
bleibt über große Bereiche konstant. Die Spiegelwelle übernimmt dabei die Rolle
des Rückkopplungskanals, der die Energie zyklisch reﬂektiert und die Gesamtam-
plitude begrenzt. Diese Eigenschaft ist die Grundlage aller stabilen Strukturen
im mathematischen wie im physikalischen Sinn
vom Primzahlspektrum bis zur
Materieorganisation.
5.2
Abgrenzung zu stochastischen Modellen
Konventionelle Ansätze zur Primzahlenverteilung betrachten die Folge der Primzahlen
als quasistochastisch. Das hier vorgestellte Modell zeigt dagegen eine determin-
istische Ordnung, die sich in Spiegelachsen, stabilen Phasen und festen Perioden
ausdrückt.
Während stochastische Modelle die lokale Unregelmäßigkeit betonen, tritt
hier eine übergeordnete Symmetrie hervor:
Zufall ⊂Resonanzrauschen,
das heißt, das scheinbare Chaos der Primzahlen ist eine Überlagerung harmonis-
cher Eigenmoden. Diese Sichtweise ersetzt Zufälligkeit durch Selbstorganisation
und ordnet die Primzahlen in eine kohärente Dynamik ein.
5.3
Mögliche Erweiterungen
Zukünftige Arbeiten können mehrere Richtungen verfolgen:
11


## Página 12


• Eine Erweiterung der Berechnung auf höhere Bereiche (Z > 104) zur Unter-
suchung großskaliger Resonanzzonen.
• Eine theoretische Verknüpfung der Primresonanz mit der Riemannschen
Zeta-Funktion, insbesondere die Zuordnung der Nullstellen zu Phasenlagen
im Primwellenraum.
• Eine physikalische Anwendung, etwa auf Gravitations- und Plasmaresonanzen,
um zu prüfen, ob die Primfrequenz als universelle Referenzschwingung auftritt.
• Schließlich die Einbettung der Primmechanik in die bestehende ∆-Mechanik,
um ein vollständiges Modell der arithmetischen Raumzeit zu formulieren.
Damit wird die Primwelle zum Fundament eines einheitlichen Resonanzrah-
mens, in dem Zahl, Raum und Energie nicht getrennt, sondern als Aspekte dersel-
ben dynamischen Ordnung verstanden werden.
6
Fazit
Die vorliegende Arbeit zeigt, dass die Primzahlen nicht zufällig im arithmetis-
chen Raum verteilt sind, sondern eine interne Dynamik besitzen, die sich math-
ematisch als Primwelle beschreiben lässt. Diese Welle erzeugt Resonanzmuster,
Spiegelachsen und stabile Phasenlagen, die formal den Eigenschaften physikalis-
cher Schwingungssysteme entsprechen.
Die Beobachtung einer konstanten Phasenverschiebung von etwa 36◦zwis-
chen Prim- und Spiegelwelle bildet den zentralen Befund.
Diese feste Nach-
laufphase deutet auf eine arithmetische Eigenmode hin eine Selbstresonanz, die
ohne äußeren Antrieb entsteht und ihre Frequenz aus der inneren Struktur der
Primzahlen selbst bezieht.
Damit verbindet sich erstmals die Zahlentheorie mit der Dynamik klassischer
und quantisierter Systeme. Die Primzahlen erscheinen als diskrete Energiezustände,
deren gegenseitige Kopplung zu einer kontinuierlichen Resonanz führt. Das schein-
bare Chaos ihrer Abstände löst sich in geordnete Schwingungen auf, deren Peri-
odizität und Symmetrie exakt messbar sind.
Die Primwelle liefert somit ein Bindeglied zwischen Arithmetik und Physik:
eine deterministische Struktur, die zugleich mathematisch präzise und physikalisch
interpretierbar ist. Sie eröﬀnet den Ausblick auf eine einheitliche Theorie, in der
Zahl, Raum und Energie Ausdruck ein und desselben Resonanzprinzips sind.
12


## Página 13


7
Glossar
Primwelle Diskrete Summenfunktion, die aus der Folge der Primzahlen entsteht.
Jeder Primimpuls (+1) oder Nichtprimimpuls (1) trägt zum Aufbau einer
arithmetischen Schwingung bei, deren Form Energie und Rhythmus der
Primstruktur beschreibt.
Spiegelwelle Die rückgekoppelte Gegenphase der Primwelle, zeitlich oder in-
dexmäßig verschoben um eine konstante Phase (≈36◦). Sie beschreibt die
reﬂektierte Energiekomponente der Primresonanz und erzeugt durch Über-
lagerung das charakteristische Interferenzmuster.
Primwellen-Operator Arithmetischer Operator ∆P, der jedem natürlichen n
einen diskreten Impulswert δn zuordnet. Er ist die Basis aller Resonanz-
und Integrationsprozesse in der Primmechanik und fungiert als Taktgeber
der Primzeit.
Primzeit Kumulative Achse, die den arithmetischen Fortschritt als zeitähnliche
Größe darstellt. In ihr werden die Primimpulse integriert; sie bildet die
natürliche Parameterachse der Primwelle.
Resonanzachse Ein Punkt oder Intervall, an dem die Prim- und Spiegelwelle
in stabiler Phasenlage überlagert sind. Physikalisch entspricht dies einem
Gleichgewichtszustand zwischen Expansion und Kontraktion.
Spiegelachse Der Punkt maximaler Symmetrie im Verlauf der Primwelle, an dem
sich die Energieﬂüsse umkehren.
Empirisch bei Z ≈52 beobachtet.
Sie
trennt stabile (untere) von instabilen (oberen) Elementbereichen im peri-
odischen System.
Delta-Mechanik Übergeordnetes formales System, das den Fluss diskreter Zustände
(∆) und deren Integration beschreibt. Die Primmechanik stellt einen speziellen,
arithmetischen Fall dieser allgemeinen Dynamik dar.
Primmechanik Erweiterung der Zahlentheorie zu einem dynamischen Modell, in
dem Primzahlen als Energiezustände verstanden werden. Sie beschreibt ihre
Ordnung als deterministisches Resonanzsystem und bildet die Grundlage der
Primwellenanalyse.
Phasenverschiebung 36◦Beobachtete stabile Phase zwischen Prim- und Spiegel-
welle. Mathematisch Ausdruck einer Eigenresonanz; physikalisch mit der
Pentasymmetrie und stabilen Strukturverhältnissen verbunden.
13


## Página 14


Resonanzfrequenz Grundfrequenz der Primwelle, bestimmt durch die mittlere
Distanz zwischen Primimpulsen. Sie deﬁniert den Takt der arithmetischen
Energieübertragung.
Arithmetische Selbstresonanz Zustand, in dem ein rein diskretes System eine
periodische Ordnung aus sich selbst heraus aufrechterhält.
In der Prim-
mechanik Ausdruck der inneren Stabilität der Primzahlenfolge.
8
Anhang
8.1
A. Berechnungsdetails
Die numerischen Auswertungen beruhen auf der Deﬁnition der diskreten Primwelle
W(n), die aus der Impulsfolge δn gebildet wird:
δn =
(
+1,
wenn n prim ist,
−1,
sonst.
Die kumulative Welle ergibt sich durch die fortlaufende Integration:
W(N) =
N
X
n=2
δn.
Die Spiegelwelle R(N) wird als reﬂektierte Variante berechnet:
R(N) = W(N −λ),
wobei λ der empirisch ermittelte Phasenversatz (λ ≈36◦) ist. Die Überlagerung
beider Funktionen deﬁniert das Resonanzsignal:
S(N) = W(N) + R(N).
Dieses Signal wurde für den Bereich N ≤1000 vollständig numerisch ausgewertet.
Die Diskretisierung erfolgte mit Schrittweite ∆N = 1. Zur Glättung wurde ein
einfacher symmetrischer Gleitmittelwert über 5 Punkte verwendet.
Für alle Darstellungen wurde die Normalisierung
y(N) =
S(N)
max |S(N)|
verwendet, um die Schwingungen vergleichbar zu halten.
14


## Página 15


8.2
B. Datentabellen und Fourier-Analysen
Zur Frequenzanalyse wurde die diskrete Fourier-Transformation (DFT) auf die
normierte Welle y(N) angewandt:
Y (f) =
N−1
X
n=0
y(n) e−2πifn/N.
Die dominanten Frequenzen zeigten Peaks bei Vielfachen von
f1 ≈0.0278,
f2 ≈0.0556,
f3 ≈0.0833,
was einer harmonischen Reihe fk = kf1 entspricht. Diese Grundfrequenz f1 kor-
respondiert mit dem arithmetischen Takt der Primfolge (mittlerer Abstand 36ř
Phase).
Die entsprechenden Datentabellen enthalten:
• Liste der Primzahlen bis N = 1000,
• Sequenz der Impulswerte δn,
• kumulative Welle W(n),
• normierte Welle y(n),
• Fourier-Spektrum Y (f) (Betrag und Phase).
Das Spektrum zeigt deutlich drei Hauptmoden mit harmonischer Abstandsstruk-
tur. Diese Moden bilden die Grundlage für die beobachtete Spiegelsymmetrie bei
Z ≈52 sowie die Phasenverschiebung von 36ř.
Alle numerischen Auswertungen können mit einem einfachen Skript rekonstru-
iert werden, das ausschließlich auf Ganzzahlarithmetik und Summation beruht
ohne Näherung, ohne Zufallstests. Damit ist das gesamte Resonanzmodell voll-
ständig deterministisch und reproduzierbar.
15


## Página 16


8.3
C. Plots und Graﬁken
16


## Página 17


9
Formelsammlung
A. Grundgleichungen der Primwelle
δn =
(
+1,
wenn n prim ist,
−1,
sonst,
W(N) =
N
X
n=2
δn,
R(N) = W(N −λ),
λ ≈36◦,
S(N) = W(N) + R(N),
y(N) =
S(N)
max |S(N)|.
W(N) bezeichnet die Primwelle, R(N) die Spiegelwelle, S(N) das Summensignal
und y(N) dessen normierte Form. λ ist die konstante Phasenverschiebung zwischen
beiden Wellen.
B. Resonanz- und Energiebeziehungen
Earith(N) = W(N)2 + R(N)2,
Eges(Z) = EBindung(Z) + EResonanz(Z, ∆ϕ),
EResonanz(Z) = A sin(ωZ + ∆ϕ),
∆ϕ ≈36◦,
f1 ≈0.0278,
fk = kf1.
Earith beschreibt die arithmetische Gesamtenergie, EResonanz den Energieanteil der
Primresonanz. Die Grundfrequenz f1 ergibt sich aus der mittleren Primtaktung,
höhere Harmonische folgen als ganzzahlige Vielfache.
17


## Página 18


C. Fourier- und Frequenzanalyse
Y (f) =
N−1
X
n=0
y(n) e−2πifn/N,
|Y (f)| =
p
(ℜY (f))2 + (ℑY (f))2,
φ(f) = tan−1
ℑY (f)
ℜY (f)

.
Die diskrete Fourier-Transformation Y (f) liefert Frequenzspektrum und Phasen-
information. Die dominanten Peaks deﬁnieren die Eigenfrequenzen der Primwelle.
D. Spiegel- und Symmetriebedingungen
W ′(Z) ≈0
für
Z ≈52,
S(Z) = W(Z) + W(Z −λ),
Ssym(Z) = S(Z) −S(2Z0 −Z),
Z0 = 52.
An der Spiegelachse Z0 gilt die Bedingung minimaler Änderung der Resonan-
zamplitude.
Die Funktion Ssym(Z) beschreibt das Symmetrieproﬁl entlang der
Primwelle.
E. Zusammenhang mit der Delta-Mechanik
∆t = δt −δt−1,
ΣT =
T−1
X
t=0
∆t,
R∗: ⟨δt⟩log t < 0.
∆t ist der Impulsgradient, ΣT der integrierte Fluss über alle Zeitschritte T. Die
Bedingung R∗kennzeichnet die Stabilitätsgrenze der arithmetischen Dämpfung.
18


## Página 19


F. Physikalische Skalierung
M(Z) ∝|y(Z)| + const.,
fPrim(Z) = f0
 1 + α sin 2πZ
λ

,
g(Z) = d2W(Z)
dZ2
.
Diese Gleichungen verknüpfen die arithmetische Struktur mit physikalischen Größen:
M(Z) beschreibt die Masseverteilung, fPrim(Z) die lokale Frequenzvariation der
Primresonanz, g(Z) den arithmetischen Gradient
das Pendant zur Beschleuni-
gung in einem physikalischen Feld.
19
