videos = [("python básico", 500, 20), ("deep learning", 400, 50), ("visualização de dados", 600, 30),("análise estatística", 350, 60)]

i_video = 0

taxas_aprovacao = []

total_likes = 0
total_dislikes = 0

for video in videos:
    likes = videos[i_video][1]
    dislikes = videos[i_video][2]
    taxa_aprovacao = (likes/(likes + dislikes))
    taxas_aprovacao.append(taxa_aprovacao)
    total_likes = likes + total_likes
    total_dislikes = total_dislikes + dislikes
    i_video += 1

print("total de likes: ", total_likes, "total de dislikes: ", total_dislikes)


i_maiortaxa = 0

i_menortaxa = 0

for taxa in taxas_aprovacao:
    if i_maiortaxa == 0:
        maior_taxa = taxas_aprovacao[0]
        i_maiortaxa += 1
    elif maior_taxa < taxa:
        maior_taxa = taxa
        i_maiortaxa += 1
    
for taxa in taxas_aprovacao:
    if i_menortaxa == 0:
        menor_taxa = taxas_aprovacao[0]
        i_menortaxa += 1
    elif menor_taxa > taxa:
        menor_taxa = taxa
        i_menortaxa += 1


if i_maiortaxa == 1:
    print("maior taxa de aprovação: python básico", maior_taxa)
elif i_maiortaxa == 2:
    print("maior taxa de aprovação: deep learning", maior_taxa)
elif i_maiortaxa == 3:
    print("maior taxa de aprovação: visualização de dados", maior_taxa)
elif i_maiortaxa == 4:
    print("maior taxa de aprovação: análise estatística", maior_taxa)


if i_menortaxa == 1:
    print("menor taxa de aprovação: python básico", menor_taxa)
elif i_menortaxa == 2:
    print("menor taxa de aprovação: deep learning", menor_taxa)
elif i_menortaxa == 3:
    print("menor taxa de aprovação: visualização de dados", menor_taxa)
elif i_menortaxa == 4:
    print("menor taxa de aprovação: análise estatística", menor_taxa)

videos1 = (
    ("Análise de componentes principais", 100, 20),
    ("ChatGPT", 800, 20),
    ("Rede neural MLP", 550, 15),
)


videos1 = list(videos1)
videos1[0] = list(videos1[0])

videos1[0][1] = 150
videos1[0][2] = 25

print(videos1)






