import pandas as pd

df = pd.read_csv("notas_alunos.csv")

medias = (df["nota_1"] + df["nota_2"]) / 2

df["media"] = medias

df.loc[df["media"] >= 7, "situacao"] = "APROVADO! PARABÉNS!"
df.loc[df["media"] < 7, "situacao"] = "REPROVADO"
df.loc[df["faltas"] > 5, "situacao"] = "REPROVADO POR FALTA"

df.to_csv("alunos_situacao.csv")

maior_faltas = df["faltas"].max()
media_geral = df["media"].mean()
maior_media = df["media"].max()

print("Maior número de faltas: " + str(maior_faltas))
print("Média geral das notas dos alunos: " + "{:.2f}".format(media_geral))
print("Maior média: " + str(maior_media))
