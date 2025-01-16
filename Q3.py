def charCount(t):
    from collections import Counter
    try:
        with open(t, 'r') as file:
            text =file.read().replace(" ", "").replace("\n", "")
            return dict(Counter(text))
    except FileNotFoundError:
        print(f"Error: The file '{t} was not")

    except:
    except: