meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    while True:
        word = input("Yazdığınız kelime sözlükte bulunmuyor. Lütfen başka bir kelime deneyin: ")
        if word in meme_dict.keys():
            print(meme_dict[word])
            breeak