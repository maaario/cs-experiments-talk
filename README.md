# EN: Talk on experiments in (computer) science

Some problems in computer science can be solved efficiently, but with large input data 
we might wait forever even with use of an efficient algorithm. For other problems even the best known
exact algorithm might need months, years and multiples of the age of the universe to compute
the solutions even for small instances. The worst problems are those, where we don't even
know how to solve the problem and we can only try our best, e.g. machine translation.
Instead of trying to reach the optimal solution, in these cases we have to be satisfied with 
approaches that can be computed in reasonable time and produce good enough results.
How can experiments in computer science look like? We code multiple solutions, we evaluate them
and we eventually use the best one. See, that was the experiment. In this talk we show how to
easily code and evaluate experiments. It might be easy to compare two programs on one data-set,
but how do you keep your sanity with 10 random heuristics, where each has 10 parameters, needs
to be re-run at least 10 times on 10 different inputs and each computation takes half an hour?

Talk for high-school students interested in CS, with [Trojsten, NGO](https://www.trojsten.org).

# SK: O experimentálnom programovaní

Niektoré informatické úlohy sú síce dobre riešiteľné, ale ak sa ich budeme snažiť riešiť pre 
obrovské vstupy, výsledku sa nemusíme dočkať. Ďalšie úlohy by aj ten najlepší možný algoritmus
počítal mesiace, roky, násobky veku vesmíru..., hoci aj pre vstupy veľkosti 100. Najhoršie sú
ale úlohy, kde ani nevieme, čo máme vlastne programovať a k výsledkom sa vieme dostať
rôznymi spôsobmi – napr. ako spraviť automatický preklad z angličtiny do slovenčiny?
Pre takéto úlohy sa teda miesto 100%-ne najlepšieho riešenia musíme uspokojiť s takým, 
ktoré dokážeme spočítať v rozumnom čase a ktoré je pre nás dostatočne dobré. Ako teda môžu vyzerať 
experimenty v informatike? Naprogramujeme si viacero variánt riešenia, vyhodnotíme ich úspešnosť 
a použijeme to najlepšie. Hľa, experiment. Na prednáške si prakticky ukážeme, ako takéto 
experimenty pekne, rýchlo a jednoducho programovať a vyhodnocovať. Porovnať dva programy môže 
byť ľahké, ale ako sa nezblázniť z toho, ak máme 10 náhodných algoritmov, pričom každému môžeme 
nastaviť 10 parametrov, spustiť ho na 10 rôznych vstupoch a každý výpočet trvá pol hodinu?

Prednáška pre stredoškolákov na [Klube Trojstenu](http://klub.trojsten.sk/), 22.3.2019.

## Contents
Experimental infrastructure, subset sum python, plotting, refactoring, commandline flags, 
sacred, interactive python, pandas.

1. Compare 2 randomized subset sum solvers
2. Repeat evaluations, fix random seeds
3. Plot histograms
4. Separate computation and visualization, two histograms in one plot
5. Solver method with parameter
6. Commandline arguments, data generator, evaluate to folder
7. Reuse argparser to programatically call experiments, comparison by scatterplot
8. Use [sacred](https://github.com/IDSIA/sacred)
9. Use [jupyterlab](https://github.com/jupyterlab/jupyterlab) and [pandas](https://pandas.pydata.org/) for tables and plots
10. Play with parameters of a genetic algoritm

## Setup
```
# Set up virtualenv and install dependencies
python3 -m venv env
. env/bin/activate
cd cs-experiments-talk
pip install -r requirements.txt
```

## Run experiments
```
# Run console version of simple experiment (1-3)
python main.py

# Simple experiment and visualization (4-5)
python main.py
python visualize.py

Generate data (6-10)
python generate_data.py

# Run one experiment (6-7)
python run_experiment.py -method=sol_repeat_random_half -num_repeats=10 -repeat=10 -seed=2

# Run one experiment (8-10)
python run_experiment.py with 'method=sol_repeat_random_half' 'params.num_repeats=10' 'repeat=10'

# Run multiple experiments (7-10)
python main.py

# Run jupyter lab for tables and plots (9-10)
jupyter lab

```