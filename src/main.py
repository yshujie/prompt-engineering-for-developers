from src.test.guideline import Guideline

def testGuideline():
    text = f"""
    泡一杯茶很容易。首先，需要把水烧开。
    在等待期间，拿一个杯子并把茶包放进去。
    一旦水足够热，就把它倒在茶包上。
    等待一会儿，让茶叶浸泡。几分钟后，取出茶包。
    如果您愿意，可以加一些糖或牛奶调味。
    就这样，您可以享受一杯美味的茶了。
    """
    
    response = Guideline.text1(text)
    
    print("Response:")
    print(response)
    


if __name__ == '__main__':
    testGuideline()