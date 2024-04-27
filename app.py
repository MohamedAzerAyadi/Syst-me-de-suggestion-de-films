import streamlit as st
import pickle

# Charger les données
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Entête de l'application
st.title("Recommandations de films")

# Sélection du film à partir d'une liste déroulante
selectvalue = st.selectbox("Choisissez votre film", movies_list)

# Fonction de recommandation des films similaires
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movies = []
    for i in distance[1:6]:  # Exclure le film lui-même (premier élément)
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

# Affichage des recommandations lorsque le bouton est cliqué
if st.button("Afficher les recommandations"):
    if selectvalue:
        recommended_movies = recommend(selectvalue)
        if recommended_movies:
            st.subheader("Films recommandés:")
            col1, col2, col3, col4, col5 = st.columns(5)
            for i, movie in enumerate(recommended_movies[:5]):
                with locals()[f"col{i+1}"]:
                    st.write(f"{i+1}. {movie}")
        else:
            st.warning("Aucun film recommandé trouvé.")
    else:
        st.warning("Veuillez choisir un film dans la liste.")
