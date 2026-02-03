# Prime System

*Convertido de: Prime System.docx*

---


<!doctype html>


<html lang="de">


<head>


<meta charset="utf-8" />


<title>Prim‑System (Generator + Index-Arithmetik)</title>


<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">


<style>


:root{--bg:#0b1120;--fg:#e2e8f0;--muted:#94a3b8;--panel:#0f172a;--line:#334155;--ok:#22c55e;--warn:#f59e0b;--err:#ef4444}


html,body{margin:0;height:100%;background:var(--bg);color:var(--fg);font:15px system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif}


.wrap{max-width:960px;margin:0 auto;padding:14px}


h1{font-size:20px;margin:6px 0 12px}


.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px;margin-bottom:12px;box-shadow:0 1px 0 #0004}


.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}


input[type=text]{flex:1;min-width:140px;padding:10px;border-radius:10px;border:1px solid var(--line);background:#0b1222;color:var(--fg);font:16px ui-monospace,Menlo,Consolas,monospace}


select{padding:10px;border-radius:10px;border:1px solid var(--line);background:#0b1222;color:var(--fg)}


.btn{appearance:none;border:0;background:#1f2937;color:var(--fg);padding:10px 12px;border-radius:10px;cursor:pointer;font-weight:600}


.btn:disabled{opacity:.5;cursor:not-allowed}


.pill{display:inline-block;padding:2px 8px;border-radius:999px;background:#0b1222;border:1px solid var(--line);font-size:12px;color:var(--muted)}


.mono{font:14px ui-monospace,Menlo,Consolas,monospace;word-break:break-all}


.hint{font-size:12px;color:var(--muted)}


.ok{color:var(--ok)} .warn{color:var(--warn)} .err{color:var(--err)}


.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px}


.sp{height:6px}


.log{font:14px ui-monospace,Menlo,Consolas,monospace;white-space:pre-wrap;word-break:break-word; max-height: 200px; overflow-y: auto; background:#0b1222; border:1px solid var(--line); border-radius: 8px; padding: 8px;}


.pval{color:var(--ok);font-weight:700}


.dbl{color:var(--warn);font-weight:700}


.newq{color:var(--info);font-weight:700}


</style>


</head>


<body>


<div class="wrap">


<h1>Prim‑System Rechner <span class="pill">Generator · Index‑Arithmetik · kein Sieb</span></h1>


<div class="card">


<div class="hint">Eingabe als Primwert <b>p</b> (z.B. 5) oder Index <b>p[n]</b> (z.B. p[3]=5). Funktionen wie n(A) oder p[n] können langsam sein, da der Generator sequentiell läuft.</div>


<div class="sp"></div>


<div class="row">


<input id="a" type="text" placeholder="A (z.B. 5 oder p[3])">


<input id="b" type="text" placeholder="B (optional, z.B. 7 oder p[4])">


<button class="btn" id="normalize">Normalisieren</button>


</div>


<div class="sp"></div>


<div class="grid">


<button class="btn" id="isPrime">Ist A prim?</button>


<button class="btn" id="prev">vorherige Primzahl</button>


<button class="btn" id="next">nächste Primzahl</button>


<button class="btn" id="index">Index n(A)</button>


<button class="btn" id="nth">p[n] aus n</button>


</div>


<div class="sp"></div>


<div class="grid">


<button class="btn" id="add">A ⊕ B</button>


<button class="btn" id="sub">A ⊖ B</button>


<button class="btn" id="mul">A ⊗ B</button>


<button class="btn" id="div">A ⊘ B</button>


<button class="btn" id="pow">A ^ k</button>


<input id="k" type="text" placeholder="k (z.B. 5)">


</div>


<div class="sp"></div>


<div id="out" class="mono"></div>


</div>


<div class="card">


<b>Generator Steuerung</b>


<div class="row">


<span class="pill">Δ-Wort: (4,2,4,2,4,6,2,6)</span>


<span class="pill">Start: 7 (j=0)</span>


<label>Schritte/Tick <input id="steps" value="20" style="width:5ch" /></label>


<button class="btn" id="step">Step</button>


<button class="btn" id="run">Run</button>


<button class="btn" id="stop" disabled>Stop</button>


<button class="btn" id="reset">Reset</button>


</div>


<div class="sp"></div>


<div class="row" style="gap:16px">


<span>n: <b id="nNow">–</b></span>


<span class="pill">j: <span id="jNow">–</span></span>


<span class="pill">Δ: <span id="dNow">–</span></span>


<span class="pill">k: <span id="kNow">0</span></span>


<span class="pill">Trigger: <span id="trNow">–</span></span>


<span class="pill">aktive q: <span id="qsNow">–</span></span>


<span class="pill">gelernt: <span id="learnNow">0</span></span>


</div>


<div class="sp"></div>


<div id="log" class="log">Generator Log...</div>


</div>


</div>


<script>


(function(){ // Start IIFE


// ---------- Helpers ----------


const $ = (id)=>document.getElementById(id);


const out = $("out"), logOut = $("log");


function show(where, html){ where.innerHTML = html; }


function ok(s){ return '<span class="ok">'+s+'</span>'; }


function warn(s){ return '<span class="warn">'+s+'</span>'; }


function err(s){ return '<span class="err">'+s+'</span>'; }


function toLocale(bi){ const s=bi.toString(); return s.replace(/\B(?=(\d{3})+(?!\d))/g,"."); }


function parseBigInt(text){


if (!text) throw new Error("leer");


let s = text.trim().toLowerCase().replaceAll('_','').replaceAll(' ','').replaceAll('.',''); // Punkte für Tausender entfernen


s = s.replace(/^(\d+)\^(\d+)$/, (_,a,b)=> (BigInt(a) ** BigInt(b)).toString());


if (/^[+-]?\d+(\.\d+)?e[+-]?\d+$/i.test(s)){


let [mant,exp] = s.split('e'); exp=parseInt(exp,10);


if (mant.includes(',')){ mant = mant.replace(',','.'); } // Komma zu Punkt für JS


if (mant.includes('.')){ const [i,f]=mant.split('.'); exp -= f.length; mant = i+f; }


if (exp>=0) return BigInt(mant) * (10n ** BigInt(exp));


const denom = 10n ** BigInt(-exp); return BigInt(mant)/denom;


}


s = s.replace(/10\^(\d+)/g, (_,e)=> '1'+'0'.repeat(parseInt(e,10)));


if (!/^[+-]?\d+$/.test(s)) throw new Error("Ungültiges Format für BigInt");


return BigInt(s);


}


function parsePrim(text){


const t = text.trim();


const m = t.match(/^p\[(\d+)\]$/i);


if (m){ const n = BigInt(m[1]); if (n<1n) throw new Error("Index n muss >= 1 sein"); return {type:'index', n}; }


const v = parseBigInt(t);


return {type:'value', v};


}


// ---------- Generator Core (Schnell & Sicher) ----------


const G = [4,2,4,2,4,6,2,6];


let n_gen, j_gen, k_gen, timer_gen=null;


const MASKS = new Map();


let learned_gen = 0;


let lastPrime = 5n;


const elN=$("nNow"), elJ=$("jNow"), elD=$("dNow"), elK=$("kNow"), elTr=$("trNow"),


elQs=$("qsNow"), elLearn=$("learnNow");


const stepsInp=$("steps"), runBtn=$("run"), stopBtn=$("stop"), stepBtn=$("step"), resetBtn=$("reset");


// Helper für BigInt GCD (Euclidean algorithm)


function gcdBI(a, b) {


a = a > 0n ? a : -a;


b = b > 0n ? b : -b;


while (b) {


let t = b;


b = a % b;


a = t;


}


return a;


}


function lcmBI(a, b){


if (a === 0n || b === 0n) return 0n;


return (a * b) / gcdBI(a, b);


}


function lcmOfBI(arr){ return arr.length ? arr.reduce((x, y) => lcmBI(x, y)) : 0n; }


function listQs(){ return Array.from(MASKS.keys()).sort((a,b)=>a-b).join(",") || "–"; }


function paintGenerator(dShown=null, trig="–"){


if (elN) elN.textContent = toLocale(n_gen); // Formatierte Ausgabe


if (elJ) elJ.textContent = String(j_gen);


if (elD) elD.textContent = dShown==null ? "–" : String(dShown);


if (elK) elK.textContent = String(k_gen);


if (elTr) elTr.textContent = trig;


if (elQs) elQs.textContent = listQs();


if (elLearn) elLearn.textContent = String(learned_gen);


}


// Modulare Tools


function modPow(base, exp, mod){


let res = 1n; base %= mod;


while (exp > 0n){


if (exp & 1n) res = (res * base) % mod;


base = (base * base) % mod;


exp >>= 1n;


}


return res;


}


function modInverse(a, m){


// Sicherstellen, dass m ein BigInt ist


const modBigInt = BigInt(m);


// Kleiner Satz von Fermat: a^(m-2) mod m, wenn m prim


// Da q prim > 5 ist, gilt gcd(30, q)=1


return modPow(a, modBigInt - 2n, modBigInt);


}


// Schneller Maskenbau


function buildMask(q){


const period = 8 * q;


const qn = BigInt(q);


const G_BIG = [4n,2n,4n,2n,4n,6n,2n,6n];


const REST_SUM = [0n];


let s=0n; for(let i=0;i<7;i++){ s+=G_BIG[i]; REST_SUM.push(s); }


const inv30 = modInverse(30n, qn);


const ones = [];


for (let jj=0; jj<8; jj++){


let b = -(7n + REST_SUM[jj]) % qn; if (b<0) b+=qn;


const m = (b * inv30) % qn;


const k = m * 8n + BigInt(jj);


ones.push(Number(k));


}


ones.sort((a,b)=>a-b);


const onesSet = new Set(ones);


return { period, ones, onesSet, m:0, q };


}


// Lernregel + Sync


function maybeActivate(nCandidate){


if (nCandidate < 7n) return;


const q = Number(nCandidate);


if (MASKS.has(q)) return;


if (q % 2 === 0 || q % 3 === 0 || q % 5 === 0) return; // Guard


try {


const spec = buildMask(q);


spec.m = (k_gen - 1 + spec.period) % spec.period; // Sync auf Takt, wo wir landeten


// spec.m muss positiv sein - ist durch Modulo oben sichergestellt, aber doppelt checken:


if (spec.m < 0) spec.m += spec.period;


MASKS.set(q, spec);


learned_gen++;


if (logOut) logOut.innerHTML = `<span class="newq">+ Aktiviert q=${q}</span>\n` + logOut.innerHTML;


} catch (e) {


// Fehler beim modInverse, wenn q keine Primzahl ist (sollte nicht passieren)


console.error(`Fehler beim Aktivieren von q=${q}: ${e.message}`);


if (logOut) logOut.innerHTML = `<span class="err">! Fehler Aktivierung q=${q}</span>\n` + logOut.innerHTML;


}


}


// Triggerprüfung E2


function triggeredNext(){


const hits = [];


for (const [q, spec] of MASKS){


let mNext = spec.m + 1;


if (mNext >= spec.period) mNext -= spec.period; // Zyklisch


if (spec.onesSet.has(mNext)) hits.push(q);


}


return hits;


}


// Zeigerfortschritt


function advancePointers(stepCount){


k_gen += stepCount; // Globalen Zähler ZUERST erhöhen


for (const spec of MASKS.values()){


// Lokal-Modulo für jeden Zeiger m


spec.m = (spec.m + stepCount) % spec.period;


}


}


// 1 Schritt (Save Logik)


function stepOnce(log=true){


const d = G[j_gen];


const hits = triggeredNext();


let stepType = 'prime'; // Standard: normaler Schritt


if (hits.length){


const d2 = G[(j_gen+1)&7];


const landed = n_gen + BigInt(d + d2);


if (log && logOut) logOut.innerHTML = `${toLocale(n_gen)} +Δ=${d},+Δ=${d2} ⇒ <span class="dbl">⇉ ${toLocale(landed)}</span> [E2 q=${hits.join('/')}]\n` + logOut.innerHTML;


lastPrime = n_gen;


n_gen = landed;


j_gen = (j_gen + 2) & 7;


advancePointers(2);


if (log) paintGenerator(d + d2, `E2 q=${hits.join('/')}`);


stepType = 'jump';


} else {


const nextCand = n_gen + BigInt(d);


if (log && logOut) logOut.innerHTML = `${toLocale(n_gen)} +Δ=${d} → <span class="pval">${toLocale(nextCand)}</span>\n` + logOut.innerHTML;


lastPrime = n_gen;


n_gen = nextCand;


j_gen = (j_gen + 1) & 7;


advancePointers(1);


// Lerne erst, NACHDEM der Zustand (n_gen, k_gen) aktualisiert ist


maybeActivate(nextCand);


if (log) paintGenerator(d, "–");


}


// Stelle sicher, dass der Log nicht zu groß wird


if (log && logOut.children.length > 200) {


logOut.removeChild(logOut.lastChild);


logOut.removeChild(logOut.lastChild); // Remove newline too if needed


}


return { p: n_gen, type: stepType };


}


function runGeneratorSteps(count){ for (let i=0; i<count; i++){ stepOnce(true); } }


function startGenRun(){


if (timer_gen) return;


runBtn.disabled = true; stopBtn.disabled = false; stepBtn.disabled = true;


timer_gen = setInterval(()=>{


const cnt = Math.max(1, parseInt(stepsInp.value||"10"),10);


runGeneratorSteps(cnt);


}, 30);


}


function stopGenRun(){


if (!timer_gen) return;


clearInterval(timer_gen); timer_gen=null;


runBtn.disabled = false; stopBtn.disabled = true; stepBtn.disabled = false;


}


function initGenerator(){


stopGenRun(); // Sicherstellen, dass kein Timer läuft


if (logOut) logOut.textContent = "5  +Δ=2  →  7  | bootstrap\n";


n_gen = 7n; j_gen = 0; k_gen = 0; learned_gen = 0; lastPrime = 5n;


MASKS.clear();


for (const q of [7,11,13]){


try {


const spec = buildMask(q);


// Korrekte Initialsynchronisierung: Zeiger m ist auf dem Takt VOR dem Start (k=0)


spec.m = (k_gen - 1 + spec.period) % spec.period;


MASKS.set(q, spec);


learned_gen++;


} catch (e) {


console.error(`Fehler Init q=${q}: ${e.message}`);


}


}


paintGenerator();


}


runBtn.onclick = startGenRun;


stopBtn.onclick = stopGenRun;


stepBtn.onclick = ()=> runGeneratorSteps(Math.max(1, parseInt(stepsInp.value||"1"),10));


resetBtn.onclick = ()=>{ stopGenRun(); initGenerator(); };


// ---------- Arithmetik & Suchfunktionen (nutzen jetzt den Generator) ----------


// isPrime: Wheel-basierte Trial Division (Wheel 30)


function isPrimeWheel(p){


if (p<2n) return false;


// Handle small primes explicitly


if (p === 2n || p === 3n || p === 5n || p === 7n) return true;


if (p % 2n === 0n || p % 3n === 0n || p % 5n === 0n || p % 7n === 0n) return false;


const limit = sqrtBI(p);


// Start checking from 11 (first prime > 7 not multiple of 2,3,5)


let d = 11n;


// Wheel 30 gaps sequence starting AFTER 11: 2, 4, 2, 4, 6, 2, 6, (4->wrap)


const GAPS = [2n, 4n, 2n, 4n, 6n, 2n, 6n, 4n]; // Gaps addiert zu d


let idx = 0;


while (d <= limit){


if (p % d === 0n) return false;


d += GAPS[idx];


idx = (idx + 1) % 8; // Cycle through the 8 gaps


}


return true;


}


function sqrtBI(n){


if (n<0n) throw new Error("sqrt von negativer Zahl nicht erlaubt");


if (n<2n) return n;


let x = n;


// Wähle Startwert genauer, z.B. basierend auf Bitlänge


const bitLength = BigInt(n.toString(2).length);


if (bitLength > 10n) { // Heuristik


x = 1n << (bitLength / 2n + 1n);


}


let y = (x + n/x) >> 1n;


while (y < x){ x = y; y = (x + n/x) >> 1n; }


return x;


}


// nextPrime(p): Nutzt den Generator


function nextPrimeGen(p){


if (p < 2n) return 2n;


if (p === 2n) return 3n;


if (p === 3n) return 5n;


if (p === 5n) return 7n;


// Sichert den aktuellen Generator-Zustand


let saved_n = n_gen, saved_j = j_gen, saved_k = k_gen;


let saved_masks_m = new Map();


for (const [q, spec] of MASKS) { saved_masks_m.set(q, spec.m); }


// Reset oder laufe weiter bis p erreicht ist (ohne log)


if (n_gen < p || n_gen > p + 10000n) { // Erweiterte Heuristik für Reset


initGenerator(); // Nutzt globalen Generator-Zustand


while (n_gen <= p) { if(stepOnce(false).type === 'stop') throw new Error("Generator stop"); }


} else {


while (n_gen <= p) { if(stepOnce(false).type === 'stop') throw new Error("Generator stop"); }


}


let result_p = n_gen; // Startwert für die Suche nach der nächsten Primzahl > p


// Wenn der Generator genau auf p steht oder drüber ist


if (result_p <= p) {


// Mache Schritte, bis eine *Primzahl* gefunden wird


let result;


do {


result = stepOnce(false);


} while (result.type === 'jump' || result.p <= p);


result_p = result.p;


}


// Stelle den alten Generator-Zustand wieder her


n_gen = saved_n; j_gen = saved_j; k_gen = saved_k;


for (const [q, spec] of MASKS) { if(saved_masks_m.has(q)) spec.m = saved_masks_m.get(q); }


// paintGenerator(); // Optional: UI updaten


return result_p;


}


// prevPrime(p): Nutzt den Generator von vorne. Langsam.


function prevPrimeGen(p){


if (p <= 2n) return 0n; // Keine Primzahl vor 2


if (p === 3n) return 2n;


if (p === 5n) return 3n;


if (p === 7n) return 5n;


// Sichert den aktuellen Generator-Zustand


let saved_n = n_gen, saved_j = j_gen, saved_k = k_gen;


let saved_masks_m = new Map();


for (const [q, spec] of MASKS) { saved_masks_m.set(q, spec.m); }


initGenerator(); // Startet den globalen Generator neu


let prevP = 5n; // Der letzte bekannte vor dem Start des Generators bei 7


let currentP = 7n;


while(currentP < p){


let result = stepOnce(false);


if (result.type === 'prime') {


prevP = currentP; // Update prevP only when a prime step occurred


currentP = result.p;


} else {


currentP = result.p; // Jump step, currentP moves, prevP stays


}


if (currentP >= p) break;


if (k_gen > 4000000) throw new Error("prevPrime Suche zu lang (>4M Schritte)"); // Sicherheitslimit


}


// Stelle den alten Generator-Zustand wieder her


n_gen = saved_n; j_gen = saved_j; k_gen = saved_k;


for (const [q, spec] of MASKS) { if(saved_masks_m.has(q)) spec.m = saved_masks_m.get(q); }


// paintGenerator(); // Optional: UI updaten


return prevP; // prevP hält die letzte Primzahl *vor* Erreichen von p


}


// nthPrime(n): Nutzt Generator von vorne. Langsam.


function nthPrimeGen(n_idx){


if (n_idx < 1n) throw new Error("Index muss >= 1 sein");


// Sichert den aktuellen Generator-Zustand


let saved_n = n_gen, saved_j = j_gen, saved_k = k_gen;


let saved_masks_m = new Map();


for (const [q, spec] of MASKS) { saved_masks_m.set(q, spec.m); }


initGenerator(); // Startet den globalen Generator neu


let count = 0n;


const initialPrimes = [2n, 3n, 5n];


if (n_idx <= 3n) {


// Stelle alten Zustand wieder her


n_gen = saved_n; j_gen = saved_j; k_gen = saved_k;


for (const [q, spec] of MASKS) { if(saved_masks_m.has(q)) spec.m = saved_masks_m.get(q); }


// paintGenerator();


return initialPrimes[Number(n_idx)-1];


}


count = 3n; // Zähle 2, 3, 5


// Generator startet bei n=7 (p[4])


let current_p = n_gen;


while (count < n_idx){


let result = stepOnce(false);


if (result.type === 'prime'){


count++;


current_p = result.p; // Update current prime only on prime steps


} else {


current_p = result.p; // Update position even on jump


}


if (count >= n_idx) break; // Early exit if target index reached


if (k_gen > 4000000) throw new Error("nthPrime Suche zu lang (>4M Schritte)"); // Sicherheitslimit


}


// Stelle den alten Generator-Zustand wieder her


n_gen = saved_n; j_gen = saved_j; k_gen = saved_k;


for (const [q, spec] of MASKS) { if(saved_masks_m.has(q)) spec.m = saved_masks_m.get(q); }


// paintGenerator(); // Optional: UI updaten


return current_p; // Return the prime found at the target index


}


// primeIndex(p): Nutzt Generator von vorne. Langsam.


function primeIndexGen(p_val){


// Schneller Vorabcheck


if (!isPrimeWheel(p_val)) throw new Error(`Die Zahl ${toLocale(p_val)} ist keine Primzahl (Wheel Test)`);


// Sichert den aktuellen Generator-Zustand


let saved_n = n_gen, saved_j = j_gen, saved_k = k_gen;


let saved_masks_m = new Map();


for (const [q, spec] of MASKS) { saved_masks_m.set(q, spec.m); }


initGenerator(); // Startet den globalen Generator neu


let count = 0n;


const initialPrimes = [2n, 3n, 5n];


for (let i = 0; i < initialPrimes.length; i++) {


if (p_val === initialPrimes[i]) {


// Stelle alten Zustand wieder her


n_gen = saved_n; j_gen = saved_j; k_gen = saved_k;


for (const [q, spec] of MASKS) { if(saved_masks_m.has(q)) spec.m = saved_masks_m.get(q); }


// paintGenerator();


return BigInt(i + 1);


}


count++; // Zähle die ersten drei


}


count = 3n; // Index für 5


// Generator startet bei n=7 (p[4])


while(n_gen < p_val){


let result = stepOnce(false);


// Zähle nur echte Primschritte


if (result.type === 'prime') {


count++;


}


if (n_gen >= p_val) break; // Exit if we reached or passed p_val


if (k_gen > 4000000) throw new Error("primeIndex Suche zu lang (>4M Schritte)"); // Sicherheitslimit


}


let final_count = (n_gen === p_val) ? count : -1n; // If we landed exactly, count is correct


// Stelle den alten Generator-Zustand wieder her


n_gen = saved_n; j_gen = saved_j; k_gen = saved_k;


for (const [q, spec] of MASKS) { if(saved_masks_m.has(q)) spec.m = saved_masks_m.get(q); }


// paintGenerator(); // Optional: UI updaten


if (final_count !== -1n) return final_count;


throw new Error("Generatorfehler oder Zahl nicht gefunden (sollte nicht passieren)");


}


// Hilfsfunktion: Bekomme {p,n} aus Input


function ensurePrimeValueGen(obj){


if (obj.type==='index'){


const n=obj.n;


if (n > 2000000n) throw new Error("Index > 2 Mio - zu langsam für Browser"); // Grenze für nthPrimeGen


const p=nthPrimeGen(n);


return {p,n};


} else {


const p=obj.v;


if (p > 30000000n) throw new Error("Wert > 30 Mio - Indexsuche zu langsam"); // Grenze für primeIndexGen


const n=primeIndexGen(p);


return {p,n};


}


}


// UI Wiring


$("normalize").onclick = ()=>{


try{ const A = $("a").value.trim(); const B = $("b").value.trim(); if (A){ const pa=parsePrim(A); $("a").value = (pa.type==='index')? `p[${pa.n}]` : pa.v.toString(); } if (B){ const pb=parsePrim(B); $("b").value = (pb.type==='index')? `p[${pb.n}]` : pb.v.toString(); } show(out, ok("OK: normalisiert.")); }catch(e){ show(out, err(e.message)); }


};


$("isPrime").onclick = ()=>{


try{ const A = parsePrim($("a").value); const va = (A.type==='index')? nthPrimeGen(A.n) : A.v; const res = isPrimeWheel(va); show(out, `${(A.type==='index')?`p[${A.n}]`:toLocale(va)} ist ${res? ok("prim") : err("nicht prim")} (Wheel-Div).`); }catch(e){ show(out, err(e.message)); }


};


$("prev").onclick = ()=>{


try{ const A = parsePrim($("a").value); const {p,n} = ensurePrimeValueGen(A); if (n<=1n) { show(out, warn("unter 2 gibt es keine vorherige Primzahl.")); return; } const r = prevPrimeGen(p); $("a").value = r.toString(); const rn = (r===0n) ? 0n : primeIndexGen(r); show(out, `prev(p[${n}]=${toLocale(p)}) → p[${rn}]=<b>${toLocale(r)}</b>`); }catch(e){ show(out, err(e.message)); }


};


$("next").onclick = ()=>{


try{ const A = parsePrim($("a").value); const {p,n} = ensurePrimeValueGen(A); const r = nextPrimeGen(p); $("a").value = r.toString(); const rn = primeIndexGen(r); show(out, `next(p[${n}]=${toLocale(p)}) → p[${rn}]=<b>${toLocale(r)}</b>`); }catch(e){ show(out, err(e.message)); }


};


$("index").onclick = ()=>{


try{ const A = parsePrim($("a").value); const {p,n} = ensurePrimeValueGen(A); show(out, `Index n(${toLocale(p)}) = <b>${n}</b>`); }catch(e){ show(out, err(e.message)); }


};


$("nth").onclick = ()=>{


try{ const txt = $("b").value || $("a").value; if (!txt) throw new Error("n fehlt"); const X = parsePrim(txt); const n = (X.type==='index')? X.n : parseBigInt(txt); const r = nthPrimeGen(n); $("a").value = r.toString(); show(out, `p[${n}] = <b>${toLocale(r)}</b>`); }catch(e){ show(out, err(e.message)); }


};


function binOp(opName, combiner){


try{ const A = ensurePrimeValueGen(parsePrim($("a").value)); const B = ensurePrimeValueGen(parsePrim($("b").value)); const n = combiner(A.n, B.n); const n2 = (n<1n?1n:n); const r = nthPrimeGen(n2); $("a").value = r.toString(); show(out, `${opName}: p[${A.n}]=${toLocale(A.p)} & p[${B.n}]=${toLocale(B.p)} → p[${n2}] = <b>${toLocale(r)}</b>`); }catch(e){ show(out, err(e.message)); }


}


$("add").onclick = ()=> binOp("⊕", (na,nb)=> na+nb);


$("sub").onclick = ()=> binOp("⊖", (na,nb)=> na-nb);


$("mul").onclick = ()=> binOp("⊗", (na,nb)=> na*nb);


$("div").onclick = ()=> binOp("⊘", (na,nb)=> (nb===0n?1n:na/nb)); // Floor division


$("pow").onclick = ()=>{


try{ const A = ensurePrimeValueGen(parsePrim($("a").value)); const k = parseBigInt(($("k").value||"").trim()); if (k<0n) throw new Error("k ≥ 0");


// BigInt exponentiation by squaring


let base=A.n; let exp=k; let res=1n;


if (base === 0n && exp === 0n) res = 1n; // Convention 0^0 = 1 for index


else if (base === 0n && exp > 0n) res = 0n;


else {


while (exp>0n){


if (exp & 1n) res=res*base;


base=base*base;


exp >>= 1n;


}


}


const n2=(res<1n?1n:res); // Ensure index is at least 1


const r = nthPrimeGen(n2);


$("a").value = r.toString();


show(out, `Index‑Potenz: (n=${A.n})^${k} → p[${n2}] = <b>${toLocale(r)}</b>`);


}catch(e){ show(out, err(e.message)); }


};


// ---------- Start ----------


initGenerator();


})(); // End IIFE


</script>


</body>


</html>
