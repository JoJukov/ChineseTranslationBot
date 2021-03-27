from enum import Enum


class ChainTypes(Enum):
    ru_to_fr_zhCN_ru = [['ru', 'ro'], ['ro', 'fr'], ['fr', 'zh-CN'], ['zh-CN', 'ru']]
    ru_ja_zhCN_ru = [['ru', 'ja'], ['ja', 'zh-CN'], ['zh-CN', 'ru']]
    ru_pl_zhCN_ru = [['ru', 'pl'], ['pl', 'zh-CN'], ['zh-CN', 'ru']]
    ru_zhTW_zhCN_ru = [['ru', 'zh-TW'], ['zh-TW', 'zh-CN'], ['zh-CN', 'ru']]
    ru_hu_yi_zhCN_ru = [['ru', 'hu'], ['hu', 'yi'], ['yi', 'zh-CN'], ['zh-CN', 'ru']]
    ru_ar_pt_zhCN_ru = [['ru', 'ar'], ['ar', 'pt'], ['pt', 'zh-CN'], ['zh-CN', 'ru']]
    ru_cs_fa_zhCN_ru = [['ru', 'cs'], ['cs', 'fa'], ['fa', 'zh-CN'], ['zh-CN', 'ru']]
    ru_bn_de_sw_zhCN_ru = [['ru', 'bn'], ['bn', 'de'], ['de', 'sw'], ['sw', 'zh-CN'], ['zh-CN', 'ru']]
