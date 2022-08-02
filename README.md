# lemonde-parite-disparitions

Petite pipeline pour avoir la proportion des genres des personnes apparaissant dans le rubrique [disparitions](https://www.lemonde.fr/disparitions/) de [lemonde.fr](https://lemonde.fr).

Pour l'instant, l'encodage est fait manuellement mais j'ai bien l'idée de faire une extraction d'entité nommée à pas cher et un peu de machine learning pour identifier les genres.


## visualisation

https://observablehq.com/@taniki/lemondefr-parite-disparitions


## données

### `daily_scraping/*.csv`

Archive quotidienne du RSS de la catégorie sous forme de fichiers `csv`.


### `articles.csv`

Liste dédupliquée des articles archivées.


### `people.csv`

Liste dédupliquée des personnes identifiées.