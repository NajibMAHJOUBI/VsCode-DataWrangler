# Visual Studio Code : Transformer ses données avec Data Wrangler



## Prérequis
- Visual Studio Code avec les packs d'extensions Python et Jupyter
- Python avec les librairies Pandas et Jupyter

Pour l'installation d'environnement virtuel Conda dédié, vous pouvez vous référer à cet article : [Article sur le sujet]

## Installer l'extension Data Wrangler
Data Wrangler est une extension vérifiée par [microsoft.com](http://microsoft.com/) disponible depuis la marketplace des extensions VS Code. Pour l'installer l'extension, suivre les étapes suivantes : 

1. Sélectionner le menu **Extensions**
2. Depuis la barre de recherche, taper le nom de l'extension : Data Wrangler
3. Parmi les extensions proposées, choisir Data Wrangler et cliquer sur **Install**

![Installation de l'extension Data Wrangler](images/Extension%20Install%2000.png)


L'extension *Data Wrangler* dépend des extensions Python et Jupyter pour VS Code. Si elles ne sont pas présentent, il vous sera proposer de les installer : 

1. Cliquer sur **Oui** si les extensions suggérées doivent être installées pour que *Data Wrangler* puisse fonctionner correctement

![[Optionnel] Installation des extensions Python et Jupyter](images/Extension%20Install%2001.png)

Après ces installations, vous pouvez vérifier depuis le menu Extensions, l'installation des extensions qui viennent d'être faites : 

1. Depuis le menu **Extension**, nettoyer le champ de recherche d'extension
2. Déployer le volet des extensions installées (**Installed**). On peut voir qu'en plus de l'extension *Data Wrangler*, nous retrouvons les pack d'extensions pour l'utilisation de *Python* et de *Jupyter* dans *VS Code*. 

![Vérifier l'installation des extensions : Data Wrangler, Python et Jupyter](images/Extension%20Install%2002.png)
 
## Scénario

Nous allons utiliser un jeu de données des prix pratiqués pour les locations de type AirnBnB. Nous souhaitons calculer le prix moyen des locations de chambre privée dans la ville de Montréal par quartier. Les prix doivent être arrondis à deux chiffres après la virgule et classés par prix moyen décroissant.

## Fonctionnalités principales de Data Wrangler

Le scénario proposé va nous permettre d'explorer et présenter différentes fonctionnalités de l'extension Data Wrangler. L'ensemble des ressources présentées dans cette article sont mis à dispositions dans ce répo GitHub dont le fichier de données utilisé dans cet exemple.

### Chargement du jeu de données
La première étape pour l'utilisation de Data Wrangler est de charger un fichier de données. Pour cela, suivre les étapes suivantes : 

1. Depuis la fenêtre **Explorer de fichier** de Vs Code
2. Sélectionner et cliquer droit sur le fichier [airbnb-canada.csv](data/airbnb-canada.csv)
3. Dans le menu, choisir l'option **Open in Data Wrangler**

![Ouverture de fichier dans Data Wrangler](images/Open%20in%20Data%20Wrangler.png)


Après l'ouverture de Data Wrangler, vous aurez un aperçu avec les options suivantes :

1. Dans la fenêtre d'**Operations**, il sera proposer les différentes options pour les opérations à construire. Dans cet exemple, modifier le champ **Delimiter** par ";" (point-virgule) et cliquer sur le bouton **Apply** : séparateur utilisée dans le fichier [airbnb-canada.csv](data/airbnb-canada.csv).

2. Dans la fenêtre **Data Summary**, vous aurez des statistiques sur les données (nombre de lignes, nombre de colonnes, ...).

3. L'aperçu des données permet de visualiser les données après chargement mais également au fur et à mesure de l'application de transformations sur les données.

4. Lorsque une transformation est réalisée via le menu **Operations**, Data Wrangler propose automatiquement le code Pandas reproduisant les opérations réalisées dans l'interface en no-code. Une fois que vous validez une transformation, cliquer sur le bouton **Apply** pour la définir comme une étape des transformations à maintenir.

![Aperçu de l'interface Data Wrangler](images/Load%20Data.png)


### Transformer des données sans code

- Pour illustrer ce point, nous proposons de sélectionner les colonnes suivantes : [**Neighbourhood, Accommodation type, Room price per night, Location**]

Après avoir chargé les données dans l'étape précédente, la suppression des colonnes peut se faire de la façon suivante : 

1. Depuis l'encart **Operations**, déplier le menu **Schema**. Cela donne l'ensemble des opérations disponibles depuis ce menu

2. Cliquer sur l'option **Drop columns**

![Sélection du menu pour supprimer des colonnes](images/Drop%20Columns%2000.png)

Le menu **Drop columns** propose alors les différentes options pour réaliser cette transformation :

1. Courte description de l'opération choisie. Ici **Drop columns - Removes the targeted columns from the data frame**.

2. Depuis le champ **Target columns**, dérouler le menu pour sélectionner les colonnes à supprimer et ainsi conserver les colonnes cibles uniquement

3. Cliquer sur le bouton **Apply** pour appliquer l'opération de suppression des colonnes

![Sélection des colonnes à supprimer](images/Drop%20Columns%2000.png)


- Transformer par l'exemple une colonne de type String 

Nous souhaitons récupérer le nom de la ville depuis la colonne Location suivant l'exemple : **Canada, Quebec city => Quebec city**. Pour cela commençons par sélectionner l'option de transformation par l'exemple : 

1. Après avoir appliquer les opérations précédentes (suppression de colonnes), l'encart d'aperçu des données donne un aperçu des données après application des transformations

2. Depuis le menu **Operations**, déplier le menu **Format**. 

3. Choisir l'option **String transform by example**


![Sélection du menu de transformation par l'exemple](images/String%20Transform%2000.png)

La mise en place d'une transformation par l'exemple peut être faite de la manière suivante : 

1. Depuis le champ **Columns to derive from**, sélectionner le ou les colonnes à partir desquelles nous souhaitons réaliser une transformation. Dans notre exemple, sélectionner la colonne *Location*

2. Dans le champ **Derived column name**, entrer le nom de la nouvelle colonne à créer. Dans notre exemple, nommer la colonne *City*

3. Depuis la nouvelle colonne (*City*), entrer un exemple de la transformation que l'on souhaite obtenir. Dans notre exemple, on souhaite obtenir *Quebec city* à partir de l'entrée *Canada, Quebec city*. Puis cliquer partout ailleurs dans la fenêtre ce qui va construire le reste des valeurs de la colonne

4. Le code *Pandas* est généré pour vous à partir de l'exemple qui a été défini dans les étapes précédentes

5. Appuyer sur le bouton **Apply** pour appliquer la transformation

![Mise en place de transformation par l'exemple](images/String%20Transform%2001.png)

### Transformer des données avec un code personnalisé Pandas
En plus des options de transformation des données proposées par DataWrangler, il est possible de définir des transformations personnalisées en écrivant du code Pandas. Pour cela, suivre les étapes suivantes :

1. Dans le menu **Operations**, choisir **Custom operation**

2. Dans l'encart, vous allez pourvoir définir écrire des transformations sur les données avec la librairie *Pandas*. La table de données est définie dans un dataframe *Pandas* nommé *df* par défaut

![Mise en place de transformation personnalisée avec Pandas](images/Custom%20Operation%2000.png)

L'écriture de transformation de données avec Python et la librairie Pandas peut se faire de cette façon : 

1. Inscrire le code [Python](python/fonction_personnalise.py) de transformation des données dans le champ dédié et cliquer sur le bouton **Apply**. Dans cette exemple, nous proposons de supprimer la colonne Location puis de filtrer les données pour ne conserver que les locations de la ville de Montréal (*df["City"] == 'Montreal'*) et de type "Chambre privée" (*df["Accommodation type"] == "Private room"*).

    ```python
    # Suppresion de la colonne Location
    df.drop(columns=["Location"], inplace=True)

    # Filtre des données de la ville de Montreal et de type 'Private room'
    df = df[(df["City"] == 'Montreal') & (df["Accommodation type"] == "Private room")]
    ```

![Écriture du code Python de transformation des données](images/Custom%20Operation%2001.png)


### Regroupement et agrégation
*Data Wrangler* permet également de définir des opérations de regroupement et d'agrégation des données. La mise en place se fait de la façon suivante : 

1. Dans le menu **Operations**, choisir l'option **Group by and aggregation** ce qui va permettre de définir les opérations de regroupement et d'agrégation

![Sélection de l'option Group by and aggregation](images/Group%20By%2000.png)

Les différents paramètres peuvent être sélectionnées de la façon suivante :

1. Dans le champ **Columns to group by**, choisir la ou les colonnes sur lesquelles regrouper les données. Dans notre exemple, nous avons sélectionné la colonne *Neighbourhood*.

2. Dans le champ **Aggregation**, choisir la colonne sur laquelle appliquer une agrégation. Dans notre exemple, choisir la colonne *Room price per night* 

3. Dans le champ **Aggregation**, pour chaque colonne à agréger choisir une opération d'agrégation. Dans notre exemple, nous choisissons de calculer la moyenne du prix par nuit (*Mean*).

En cliquant sur l'option **+ Add aggregation**, il est possible d'ajouter d'autre colonne à agréger et de définir l'opération d'agrégation souhaitée.

![Mise en place d'un regroupement de colonnes et d'une agrégation](images/Group%20By%2001.png)

### Utiliser GitHub Copilot pour générer du code
*Data Wrangler* offre la possibilité d'utiliser GitHub Copilot pour de la génération de code assisté par IA en décrivant ce qui est souhaité en langage naturel. Comme vu précédemment, choisir l'option **Describe operations with copilot** dans le menu **Operations**.

1. Entrer une instruction en langage naturel. Par exemple : "*renommer la colonne 'Rommpricepernight_mean*' en '*Prix Moyen*' et arrondir les valeurs de la colonne 'Prix Moyen' à deux décimales". Si l'extension GitHub Copilot n'est pas installé, Vs Code va vous proposer de l'installer.

2. Appuyer sur le bouton **Apply** pour générer le code Pandas et appliquer la transformation

3. L'aperçu permet de valider visuellement les transformations qui ont été décrite en langage naturel. 

4. Le code *Pandas* généré par IA suite à l'interprétation de l'instruction en langage naturel 

![Utilisation de GitHub Copilot](images/Copilot%2004.png)

### Générer le code Python
Une fois le résultat final souhaité obtenu, il est possible de visualiser le code Python qui a servi à obtenir ce résultat. Ainsi l'ensemble des étapes construites dans cet exemple sont résumées en Python via la librairie *Pandas*.

1. L'encart **Cleaning steps** résument l'ensemble des étapes qui ont été validées successivement. Dans notre exemple, nous retrouvons l'ensemble des transformations décrite ci-dessus.

2. Cliquer sur **Preview code for all steps** pour générer le code Python

3. L'encart donne le code Python généré

4. Cliquer sur **Export to notebook** pour générer un notebook *Jupyter* reprenant l'ensemble des transformations

5. Visualisation du notebook généré

![Génération du code Python des transformations des données](images/Python%20&%20Juyter.png)


### Exporter les données transformées

Au lieu d'exporter le code Pandas généré par Data Wrangler, il est possible d'exporter le résultat dans des fichiers de données CSV ou Parquet. Pour cela, 

1. Cliquer sur le bouton **Export to file**

2. Choisir le format de fichier souhaité (CSV ou Parquet) puis suivre les étapes dans l'explorateur de fichier Windows pour enregistrer le fichier résultat. 

![Export des résultats dans un fichier de données CSV ou Parquet](images/Python%20&%20Juyter.png)

## Conclusion
Cet article a montré comment *Data Wrangler* est un outil puissant pour nettoyer, transformer et analyser les données dans Vs Code en no code.

Cette extension vous permettra : 

- de réduire le temps de nettoyage de vos données
- définir des workflow de transformation des données reproductibles
- visualiser immédiatement la qualité et les transformations des données 