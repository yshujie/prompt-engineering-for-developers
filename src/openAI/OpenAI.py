import openai

class OpenAI:
    
    apiKey = None
    
    def __init__(self):
        # 环境变量中获取 API Key
        apiKey = os.environ.get('OPENAI_API_KEY')
        
        # 验证 API Key
        if apiKey is None:
            raise Exception("OpenAI API Key not found.")
        
        # 设置 API Key
        self.apiKey = apiKey
        
    def getCompletion(prompt, model='gpt-3.5-turbo') -> str:
        """
        prompt: 提示词
        model: 使用的模型，默认为 gpt-3.5-turbo
        """
        messages = [
            {"role": "user", "content": prompt},
        ]
        
        response = openai.Completion.create(
            model=model,
            prompt=messages,
            temperature=0,
        )
        
        return response.choices[0].text
        
        
        