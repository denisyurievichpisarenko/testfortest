def clear_text(text, trash_tokens):
    text = text.strip(trash_tokens)
    return text
def get_words(text):
    tokens = text.split()
    trash_tokens = ',./\\=+[]-:;!?()'
    good_tokens = []
    for token in tokens:
        clean_token = clear_text(token, trash_tokens)
        if clean_token != '':
            clean_token = clean_token.lower()
            good_tokens.append(clean_token)
    return good_tokens

def main():
    filename = r'C:\Users\student\Desktop\quotes.txt'
    DASH = '—'
    list_of_authors = []
    with open(filename, encoding = 'utf-8') as fid:
        for line in fid:
            line = line.strip()
            parts = line.split(DASH)
            quote = parts[0]
            author = parts[1]

            quote_words = get_words(quote)
            

            if 'разум' in quote_words:
                list_of_authors.append(author)
    print("слово 'разум' содержится в"
          ,len(list_of_authors),
          "цитатах")
    print(', '.join(list_of_authors))
            

if __name__ == '__main__':
    main()
        
        
    
