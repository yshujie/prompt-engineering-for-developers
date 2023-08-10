
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
    
    def limitSummary(self) -> str :
        """
        对产品说明书进行总结，
        并限制输出的字数
        """
        pass
        prompt = f"""
        您的任务是帮助营销团队基于技术说明书创建一个产品的营销描述。
        根据 ``` 标记的技术说明书中提供的信息，编写一个产品描述。

        要求：营销描述最多 50 个字。
        
        技术说明书：
        ```{self._productManual}```
        """
        return OpenAI().getCompletion(prompt = prompt, temperature=0)
    
    def summaryWithUsageScenarios(self) -> str:
        """
        对产品说明书进行总结，
        并限制输出的字数、说明使用场景
        """
        pass
        prompt = f"""
        您的任务是帮助营销团队基于技术说明书创建一个产品的营销描述。
        根据 ``` 标记的技术说明书中提供的信息，编写一个产品描述。

        该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。
        最多使用 50 个字。
        
        在描述末尾，包括技术规格中每个7个字符的产品ID。
        
        技术说明书：
        ```{self._productManual}```
        """
        return OpenAI().getCompletion(prompt = prompt, temperature=0)
    
    def summaryWithTable(self) -> str:
        """
        对产品说明书进行总结，
        并限制输出的字数、说明使用场景、使用表格进行可视化展示
        """
        pass
        prompt = f"""
        您的任务是帮助营销团队基于技术说明书创建一个产品的营销描述。
        根据 ``` 标记的技术说明书中提供的信息，编写一个产品描述。

        该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。
        最多使用 50 个字。
        
        在描述末尾，包括技术规格中每个7个字符的产品ID。
        
        在描述之后，包括一个表格，提供产品的尺寸。表格应该有两列。第一列包括尺寸的名称。第二列只包括英寸的测量值。
        给表格命名为“产品尺寸”。
        将所有内容格式化为可用于网站的HTML格式。将描述放在<div>元素中。

        技术说明书：
        ```{self._productManual}```
        """
        return OpenAI().getCompletion(prompt = prompt, temperature=0)
