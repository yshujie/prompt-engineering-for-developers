from openAI.OpenAI import OpenAI

class Interring:
    """
    Prompt Engineering for Developer -- 5.推断 Interring 案例实现
    """
    pass

    def __init__(self):
        self.openAI = OpenAI()
        
    def emotionRecognition(self, review):
        """
        1.情感识别，使用 Prompt ，通过 LLM 时别评论的情感
        """
        pass
        print("in emotionRecognition")
        
        print("review: ", review)
        
        prompt1 = f"""
        以下用三个反引号分隔的产品评论的情感是什么？

        评论文本: ```{review}```
        """
        print("prompt1: ", prompt1)
        print("result：", self.openAI.getCompletion(prompt1))
        
        prompt2 = f"""
        以下用三个反引号分隔的产品评论的情感是什么？
        评论文本: ```{review}```
        """
        print("prompt2: ", prompt2)
        print("result：", self.openAI.getCompletion(prompt2))
        
        prompt3 = f"""
        以下用```分隔的产品评论的情感是什么？

        评论文本: ```{review}``` 
        """
        print("prompt3: ", prompt3)
        print("result：", self.openAI.getCompletion(prompt3))
        
    def emotionRecognition2(self, review):
        """
        1.情感识别，使用 Prompt ，通过 LLM 时别评论的情感，输出指定格式的结果
        """
        pass
        print("in emotionRecognition")
        
        print("review: ", review)
        
        prompt1 = f"""
        以下用三个反引号分隔的产品评论的情感是什么？
        
        用一个单词回答：「正面」或「负面」。

        评论文本: ```{review}```
        """
        print("prompt1: ", prompt1)
        print("result：", self.openAI.getCompletion(prompt1))
        
        prompt2 = f"""
        以下用三个反引号分隔的产品评论的情感是什么？
        
        用一个单词回答：「正面」或「负面」
        
        评论文本: ```{review}```
        """
        print("prompt2: ", prompt2)
        print("result：", self.openAI.getCompletion(prompt2))
        
        prompt3 = f"""
        以下用```分隔的产品评论的情感是什么？
        用一个单词回答：「正面」或「负面」
        评论文本: ```{review}``` 
        """
        print("prompt3: ", prompt3)
        print("result：", self.openAI.getCompletion(prompt3))   