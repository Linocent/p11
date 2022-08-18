# Améliorer un projet existant en Python
***

## Contexte
“ô rage ! ô désespoir ! ô vieillesse ennemie ! N’ai-je donc tant vécu que pour cette infamie ?” vous exclamez-vous en découvrant dans votre boîte mail un message de votre dernier client, pourtant si content lors de la dernière mise en production.


“Bonjour,

Je vous remercie pour le travail réalisé. Néanmoins nous avons découvert qu’il manquait une fonctionnalité importante que nous aimerions développer. Combien de temps cela vous prendrait-il ?

Nous avons également remarqué des dysfonctionnements (rien n’apparaît lorsque nous lançons Internet Explorer). Nos développeurs ont essayé de résoudre les bugs mais en vain, apparemment. Ils viennent de me dire de vous contacter car les tests sont cassés (je ne sais pas ce que cela signifie mais je transmets) et menacent la production (ça, j'ai bien compris - ils ont travaillé directement sur le site en ligne !).

C’est tout pour aujourd’hui.

Merci.

Cordialement,

Dona Jimena”


Évidemment, vous allez corriger… Car, comme diraient les Shadoks, s’il n’y a pas de solution, c’est qu’il n’y a pas de problème. Allez, c’est parti !

***
## Fonctionnalités
Basez-vous sur l’un des projets que vous avez déjà réalisés dans ce parcours de formation ou dans votre carrière. Choisissez une fonctionnalité à ajouter. Elle doit être assez importante pour justifier des tests fonctionnels. Votre mentor jouera le rôle du client. Jouez le jeu et communiquez avec lui de la même manière que vous le feriez avec un client : soignez votre présentation, l’endroit où se déroule votre session de mentorat et l’orthographe dans vos e-mails !

Quant aux tests, cassez-en un puis réparez-le en le refactorant. Je suis sûre que vous avez un test caché quelque part qui mérite une nouvelle jeunesse !

***
## Livrables
* Code source modifié et hébergé sur Github. Il inclut les commits d’ajout de la nouvelle fonctionnalité et de correction des tests (soignez vos messages !).
* E-mails de réponse au client : première réponse prenant bien note de la menace en production, seconde réponse informant de la correction du bug et troisième réponse présentant votre nouveau travail (ajout de la fonctionnalité demandée).
* Document écrit expliquant votre démarche de création, les difficultés rencontrées et la manière dont vous les avez résolues. Le document doit être en format pdf et ne pas excéder 2 pages A4. Il peut être rédigé en anglais ou en français, au choix, mais prenez bien en considération que les fautes d’orthographe et de grammaire seront évaluées !

***
## Contraintes
* Votre code est sur Github et comporte un historique de commits cohérent,
* Votre code est écrit en anglais : commentaires, variables, …
* Votre nouvelle fonctionnalité inclut des tests unitaires et fonctionnels. Vous pouvez coder en TDD si vous le souhaitez.

***
## How to get this app:
1. Clone this repo;
2. Create a database whit PostgreSQL;
3. Create and open a virtualenv;
4. Install requirement ```pip install -r requirements.txt```;
5. Change password of the database in ```settings.py```;
6. update the database with ```python manage.py makemigrations``` & ```python manage.py migrate```;
7. Download the product with ```python manage.py category``` & ```python manage.py product```;
8. Run the app with ```python manage.py runserver```;
