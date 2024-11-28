Un système de suggestion de films construit avec Streamlit et basé sur l'algorithme CountVectorizer de scikit-learn. 
La recommandation des films se fait en analysant le tag = description du film + titre.

Fonctionnalités : 
- L'utilisateur choisit un titre de film.
- Le système utilise CountVectorizer pour analyser le tag du film selectionné et suggére des films similaires.
- Les suggestions de films sont affichées en temps réel dans une interface web créé avec la bibliothèque streamlit de Python.

Pour lancer l'application web en local il faut : 
- Cloner le dépot git en local.
- Lancer streamlit avec la commande : "streamlit run app.py"


