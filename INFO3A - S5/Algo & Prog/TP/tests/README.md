### Pré-requis

La suite de tests requiert le paquage Python `pytest`.
Pour l'installer, si nécessaire, on utilise le gestionnaire de paquets `pip` dans une fenêtre de terminal:
```shell
$ pip install pytest
```

L'archive `tests-<version>.zip` contient un seul répertoire `tests/` à déposer à la racine du projet `PyCharm` qui contient tous vos exercices organisés en paquets (`tp1/` pour les exerices du TP1, etc.).


### Contenu du répertoire `tests/`

On se contente de lister les fichiers et dossiers les plus intéressants.

- `conftest.py` : détermine la logique lors de l'exécution des tests. __Ne pas modifier__.
- `setup.py` : définit la progression de tous les TP.
- `tp3/` : contient tous les fichiers dans lesquels sont définies les fonctions de test à exécuter pour le tp3.
- `ongoing/`: contient les fichiers de test encore en cours d'écriture.
- `test_dummy_global.py` : définit un seul test, trivial, qui s'exécute systématiquement, quel que soit le tp en cours.


Chaque fichier de test est préfixé par `test_`. A l'intérieur, on trouve des définitions de fonctions de test également préfixées par `test_`.


### Guide de l'utilisateur

La commande `pytest` s'exécute comme un module Python :
```shell
$ python -m pytest
```

La commande `pytest` admet un nombre d'options considérable, que l'on peut consulter dans l'aide:
```shell
$ python -m pytest -h
```

Pour les TP d'Algorithmique et structures de données_, nous avons défini une logique d'exécution particulière.
Il faut spécifier :
 - un répertoire de test, correspondant à un tp comme par exemple `tests/tp3` ou `tests/tp5` ;
 - une _clé_ correspondant à l'exercice et la question dont vous souhaitez tester les fonctions, comme par exemple `e5q3` pour désigner la question 3 de l'exercice 5. 

 Il est important de noter que **tous les tests du début du TP jusqu'à la question courante seront exécutés**.

Finalement, une exécution standard prend la forme suivante :
```shell
$ python -m pytest tests/tp3 --key=e4q2
```
pour évaluer tous les tests du TP3 jusqu'à la question 2 de l'exercice 4 incluse.


#### Les variantes


Pour lancer tous les tests présents dans l'arborescence de `tests/` :
```shell
$ python -m pytest
```

Il est également possible d'exécuter une suite de tests indépendante de tout TP à l'aide de la clé `global` :
```shell
$ python -m pytest --key=global
```

L'ensemble des tests définis pour un TP en particulier, par exemple le TP3, peut être exécuté simplement par :
```shell
$ python -m pytest tests/tp3
```
sans spécifier de clé.


#### Pour ajouter ses propres tests

Il suffit de créer un fichier `Python` dans l'arborescence de `tests/` dont le nom commence par `test_`, puis d'y définir une ou plusieurs fonction(s) de test (dont le nom commence par `test_`) comme sur l'exemple suivant :
```python
# contenu du fichier tests/test_mes_tests_a_moi_perso.py
import pytest

@pytest.mark.key('global')
def test_f():
	assert 4 + 3 == 7

@pytest.mark.key('global')
def test_g():
	a = [1 , 2, 3]
	assert len(a) == 3 and a[0] == 1
```

Le marquage à l'aide de l'annotation de clé  `key('global')` en tête de chaque fonction est nécessaire, selon la logique que nous avons définie pour les tests des TP.

Si vous souhaitez que vos fonctions de test soient évaluées uniquement avec un énoncé de TP particulier, il est nécessaire de placer le fichier de test dans le répertoire correspondant (`tests/tp<n>`).


### Pour les étudiants pressés

Pour commencer à jouer avec les tests:

```shell
$ pip install pytest
$ python -m pytest tests/tp3 --key=e4q3
```

À chaque exécution des tests (commande `pytest`), il faut spécifier le tp (`tests/tp3`) et la question en cours (`--key=e5q2`). 


### Pour aller plus loin

La documentation officielle de [pytest](https://docs.pytest.org/).
