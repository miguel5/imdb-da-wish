import csv
import re

file = open("movies.ttl", "a", encoding="utf-8")

actors = []
genres = []
producers = []
directors = []
writers = []

with open('movies.csv', encoding="utf-8") as movies_csv:
    csv_reader = csv.reader(movies_csv, delimiter=',')
    col_names = []

    for row in csv_reader:

        file.write("###  http://www.semanticweb.org/joaop/ontologies/2021/5/movies#" + row[0] + "\n")
        file.write(":" + row[0] + " rdf:type owl:NamedIndividual ,\n")
        file.write(" "*8 + ":Filme ;\n")


        movie_actors = row[12].split(",")

        if len(movie_actors) > 0:
            

            file.write(" "*8 + ":temAtor :" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",movie_actors[0].replace(" ","")))
            
            if len(movie_actors) == 1:
                file.write(" ;\n")
            else:
                file.write(" ,\n")


            for actor in movie_actors[1:]:
                if actor not in actors:
                    actors.append(actor)
                
                file.write(" "*17 + ":" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",actor.replace(" ","")))

                if movie_actors.index(actor) == len(movie_actors)-1:
                    file.write(" ;\n")
                else:
                    file.write(" ,\n")

        movie_genres = row[5].split(",")
        
        if len(movie_genres) > 0:

            file.write(" "*8 + ":temGenero :" + movie_genres[0])

            if len(movie_genres) == 1:
                file.write(" ;\n")
            else:
                file.write(" ,\n")

            for genre in movie_genres[1:]:
                if genre not in genres:
                    genres.append(genre)

                file.write(" "*8 + ":" + genre.replace(" ",""))

                if movie_genres.index(genre) == len(movie_genres)-1:
                    file.write(" ;\n")
                else:
                    file.write(" ,\n")
        
        movie_directors = row[9].split(",")

        if len(movie_directors) > 0:
            file.write(" "*8 + ":temDiretor :" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",movie_directors[0].replace(" ","")))

            if len(movie_directors) == 1:
                file.write(" ;\n")
            else:
                file.write(" ,\n")

            for director in movie_directors[1:]:
                if director not in directors:
                    directors.append(director)

                file.write(" "*19 + ":" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",director.replace(" ","")))

                if movie_directors.index(director) == len(movie_directors)-1:
                    file.write(" ;\n")
                else:
                    file.write(" ,\n")

        movie_writers = row[10].split(",")

        if len(movie_writers) > 0:
            file.write(" "*8 + ":temEscritor :" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",movie_writers[0].replace(" ","")))

            if len(movie_writers) == 1:
                file.write(" ;\n")
            else:
                file.write(" ,\n")

            for writer in movie_writers[1:]:
                if writer not in writers:
                    writers.append(writer)
                
                file.write(" "*20 + ":" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",writer.replace(" ","")))

                if movie_writers.index(writer) == len(movie_writers)-1:
                    file.write(" ;\n")
                else:
                    file.write(" ,\n")

        producers.append(row[11])

        file.write(" "*8 + ':temProdutor :' + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",row[11].replace(" ","")) + ' ;\n')

        file.write(" "*8 + ':titulo "' + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",row[1]) + '" ;\n')
        file.write(" "*8 + ':ano "' + row[3] + '" ;\n')
        file.write(" "*8 + ':duracao "' + row[6] + '" ;\n')
        file.write(" "*8 + ':pais "' + row[7] + '" ;\n')
        file.write(" "*8 + ':linguagem "' + row[8] + '" ;\n')
        file.write(" "*8 + ':classificacao "' + row[14] + '" ;\n')
        file.write(" "*8 + ':descricao "' + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",row[13].replace("\n"," ")) + '" ;\n')

        if row[16]:
            file.write(" "*8 + ':orcamento "' + row[16] + '" ;\n')

        if row[20]:
            file.write(" "*8 + ':criticas_utilizadores "' + row[20] + '" ;\n')

        if row[21]:
            file.write(" "*8 + ':criticas_criticos "' + row[21] + '" ;\n')

        file.write(" "*8 + ':numero_votos "' + row[15] + '" .\n')


        file.write("\n\n")

    for actor in actors:
        file.write("###  http://www.semanticweb.org/joaop/ontologies/2021/5/movies#" + actor.replace(" ","") + "\n")
        file.write(":" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",actor.replace(" ","")) + " rdf:type owl:NamedIndividual ,\n")
        file.write(" "*8 + ":Ator ;\n")
        file.write(" "*8 + ':nome "' + actor + '" .\n\n')

    for genre in genres:
        file.write("###  http://www.semanticweb.org/joaop/ontologies/2021/5/movies#" + genre.replace(" ","") + "\n")
        file.write(":" + genre.replace(" ","") + " rdf:type owl:NamedIndividual ,\n")
        file.write(" "*8 + ":Genero ;\n")
        file.write(" "*8 + ':nome "' + genre + '" .\n\n')

    for producer in producers:
        file.write("###  http://www.semanticweb.org/joaop/ontologies/2021/5/movies#" + producer.replace(" ","") + "\n")
        file.write(":" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",producer.replace(" ","")) + " rdf:type owl:NamedIndividual ,\n")
        file.write(" "*8 + ":Produtor ;\n")
        file.write(" "*8 + ':nome "' + producer + '" .\n\n')

    for director in directors: 
        file.write("###  http://www.semanticweb.org/joaop/ontologies/2021/5/movies#" + director.replace(" ","") + "\n")
        file.write(":" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",director.replace(" ","")) + " rdf:type owl:NamedIndividual ,\n")
        file.write(" "*8 + ":Diretor ;\n")
        file.write(" "*8 + ':nome "' + director + '" .\n\n')

    for writer in writers:
        file.write("###  http://www.semanticweb.org/joaop/ontologies/2021/5/movies#" + writer.replace(" ","") + "\n")
        file.write(":" + re.sub(r'["\',\.()\&\/\[\]!:\+\?\=]',"",writer.replace(" ","")) + " rdf:type owl:NamedIndividual ,\n")
        file.write(" "*8 + ":Escritor ;\n")
        file.write(" "*8 + ':nome "' + writer + '" .\n\n')


file.close()

