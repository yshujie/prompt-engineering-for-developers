from test.guideline import Guideline

def testGuideline():    
    response = Guideline.text6()
    
    print("Response:")
    print(response)

if __name__ == '__main__':
    testGuideline()