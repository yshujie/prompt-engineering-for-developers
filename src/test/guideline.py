from openAI.OpenAI import OpenAI

class Guideline:
    def text1(text):
        """
        案例1: 通过 Prompt 对文本进行加工
        此案例练习的 Prompt 编写原则：
        1. 编写清晰、具体的指令
            i. 获得用户的输入
            ii. 若输入满足条件1，则执行操作1
            iii. 若输入满足条件2，则执行操作2
        """
        
        prompt = f"""
        您将获得由三个引号扩起来的文本。\
        
        如果它包含一些列的指令，则需要按照以下格式重新编写这些指令：
        第一步: ***
        第二步: ***
        ... 
        第N步: ***
        
        如果文本中不包含一系列的指令，则直接写`未提供步骤`。
        
        您获得的文本如下：
        \"\"\"{text}\"\"\"
        """

        return OpenAI().getCompletion(prompt = prompt)
    
    def text2(text):
        """
        案例2: 通过 Prompt 对文本进行加工，要求 LLM 对输出进行格式化
        此案例练习使用 Prompt 要求 LLM 输出 JSON 格式的数据。
        """
        
        prompt = f"""
        您将获得由三个引号扩起来的文本。\
            
        如果它包含一些列的指令，则需要按照以下格式重新编写这些指令：
        第一步: ***
        第二步: ***
        ... 
        第N步: ***
        
        如果文本中不包含一系列的指令，则直接写`未提供步骤`。
        
        请使用 JSON 格式对文本进行格式化，JSON 格式如下：
        [
            {{
                "step": "第一步",
                "content": "..."
            }},
        ]
        
        您获得的文本如下：
        \"\"\"{text}\"\"\"
        """ 
        
        return OpenAI().getCompletion(prompt = prompt)