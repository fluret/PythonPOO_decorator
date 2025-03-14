from article import Article

if __name__ == "__main__":
    # Demander le taux de TVA pour tous les articles
    Article.taux_tva = float(input("Donner le taux de TVA pour tous les articles : "))
    print(f"Le taux TVA est : {Article.taux_tva}%\n")

    # Article 1
    article1 = Article()
    print("Article 1:")
    article1.afficher_article()
    print()

    # Article 2
    article2 = Article(111, "ATA", 100)
    print("Article 2:")
    article2.afficher_article()
    print()

    # Article 3
    article3 = Article(122, "RER")
    print("Article 3:")
    article3.afficher_article()
    print()

    # Article 4 (copie de l'article 2)
    article4 = Article(article2.reference, article2.designation, article2.prix_ht)
    print("Article 4:")
    article4.afficher_article()