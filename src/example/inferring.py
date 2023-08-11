from openAI.OpenAI import OpenAI

class Interring:
    """
    Prompt Engineering for Developer -- 5.推断 Interring 案例实现
    """
    pass

    def __init__(self):
        self.openAI = OpenAI()
        
    def emotionRecognition(review):
        """
        1.情感识别，使用 Prompt ，通过 LLM 时别评论的情感
        """
        pass
        
        prompt1 = """
        以下用三个反引号分隔的产品评论的情感是什么？

        评论文本: ```{review}```
        """
        print("prompt1: ", prompt1)
        print("result：", self.openAI.completion(prompt1))
        
        prompt2 = """
        以下用三个反引号分隔的产品评论的情感是什么？
        评论文本: ```{review}```
        """
        print("prompt2: ", prompt2)
        print("result：", self.openAI.completion(prompt2))
        
        
        prompt3 = """
        以下用```分隔的产品评论的情感是什么？

        评论文本: ```{review}``` 
        """
        print("prompt3: ", prompt3)
        print("result：", self.openAI.completion(prompt3))
        
        

