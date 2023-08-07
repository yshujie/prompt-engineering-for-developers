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
        pass
        
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
        pass
        
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
    
    def text3(text):
        """ 
        案例3：通过 Prompt 对文本进行加工，给 LLM 提供示例。
        """
        pass
    
        prompt = f"""
        您将获得由三个引号扩起来的文本，您的任务是以一致的风格回答问题。
        
        以下是一个示例：
        <孩子>：请教我耐心。
        <祖父母>：挖出最深峡谷的河流源于一处不起眼的泉眼；最宏伟的交响乐从单一的音符开始；最复杂的挂毯以一根孤独的线开始编织。
        ------
        
        您需要回答的问题：
        <孩子>：\"\"\"{text}\"\"\"
        您的回答：
        """    
        return OpenAI().getCompletion(prompt = prompt, temperature=0.9)
        
    def text4(text):
        """
        案例4：通过 Prompt 提示 LLM 对文本进行加工。
        给模型时间去思考，指定完成任务所需的步骤。
        """
        pass
    
        prompt = f"""
        执行一下操作：
        1. 用一句话概括下面用三个反括号括起来的文本
        2. 将摘要翻译为法语
        3. 在法语摘要中列出每个人名
        4. 输出一个 JSON 对象，其中包含以下键：French_summary, num_names
        
        请用换行符分割您的答案。
        
        Text:
        ```{text}```
        """
        
        return OpenAI().getCompletion(prompt = prompt, temperature=0)
    
    def text5(text):
        """
        案例4：通过 Prompt 提示 LLM 对文本进行加工。
        给模型时间去思考，指定完成任务所需的步骤。     
        """
        pass 
        
        prompt = f"""
        1. 用一句话概括下面用<>括起来的文本
        2. 将摘要翻译为英语
        3. 在英语摘要中列出每个人名
        4. 输出一个 JSON 对象，其中包含以下键：English_summary, num_names 
        
        请使用以下格式：
        文本：<要总结的文本>
        摘要：<摘要>
        翻译：<摘要的翻译>
        名称:<英文找药中的名称列表>
        输出 JSON：<带有 English_summary 和 num_names 的 JSON>
        
        Text：<{text}>
        
        您的回答：
        """
        return OpenAI().getCompletion(prompt = prompt, temperature=0)
    
    def text6():
        """
        案例6：通过 Prompt 提示 LLM 对文本进行加工。
        给模型时间去思考，指导模型在下结论之前找出自己的解法 
        
        注意：LLM 给的回答为：“学生的解决方案是正确的。他们正确地计算了土地费用、太阳能电池板费用和维护费用，并将它们相加得到了总费用。总费用是450x+100,000美元。”
        但实际上学生的解决方案是错误的。
        """
        pass
        prompt = f"""
        请判断学生的解决方案是否正确，请通过如下步骤解决这个问题：

        步骤：

            首先，自己解决问题，解决问题时列数学表达式。
            然后将您的解决方案与学生的解决方案进行比较，并评估学生的解决方案是否正确。
            在自己完成问题之前，请勿决定学生的解决方案是否正确。

        使用以下格式：

            问题：问题文本
            学生的解决方案：学生的解决方案文本
            实际解决方案和步骤：实际解决方案和步骤文本
            学生的计算结果：学生的计算结果文本
            实际计算结果：实际计算结果文本
            学生的计算结果和实际计算结果是否相同：是或否
            学生的解决方案和实际解决方案是否相同：是或否
            学生的成绩：正确或不正确

        问题：

            我正在建造一个太阳能发电站，需要帮助计算财务。 
            - 土地费用为每平方英尺100美元
            - 我可以以每平方英尺250美元的价格购买太阳能电池板
            - 我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付每平方英尺10美元
            作为平方英尺数的函数，首年运营的总费用是多少。

        学生的解决方案：

            设x为发电站的大小，单位为平方英尺。
            费用：
            1. 土地费用：100x
            2. 太阳能电池板费用：250x
            3. 维护费用：100,000+100x
            总费用：100x+250x+100,000+100x=450x+100,000

        实际解决方案和步骤：
        """
        return OpenAI().getCompletion(prompt = prompt, temperature=0)