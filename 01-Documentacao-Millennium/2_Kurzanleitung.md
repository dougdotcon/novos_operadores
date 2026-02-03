# 2_Kurzanleitung

*Convertido de: 2_Kurzanleitung.PDF*

---


## Página 1


Kurzanleitung:
1 Startpunkt: Das deterministische Euler--Protokoll
Um die folgenden
Ergebnisse sofort
nachvollziehbar
zu
machen,
geben
wir
zunächst den konkreten Rechenweg an, der ohne Unendlichkeiten und ohne Siebe
auskommt.
1. Deﬁnition des Δ--Operators
Wir ﬁxieren das Wheel W=30 mit den acht Restklassen
{1,7,11,13,17,19,23,29}.
Die Kandidatenfolge entsteht durch zyklisches Durchlaufen der Lücken
[6,4,2,4,2,4,6,2].
Deﬁnition: Δ(n) ist die kleinste positive Lücke des Zyklus, die zum nächsten
Kandidaten führt. Sobald ein Kandidat prim ist, gilt Δ=0. Damit liefert Δ
deterministisch die nächste Primzahl.
2. Endlichkeit des Protokolls
Für jede gewählte Schranke x liefert Δ alle Primzahlen bis x. Damit ist die
Chebyshev--Funktion
θ(x)=∑pxlogp
endlich berechenbar.
Für jede Höhe t auf der kritischen Linie genügt
N=⌊t2π⌋,
sodass die Riemann--Siegel--Summenformel für Z(t) nur N Terme benötigt. Auch
dieser Schritt ist endlich.
3. Minimalbeispiele
• Δ(100)=1, nächster Kandidat 101 ist prim, dort Δ=0.
• Δ(106)=3, nächster Kandidat 1,000,003 ist prim, dort Δ=0.
1


## Página 2


• θ(10
6)=998484.175 (aus Δ--Primzahlen).
• Z(14.1340)<0, Z(14.1350)>0 ⇒Nullstelle dazwischen auf der kritischen
Linie.
4. Schlussfolgerung
Das Euler--Protokoll
Δ⟶θ(x)⟶Θ(t)⟶Z(t)
arbeitet vollständig endlich und deterministisch. Alle benötigten Daten stammen
aus dem Δ--Operator. Ein Beweis über „Unendlichkeiten“ ist nicht nötig, denn
jede gewünschte Höhe t oder Schranke x kann direkt ausgerechnet werden.
2
