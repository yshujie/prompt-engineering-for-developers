
from openAI.OpenAI import OpenAI


class ProductMarketingCopyEditor:
    
    def __init__(self, productManual):
        self._productManual = productManual

    def getProductManual(self) -> str:
        return self._productManual
    
    def summary(self) -> str:
        """
        对产品说明书进行总结
        """
        pass
        prompt = f"""
        您的任务是帮助营销团队基于技术说明书创建一个产品的营销描述。
        根据 ``` 标记的技术说明书中提供的信息，编写一个产品描述。

        技术说明书：
        ```{self._productManual}```
        """

        return OpenAI().getCompletion(prompt = prompt, temperature=0)