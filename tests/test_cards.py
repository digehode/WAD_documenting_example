import cards

def test_counts():
    d=cards.createDeck()
    assert len(d)==52



# How do we test shuffle?

# How do we test dealing a hand?
# This is more complex because we have input. What should happen if the input is "bad"?
    
