from example.productMarketingCopyEditor import ProductMarketingCopyEditor

# 定义产品说明书常量
PRODUCT_MANUAL = """
概述

    美丽的中世纪风格办公家具系列的一部分，包括文件柜、办公桌、书柜、会议桌等。
    多种外壳颜色和底座涂层可选。
    可选塑料前后靠背装饰（SWC-100）或10种面料和6种皮革的全面装饰（SWC-110）。
    底座涂层选项为：不锈钢、哑光黑色、光泽白色或铬。
    椅子可带或不带扶手。
    适用于家庭或商业场所。
    符合合同使用资格。

结构

    五个轮子的塑料涂层铝底座。
    气动椅子调节，方便升降。

尺寸

    宽度53厘米|20.87英寸
    深度51厘米|20.08英寸
    高度80厘米|31.50英寸
    座椅高度44厘米|17.32英寸
    座椅深度41厘米|16.14英寸

选项

    软地板或硬地板滚轮选项。
    两种座椅泡沫密度可选：中等（1.8磅/立方英尺）或高（2.8磅/立方英尺）。
    无扶手或8个位置PU扶手。

材料
外壳底座滑动件

    改性尼龙PA6/PA66涂层的铸铝。
    外壳厚度：10毫米。
    座椅
    HD36泡沫

原产国

    意大利
"""

class TestProductMarketingCopyEditor:
    def __init__(self):
        self._productManual = PRODUCT_MANUAL
        self._productMarketingCopyEditor = ProductMarketingCopyEditor(self._productManual)

    def testSummary(self):
        """
        测试 -- 对产品说明书进行总结
        """
        pass

        summary = self._productMarketingCopyEditor.summary()

        print("summary: ", summary)
    
    def testLimitSummary(self):
        """
        测试 -- 对产品说明书进行总结，并限制输出的字数
        """
        pass

        limitSummary = self._productMarketingCopyEditor.limitSummary()

        print("limitSummary: ", limitSummary)
        print("len(limitSummary): ", len(limitSummary))

    def testSummaryWithUsageScenarios(self):
        """
        测试 -- 对产品说明书进行总结，并限制输出的字数、说明使用场景
        """
        pass

        summaryWithUsageScenarios = self._productMarketingCopyEditor.summaryWithUsageScenarios()

        print("summaryWithUsageScenarios: ", summaryWithUsageScenarios)
        print("len(summaryWithUsageScenarios): ", len(summaryWithUsageScenarios))


    def testSummaryWithTable(self):
        """
        测试 -- 对产品说明书进行总结，并限制输出的字数、说明使用场景、使用表格进行展示
        """
        pass

        summaryWithTable = self._productMarketingCopyEditor.summaryWithTable()

        print("summaryWithTable: ", summaryWithTable)