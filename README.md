# computor-v1

Solveur d'équations polynomiales de degré 0, 1 ou 2, écrit en Python (sans dépendance externe).

Le programme prend une équation en argument, la ramène à sa forme réduite `... = 0`, affiche son degré puis ses solutions.

## Fonctionnement

Le traitement se fait en trois étapes, chacune dans son module :

| Étape | Module | Rôle |
|-------|--------|------|
| Parsing | `parser.py` | Vérifie l'équation (un seul `=`, caractères autorisés, pas de puissance négative) puis lit chaque membre terme par terme. Les termes du membre de droite sont soustraits de ceux du membre de gauche, ce qui donne un dictionnaire `{puissance: coefficient}`. |
| Réduction | `polynomial.py` | Supprime les termes de coefficient nul et calcule le degré (plus grande puissance restante, 0 si le polynôme est vide). |
| Résolution | `solver.py` | Résout selon le degré (voir ci-dessous). |

`utils.py` s'occupe de l'affichage de la forme réduite et des traces du mode `--steps`, `main.py` enchaîne les étapes.

Résolution selon le degré :

- **Degré 0** : `Every real number is a solution.` si la constante est nulle, sinon `No solution.`
- **Degré 1** : solution `-b / a`, affichée sous forme de fraction quand c'est possible.
- **Degré 2** : calcul du discriminant `Δ = b² - 4ac`
  - `Δ > 0` : deux solutions réelles ;
  - `Δ = 0` : une solution double ;
  - `Δ < 0` : deux solutions complexes conjuguées.

  Les solutions sont affichées en fraction (dénominateur jusqu'à 1000) si elles tombent juste, sinon en décimal.
- **Degré > 2** : `The polynomial degree is strictly greater than 2, I can't solve.`

## Format de l'équation

Chaque terme doit être écrit sous la forme `a * X^p` :

```
5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
```

- `a` est un nombre (entier ou décimal), éventuellement précédé de `+` ou `-` ;
- `p` est une puissance entière positive ;
- les caractères autorisés sont les chiffres, `+ - * . = X ^`, les espaces et les tabulations.

Une équation vide, sans `=` ou avec plusieurs `=`, contenant d'autres caractères ou une puissance négative provoque un message `Error parsing equation: ...`.

> Attention : seuls les termes de la forme `a * X^p` sont reconnus. Une constante écrite seule (`5`) ou un `X` sans puissance (`X`) est ignoré : il faut écrire `5 * X^0` et `1 * X^1`.

## Utilisation

Prérequis : Python 3 (le script `computor` appelle la commande `python`).

```bash
./computor "équation"
./computor --steps "équation"   # affiche les étapes intermédiaires
```

Sans argument (ou avec un mauvais nombre d'arguments), le programme affiche :

```
Usage: ./computor [--steps] "equation"
```

On peut aussi lancer directement `python3 main.py "équation"`.

### Exemples

Degré 2, discriminant positif :

```
$ ./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4.0 * X^0 + 4.0 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
-0.47513146390886934
0.9052389907905898
```

Degré 1 :

```
$ ./computor "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1.0 * X^0 + 4.0 * X^1 = 0
Polynomial degree: 1
The solution is:
-1/4
```

Degré 2, discriminant négatif (solutions complexes) :

```
$ ./computor "1 * X^0 + 2 * X^1 + 5 * X^2 = 0 * X^0"
Reduced form: 1.0 * X^0 + 2.0 * X^1 + 5.0 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly negative, the two complex solutions are:
-1/5 + 2/5i
-1/5 - 2/5i
```

Degré 3 :

```
$ ./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
Reduced form: 5.0 * X^0 - 6.0 * X^1 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is strictly greater than 2, I can't solve.
```

Mode `--steps` :

```
$ ./computor --steps "1 * X^0 + 2 * X^1 + 5 * X^2 = 0 * X^0"
Initial equation: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0 * X^0
Parsed terms: {0: 1.0, 1: 2.0, 2: 5.0}
After reduction: {0: 1.0, 1: 2.0, 2: 5.0}
Calculated degree: 2
Reduced form: 1.0 * X^0 + 2.0 * X^1 + 5.0 * X^2 = 0
Polynomial degree: 2
[STEP] Coefficients: a=5.0, b=2.0, c=1.0
[STEP] Discriminant = b² - 4ac = 2.0² - 4×5.0×1.0 = -16.0
Discriminant is strictly negative, the two complex solutions are:
[STEP] Real part = -b / 2a = -2.0 / 10.0 = -0.2
[STEP] Imaginary part = √(-Δ) / 2a = √16.0 / 10.0 = 0.4
-1/5 + 2/5i
-1/5 - 2/5i
```

## Tests

Les tests unitaires (`test_computor.py`, module `unittest` de la bibliothèque standard) couvrent le parsing, la réduction et la résolution. Depuis la racine du dépôt :

```bash
python3 -m unittest -v test_computor
# ou
python3 test_computor.py
```

## Structure

```
.
├── computor          # script de lancement (bash)
├── main.py           # point d'entrée : arguments, enchaînement des étapes
├── parser.py         # validation et parsing de l'équation
├── polynomial.py     # réduction et calcul du degré
├── solver.py         # résolution (degrés 0, 1 et 2)
├── utils.py          # affichage et traces du mode --steps
└── test_computor.py  # tests unitaires
```
