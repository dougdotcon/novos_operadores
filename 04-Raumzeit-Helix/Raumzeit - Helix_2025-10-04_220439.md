# Raumzeit - Helix_2025-10-04_220439

*Convertido de: Raumzeit - Helix_2025-10-04_220439.PDF*

---


## Página 1


Die Raumzeit–Helix
Von
der
Primzeit
zur
geometrischen
Raumstruktur
Jeanette Tabea Leue
4.~Oktober~2025
1


## Página 2


Einleitung
Dieses Dokument entwickelt die Raumzeit--Helix als ein deterministisches Modell,
das
die
Folge
der
Primzahlen
in
eine
geometrische
Bewegung
überführt.
Ausgehend von der logarithmischen Primzeit wird eine dreidimensionale Struktur
konstruiert, deren Dynamik durch einen selbstadjungierten Operator beschrieben
werden
kann.
Die
Raumzeit--Helix
verbindet
arithmetische
Diskretheit
mit
kontinuierlicher
Geometrie:
jede
Primzahl
entspricht
einem
Zeittakt,
dessen
Beitrag eine stabile, schwingende und blockweise gespiegelte Form hervorbringt.
Nach der Deﬁnition der Variablen und Parameter werden die elementaren
Lemmata
und
deren
Beweise
vorgestellt.
Darauf
folgt
eine
kompakte
Zusammenfassung der wichtigsten Formeln sowie die Analyse zweier zeitlicher
Modi: der normale Verlauf und der beschleunigte „Urknall“-Start. Abschließend
werden die Stabilität, Sättigung und Spiegelstruktur der Raumzeit--Helix durch
numerische Tests überprüft.
2


## Página 3


Contents
1 Die Raumzeit–Helix: vollständige Deﬁnition und Beweisstruktur
4
1.1 Grundgedanke . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.2 Konstruktion der Variablen . . . . . . . . . . . . . . . . . . . . . 4
1.3 Lemmata und Beweise . . . . . . . . . . . . . . . . . . . . . . . .
6
1.4 Zusammenfassung der Eigenschaften . . . . . . . . . . . . . . . .
7
1.5 Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2 Raumzeit–Helix: Deﬁnitionen und elementare Lemmata . . . . .
7
2.1 Modell-Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Elementare Lemmata . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.3 Folgerungen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 Raumzeit–Helix: Modi, Navigation und Tests . . . . . . . . . . . . 9
3.1 Parameter und Zeitmodi . . . . . . . . . . . . . . . . . . . . . . . 9
3.2 Vorwärts: Primtakt
Koordinaten . . . . . . . . . . . . . . . . . . 9
3.3 Rückwärts: Koordinate Primzahl . . . . . . . . . . . . . . . . . . 9
3.4 Sprung-Events (Navigation) . . . . . . . . . . . . . . . . . . . .
10
3.5 Minimal-Algorithmus (Zustandsupdate) . . . . . . . . . . . . .
10
3.6 Tests (Parameter: =1,T=,a=1,L=5,t_0=0,=12) . . . . . . . . .
10
4 Zusatz A: Rückwärtsveriﬁkation und numerische Rekonstruktion13
4.1 A.1 Ziel und Aussage . . . . . . . . . . . . . . . . . . . . . . . . 13
4.2 A.2 Rahmen, Notation, feste Parameter . . . . . . . . . . . . . . 13
4.3 A.3 Vorwärtsabbildung (kurz) . . . . . . . . . . . . . . . . . . . 13
4.4 A.4 Inverse Abbildung über den Höhenkanal . . . . . . . . . .
13
4.5 A.5 Sensitivität und Konditionierung . . . . . . . . . . . . . .
14
4.6 A.6 Ereignisbasierte Rekonstruktion (Triggerpunkte) . . . . . .
14
4.7 A.7 Algorithmus (schrittweise, deterministisch) . . . . . . . . .
14
4.8 A.8 Fehlerfortpﬂanzung und Präzision . . . . . . . . . . . . . .
15
4.9 A.9 Parameterabhängigkeit . . . . . . . . . . . . . . . . . . . . . 15
4.10 A.10 Validierungsprotokoll (empfohlen) . . . . . . . . . . . . .
15
4.11 A.11 Typische Beobachtungen . . . . . . . . . . . . . . . . . .
15
4.12 A.12 Grenzfälle und Schutz . . . . . . . . . . . . . . . . . . . . 16
4.13 A.13 Tabelle A.1 (Beispielstruktur) . . . . . . . . . . . . . . .
16
5 Zusatz B: Tabellen und numerische Daten . . . . . . . . . . . . .
17
5.1 B.1 Übersicht . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
5.2 B.2 Vorwärtsberechnung (Normalmodus) . . . . . . . . . . . . . 17
5.3 B.3 Rückwärtsrekonstruktion (Normalmodus) . . . . . . . . . .
17
5.4 B.4 Vergleich mit Yang–Kopplung . . . . . . . . . . . . . . . .
18
5.5 B.5 Hinweise zur Reproduktion . . . . . . . . . . . . . . . . . .
18
5.6 B.6 Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . .
18
3


## Página 4


1 Die Raumzeit–Helix: vollständige Deﬁnition und
Beweisstruktur
1.1 Grundgedanke
Die Raumzeit–Helix beschreibt den Übergang von diskreten Primzahlen zu einer
kontinuierlichen geometrischen Struktur. Jede Primzahl pk liefert dabei
einen
diskreten Zeittakt. Die Summe ihrer Logarithmen deﬁniert eine arithmetische Zeit
tk, aus der durch deterministische Transformationen eine stabile, schwingende
und zugleich begrenzte Raumstruktur entsteht.
1.2 Konstruktion der Variablen
Die Parameter
α>0,β∈,T>0,a>0,L>0,t0∈
werden als feste Systemkonstanten gewählt. Sie legen Frequenz, Phasenversatz,
Blocklänge, Dämpfung, Raumhöhe und Startzeit fest.
Primzeit.
tk=∑
k
j=1lnpj,(k1)
tk wächst streng monoton, da lnpj>0. Sie ist die Primzeit, eine interne Uhr, die
aus der Primstruktur selbst entsteht.
Phase.
Θk=αtk+β.
Sie bestimmt den Phasenwinkel des Systems. Jede neue Primzahl pk+1 verschiebt
die Phase um αlnpk+1:
Θk+1-Θk=αlnpk+1.
Fraktionale Phase. Da nur die relative Phase zählt, wird der Wert auf die
Blocklänge T moduliert:
φk=(Θk
T)∈[0,1),
4


## Página 5


wobei (x)=x-⌊x⌋den gebrochenen Anteil bezeichnet.
Zentrierte Phase und Wellenform. Aus der fraktionalen Phase entstehen
Pk=φk-12,Ck=1-2|Pk|.
Pk
misst
die
Abweichung
vom
Zentrum,
Ck
liefert
eine
Sägezahn-artige
Modulation zwischen 0 und 1.
Blockweise Spiegelung. Zur Sicherung der Symmetrie wird
pro Block der
Vorzeichenfaktor
sk=(-1)
⌊(tk-t0)/T⌋
eingeführt. Er spiegelt die Welle periodisch, sobald tk eine neue Blockgrenze
t0+mT erreicht. Damit erhält das System eine interne Parität, vergleichbar der
„kritischen Linie“ in der Riemannschen Symmetrie.
Dämpfung (Birch). Zur Stabilisierung der Energie wird ein Dämpfungsfaktor
eingeführt:
Dk=1
1+aα
2C
2k,a>0.
Für kleine Ck wirkt Dk≈1, bei großen Amplituden sinkt Dk und begrenzt die
Dynamik. Physikalisch entspricht dies einer endlichen Energiekapazität.
Hodge-Höhe. Die vertikale Einbettung geschieht über
zk=Ltanh(tk
L),L>0.
Die Funktion tanh sorgt für ein asymptotisches Plateau: zk wächst monoton und
nähert
sich
L von
unten.
Damit
ist
der
Raum endlich,
aber
ohne harte
Begrenzung.
Helix-Koordinaten. Die räumlichen Koordinaten der Raumzeit–Helix lauten:
xk=2DkPk,yk=skDkCk,zk=Ltanh(tk
L).
xk bildet die horizontale Phase, yk enthält das blockweise gespiegelt modulierte
Signal,
zk
beschreibt
die
vertikale
Sättigung.
Das
Ergebnis
ist
eine
dreidimensionale, sich stabil windende Helix.
5


## Página 6


1.3 Lemmata und Beweise
Lemma 1 (Monotonie und Sättigung).
zk=Ltanh(tk
L),tk=∑jklnpj.
Dann gilt 0<z1<z2<<L und limk∞zk=L. Beweis: tanh ist streng wachsend und
beschränkt durch 1. Da lnpj>0, wächst tk streng monoton. Somit ist zk streng
wachsend und nähert sich L an.
Lemma 2 (Block-Spiegelung).
sk=(-1)
⌊(tk-t0)/T⌋,Im=[t0+mT,t0+(m+1)T).
sk ist auf jedem Intervall Im konstant und wechselt sein Vorzeichen genau bei
tk=t0+mT. Beweis: folgt direkt aus der Deﬁnition des ganzzahligen Teils.
Lemma 3 (Gebundener Radius).
Pk∈[-12,12]⇒Ck=1-2|Pk|∈[0,1],
Dk=1
1+aα2C2k∈[1
1+aα2,1].
Daraus folgt
|xk|=|2DkPk|Dk1,|yk|=|DkCk|Dk1.
Die Bahn bleibt in einem Zylinder mit Radius 1 und Höhe L.
Lemma 4 (Phasen-Update).
θn=αlnn+β,θn+1-θn=αln(1+1
n).
Beweis: direkte Subtraktion.
Lemma 5 (Selbstadjungierter Diskret-Laplace-Operator).
(Hf)(n)=f(n+1)-2f(n)+f(n-1),n1,f(0)=0.
H ist dicht deﬁniert, symmetrisch und selbstadjungiert auf ℓ2(N). Beweis: H ist
6


## Página 7


eine reelle, dreidiagonale Jacobi-Matrix mit konstanten Koeﬃzienten. Für solche
Operatoren
sind
die
Deﬁzienzindizes
(0,0),
daher
folgt
wesentliche
Selbstadjungiertheit (Weyl-Kriterium).
1.4 Zusammenfassung der Eigenschaften
• Die Raumzeit–Helix ist monoton im Parameter tk und asymptotisch
begrenzt durch L.
• Sie weist eine echte Block-Spiegelung auf, die nicht durch Anpassung,
sondern durch Konstruktion entsteht.
• Die radialen Komponenten (xk,yk) bleiben
durch Dk gedämpft und
beschränkt.
• Der zugrunde liegende Operator H besitzt ein reelles Spektrum, was die
physikalische Stabilität und mathematische Selbstkonsistenz des Systems
garantiert.
1.5 Interpretation
Die Raumzeit–Helix ist damit ein deterministisches, selbstbegrenztes System, das
von
der
Primstruktur
bis
zur
geometrischen
Raumzeit
eine
kontinuierliche
Abbildung bildet:
Primzahlen⇒Primzeittk⇒PhaseΘk⇒Raumtrajektorie(xk,yk,zk).
Sie verbindet Zahlentheorie, Schwingung und Geometrie in einem konsistenten
Modell.
Jede Primzahl
fügt
der Helix einen
weiteren
Takt
hinzu,
der die
Raumzeit diskret fortschreibt.
2 
Raumzeit–Helix:
Deﬁnitionen
und
elementare
Lemmata
2.1 Modell-Deﬁnition
Seien feste Parameter
α>0,β∈,T>0,a>0,L>0,t0∈
gegeben. Sei (pk)k1 die aufsteigende Folge der Primzahlen und
tk=∑k
j=1lnpj(k1)
die Primzeit-Akkumulation. Die Phase ist
7


## Página 8


Θk=αtk+β,
die fraktionale Phase (modulo T)
φk=frac(Θk
T)∈[0,1),
sowie
Pk=φk-12∈[-12,12],Ck=1-2|Pk|∈[0,1].
Der blockweise Spiegel-Faktor lautet
sk=(-1)
⌊(tk-t0)/T⌋∈{-1,+1}.
Die Birch-Dämpfung ist
Dk=1
1+aα2C2k∈[1
1+aα2,1],
und die Hodge-Höhe
zk=Ltanh(tk
L)∈(0,L).
Die Prime-Helix-Koordinaten sind schließlich
xk=2DkPk,yk=skDkCk,zk=Ltanh(tk
L).
2.2 Elementare Lemmata
2.3 Folgerungen
Aus Lemma ? und ? ist die Prime-Helix global beschränkt und saturiert in z
gegen L; Lemma ? liefert die echte (nicht-ﬁtbare) Spiegelstruktur; Lemma ? stellt
sicher, dass die zugrunde liegende Dynamik auf einem Operator mit reellem
Spektrum liegt. Diese Aussagen sind rein deterministisch und benötigen keine
numerischen Annahmen.
8


## Página 9


3 Raumzeit–Helix: Modi, Navigation und Tests
3.1 Parameter und Zeitmodi
Feste Parameter: α>0,T>0,a>0,L>0,t0∈,β∈. Zwei Zeitmodi für den Primtakt Δtk:
Normal: Δtk=lnpk
Urknall(schnellerStart): Δtk=1
lnpk
3.2 Vorwärts: Primtakt →Koordinaten
tk=∑jkΔtj
Θk=Θk-1+αΔtk,Θ0=β
φk=frac(Θk
T)
Pk=φk-12,Ck=1-2|Pk|
Dk=1
1+aα2C2k
zk=Ltanh(tk
L)
hk=1-(zk
L)
2=sech
2(tk
L)
sk=(-1)
⌊tk-t0
T ⌋
xk=2DkPkhη
k,yk=skDkCk,zk=Ltanh(tk
L),0η1
3.3 Rückwärts: Koordinate →Primzahl
An Triggerpunkten (z.B. feste Phase) wird zk gemessen:
9


## Página 10


tk=Lartanh(zk
L),Δtk=tk-tk-1
Normal: lnpk=Δtk ⇒ pk=exp(Δtk)
Urknall: 1
lnpk=Δtk ⇒ pk=exp(1
Δtk)
3.4 Sprung-Events (Navigation)
Achsentreﬀer: Ck=0 ⇔yk=0. Spiegelkante: sk ﬂippt bei tk=t0+mT. Kamm: Ck lokal
maximal
⇒|yk|
lokal
maximal.
Allgemein
zum Ziel
(x∗,y∗,z∗):
wähle k
mit
minimaler Distanz in
3.
3.5 Minimal-Algorithmus (Zustandsupdate)
Init:
t=0, Θ=β, k=0.
Bei
jedem
Primimpuls:
k←k+1,
Δt∈{lnpk, 1/lnpk},
t←t+Δt, Θ←Θ+αΔt.
Dann
φ=(Θ/T),
P=φ-12,
C=1-2|P|,
D=1
1+aα2C2,
z=Ltanh(t/L), h=1-(z/L)2, s=(-1)
⌊(t-t0)/T⌋, x=2DPhη, y=sDC.
3.6 Tests (Parameter: α=1, T=π, a=1, L=5, t0=0, η=12)
Die
folgenden
Werte
sind
gerundet;
sie
zeigen
Stabilität,
Spiegelung
und
Sättigung.
Normaler Start (Δt=lnp):
k=50: p50=229, y≈+0.187, x≈0.000, z≈5.000
k=100: p100=541, y≈+0.352, x≈0.000, z≈5.000
k=1000: p1000=7919, y≈+0.421, x≈0.000, z≈5.000
k=10000: p10000=104729, y≈-0.137, x≈-0.000, z≈5.000
Urknall-Start (Δt=1
lnp):
k=50: p50=229, y≈+0.498, x≈+0.005, z≈4.967
k=100: p100=541, y≈-0.387, x≈-0.009, z≈4.999
k=1000: p1000=7919, y≈+0.348, x≈0.000, z≈5.000
k=10000: p10000=104729, y≈+0.318, x≈0.000, z≈5.000
Direktsprung auf die k-te Primzahl (Vorwahl)
Für große k liefert
̂p(k)=k(lnk+lnlnk-1+lnlnk-2
lnk
)
10


## Página 11


eine gute Startschätzung. Vorwahl mit ̂p(k) gibt korrekte Blöcke und fast korrekte
Phasen; exakte Phase durch lokales Einrasten mit echten Primimpulsen.
11


## Página 12


Schlussbemerkung und Ausblick
Am Ende dieser Arbeit bleibt kein leeres Bild von Anfang und Ordnung der
Welt, sondern ein System, das in sich rund ist: eine schwingende Raumzeit,
deren
Ursprung
aus
der
inneren
Struktur
der
Primzahlen
hervorgeht.
Die
Raumzeit–Helix
beschreibt
diese
Ordnung
nicht
als
Zufall,
sondern
als
Resonanzformel eines stabilen, selbstreferenziellen Universums.
Die Primzeit
dient
dabei
als
fundamentale Skala,
auf
der
sich
Phase,
Amplitude
und
Raumdimensionen
aufbauen.
Die
Symmetrie,
die
in
der
Blockspiegelung
sichtbar
wird,
spiegelt
die
Dualität
von
Expansion
und
Rückkopplung wider. So entsteht ein Bild des Kosmos, das weder aus der Ruhe
noch
aus
dem
Chaos,
sondern
aus
einem
Gleichgewicht
der
Gegensätze
hervorgeht.
Das
zentrale
Ergebnis
lautet:
Die
Struktur
der
Primzahlen
erzeugt
eine
geometrische Helix, deren Form die Raumzeit selbst deﬁniert. Der Übergang von
Zahl zur Geometrie, von Diskretion zu Kontinuum, ist kein Sprung, sondern eine
stetige
Resonanz.
Die
Energie
verteilt
sich
nicht
explosionsartig,
sondern
rhythmisch — eine Pulsation, die den Raum stabil hält.
Ausblick
Die vorgestellte Theorie öﬀnet mehrere Perspektiven für zukünftige Forschung:
• Umkehrung
der
Helix:
Die
Untersuchung
des
inversen
Flusses
(Urknallrichtung) könnte erklären, warum Expansion und Abkühlung nicht
getrennt, sondern gekoppelt auftreten.
• Kontinuumserweiterung:
Eine Diﬀerentialform
der
Helixgleichungen
würde eine direkte Verbindung
zur Quantenfeldtheorie und
Relativität
erlauben.
• Numerische Simulation: Durch präzise Berechnung der Helix bis in
hohe Primindizes (k>109) lassen sich Resonanzzonen, Spiegelachsen und
Energieplateaus quantitativ erfassen.
• Kosmologische Anwendung: Die Raumzeit–Helix könnte eine natürliche
Erklärung
für
Rotverschiebung,
Krümmung
und
die
beobachtete
Energieverteilung liefern.
Damit
schließt
sich
der
Kreis:
Aus
der
Primzeit
entsteht
Bewegung,
aus
Bewegung Raum, und aus Raum schließlich Zeit. Was als Zahl begann, endet als
Geometrie – eine universelle Sprache, die in jeder Dimension dieselbe Melodie
trägt.
12


## Página 13


4 Zusatz A: Rückwärtsveriﬁkation und numerische
Rekonstruktion
4.1 A.1 Ziel und Aussage
Dieser
Zusatz
zeigt
rückwärts,
dass
die
Raumzeit–Helix
die
Primstruktur
eindeutig kodiert. Kernpunkt ist die Invertierbarkeit des Höhenkanals:
zk=Ltanh(tk
L)⟹tk=Lartanh(zk
L),Δtk=tk-tk-1.
Im Normalmodus gilt daraus direkt
lnpk=Δtk⟹p
=exp
k
(Δtk).
Im Urknallmodus (schneller Start) ist
1
lnpk=Δtk⟹p=exp
k
(1
Δtk).
Numerisch stimmen pk und pk (bis auf unvermeidliche Rundung). Die Helix ist
somit reversibel.
4.2 A.2 Rahmen, Notation, feste Parameter
Feste Parameter α>0, β∈, T>0, a>0, L>0, t0∈. Primzahlen pk aufsteigend,
Primzeit
tk=∑k
j=1Δtj,Δtj=
Phase Θk=αtk+β, fraktionale Phase φk=(Θk/T), zentrierte Phase Pk=φk-12, Kamm
Ck=1-2|Pk|,
Spiegel
sk=(-1)
⌊(tk-t0)/T⌋,
Dämpfung
Dk=(1+aα2C2
k)-1,
Höhe
zk=Ltanh(tk/L), Koordinaten xk=2DkPk, yk=skDkCk.
4.3 A.3 Vorwärtsabbildung (kurz)
(lnp1,lnp2,)  Summation  tk  Θ,  T  φk,Pk,Ck,sk,Dk  Koordinaten  (xk,yk,zk).
Diese Abbildung ist wohldeﬁniert, stabilisiert radial durch Dk, vertikal durch zk.
4.4 A.4 Inverse Abbildung über den Höhenkanal
13


## Página 14


Da tanh streng wachsend ist,
tk=Lartanh(zk
L)lieferteindeutigtk.
Damit folgt
Δtk=tk-tk-1,unddaraus
Die Rekonstruktion von pk benötigt nur zk (und t0), keine weiteren Signale.
4.5 A.5 Sensitivität und Konditionierung
Ableitung der Inversen:
∂t
∂z=1
1-(z/L)2.
Damit für kleine Fehler δz:
δt≈δz
1-(z/L)2.
Folglich
δ(lnpk)=δ(Δtk)=δtk-δtk-1,δpk≈pkδ(lnpk).
Interpretation: Nahe z≈L wächst 1/(1-(z/L)2); die Inversion ist dort numerisch
anspruchsvoll. Praxis: Rekonstruktion bis kurz vor Sättigung verwenden oder mit
hoher Präzision rechnen.
4.6 A.6 Ereignisbasierte Rekonstruktion (Triggerpunkte)
Spezielle Indizes erleichtern die Auswertung:
Achsentreffer:Ck=0 ⇔ yk=0,Kammmaxima:Ck lokalmaximal,Blockkanten:tk=t0+mT.
An solchen Punkten ist die Phase strukturiert; zk bleibt der alleinige Träger der
Taktinformation.
4.7 A.7 Algorithmus (schrittweise, deterministisch)
1.
Eingabe: Folge (zk)N
k=1, Parameter L, t0 (meist t0=0).
2.
Für jedes k: tk←Lartanh(zk/L).
3.
Für k=1: Δt1←t1-t0; für k2: Δtk←tk-tk-1.
14


## Página 15


4.
Normalmodus: p
=exp
k
(Δtk); Urknallmodus: p
=exp
k
(1/Δtk).
5.
Validierung: Vergleiche pk mit Referenz pk (falls vorhanden); berechne
Fehlerkennzahlen.
4.8 A.8 Fehlerfortpﬂanzung und Präzision
• Rundung: Für zk nahe L erhöht sich die Konditionszahl. Abhilfe: hohe
Präzision; Clipping mit fester Toleranz ε≪1 nur am Sättigungsrand.
• Diﬀerenzenbildung: Δtk=tk-tk-1 reduziert korrelierte Fehler.
Empfohlen:
konsistente Präzision für tk und tk-1.
• Validierungsmetrik:
maxk|p-p
kk|,
maxk|lnp-ln
k pk|,
relative
Fehlernormen
blockweise.
4.9 A.9 Parameterabhängigkeit
• L: Skaliert z und t symmetrisch; die Inversion nutzt dieselbe L und bleibt
exakt.
• a,α: Beeinﬂussen Dk und die Radialanteile (x,y), nicht die Invertierbarkeit
von z.
• T,t0: Strukturieren die Spiegelung sk; sie ändern nicht die z-Inversion.
• Yang-Kopplung γ: Glättet Θ über Blöcke (Phasenträgheit), belässt z
-Kanal unangetastet.
4.10 A.10 Validierungsprotokoll (empfohlen)
• Datensatz: Erste N Primimpulse; Normal- und Urknallmodus separat.
• Schritte: (i) Vorwärtsrechnung (x,y,z), (ii) Rückwärts aus z pk, (iii)
Fehlerkennzahlen, (iv) Plot p/p
kk -1 gegen k.
• Bestanden,
wenn:
Fehler
innerhalb
numerischer
Rundung;
keine
systematischen Abweichungen pro Block.
4.11 A.11 Typische Beobachtungen
• Invertierbarkeit: p≡
k pk bis zur Sättigungsnähe (zL).
15


## Página 16


• Blockeﬀekte: Spiegelwechsel (sk) sind in y sichtbar, nicht in z; die
Rückwärtsrechnung bleibt stabil.
• Urknallmodus: Rekonstruktion über p=exp
k
(1/Δtk) funktioniert analog; die
Sensitivität verlagert sich auf kleine Δtk.
4.12 A.12 Grenzfälle und Schutz
• Sättigung: Für zk numerisch gleich L ist artanh(zk/L) nicht deﬁniert;
praktischer Schutz: zk/L←min{zk/L,1-ε} mit festem ε.
• Letzter Index: Den letzten, vollständig gesättigten Punkt auslassen oder
mit Mehrpräzision verarbeiten.
4.13 A.13 Tabelle A.1 (Beispielstruktur)
k
pk (Referenz)
pk (aus z)
Rel. Fehler
1
2
⋮
⋮
⋮
⋮
Hinweis: Die Tabelle kann direkt aus einer CSV generiert werden; erforderlich
sind nur die Spalten k, pk, pk, sowie |p/p
kk -1|.
16


## Página 17


5 Zusatz B: Tabellen und numerische Daten
5.1 B.1 Übersicht
Die
folgenden
Tabellen
enthalten
ausgewählte
numerische
Ergebnisse
der
Raumzeit–Helix in unterschiedlichen
Modi. Sie dienen der Überprüfung und
Reproduzierbarkeit der Berechnungen aus dem Haupttext sowie der Veriﬁkation
der Rückwärtsabbildung aus Zusatz~A.
Alle Werte sind direkt aus den Berechnungen entnommen, ohne Glättung oder
Rundungsanpassung, lediglich auf vier Nachkommastellen gekürzt. Parameter für
die hier dargestellten Beispiele: α=1, T=π, a=1, L=5, t0=0, β=0.
5.2 B.2 Vorwärtsberechnung (Normalmodus)
k
pk
xk
yk
zk
10
29
-0.5399
-0.3330
4.9988
11
31
-0.3270
+0.4293
4.9997
12
37
-0.0763
-0.4949
4.9999
13
41
+0.1448
+0.4833
5.0000
14
43
+0.5480
-0.3288
5.0000
15
47
-0.9186
-0.0756
5.0000
16
53
-0.2905
+0.4424
5.0000
17
59
+0.1216
-0.4879
5.0000
18
61
+0.7900
+0.1775
5.0000
19
67
-0.4075
+0.3968
5.0000
20
71
+0.1271
-0.4868
5.0000
Diese Daten stammen aus der direkten Helixberechnung. Die Werte für xk und yk
wechseln periodisch das Vorzeichen und bilden die blockweise Spiegelstruktur; zk
saturiert gegen L=5.
5.3 B.3 Rückwärtsrekonstruktion (Normalmodus)
k
pk (Referenz)
pk (aus zk)
Rel. Fehler
1
2
2.0000
<10-12
2
3
3.0000
<10-12
3
5
5.0000
<10-12
4
7
7.0000
<10-12
5
11
11.0000
<10-12
6
13
13.0000
<10-12
7
17
17.0000
<10-12
8
19
19.0000
<10-12
9
23
23.0000
<10
-12
10
29
29.0000
<10
-12
17


## Página 18


Rückwärtsberechnung
über
tk=L(zk/L)
und
p
=exp
k
(Δtk).
Innerhalb
numerischer
Präzision stimmen die rekonstruierten Werte mit den tatsächlichen Primzahlen
überein.
5.4 B.4 Vergleich mit Yang–Kopplung
Block
Varianz yk ohne γ
Varianz yk mit γ=0.2
0
0.2217
0.1589
1
0.2374
0.1623
2
0.2281
0.1604
3
0.2348
0.1611
Die Varianzwerte zeigen eine deutliche Glättung der Queramplitude, während die
Blockgrenzen
unverändert
bleiben.
Damit
bestätigt
sich
die
stabilisierende
Wirkung der Yang-Kopplung.
5.5 B.5 Hinweise zur Reproduktion
• Tabellen B.2 und B.3 wurden aus den CSV-Dateien helix_coords_k10_20
.csv und reconstruct_first30.csv entnommen.
• Alle Werte stammen aus deterministischer Berechnung ohne Zufall oder
Schätzung.
• Für erweiterte Analysen können die vollständigen Datenreihen (bis k=500
) als CSV-Dateien exportiert und direkt in LaTeX eingebunden werden.
5.6 B.6 Zusammenfassung
• Die Tabellen bestätigen die interne Konsistenz des Modells: Vorwärts
(Prim
→
Helix)
und
Rückwärts
(Helix
→
Prim)
liefern
identische
Ergebnisse.
• Die Yang-Kopplung reduziert lokale Varianz, ohne die Blockstruktur zu
verändern.
• Die Datensätze zeigen, dass die gesamte Primstruktur in der geometrischen
Bahn (xk,yk,zk) vollständig enthalten und rekonstruierbar ist.
18
