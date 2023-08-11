from example.inferring import Interring

class TestInferring:
    """
    推理模块的测试类
    """
    pass
    
    def __init__(self):
        self._interring = Interring()
        
    def test(self):
        """ 
        对外暴露的测试方法
        """
        pass
    
        # 测试情感识别
        self._testEmotionRecognition()
         
    def _testEmotionRecognition(self):
        review = """
        我需要一盏漂亮的卧室灯，这款灯具有额外的储物功能，价格也不算太高。\
        我很快就收到了它。在运输过程中，我们的灯绳断了，但是公司很乐意寄送了一个新的。\
        几天后就收到了。这款灯很容易组装。我发现少了一个零件，于是联系了他们的客服，他们很快就给我寄来了缺失的零件！\
        在我看来，Lumina 是一家非常关心顾客和产品的优秀公司！
        """
        
        print("情感识别测试：")
        
        self._interring.emotionRecognition2(review)
        
        