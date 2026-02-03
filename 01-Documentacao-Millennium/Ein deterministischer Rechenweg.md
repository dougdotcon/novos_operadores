# Ein deterministischer Rechenweg

*Convertido de: Ein deterministischer Rechenweg.PDF*

---


## Página 1


Immer die nächste Primzahl:
Ein deterministischer Rechenweg mit ∆-Operator und
Primarkode
Jeanette Tabea Leue
3. September 2025
1. Grundidee
Wir beschreiben einen deterministischen Algorithmus, der zu jeder ganzen Zahl x ≥2
die nächste Primzahl p = min{q > x : q ist prim} berechnet. Die Mechanik basiert auf
einem ∆-Update (Takt) und dem Primarkode
0 = Kompositum,
1 = Prim,
+1 = Schritt (Tick).
2. ∆-Operator und Primarkode (segmentiertes Resonanz-
Sieb)
Definition 1 (Arbeitsblock). Sei [a, b] ⊂N ein Intervall. Als Grundfrequenzen verwen-
den wir alle Primzahlen p ≤
√
b.
Definition 2 (Reste-Initialisierung). Zu Beginn (n = a) erhält jede Grundfrequenz p
einen Zustand
rp := (−a) mod p ∈{0, 1, . . . , p −1},
d. h. nach genau rp Ticks trifft das erste Vielfache von p im Block ein.
Definition 3 (∆-Tick, Event, Commit). Für n = a, a + 1, . . . , b wiederhole:
1. ∆-Tick (“+1”): für jedes p setze
rp ←
(
p −1,
rp = 0,
rp −1,
sonst.
2. Event-Test (“0”): falls (äquivalent: vor dem Tick) rp = 0 für ein p, wird n als
Kompositum markiert.
3. Commit (“1”): falls kein Event ausgelöst wird, ist n Primzahl und wird ausgegeben.
Lemma 1 (Korrektheit des Blocks). Nach Durchlauf von [a, b] sind genau die unmarkier-
ten n prim.
Beweisskizze. Jedes Kompositum m ≤b besitzt einen Primteiler p ≤
√
b; die Restklasse
zu p trifft bei m (Vielfaches) exakt den Event-Zustand und markiert m. Primzahlen haben
keine solchen Events und bleiben unmarkiert.
1


## Página 2


3. Nächste Primzahl Next(x)
Definition 4 (Nächste Primzahl). Für x ≥2 definiere
Next(x) := min{q > x : q ist prim}.
Definition 5 (Algorithmus N für Next(x)). Setze a := x+1. Wähle b so, dass garantiert
eine Primzahl in [a, b] liegt (z. B. b := 2x für x ≥2). Führe den Blockalgorithmus aus
Abschnitt 2 auf [a, b] aus und gib das erste ausgegebene n als Next(x) zurück.
Satz 1 (Terminierung und Korrektheit von N). Für jedes x ≥2 terminiert N und liefert
Next(x).
Beweisskizze. (Terminierung) Nach dem Satz von Bertrand/Čebyšev liegt für x ≥2 stets
eine Primzahl im Intervall [x + 1, 2x]. Der Algorithmus betrachtet endlich viele n in
[a, b] = [x + 1, 2x] und terminiert daher.
(Korrektheit) Nach Lemma 1 gibt der Blockalgorithmus genau die Primzahlen in [a, b]
aus. Die erste ausgegebene ist definitionsgemäß die kleinste Primzahl > x, also Next(x).
Bemerkung (Determinismus). Der Ablauf (Reste, Ticks, Events, Commit) ist rein regel-
basiert; gleiche Eingabe ⇒gleiche Ausgabe.
4. Index-Sicht und Primar-Arithmetik
Bezeichne die aufsteigende Folge der Primzahlen mit p1, p2, p3, . . . .
Definition 6 (Index-Nachfolger). Der Prim-Index-Nachfolger ist succ(k) := k + 1 mit
psucc(k) = Next(pk).
Satz 2 (Iterierbarkeit). Für jedes k und jedes t ∈N gilt
pk+t = Next(Next(· · · Next
|
{z
}
t mal
(pk) · · · )).
Beweis. Induktion über t unter Verwendung von Satz 2.
Definition 7 (Primar-Arithmetik auf Indizes). Für m, n, a ∈N definieren wir Operatio-
nen auf der Indexebene:
pm⊗pn := pm·n,
pm⊘d := pm/d (d | m),
(pm)⟨a⟩:= pma,
⟨a⟩√pm := pm1/a (m = a-te Potenz).
Das Ergebnis ist jeweils eine eindeutig bestimmte Primzahl; die Auswertung p• erfolgt
deterministisch via Next (Abschnitt 3).
5. Beispiele (auswertbar ohne Raten)
p2 ⊗p2 = p4 = 7,
p9 ⊘3 = p3 = 5,
⟨2⟩√p36 = p6 = 13,
(p6)⟨2⟩= p36 = 151,
p100 ⊗p10 = p1000 = 7919.
2


## Página 3


6. Fazit
Der ∆-Operator mit Primarkode liefert einen deterministischen, terminierenden und kor-
rekten Rechenweg zur nächsten Primzahl. Durch Iteration entsteht die gesamte unendliche
Primfolge. Damit ist das Rechnen mit Primzahlen (auf Indexebene mit deterministischer
Auswertung zu konkreten Werten) formal begründet.
3
