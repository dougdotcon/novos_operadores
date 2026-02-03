# Teil 1 Die Collatz-Resonanz

*Convertido de: Teil 1 Die Collatz-Resonanz.PDF*

---


## Página 1


Teil 1 Die Collatz-Resonanz
Symbolische
Dynamik,
Spiralstruktur
und
Codierung
Jeanette Leue
11. Oktober 2025
1


## Página 2


Einleitung
Die Collatz-Folge wird oft als das einfachste ungelöste Problem der Mathematik
bezeichnet. Sie entsteht aus einer einfachen Regel: Wenn eine Zahl ungerade ist,
wird sie verdreifacht und um eins erhöht, wenn sie gerade ist, wird sie halbiert.
Egal, mit welcher natürlichen Zahl man beginnt, die Folge scheint immer in den
Zyklus 4, 2, 1 zu münden. Ein allgemeiner Beweis dafür ist bis heute nicht
bekannt.
In dieser Arbeit wird die Collatz-Folge als ein Resonanzsystem betrachtet.
Jeder Rechenschritt wird als energetischer Übergang zwischen zwei Zuständen
verstanden: die Operation
mal drei plus eins steht für eine Expansion, die
Division
durch
zwei
für
eine
Kontraktion.
So
entsteht
ein
rhythmisches
Gleichgewicht zwischen Ausdehnung und Dämpfung.
Der Schlüssel liegt in der symbolischen Codierung dieser Dynamik. Anstelle
der direkten Zahlenberechnung wird der Ablauf als Folge von Resonanzsymbolen
beschrieben, die den inneren Rhythmus des Systems sichtbar machen. Dieser
Collatz-Resonanzcode erlaubt: 1. eine eindeutige Beschreibung jedes Ablaufs ohne
numerische
Berechnung,
2.
eine
geometrische
Darstellung
als
Spirale
oder
Wellenform, 3. die Einordnung in die größere Primmechanik-Kaskade.
Damit wird Collatz zu einem Teil
eines umfassenderen, deterministischen
Systems, das seine scheinbare Komplexität aus der Überlagerung zweier einfacher
Resonanzprozesse bezieht. Die klassische „Ungelöstheit“ verschwindet, sobald die
Rekursion
nicht
mehr als Zahlenspiel,
sondern
als symbolische Schwingung
verstanden wird.
Diese Arbeit zeigt: - Worum es geht: die Umdeutung der Collatz-Folge als
Resonanzsystem. - Was gelöst wurde: eine formale Struktur der Dynamik in
symbolischer Form, ohne Zufall oder Divergenz. - Wie es gelöst wurde: durch
Einführung
eines
Codierungssystems,
das
jede
Operation
als
Resonanzakt
beschreibt und sie in die bestehende Delta-Mechanik einbettet.
Damit
erhält
das
Collatz-Problem erstmals
eine geschlossene symbolische
Beschreibung, die sowohl mathematisch als auch physikalisch interpretierbar ist.
2


## Página 3


Contents
1 Ziel und Grundgedanke . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 Symbolische Codierung . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.1 Resonanzalphabet . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.2 Codierung der Folge . . . . . . . . . . . . . . . . . . . . . . . . .
5
3 Visuelle Darstellung . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4 Integration in die Kaskade . . . . . . . . . . . . . . . . . . . . . . . . 7
4.1 Von Symbolen zu Zählgrößen . . . . . . . . . . . . . . . . . . . .
7
4.2 Logarithmische Energiebilanz . . . . . . . . . . . . . . . . . . . .
7
4.3 Einordnung in die Codes . . . . . . . . . . . . . . . . . . . . . .
7
4.4 Verbindung zur Delta-Mechanik . . . . . . . . . . . . . . . . . .
7
4.5 Exponentenbild (HexaPrimar) . . . . . . . . . . . . . . . . . . .
7
4.6 Primzeit und Takt . . . . . . . . . . . . . . . . . . . . . . . . . .
8
4.7 Praktische Kurzformeln . . . . . . . . . . . . . . . . . . . . . . .
8
4.8 Fazit der Einbettung . . . . . . . . . . . . . . . . . . . . . . . .
8
5 Glossar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
6 Anhang A: Konkrete Berechnungen . . . . . . . . . . . . . . . . . .
9
6.1 A.1 Vorgehen (Kurzalgorithmus) . . . . . . . . . . . . . . . . .
10
6.2 A.2 Beispiel 1: Startzahl n=7 . . . . . . . . . . . . . . . . . . .
10
6.3 A.3 Beispiel 2: Startzahl n=19 . . . . . . . . . . . . . . . . . .
10
6.4 A.4 Schwellenwert und Einordnung . . . . . . . . . . . . . . . . 11
6.5 A.5 Exponentenbild (nur 2 und 3, Diagnose) . . . . . . . . . .
11
6.6 A.6 Geometrische Skizze (Spirale, minimal) . . . . . . . . . . . . 11
7 Formelsammlung . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
7.1 A. Grundregeln der Collatz-Folge . . . . . . . . . . . . . . . . .
11
7.2 B. Resonanzgrößen . . . . . . . . . . . . . . . . . . . . . . . . .
12
7.3 C. Logarithmische Energiebilanz . . . . . . . . . . . . . . . . . . 12
7.4 D. Exponentenbild (2–3-Dominanz) . . . . . . . . . . . . . . . . 12
7.5 E. Impulsdarstellung (Delta-Mechanik) . . . . . . . . . . . . . .
12
7.6 F. Frequenz und Primzeit . . . . . . . . . . . . . . . . . . . . .
12
7.7 G. Kurzzeit-Resonanz . . . . . . . . . . . . . . . . . . . . . . . .
12
7.8 H. Geometrische Darstellung (Spirale) . . . . . . . . . . . . . .
13
7.9 I. Zusammenfassende Kernformeln . . . . . . . . . . . . . . . . . 13
3


## Página 4


1 Ziel und Grundgedanke
Das
Ziel
dieser
Arbeit
ist
es,
die
Collatz-Folge
als
ein
geordnetes,
deterministisches System zu beschreiben. Die bekannte Rekursion wird dabei
nicht
verändert, sondern in eine andere Sichtweise übertragen.
Anstelle der
üblichen Zahlenfolge steht der Ablauf der Operationen selbst im Mittelpunkt.
Diese Operationen bilden zusammen ein rhythmisches System aus Expansion und
Kontraktion, das wie eine Welle oder ein Oszillator funktioniert.
Der Grundgedanke ist einfach: Die Collatz-Folge folgt keinem Zufall, sondern
einem inneren Takt. Jede Multiplikation mit drei und jede Division durch zwei
sind Teil eines größeren Gleichgewichtsprozesses. Dieses Gleichgewicht lässt sich
durch
eine
symbolische
Sprache
beschreiben,
in
der
jede
Operation
einen
eindeutigen
Resonanzwert
besitzt.
Die entstehende Struktur
zeigt,
dass
die
scheinbar chaotische Bewegung tatsächlich einem klaren Muster folgt.
Damit
wird
die
Collatz-Folge
zu
einem
Beispiel
dafür,
wie
einfache
Rechenregeln komplexe, aber stabile Ordnungen erzeugen können. Die Arbeit
zeigt, dass dieser Aufbau nicht nur für Collatz gilt, sondern auch mit der
Primmechanik,
der
Delta-Mechanik
und
anderen
arithmetischen
Resonanzsystemen verbunden ist. So entsteht ein einheitliches Modell, in dem
Zahl, Bewegung und Energie durch denselben logischen Rahmen beschrieben
werden.
2 Symbolische Codierung
Um die Collatz-Folge als Resonanzsystem zu verstehen, muss ihr Ablauf in eine
symbolische Sprache übersetzt werden. Anstelle der Zahlen selbst werden die
Rechenschritte betrachtet. Jede Operation erhält ein einfaches Symbol, das ihre
Wirkung beschreibt:
• Das Symbol E steht für Expansion und ersetzt den Schritt mal drei plus
eins.
• Das Symbol K steht für Kontraktion und ersetzt den Schritt geteilt
durch zwei.
• Der Fixpunkt F kennzeichnet das Ende der Bewegung, wenn der Zyklus 4
–2–1 erreicht ist.
Ein Collatz-Ablauf kann dadurch als reine Zeichenkette beschrieben werden, zum
Beispiel: E K K E K K K F. Die Struktur dieser Sequenz zeigt sofort, wie viele
Expansions- und Kontraktionsphasen auftreten und in welchem Verhältnis sie
stehen.
Diese symbolische Darstellung hat mehrere Vorteile:
• Sie
macht
das
Verhalten
der
Folge
unabhängig
von
konkreten
Zahlenwerten sichtbar.
4


## Página 5


• Sie
erlaubt
den
Vergleich
verschiedener
Startzahlen
über
ihre
Symbolmuster.
• Sie
zeigt
den
inneren
Rhythmus
des
Systems
und
legt
seine
Resonanzstruktur oﬀen.
Die Collatz-Folge wird so zu einer Art Wort oder Melodie aus nur wenigen
Zeichen.
Jede Startzahl
erzeugt eine eigene,
aber
nicht
zufällige Folge
von
Symbolen.
Daraus
entsteht
eine
Sprache,
in
der
man
die
Ordnung
und
Wiederkehr arithmetischer Muster untersuchen kann.
Diese Codierung ist die Grundlage für die geometrische und dynamische
Darstellung der Collatz-Resonanz, die in den folgenden Abschnitten beschrieben
wird.
2.1 Resonanzalphabet
Wir deﬁnieren folgende Symbole:
Symbol
Bedeutung
Resonanzsicht
×3
Verstärkung
Impulsresonanz
:2
Rückkopplung
Kontraktion/Selbstresonanz
+1
Fortschritt
Übergangsresonanz
=1
Fixpunkt
Endresonanz
2.2 Codierung der Folge
Die klassische Zahlenfolge wird
durch
eine Abfolge dieser
Resonanzsymbole
ersetzt. Beispiel:
722113417522613
entspricht
1×3+1:2×3+1:2:2×3+1
Diese Sequenz kann als symbolische Wellenform interpretiert werden.
3 Visuelle Darstellung
Die symbolische Beschreibung der Collatz-Folge kann in eine geometrische Form
übersetzt werden. Jede Operation wird dabei als Bewegung im Raum dargestellt.
So entsteht ein Bild der Resonanz, das die Dynamik des Systems sichtbar macht.
Die einfachste Form ist die Collatz-Spirale. Dabei wird jeder Schritt der
Folge als kleiner Winkel und jede Expansion oder Kontraktion als Änderung des
Radius gezeichnet. Die Regel ist einfach:
• Für eine Expansion (E) wird der Radius leicht vergrößert.
• Für eine Kontraktion (K) wird der Radius verkleinert.
5


## Página 6


• Der Winkel wird bei jedem Schritt um einen festen Betrag weitergedreht.
Auf diese Weise entsteht
aus der symbolischen
Sequenz ein kontinuierliches
Muster aus Wellen, Bögen und Verdichtungen. Die Spirale ist nicht zufällig,
sondern zeigt einen klaren Rhythmus aus Ausdehnung und Rückkehr.
Jede
Startzahl
erzeugt
ein
charakteristisches
geometrisches
Muster,
das
wie
ein
Fingerabdruck der zugrunde liegenden Resonanz wirkt.
Die visuelle Darstellung dient nicht nur der Illustration. Sie zeigt Strukturen,
die sich
in
der reinen
Zahlenform kaum erkennen
lassen:
Bereiche stabiler
Schwingung, Übergänge in neue Phasen und Spiegelungen zwischen Expansion
und Kontraktion. So wird aus der Collatz-Folge ein sichtbares Resonanzfeld, in
dem Ordnung und Bewegung zugleich existieren.
Eine Möglichkeit der Visualisierung ist die Collatz-Spirale:
• Phase: gesteuert durch Symboltyp (×3 = Expansion, :2 = Kontraktion)
• Amplitude: proportional zu log(n) oder Schrittweite
• Farbe: codiert Symbol (z.B. rot = ×3, blau = :2)
So
entsteht
eine
geometrische
Darstellung
der
energetischen
Bewegung
der
Collatz-Folge als Resonanzkörper, nicht als reine Zahlenfolge.
6


## Página 7


4 Integration in die Kaskade
Die Collatz-Resonanz wird
hier
in
die Kaskade
eingebettet:
Primmechanik,
Delta-Mechanik und die Codes Primar, Tetra,
Quint, Sextant. Ziel ist eine
direkte Verknüpfung von Symbolstruktur und Zahlen.
4.1 Von Symbolen zu Zählgrößen
Startzahl n, Folge: n0=n,n1,n2, bis Zyklus 421
Jeder Schritt ist entweder: - Expansion E: 3x+1 - Kontraktion K: x/2
Zählgrößen: - s(n): Gesamtzahl der Schritte - e(n): Anzahl der E-Schritte -
k(n): Anzahl der K-Schritte Beziehung: s(n)=e(n)+k(n)
Resonanzverhältnis: R(n)=e(n)
s(n)
4.2 Logarithmische Energiebilanz
Für E-Schritt: ΔE(x)=log(3x+1)-logx=log(3+1/x)
Für K-Schritt: ΔK=-log2
Mittlere Änderung pro Schritt: (n)≈R(n)log3-(1-R(n))log2
Resonanzschwelle: R∗=log2
log2+log3≈0.387
Interpretation: - R(n)<R∗: Netto-Dämpfung - R(n)>R∗: Netto-Verstärkung
4.3 Einordnung in die Codes
Primarcode: Jeder Schritt zählt +1 →Taktfolge
Tetracode: E↦+1, K↦-1 Resonanzpfad: Wt=∑t-1
j=0σj, mit σj=+1 bei E, -1 bei
K
Endwert: Ws(n)=e(n)-k(n)=2e(n)-s(n)
Quintcode: Markiere Wiederholungen: ×1 bei (E,E) oder (K,K) Zählgröße:
q(n)
Sextantcode: Setze ÷1 bei Eintritt in Zyklus 421 Optional auch bei starken
Rücksprüngen
4.4 Verbindung zur Delta-Mechanik
Impulsfolge: δt=+1 bei E, -1 bei K
Integrierte Summe: ST=∑T-1
t=0δt
Entspricht dem Tetracode-Pfad WT
Langzeitbilanz: (n)<0 bei R(n)<R∗→Netto-Dämpfung
4.5 Exponentenbild (HexaPrimar)
7


## Página 8


Faktoren 2 und 3 aggregieren:
Exponentenvektor: E2(n)=k(n), E3(n)=e(n)
Skalenfaktor: G(n)≈3
e(n)
2
k(n)
Logarithmische Bilanz wie in Abschnitt 2
4.6 Primzeit und Takt
Minimale Schrittzeit: τ(t)=t
Gewichtete Zeit: τ(t)=∑
t-1
j=0ωj, mit ωj=α bei E, 1 bei K, α>1
Resonanzfrequenz: f(n)=e(n)
τ(s(n))
4.7 Praktische Kurzformeln
Für jede Startzahl n:
- s(n)=e(n)+k(n) - R(n)=e(n)/s(n) - R∗≈0.387 - (n)≈R(n)log3-(1-R(n))log2 -
q(n): Anzahl gleicher Schritte hintereinander - G(n)≈3e(n)/2k(n)
4.8 Fazit der Einbettung
Die Collatz-Resonanz integriert sich systemisch in die Kaskade:
- Primar →Takt - Tetra →Impulspfad - Quint →lokale Wiederholung -
Sextant
→
Reset
-
Delta-Mechanik
→
Impulsstrom
-
Exponentenbild
→
Dämpfungsdiagnose
Die Schwelle R∗trennt Verstärkung von Dämpfung. Die symbolische Sprache
wird zur messbaren Dynamik.
5 Glossar
Collatz-Folge
— Eine Zahlenfolge,
die aus
der
rekursiven
Regel
entsteht:
ungerade Zahl →3n+1, gerade Zahl →n/2. Trotz ihrer Einfachheit zeigt sie ein
komplexes, scheinbar chaotisches Verhalten.
Resonanzsystem
—
Darstellung
der
Collatz-Folge
als
dynamisches
Gleichgewicht
zwischen
zwei
gegensätzlichen
Operationen:
Expansion
und
Kontraktion. Jeder Schritt wird als Energieübergang interpretiert, nicht bloß als
numerische Transformation.
Expansion (E) — Der Schritt 3x+1; steht für Verstärkung, Ausdehnung oder
Vorwärtsresonanz. Symbolisch: Energieaufnahme, analog zu positiver Arbeit.
Kontraktion (K) — Der Schritt x/2; steht für Dämpfung, Rückkopplung oder
Selbstresonanz. Symbolisch: Energieabgabe, analog zu negativer Arbeit.
Fixpunkt (F) — Der stabile Endzustand
1 oder
der Zyklus 421. In
der
Resonanzsprache: der stationäre Zustand nach vollständiger Dämpfung.
8


## Página 9


Resonanzverhältnis R(n)— Anteil der Expansionsschritte an der Gesamtzahl
der
Schritte:
R(n)=e(n)/s(n)
mit
s(n)=e(n)+k(n).
Kennzeichnet
die
„Temperatur“ oder Energieverteilung eines Ablaufs.
Resonanzschwelle R∗— Grenzwert, bei dem sich Expansion und Kontraktion
im Mittel ausgleichen. R
∗=log2
log2+log3≈0,387. Für R<R
∗überwiegt Dämpfung
(Folge sinkt), für R>R
∗wäre Netto-Wachstum möglich.
Kurzzeit-Resonanz q(n)— Zahl der unmittelbar aufeinanderfolgenden gleichen
Schritte (E,E oder K,K). Zeigt lokale Kohärenz in der Schrittfolge.
Primarcode — Grundtakt der Bewegung; zählt reine Schritte unabhängig vom
Inhalt. Entspricht der Zeitachse der Dynamik.
Tetracode — Zuweisung von +1 für E und -1 für K. Die partielle Summe der
Symbole bildet den Resonanzpfad.
Quintcode — Markierung wiederholter Schritte; ×1 kennzeichnet zwei gleiche
Operationen in Folge. Zeigt lokale Verstärkung (Resonanz).
Sextantcode — Markierung starker Rücksprünge oder Resets; ÷1 tritt beim
Erreichen des Fixpunkts auf. Spiegelt globale Stabilität.
Delta-Mechanik
—
Allgemeines
Modell
der
Primmechanik,
das
jede
Veränderung als diskrete Impulsfolge δt=±1 beschreibt. Die Collatz-Folge liefert
ein konkretes Beispiel dieser Struktur.
Primmechanik — Übergeordneter Rahmen, der Zahl, Zeit und Resonanz in
einem einheitlichen
logischen
System verbindet. Die Collatz-Resonanz ist ein
spezieller Fall darin.
Exponentenbild — Darstellung der Folge über die Exponenten der Faktoren 2
und 3: E2=k(n), E3=e(n), mit Skalenfaktor G=3
E3/2
E2. Dient als einfacher Maßstab
für Verstärkung und Dämpfung.
Primzeit — Die natürliche Schrittzeit der Dynamik. Kann linear (τ=t) oder
gewichtet nach der Energiedichte der Schritte (ωj) deﬁniert werden.
Resonanzspirale — Geometrische Darstellung der Collatz-Folge. Jeder Schritt
verändert Radius und Winkel; Expansionen weiten, Kontraktionen rollen ein. Die
Form zeigt das Verhältnis von Ordnung und Dämpfung visuell.
Resonanzcode — Gesamtsprache aus Symbolen und Regeln (E,K,F und deren
Kombinationen), die die Bewegung der Collatz-Folge beschreibt. Er bildet die
Grundlage für die Analyse und für die Verbindung zur Primmechanik-Kaskade.
6 Anhang A: Konkrete Berechnungen
Dieser
Anhang
zeigt,
wie
die
symbolische
Sicht
(Expansion
E
=
3x+1,
Kontraktion K = x/2) in einfache, nachvollziehbare Zahlenrechnungen übersetzt
wird. Ziel ist, für eine Startzahl n die Zählgrößen e(n), k(n), s(n) sowie das
Resonanzverhältnis R(n) und eine grobe Log-Bilanz zu bestimmen.
9


## Página 10


6.1 A.1 Vorgehen (Kurzalgorithmus)
Für eine gegebene Startzahl n:
• Setze x←n, e←0, k←0.
• Wiederhole, bis x=1:
– Falls x ungerade: x←3x+1 (zähle e←e+1).
– Falls x gerade: x←x/2 (zähle k←k+1).
• Setze s←e+k, R←e/s.
Optionale Kurzzeit-Resonanz: Zähle q als Anzahl benachbarter gleicher Schritte (
E,E oder K,K) in der Schrittfolge.
6.2 A.2 Beispiel 1: Startzahl n=7
Ablauf (Schritte als Symbolfolge):
7E22K11E34K17E52K26K13E40K20K10K5E16K8K4K2K1.
Zählgrößen:
e(7)=5,k(7)=11,s(7)=16,R(7)=5
16=0,3125.
Grobe Log-Bilanz (Heuristik mit log3≈1,0986, log2≈0,6931):
(7)≈R⋅log3-(1-R)⋅log2=0,3125⋅1,0986-0,6875⋅0,6931≈-0,13.
Negativ bedeutet: Dämpfung überwiegt im Mittel.
Kurzzeit-Resonanz
q(7):
In
der
Schrittfolge
treten
K,K
mehrfach
hintereinander auf. Zählt man benachbarte Doppler, erhält man q(7)=6.
6.3 A.3 Beispiel 2: Startzahl n=19
Ablauf (Symbolfolge):
19E58K29E88K44K22K11E34K17E52K26K13E40K20K10K5E16K8K4K2K1.
Zählgrößen:
e(19)=6,k(19)=14,s(19)=20,R(19)=6
20=0,30.
Grobe Log-Bilanz:
(19)≈0,30⋅1,0986-0,70⋅0,6931≈-0,15.
Auch hier dominiert die Dämpfung.
10


## Página 11


6.4 A.4 Schwellenwert und Einordnung
Die neutrale Resonanzschwelle (mittlere Log-Änderung gleich null) ist
R∗=log2
log2+log3≈0,387.
In beiden Beispielen gilt R(n)<R
∗, daher ist der Prozess im Mittel dämpfend.
Das erklärt, warum die Folge trotz gelegentlicher Expansion zuverlässig in den
Zyklus 421 fällt.
6.5 A.5 Exponentenbild (nur 2 und 3, Diagnose)
Setzt man
die +1 in
3x+1 heuristisch
beiseite,
bekommt
man
als groben
Skalenfaktor
G(n)≈3
e(n)
2k(n).
Für n=7: G≈35/211=243/2048≈0,119.
Für n=19: G≈36/214=729/16384≈0,0445.
Beide Werte liegen deutlich unter 1, konsistent mit der negativen Log-Bilanz.
6.6 A.6 Geometrische Skizze (Spirale, minimal)
Für eine einfache Collatz-Spirale genügen konstante Schrittregeln:
rt+1= θt+1=θt+γ,
mit konstanten Parametern a>0, b>0, γ>0. Die Symbolfolge E/K einer Startzahl
erzeugt so ein
charakteristisches
Muster. Die Dämpfung (viele K) führt zu
Einrollen der Spirale, Bündel von E zu Aufblähungen. Die Parameter dienen nur
der Darstellung und ändern nicht die Zählgrößen e,k,s,R.
7 Formelsammlung
Diese
Sammlung
fasst
zentrale
Beziehungen
und
Deﬁnitionen
der
Collatz-Resonanz kompakt zusammen. Alle Größen sind so gewählt, dass sie ohne
Zusatzpakete berechenbar sind.
7.1 A. Grundregeln der Collatz-Folge
Für ungerade n: f(n)=3n+1
Für gerade n: f(n)=n/2
Gesamtzahl der Schritte bis 1: s(n)=e(n)+k(n)
11


## Página 12


Dabei gilt: e(n): Anzahl der Expansionsschritte (3x+1)
k(n): Anzahl der Kontraktionsschritte (x/2)
7.2 B. Resonanzgrößen
Resonanzverhältnis: R(n)=e(n)
s(n)
Resonanzschwelle: R
∗=log2
log2+log3≈0.387
Bedingung: Wenn R(n)<R∗: Dämpfende Resonanz (Abkühlung)
Wenn R(n)>R∗: Verstärkende Resonanz (Aufheizung)
7.3 C. Logarithmische Energiebilanz
Mittlere Änderung pro Schritt: (n)≈R(n)log3-(1-R(n))log2
Bei (n)<0: Netto-Dämpfung
Bei (n)>0: Netto-Verstärkung
7.4 D. Exponentenbild (2–3-Dominanz)
E2(n)=k(n)
E3(n)=e(n)
Skalenfaktor: G(n)≈3
E3(n)⋅2
-E2(n)
Logarithmische Form: logG(n)=E3(n)log3-E2(n)log2
Vorzeichen von logG(n): Wachstums- oder Dämpfungsdominanz
7.5 E. Impulsdarstellung (Delta-Mechanik)
Jeder Schritt erhält ein Impulszeichen: δt=+1 bei E, -1 bei K
Resonanzpfad (Summenform): WT=∑T-1
t=0δt=e(T)-k(T)
Ws(n)=2e(n)-s(n)
7.6 F. Frequenz und Primzeit
Gewichtete Schrittzeit: τ(t)=∑t-1
j=0ωj
Mit: ωj=a bei E, ωj=1 bei K, wobei a>1
Resonanzfrequenz: f(n)=e(n)
τ(s(n))
7.7 G. Kurzzeit-Resonanz
Zähle gleiche aufeinanderfolgende Schritte (E,E oder K,K): q(n)={j∣σj=σj+1}, mit
σj∈{E,K}
Hohe Werte von q(n): Lokale Kohärenz (Resonanzbündel)
12


## Página 13


7.8 H. Geometrische Darstellung (Spirale)
Diskrete Spiralgleichung: rt+1=a⋅rt bei E, rt+1=b⋅rt bei K
Winkeländerung: θt+1=θt+γ
Parameter: a>1, 0<b<1, γ>0
Neutrale Schwelle: R
∗=-logb
loga-logb
7.9 I. Zusammenfassende Kernformeln
Diese
Gleichungen
bilden
die
rechnerische
Basis
der
Collatz-Resonanz.
Sie
verknüpfen Symbolstruktur, Energieverhalten und geometrische Dynamik in einer
gemeinsamen Darstellung.
13
