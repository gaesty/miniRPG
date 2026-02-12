# miniRPG

## DesignPattern
Voici les choix que nous avons fait :

- Abstract Factory pour le personnage du joueur, les ennemis, les items et les zones : Le DesignPattern "Builder" est plus adapté au projet mais ce design pattern est lourd à mettre en place et au vu du manque de temps sur le projet il vaut mieux se rabattre sur une Abstract Factory.

- Facade qui initialise des Decorators pour le moteur de combat
- Strategy pour les effets et le statuts
- Observer pour le Boss

- Exploration par menu -> Iterator : On a hésité à choisir le State mais ce dernier n'est pas adapté à l'exploration step by step du RPG.
- Combat tour par tour -> Command & Strategy 
- Inventaire + équipement -> Strategy 
- Mini-ligne de quête -> State 
- Sauvegarde/chargement -> Adapter : On voulait choisir le Memento mais ce design pattern est fait pour stocker dans la ram donc non persistant. L'adapter permet de convertir en JSON.