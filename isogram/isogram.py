def is_isogram(string):

    string = "".join(ch for ch in string if ch.isalnum()).lower()
    #a "".join azt csinálja hogy egyesíti a szövegeket
    # amit itt egyesít szöveg az a zárójel után van azonnal a (ch
    # a ch az a stringen végigmenve minden karakter egyesével
    # de csak akkor teljesíti ezt ha a ch.isalnum igaz ami akkor igaz ha a ch számvagybetű is-alfa-numeric
    # nem vagyok biztos benne hogy a joint nem teljesíti vagy a ciklus ugorja át vagy pontosan hogy van
    # .lower() kisbetűssé alakít minden karaktert
    # abban sem vagyok biztos hogy karakterenként alakítja-e kisbetűvé vagy egyből az egészet vagy a végén az egészet, de szerintem karakterenként mert az éppen joinolt elemen végzi el
    #neten találtam arra hogyan kell spec karaktereket szűrni (számokat nem kellett külön nincs a tesztben)
    # a lowert én csaptam mellé volt olyan változatom is hogy lent lowerelem kétszer a stringet de sikerült ebbe tennem és így csak egyszer kell

    for rep in string:
        if string.count(rep) > 1:
            return False

    return True
