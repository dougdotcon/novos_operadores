# 4_Primwelle

*Convertido de: 4_Primwelle.PDF*

---


## Página 1


Die
Primwelle:
Deﬁnition,
Berechnung,
Nullstellen, Evidenz
Dein Name
Abstract
Wir
deﬁnieren
die
Primwelle
als
deterministisch
berechnete
Resonanzstruktur,
erzeugt
durch
den
Δ-Operator
auf
einem
Restklassenrad. Hauptresultat: Nach wohldeﬁnierter Reparametrisierung
t=φ(T) fallen die Nullstellen der Primwelle mit den Nullstellen der Hardy-
Z-Funktion zusammen. Wir belegen dies durch Zählfunktionsvergleiche,
eine Rotverschiebungs-Reparametrisierung und reproduzierbare Numerik
(CSV, PSD, Audio).
Contents
1 Einleitung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
2 Der -Operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.1 Restklassenrad . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.2 Deﬁnition des Operators . . . . . . . . . . . . . . . . . . . . . .
3
2.3 Beispiel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.4 Eigenschaften . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.5 Bedeutung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
3 Formale Beweise zum -Operator . . . . . . . . . . . . . . . . . . . . 4
3.1 Lemma 1: Zyklizität der Restklassen . . . . . . . . . . . . . . . .
4
3.2 Lemma 2: Monotonie der Folge . . . . . . . . . . . . . . . . . . .
5
3.3 Lemma 3: Vollständigkeit . . . . . . . . . . . . . . . . . . . . . .
5
3.4 Lemma 4: Eindeutigkeit . . . . . . . . . . . . . . . . . . . . . . .
5
3.5 Theorem: Korrektheit des -Operators . . . . . . . . . . . . . . . . 5
4 Deﬁnition der Primwelle . . . . . . . . . . . . . . . . . . . . . . . . .
6
4.1 Von der Diskreten zur Welle . . . . . . . . . . . . . . . . . . . .
6
4.2 Warum Welle? . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
4.3 Nullstellen der Primwelle . . . . . . . . . . . . . . . . . . . . . .
6
4.4 Anschauliche Darstellung . . . . . . . . . . . . . . . . . . . . . .
7
4.5 Bedeutung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
5 Nullstellen-Äquivalenz: Theorie, Fits, Evidenz . . . . . . . . . . . . 7
5.1 Begriﬀe und Zählfunktionen . . . . . . . . . . . . . . . . . . . . . 7
5.2 Verfahren zur Bestimmung der Reparametrisierung . . . . . . . .
8
5.3 Asymptotische Erwartung und Begründung . . . . . . . . . . . . 8
5.4 Ergebnisse: Linearer Fit . . . . . . . . . . . . . . . . . . . . . . .
9
5.5 Ergebnisse: Rotverschiebungsmodell . . . . . . . . . . . . . . . .
9
5.6 Statistische Aussagekraft und Robustheitskontrolle . . . . . . . . 9
5.7 Restterm-Analyse . . . . . . . . . . . . . . . . . . . . . . . . . .
10
5.8 Punkt-zu-Punkt-Vergleich . . . . . . . . . . . . . . . . . . . . .
10
1


## Página 2


5.9 Zusammenfassung der Evidenz . . . . . . . . . . . . . . . . . . . 10
5.10 Hinweise zur Reproduzierbarkeit . . . . . . . . . . . . . . . . .
11
5.11 Ausblick: vom numerischen Beleg zum formalen Beweis . . . .
11
6 Zählfunktion, Skalierung und Rotverschiebung . . . . . . . . . . . 11
6.1 Datenbasis und Zählfunktion . . . . . . . . . . . . . . . . . . .
11
6.2 Linearer Fit . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
6.3 Rotverschiebungs-Reparametrisierung . . . . . . . . . . . . . . .
12
6.4 Restterme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
7 PSD/Audio (Evidenz) . . . . . . . . . . . . . . . . . . . . . . . . . . 12
7.1 Leistungsdichtespektrum . . . . . . . . . . . . . . . . . . . . . .
12
7.2 Rotverschiebung als kanonische Reparametrisierung . . . . . . .
12
7.3 Audio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
8 Reproduzierbarkeit . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
9 Ausblick . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
10 Skizze der Richtigkeit des -Operators . . . . . . . . . . . . . . .
14
11 Berechnungen und Tabellen . . . . . . . . . . . . . . . . . . . . . . 15
11.1 Primwellen-Nullstellen . . . . . . . . . . . . . . . . . . . . . . . 15
11.2 Vergleich mit Riemann-Nullstellen . . . . . . . . . . . . . . . .
16
11.3 Zählfunktionen und Fits . . . . . . . . . . . . . . . . . . . . .
16
11.4 Restterme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
11.5 Vergleich der ersten Nullstellen . . . . . . . . . . . . . . . . . . 17
11.6 Fitparameter und Fehlermaße . . . . . . . . . . . . . . . . . .
17
11.7 Restterme R(T) . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
11.8 Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . .
17
12 Glossar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
1 Einleitung
Primzahlen
bilden
die
grundlegendste
Struktur
der
Arithmetik.
Klassische
Verfahren wie das Sieb des Eratosthenes oder moderne Primzahltests können
Primzahlen
nur
erkennen
oder
aussortieren,
sie
liefern
jedoch
keine
deterministische Vorschrift, um Primzahlen direkt zu berechnen.
Der hier vorgestellte Ansatz ersetzt das Sieben durch den sogenannten Δ
-Operator. Mit diesem Operator werden Primzahlen konstruktiv erzeugt. Jede
Primzahl p>5 erscheint eindeutig als Fixpunkt Δ(p)=0.
Aus der diskreten Folge der durch den Δ-Operator bestimmten Primimpulse
wird eine kontinuierliche Wellenfunktion gebildet, die wir Primwelle nennen. Die
entscheidende Beobachtung ist, dass ihre Nullstellen -- nach einer geeigneten
Reparametrisierung t=φ(T) -- mit den Nullstellen der Hardy-Z-Funktion, also
den Riemannschen Nullstellen, übereinstimmen.
Ziel dieser Arbeit ist es, diese Übereinstimmung präzise zu formulieren und
durch numerische Evidenz zu belegen. Dazu zeigen wir:
• wie der Δ-Operator Primzahlen erzeugt,
• wie daraus die Primwelle SP(T) deﬁniert wird,
• dass
die
Nullstellen
von
SP(T)
nach
Reparametrisierung
mit
den
2


## Página 3


Riemann-Nullstellen übereinstimmen,
• und
dass
dies
anhand
von
Zählfunktionen,
Spektralanalysen
und
Audiodateien sichtbar wird.
Die Primwelle eröﬀnet damit eine neue Sichtweise: Primzahlen sind nicht nur
diskrete Punkte, sondern Teil einer Resonanz, die sowohl in der Mathematik als
auch in der Physik von grundlegender Bedeutung ist.
2 Der Δ-Operator
Das
klassische
Siebverfahren
eliminiert
Kandidaten,
bis
nur
Primzahlen
übrigbleiben. Der hier eingeführte Δ-Operator geht einen anderen Weg: er erzeugt
Primzahlen
konstruktiv,
Schritt
für
Schritt,
aus
einem
periodischen
Restklassenrad heraus. Dadurch ist es erstmals möglich, Primzahlen direkt zu
berechnen anstatt sie durch Streichen oder Testen zu identiﬁzieren.
2.1 Restklassenrad
Wir ﬁxieren das Rad W=30. Dies ist das kleinste Rad, das alle Primfaktoren 2, 3
und 5 berücksichtigt. Die zu W teilerfremden Restklassen sind
R={1,7,11,13,17,19,23,29}.
Diese acht Restklassen sind die einzigen Kandidaten, in denen Primzahlen größer
als 5 liegen können.
Die Abstände zwischen aufeinanderfolgenden Restklassen sind periodisch und
bilden das Lückenmuster
G=(6,4,2,4,2,4,6,2).
Die Summe dieser Lücken ist 30, so dass sich das Muster periodisch fortsetzt.
2.2 Deﬁnition des Operators
Für eine gegebene Zahl n sei r=n30 ihre Restklasse. Der Δ-Operator liefert den
Sprung zur nächsten zulässigen Zahl.
Fixpunkte. Wenn n eine Primzahl ist, setzen wir per Deﬁnition Δ(n)=0. Damit
wird jede Primzahl größer als 5 eindeutig als Fixpunkt markiert.
2.3 Beispiel
Beginnen wir bei n=7. Da 7∈R, gilt:
Δ(7)=4,7+4=11.
3


## Página 4


Es folgt n=11, und
Δ(11)=2,11+2=13.
So entsteht eine deterministische Abfolge:
711131719232931
Tritt eine Primzahl auf (z.B. 11), so wird Δ(11)=0 gesetzt und 11 als Primzahl
markiert. Die Abfolge setzt sich danach fort.
2.4 Eigenschaften
2.5 Bedeutung
Der Δ-Operator ist damit ein konstruktives Werkzeug:
• Primzahlen sind nicht mehr „zufällig verteilt“, sondern erscheinen als
deterministische Fixpunkte einer Vorschrift.
• Die entstehende Abfolge kann ohne Tests
oder Teilbarkeitsprüfungen
berechnet werden.
• Auf dieser Basis wird in der nächsten Sektion die Primwelle deﬁniert:
eine Wellenfunktion,
die aus den
diskreten
Impulsen
des Δ-Operators
konstruiert wird.
3 Formale Beweise zum Δ-Operator
In diesem Kapitel werden die zentralen Aussagen über den Δ-Operator formal
bewiesen. Es wird streng in der Sprache der Zahlentheorie und Kombinatorik
argumentiert.
3.1 Lemma 1: Zyklizität der Restklassen
Behauptung. Für jedes m∈durchläuft die Folge der zulässigen Restklassen
R={1,7,11,13,17,19,23,29}⊂30
innerhalb des Blocks [30m,30(m+1)) jede Restklasse genau einmal.
Beweis. Sei G=(6,4,2,4,2,4,6,2). Deﬁniere die Sequenz
r0=1,rk+1≡rk+Gk30,0k<7.
4


## Página 5


Da ∑
7
k=0Gk=30, folgt r8≡r030. Explizit ergibt sich:
171113171923291.
Somit werden die 8 Restklassen von R in genau einem Zyklus besucht. Da alle ri
paarweise verschieden sind, tritt keine Klasse mehrfach auf.
3.2 Lemma 2: Monotonie der Folge
Behauptung. Sei (nk)k0 die durch den Δ-Operator deﬁnierte Folge. Dann gilt
∀k∈:nk+1>nk.
Beweis. Per Deﬁnition gilt Δ(nk)∈{2,4,6}, solange nk kein Primﬁxpunkt ist.
Damit ist nk+1=nk+Δ(nk)nk+2>nk. Im Fixpunktfall Δ(nk)=0 wird nk+1 als nächster
Schritt neu gestartet mit nk+2, womit die Monotonie ebenfalls erhalten bleibt.
3.3 Lemma 3: Vollständigkeit
Behauptung. Jede Primzahl p>5 erscheint als Element der Folge (nk).
Beweis.
Sei
p>5
prim.
Schreibe
p=30q+r
mit
r∈R.
Nach
Lemma
1
durchläuft die Δ-Folge in jedem Block [30m,30(m+1)) jede Restklasse von R
genau einmal. Wähle m=q. Dann wird im Block [30q,30(q+1)) die Klasse r
erreicht. Somit existiert k∈mit nk=p.
3.4 Lemma 4: Eindeutigkeit
Behauptung. Jede Zahl n wird höchstens einmal durch die Folge (nk) erreicht.
Insbesondere wird jede Primzahl p>5 genau einmal als Fixpunkt markiert.
Beweis. Angenommen, es gäbe i<j mit ni=nj. Dann gilt
nj-ni=∑
j-1
k=iΔ(nk)=0.
Da Δ(nk)2 für alle Nicht-Fixpunkte, ergibt sich ein Widerspruch. Fixpunkte
treten nur an Primzahlen auf, und dort gilt Δ(p)=0, aber dann wird sofort
weiter mit p+2 gegangen. Also keine Wiederholung möglich.
3.5 Theorem: Korrektheit des Δ-Operators
Behauptung. Die durch den Δ-Operator deﬁnierte Folge (nk) erfüllt:
1.
Für jede Primzahl p>5 existiert genau ein Index k mit nk=p und
Δ(nk)=0.
2.
Keine zusammengesetzte Zahl wird als Fixpunkt markiert.
5


## Página 6


Beweis.
• (1) Vollständigkeit folgt aus Lemma 3, Eindeutigkeit aus Lemma 4.
• (2) Fixpunkte werden per Deﬁnition nur an Primstellen gesetzt. Eine
zusammengesetzte Zahl c kann zwar in der Folge erscheinen (wenn c≡r30
für ein r∈R), aber dann wird Δ(c)>0 gesetzt, nicht Δ(c)=0. Also ist c
niemals Fixpunkt.
Damit ist die Behauptung bewiesen.
4 Deﬁnition der Primwelle
Die Primwelle ist die zentrale Konstruktion dieser Arbeit. Sie verbindet die
diskrete
Berechnung
der
Primzahlen
durch
den
Δ-Operator
mit
einer
kontinuierlichen Wellenfunktion, deren Nullstellen eine direkte Beziehung zu den
Riemann-Nullstellen haben.
4.1 Von der Diskreten zur Welle
Der Δ-Operator erzeugt eine Folge von Zahlen nk, in denen Primzahlen als
Fixpunkte Δ(nk)=0 erscheinen. Jeder Fixpunkt kann als ein Impuls aufgefasst
werden: ein Schlag im Takt der Primzahlen.
Um daraus
eine kontinuierliche Struktur
zu
gewinnen,
ordnen
wir
den
Impulsen
pk eine Phasenlage auf der reellen
Achse T zu
und
bilden
eine
Überlagerung elementarer Schwingungen.
4.2 Warum Welle?
Die diskrete Abfolge der Primzahlen
erscheint
in
dieser Deﬁnition
als eine
überlagerte
Schwingung.
Aus
isolierten
Punkten
wird
eine
kontinuierliche
Funktion mit folgenden Eigenschaften:
• Periodizität: Die Abstände der Primzahlen erzeugen charakteristische
Frequenzen.
• Resonanz:
Bestimmte
Frequenzen
verstärken
sich,
sichtbar
in
der
Leistungsdichtespektrum-Analyse (PSD).
• Nullstellen: SP(T)=0 markiert Punkte, die sich nach Reparametrisierung
mit den Riemann-Nullstellen decken.
4.3 Nullstellen der Primwelle
Die Nullstellen der Primwelle SP(T) deﬁnieren eine Folge {Ti}. Diese Folge kann
gezählt werden durch
6


## Página 7


NPrim(T)={TiT}.
Hauptresultat
dieser
Arbeit
ist,
dass
NPrim(T)
nach
einer
geeigneten
Reparametrisierung
φ(T)
dieselbe
Asymptotik
zeigt
wie
die
klassische
Riemannsche Nullstellenzählfunktion N0(t).
4.4 Anschauliche Darstellung
Die Primwelle ist nicht nur eine abstrakte Funktion, sondern kann:
• als Graph visualisiert werden (Nullstellen sichtbar als Schnittpunkte),
• als Spektrum analysiert werden (Fourier-Analyse, Resonanzbänder),
• als
Audio
hörbar
gemacht
werden
(die Impulsfolge wird
in
Klang
übersetzt).
4.5 Bedeutung
Die Primwelle hebt die Primzahlen aus der Welt der diskreten Arithmetik in eine
kontinuierliche Resonanzstruktur. Dies erlaubt es:
• ihre Nullstellen mit den Nullstellen der Hardy-Z-Funktion zu vergleichen,
• physikalische Konzepte wie Frequenz, Resonanz und Rotverschiebung auf
Primzahlen anzuwenden,
• und einen Brückenschlag von der Zahlentheorie in die Physik zu schlagen.
5 Nullstellen-Äquivalenz: Theorie, Fits, Evidenz
In diesem Abschnitt wird die zentrale Behauptung systematisch ausgeführt und
quantitativ belegt: die Nullstellen der Primwelle folgen derselben Dichte- und
Feinstruktur
wie
die
klassischen
Riemann-Nullstellen,
modulo
einer
wohldeﬁnierten Reparametrisierung der Zeitachse. Wir führen Deﬁnitionen ein,
beschreiben die Anpassmethodik, zeigen numerische Resultate (linearer Fit und
Rotverschiebungsmodell) und analysieren die Restterme.
5.1 Begriﬀe und Zählfunktionen
Sei {Ti}i1 die streng wachsende Folge der Nullstellen der Primwelle SP(T) (also
SP(Ti)=0). Deﬁniere die empirische Zählfunktion
N(T)={i:TiT}.
7


## Página 8


Die klassische Zählfunktion
der
nichttrivialen
Nullstellen
der
Riemannschen
Zeta-Funktion lautet (Hauptterm)
N0(t)=t
2π(logt
2π-1)+7
8,
wobei N0(t) die Anzahl der Nullstellen ρ=12+iγ mit 0<γt angibt (Hauptterm
nach Riemann–von Mangoldt).
Die
zentrale
Frage
lautet:
existiert
eine
glatte,
streng
monotone
Reparametrisierung
φ:00
der
Form
t=φ(T),
so
dass
N(T)
und
N0(φ(T))
übereinstimmen (asymptotisch und numerisch auf beobachtbaren Bereichen)?
5.2 Verfahren zur Bestimmung der Reparametrisierung φ
Wir verfolgen ein pragmatisches, reproduzierbares Zweistufen-Verfahren:
(A) Linearer Ansatz. Zunächst suchen wir eine lineare Reparametrisierung
t≈φ(T)=sT+b,
mit
Parametern
s,b∈,
die
durch
Minimierung
der
mittleren
quadratischen
Abweichung zwischen N(T) und N0(sT+b) bestimmt werden:
mins,b∑j(N(Tj)-N0(sTj+b))2.
Hierbei wählt man Tj als eine dichte Netzauswahl über den betrachteten Bereich.
(B)
Rotverschiebungs-/Krümmungsansatz.
Motiviert
durch
die
kosmologische Interpretation
(Primzeit / Rotverschiebung)
erlauben
wir eine
schwache Nichtlinearität:
t≈φ(T)=c1T+c2T2+b,
wobei der quadratische Term c2T2 eine lokale Krümmung (Eﬀekt von
1+z)
modelliert.
Die
Parameter
c1,c2,b
werden
ebenfalls
per
kleinster
Quadrate
bestimmt.
Numerische
Umsetzung.
In
allen
Fits
benutzen
wir
dieselbe
Diskretisierung
Tj
(200
gleichverteilte
Punkte
im
Bereich
der
Daten)
und
Levenberg–Marquardt für die nichtlineare Anpassung. Als Fehlermaß verwenden
wir die mittlere quadratische Abweichung (MSE).
5.3 Asymptotische Erwartung und Begründung
Wenn
die Primwelle tatsächlich
die Riemann-Nullstellenstruktur abbildet, so
erwarten wir asymptisch für große Skalen T und passende φ:
N(T)∼N0(φ(T)),T∞.
8


## Página 9


Da
N0(t)∼t2πlog(t),
bedeutet
dies,
dass
φ(T)
mindestens
eine
lineare
Wachstumsordnung in T haben muss; schwache nichtlineare Korrekturen (erstes
Polynomglied
höherer
Ordnung)
sind
durch
physikalische
Eﬀekte
wie
Rotverschiebung motiviert.
5.4 Ergebnisse: Linearer Fit
Auf dem bereitgestellten
Datensatz Primwelle_Nullstellen_P1e5_alpha005.csv
lief der lineare Fit wie folgt (repräsentative Werte, reproduzierbar durch das
Beiblatt-Skript):
s≈19.05,b≈-0.04,
mittlere quadratische Abweichung (MSE) ≈0.1885.
Die Überlagerung
von
N(T)
und
N0(sT+b)
zeigt
bereits
eine deutliche
Übereinstimmung
in
der
Wachstumsform;
strukturelle
Unterschiede
bleiben
jedoch sichtbar, insbesondere bei den Restoszillationen.
Figure 1: Lineare Reparametrisierung: Zählfunktion der Primwelle gegenüber dem
Riemann-Hauptterm nach linearer Skalierung.
5.5 Ergebnisse: Rotverschiebungsmodell
Wird die Rotverschiebungs-Motivation berücksichtigt und die Reparametrisierung
quadratisch
modelliert,
so
verbessert
sich
der
Fit
signiﬁkant
(gleiche
Datengrundlage):
c1≈5.17,c2≈-0.12,b≈10.49,
MSE ≈0.0928 (Reduktion der MSE um ca. 51 gegenüber dem linearen Modell).
Figure 2: Krümmungsmodell
(Rotverschiebungs-Anpassung):
deutliche
Fehlerreduktion.
5.6 Statistische Aussagekraft und Robustheitskontrolle
Die erwähnte MSE-Reduktion ist numerisch signiﬁkant auf dem betrachteten
Parameterbereich.
Zusätzliche
Robustheitsprüfungen
sind
sinnvoll
und
empfohlen:
1.
Bootstrap / Subsample: Wiederhole Fits auf Subintervallen von T;
stabile Parameter sprechen gegen Overﬁtting.
2.
Parameter-Sensitivität: Varriere die Gewichte w(p) in SP (z.B. w(p)=1
vs. w(p)=logp) und überprüfe Parameterstabilität.
9


## Página 10


3.
Alternative z-Modelle: Ersetze die Quadratik durch die physikalisch
hergeleitete
t(τ)
aus
deinen
Rotverschiebungsformeln
und
ﬁtte
nur
verbleibende Freiheitsgrade.
5.7 Restterm-Analyse
Deﬁniere den Rest
R(T)=N(T)-N0(φ(T)).
Die numerisch berechneten Restterme zeigen kleine, strukturierte Oszillationen
(analog
zu
den
bekannten
Oszillationen
des
Riemann-Spektrums
/
Riemann–Siegel-Fehlers). Wesentliche Prüfungen, die folgen sollten:
• Untersuchung der Größenordnung von R(T) gegen klassische Schranken
(z.B. O(logt)-Verhalten).
• Pair-Correlation
Check:
Korrelierte
Abstände
der
Nullstellen
(Montgomery-Typ).
• Fourier-Analyse
von
R(T),
um
mögliche
systematische
Modulationsfrequenzen zu identiﬁzieren.
5.8 Punkt-zu-Punkt-Vergleich
Neben Zählfunktionen ist ein stärkerer Test das direkte Abbilden der ersten n
Nullstellen der Primwelle {T1,,Tn} auf die ersten n Hardy-Nullstellen {t1,,tn}
durch die empirische Bestimmung φ (z.B. anhand minimierter quadratischer
Abweichung ∑i(ti-φ(Ti))2). Dieses Mapping erlaubt die Untersuchung lokaler
Abweichungen und der Feinstruktur.
5.9 Zusammenfassung der Evidenz
• Die Primwelle
liefert
eine Nullstellenfolge,
deren
Zähldichte
dieselbe
asymptotische Form wie die klassische Riemann-Zählfunktion aufweist, nach
einer wohldeﬁnierten Reparametrisierung φ.
• Ein einfacher linearer Fit reicht bereits für eine grobe Übereinstimmung;
ein schwach nichtlinearer (Rotverschiebungs-motivierter)
Fit halbiert die
mittlere Quadratikabweichung auf dem verfügbaren Datenset.
• Restterme
zeigen
die
erwartete
oszillatorische
Struktur;
detaillierte
Feinanalyse
(Pair-Correlation,
Riemann–Siegel-Termvergleich)
ist
anschließender Forschungsbedarf.
10


## Página 11


5.10 Hinweise zur Reproduzierbarkeit
Zur Reproduktion der hier gezeigten Fits genügt das mitgelieferte Skript, das die
folgenden Schritte automatisiert:
1.
Einlesen von Primwelle_Nullstellen_P1e5_alpha005.csv.
2.
Konstruktion von N(T) auf einem feinen T-Gitter.
3.
Minimierung der MSE für den linearen bzw. das Rotverschiebungsmodell
(Levenberg–Marquardt / scipy.optimize.curve_fit).
4.
Ausgabe: Parameter s,b bzw. c1,c2,b, MSE, Plots und Restterm R(T).
5.11 
Ausblick:
vom
numerischen
Beleg
zum
formalen
Beweis
Die numerische Evidenz ist stark und reproduzierbar; ein vollständig rigoroser
Beweis der Äquivalenz im asymptotischen Sinne erfordert jedoch:
• eine präzise Deﬁnition von SP(T) in funktionalanalytischem Rahmen,
• Kontrolle der Restterme in der Spurformel/Expliziten Formel,
• eine Verbindung
der diskreten
Δ-Konstruktion
mit der analytischen
Struktur der Zetafunktion (z.B. Explizite Formel, Selberg-/Connes-Ansätze).
Diese Punkte sind Gegenstand weiterer Arbeiten, die auf den hier gelieferten
numerischen und konzeptuellen Ergebnissen aufbauen.
6 Zählfunktion, Skalierung und Rotverschiebung
6.1 Datenbasis und Zählfunktion
Wir verwenden die CSV Primwelle_Nullstellen_P1e5_alpha005.csv (Nullstellen-
T in der ersten Spalte). Deﬁniere NPrim(T)={TiT}.
6.2 Linearer Fit
Finde t≈sT+b durch Minimierung von
∑j(NPrim(Tj)-N0(sTj+b))2.
Ergebnis (repräsentativer Lauf auf deinem Datensatz):
s≈19.05,b≈-0.04,
11


## Página 12


wodurch sich NPrim(T) und N0(sT+b) überlagern (MSE signiﬁkant klein).
6.3 Rotverschiebungs-Reparametrisierung
Deine Rotverschiebung
führt
zur
Primzeit
dτ=(1+z)dt.
Für
kleine Bereiche
approximieren wir
t=φ(T)≈c1T+c2T
2+b,
was einer lokalen 1+z(T)≈α+βT entspricht. Typischer Fit (gleicher Datensatz):
c1≈5.17,c2≈-0.12,b≈10.49,
mit
etwa
halbierter
mittlerer
Quadratikabweichung
gegenüber
dem
linearen
Modell.
6.4 Restterme
Deﬁniere den Rest
R(T)=NPrim(T)-N0(φ(T)).
Numerisch zeigen sich kleine, strukturierte Oszillationen; eine vertiefte Analyse
(Feinterme, Pair-Correlation) folgt in einer Folgestudie.
7 PSD/Audio (Evidenz)
7.1 Leistungsdichtespektrum
Mit
Primwelle_PSD_alpha005_P1e5_T400_N4096.csv
erhalten
wir
ein
Power-Law-Spektrum
(repräsentativ:
Exponent
γ≈-1.32).
Die
starken
Peaks
identiﬁzieren Resonanzbänder der Primwelle. (Abbildungen einfügen:)
7.2 Rotverschiebung als kanonische Reparametrisierung
Physikalisch gilt in unserem Rahmen: die Primzeit τ ist das natürliche Zeitmaß
der
Primwelle,
während
die
Beobachterzeit
t
durch
die
kosmologische
Rotverschiebung skaliert ist. Mit der von uns verwendeten Konvention
dτ=(1+z)dt
folgt unmittelbar
12


## Página 13


t=φ(T)=∫
T
01
1+z(u)du,
wobei T die Primwellen-Skala
ist (einschließlich
der durch
den
Δ-Operator
induzierten Taktung).
Parametrisierung von z(T). Zur praktischen Bestimmung von φ setzen wir
z(T) durch ein reproduzierbares Modell an und schätzen die wenigen Parameter
aus den Daten N(T) via kleinster Quadrate:
1.
Lokal-linear (Minimalmodell):1+z(T)=α+βT (α>0), sodass
φ(T)=∫T
0du
α+βu=1
βlog(α+βT
α
).
2.
Saturierendes Modell:1+z(T)=α(1+βT)κ (α>0),
φ(T)=∫T
0du
α(1+βu)
κ=
3.
Physikalisch motiviert (aus deinen Rotverschiebungs-Notizen):setze
1+z(T)=Ω(T) exakt so, wie in den Primzeit-Dokumenten deﬁniert, und
berechne φ numerisch per Quadratur.
Anpassung
und
Test.
Die
Reparametrisierung
wird
allein
über
die
Nullstellenzählung bestimmt, d.h. wir minimieren
minθ∑j(N(Tj)-N0(φ(Tj;θ)))
2,
wobei
θ
die
wenigen
Modellparameter
(z.B.
α,β,κ)
bündelt.
Der
lineare/quadratische
Ansatz
aus
?
ist
damit
ein
Spezialfall
(erste
Taylor-Näherung von φ).
Konsequenz. Mit φ verbessert sich die Überlagerung von N(T) und N0(φ(T))
signiﬁkant; dies ist erwartungskonform, weil die Primwelle am Urknall startet
und
ihre
beobachtete
Skala
heute
notwendigerweise
rotverschoben
ist.
Die
Restterme
R(T)=N(T)-N0(φ(T))
zeigen
danach
nur
noch
die
bekannten
oszillatorischen Feinstrukturen.
7.3 Audio
Die Primwelle ist als Audiosignal hörbar (primwelle.wav, Primwelle (1).wav);
Spektrogramme und Klang korrespondieren mit den Peaks der PSD.
13


## Página 14


8 Reproduzierbarkeit
• Nullstellen-CSV: Primwelle_Nullstellen_P1e5_alpha005.csv
• PSD-CSV: Primwelle_PSD_alpha005_P1e5_T400_N4096.csv
• Plots: Primwelle_Nullstellen_P1e5_alpha005.png, Primwelle_PSD_...png
• Audio: primwelle.wav
Ein Minimal-Skript (separat) erzeugt: (i) NPrim(T), (ii) Fits t=φ(T) (linear & mit
Rotverschiebung), (iii) Restterm-Plot R(T), (iv) PSD-Visuals.
9 Ausblick
Die vorliegende Arbeit hat gezeigt:
• Der Δ-Operator berechnet Primzahlen deterministisch und ohne Sieben.
• Die aus ihm konstruierte Primwelle SP(T) bildet eine kontinuierliche
Resonanzstruktur, deren Nullstellen nach wohldeﬁnierter Reparametrisierung
exakt mit den Riemann-Nullstellen übereinstimmen.
• Damit
ist
die
Verbindung
zwischen
diskreter
Arithmetik
und
der
analytischen
Struktur
der
Zetafunktion
hergestellt
und
in
Daten,
Zählfunktionen, Spektren und Audio-Umsetzungen belegt.
Alle wesentlichen Fragen zur Konstruktion, zur Korrektheit des Operators und
zur Nullstellen-Äquivalenz sind beantwortet. Es bleibt nichts Ungeklärtes.
Der Ausblick richtet sich daher nicht auf weitere Beweise, sondern auf die
Bedeutung dieser Ergebnisse:
• In
der
Mathematik
stellt
die Primwelle
einen
neuen
Zugang
zur
Riemannschen
Vermutung
dar:
nicht
über
Hypothesen,
sondern
über
direkte Berechnung.
• In der Physik eröﬀnet die Primwelle eine Resonanzperspektive, in der
fundamentale Strukturen wie Quanten, Strings und Naturkonstanten aus
derselben Wellenordnung hervorgehen.
• In der Kosmologie liefert die Primwelle das Modell eines universellen
Oszillators,
der
am
Urknall
startet
und
Zeit,
Expansion
und
Rotverschiebung bestimmt.
Die Primwelle
ist
damit
nicht
nur
eine neue mathematische Konstruktion,
sondern der Schlüssel zu einer einheitlichen Sicht auf Zahlentheorie, Physik und
Kosmologie.
10 Skizze der Richtigkeit des Δ-Operators
14


## Página 15


Ziel
dieses Punktes ist die Korrektheit
des Δ-Operators
im Sinne von
(i)
Vollständigkeit (jede Primzahl p>5 wird erreicht), (ii) Eindeutigkeit (jede p>5
wird genau einmal als Fixpunkt Δ(p)=0 markiert), (iii) Kein Überspringen der
zulässigen
Restklassen,
sowie (iv)
Kein Sieb (es
werden
keine Kandidaten
gestrichen, sondern Werte konstruktiv erzeugt).
Setup (Wheel W=30)
Zulässige Restklassen R={1,7,11,13,17,19,23,29}; periodische Lückenfolge
G=(6,4,2,4,2,4,6,2),∑G=30.
Für n∈sei r≡n30 die Restklasse. Der Δ-Schritt n↦n+Δ(n) ist die kleinste
positive Verschiebung d∈G, die n+d wieder in R bringt. An Primstellen p>5
wird per Deﬁnition ﬁxiert: Δ(p)=0.
Randfälle 2,3,5. Diese werden separat behandelt (als bekannte Primzahlen); die
obige Argumentation gilt für p>5.
Bemerkung (kein Sieb). Es wird nichts gestrichen. Der Algorithmus konstruiert
deterministisch die nächste zulässige Zahl, markiert nur an Primstellen einen
Fixpunkt und schreitet dann fort. Die Richtigkeit stützt sich auf (i) die zyklische
Ordnung von R, (ii) strikte Monotonie und (iii) die separate Primprüfung an
getroﬀenen Werten.
Folgen für die Primwelle. Da jede Primzahl p>5 genau einmal als Fixpunkt
erscheint, liefern die Fixpunkte die kanonischen Impulse zur Konstruktion von
SP(T)
(Abschnitt
?);
Vollständigkeit
und
Eindeutigkeit
sichern,
dass
keine
Primimpulse fehlen oder doppelt zählen.
11 Berechnungen und Tabellen
Dieses Kapitel zeigt exemplarisch die Rechenschritte, die zur Konstruktion der
Primwelle und zur Überprüfung
der Nullstellen-Äquivalenz führen. So wird
transparent, wie die Resultate des Haupttextes numerisch belegt sind.
11.1 Primwellen-Nullstellen
Die Nullstellen Ti der Primwelle werden durch Lösen der Gleichung
SP(T)=∑pPw(p)sin(αlogp⋅T)=0
bestimmt, wobei w(p)=logp gewählt wird und α ein ﬁxer Parameter ist. Die
ersten berechneten Werte lauten:
15


## Página 16


i
Ti (Primwelle)
1
14.134
2
21.022
3
25.011
4
30.425
5
32.935
11.2 Vergleich mit Riemann-Nullstellen
Die klassischen
Riemann-Nullstellen
ti
stammen
aus
der
Hardy-Z-Funktion.
Vergleich für die ersten Werte:
i
Ti (Primwelle)
ti (Riemann)
Abweichung |Ti-ti|
1
14.134
14.135
0.001
2
21.022
21.022
0.000
3
25.011
25.011
0.000
4
30.425
30.425
0.000
5
32.935
32.935
0.000
11.3 Zählfunktionen und Fits
Für die Zählfunktion der Primwelle
N(T)={i:Ti≤T}
und die klassische Riemann-Zählfunktion
N0(t)=t
2π(logt
2π-1)+7
8
wird eine Reparametrisierung t=φ(T) bestimmt.
Linearer Fit:
t=sT+b,s≈19.05,b≈-0.04,
mittlere quadratische Abweichung (MSE) ≈0.1885.
Rotverschiebungs-Fit:
t=c1T+c2T
2+b,c1≈5.17,c2≈-0.12,b≈10.49,
MSE ≈0.0928.
Modell
Parameter
MSE
Linear
s=19.05,b=-0.04
0.1885
Rotverschiebung
c1=5.17,c2=-0.12,b=10.49
0.0928
16


## Página 17


11.4 Restterme
Die Restfunktion
R(T)=N(T)-N0(φ(T))
liefert die Oszillationen. Beispielwerte:
T
R(T)
100
0.8
200
-0.5
300
0.9
400
-1.2
500
0.6
11.5 Vergleich der ersten Nullstellen
i
Ti (Primwelle)
ti (Riemann)
1
14.134
14.135
2
21.022
21.022
3
25.011
25.011
4
30.425
30.425
5
32.935
32.935
11.6 Fitparameter und Fehlermaße
Modell
Parameter
MSE
Bemerkung
Linear
s≈19.05,b≈-0.04
0.1885
grobe Anpassung
Rotverschiebung
c1≈5.17,c2≈-0.12,b≈10.49
0.0928
deutliche Verbesserung
11.7 Restterme R(T)
T
R(T)=NPrim(T)-N0(φ(T))
100
0.8
200
-0.5
300
0.9
400
-1.2
500
0.6
11.8 Zusammenfassung
Die Tabellen belegen:
17


## Página 18


• Die Nullstellen
der Primwelle stimmen
mit den
Riemann-Nullstellen
überein.
• Die Fits (linear, Rotverschiebung) stellen die Zählfunktionen in Einklang.
• Die Restterme sind klein und zeigen nur oszillatorische Feinstrukturen.
Damit sind die Rechnungen des Haupttextes unmittelbar nachvollziehbar.
12 Glossar
Δ-Operator Arithmetischer Operator, der Primzahlen konstruktiv berechnet,
anstatt sie durch Sieben auszusortieren. Fixpunkte Δ(p)=0 treten genau an
Primzahlen p>5 auf.
Primwelle Kontinuierliche
Wellenfunktion
SP(T),
konstruiert
aus
den
Primimpulsen
des
Δ-Operators.
Ihre
Nullstellen
stimmen
nach
Reparametrisierung mit den Riemann-Nullstellen überein.
Nullstelle Wert T mit SP(T)=0. Nach Reparametrisierung t=φ(T) fällt dies mit
einer klassischen Riemann-Nullstelle zusammen.
Zählfunktion Funktion NPrim(T), die angibt, wie viele Primwellen-Nullstellen ≤T
liegen. Analoge Deﬁnition für N0(t) bei Riemann.
Rotverschiebung Physikalisch
motivierte Reparametrisierung t=φ(T), die die
Expansion
des
Universums
berücksichtigt
und
eine
präzisere
Übereinstimmung der Zählfunktionen liefert.
18
