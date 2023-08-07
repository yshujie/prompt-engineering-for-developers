from test.guideline import Guideline

def testGuideline():
    text = f"""
    在一个迷人的村庄里，兄妹杰克和吉尔出发去一个山顶井里打水。
    他们一边唱着欢乐的歌，一边往上爬，
    然而不幸降临——杰克绊了一块石头，从山上滚了下来，吉尔紧随其后。
    虽然略有些摔伤，但他们还是回到了温馨的家中。
    尽管出了这样的意外，他们的冒险精神依然没有减弱，继续充满愉悦地探索。
    """
    
    response = Guideline.text5(text)
    
    print("Response:")
    print(response)

if __name__ == '__main__':
    testGuideline()