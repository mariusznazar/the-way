# Run brief (Mariusz's instruction for this cycle, verbatim; path backslashes lost in pasting restored)

Przeprowadź jedno zadanie the-way przez cykl implement-task. To jednorazowy przebieg na samym repo the-way, przed
powstaniem gałęzi main. Ustalenia poniżej zastępują te miejsca skilla cyklu, które zakładają produkt z przypiętym
.the-way; resztę skilla wykonuj bez zmian.

Zadanie: <private notes>/Notes\Projects\(P) Proces pracy nad produktem\_zadania\skille_the_way_w_sesjach_na_the_way.md

Wersja procesu. Przebieg idzie według the-way z commita c64a6071384fb57cdb9d7e9db4560ddc43e3b355. Załóż z niego
odłączony worktree tylko do odczytu:
git -C C:\Storage\repos\the-way worktree add --detach C:\Storage\repos\the-way-process c64a6071384fb57cdb9d7e9db4560ddc43e3b355
To jest korzeń procesu. Skill cyklu czytaj z C:\Storage\repos\the-way-process\task-cycle\skill\SKILL.md, a każdy
skill the-way, który on albo jego pliki nazywają, z jego katalogu w tym korzeniu (np.
elements\decisions\skill\SKILL.md, elements\common\critique\SKILL.md, project-level\task\skill\SKILL.md). Nie używaj
skilli the-way zainstalowanych globalnie ani skilli o tych samych nazwach z innych źródeł (refine-task i critique z
vox-ai-tools). Sprawdzenie przypięcia z kroku 2 skilla zastąp sprawdzeniem, że korzeń procesu stoi na tym commicie.
Zmiany, które zadanie wnosi do plików procesu, robisz w worktree zadania; nie zmieniają one reguł tego przebiegu.

Produkt i gałąź. Produktem jest repo C:\Storage\repos\the-way: fundament w foundations/, instrukcje w AGENTS.md i
agent-instructions/README.md. Gałąź docelowa: foundations na commicie c64a6071384fb57cdb9d7e9db4560ddc43e3b355. Gałąź
zadania załóż od niej z --no-track, w osobnym worktree. Sprawdzenia prowadź według agent-instructions/README.md: testy
każdej zmienionej części przez python -B gate/run_tests.py <katalog>, zawsze python -B gate/run_tests.py gate,
strażnicy formatu zmienionych plików fundamentu z --base none i --merge-onto none. Wynik nazywaj tym, czym jest —
częściowymi sprawdzeniami, nigdy przejściem pełnej bramki. Request otwórz jako draft do foundations; scala Mariusz.

Poza repo. Nie zmieniaj niczego poza worktree zadania i worktree procesu. Jedyny wyjątek: w linii tego zadania w
<private notes>/Notes\Projects\(P) Proces pracy nad produktem\_tasks_active.md możesz dopisać link do
requestu. Punkt zadania, który wymaga zmiany poza repo (zdjęcie dowiązań w C:\Users\Mariusz\.claude\skills),
przygotuj jako krok dla człowieka — dokładne polecenia w opisie requestu, do wykonania po scaleniu — i nie wykonuj go.

Zapis przebiegu. Para commitów z zapisem w docs/task-cycles/<slug>/ (dodanie, zaraz po nim usunięcie) zostaje, ale
po parze w drzewie nie może zostać nic w docs/ — WAY-09 nie przewiduje tego katalogu w the-way. Sprawdzenia uruchom
ponownie po commicie usuwającym.

Uwagi o procesie. Każde miejsce, w którym skill cyklu nie pasował do the-way jako produktu, a te ustalenia musiały
go zastąpić, wpisz do "Process remarks on the-way" w zapisie przebiegu, z cytatem kroku skilla. To materiał na
zadanie, które zrobi z tego stały tryb.

Punkt 4 to piąte zderzenie, które wyszło dopiero przy pisaniu polecenia. Cykl kopiuje zapis do docs/task-cycles/, a
WAY-09 nie przewiduje katalogu docs/ w repo the-way. Polecenie radzi sobie z tym tak, że po parze commitów nic tam nie
zostaje.

Punkt 5 sprawia, że ten przebieg zbiera materiał na stały tryb cyklu dla the-way. Opis tamtego zadania można potem
napisać z gotowych uwag, zamiast zgadywać.
