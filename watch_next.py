def next_mov(mov_watched):  #  Recommends next movie to watch.
  mov_watched = nlp(mov_watched)  #  Tokenises watched movie data.
  mov_rank = 0  
  for count, mov in enumerate(mov_list):
    data = mov.split(":")  #  Splits movie title from description.
    mov_compare = data[1]
    mov_compare = nlp(mov_compare)  #  Tokenises movie to compare data.
    mov_sim = (mov_compare.similarity(mov_watched))  #  Compares watched and movie from list.
    if mov_sim > mov_rank:  #  Compares and retains highest similarity.
      mov_rank = mov_sim
      mov_nxt = count  #  Keeps track of movie with higest similarity to watched movie.

  print(f"\nThe next movie suggested is: ")
  print(f"\n{mov_list[mov_nxt]}")  #  Displays movie with higest similarity as suggestion.
  

#==================== START OF PROGRAM =======================
  
import spacy  #  Imports spacy.
nlp = spacy.load('en_core_web_md')  #  Loads language model.

mov_watched = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

with open('movies.txt', 'r') as f:  #  Reads data file into list of movies.
  mov_list = []
  for data in f:
    mov_list.append(data)

next_mov(mov_watched)


