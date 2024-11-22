## Health Calculator Microservice

    Un microservice RESTful qui calcule les métriques de santé BMI (Indice de Masse Corporelle) et BMR (Taux Métabolique Basal) avec un pipeline CI/CD sur Azure.

## Fonctionnalités

    Calcul du BMI (Body Mass Index)

    Calcul du BMR (Basal Metabolic Rate)

    API RESTful avec Flask

    Tests unitaires

    Conteneurisation Docker

    Pipeline CI/CD avec GitHub Actions

    Déploiement automatisé sur Azure

## Prérequis

    Python 3.9 ou supérieur

    Docker

    Make

    Un compte Azure (pour le déploiement)

    Git

## Installation

1- Cloner le dépot :

    git clone https://github.com/yannick-kenang-supdevinci/Markdown.git

    cd Markdown

2- Installez les dépendances :

    make init

## Utilisation

1- Lancer l'application en local :

    make run

2- make test

    make test

3- Lancer avec Docker :

    make build

    make docker-run

4- Calcul du BMI

    POST /bmi

5- Calcul du BMR

    POST /bmr

## Déploiement

1- Créez une App Service sur Azure

2- Téléchargez le profil de publication depuis Azure

3- Ajoutez le profil aux secrets GitHub :

    Nom : AZURE_WEBAPP_PUBLISH_PROFILE
    Valeur : Contenu du profil de publication


4- Poussez sur la branche main pour déclencher le déploiement

