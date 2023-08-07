from test.guideline import Guideline

def testGuideline():
    text = f"请教我韧性"
    
    response = Guideline.text3(text)
    
    print("Response:")
    print(response)

if __name__ == '__main__':
    testGuideline()