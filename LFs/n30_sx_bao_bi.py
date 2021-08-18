#author=hanghust

from snorkel.labeling import labeling_function
from snorkel.preprocess.nlp import SpacyPreprocessor
spacy_cn = SpacyPreprocessor(text_field="company_name", doc_field="doc", memoize=True)

@labeling_function(pre=[spacy_cn])
def sx_bao_bi_30(x):
    sx_bao_bi = set(['bao_bì', 'nhãn_mác', 'bao', 'bì', 'nắp'])
    # if any(substring in x.company_name for substring in sx_bao_bi_cn):
    #     return 30
    for substring in sx_bao_bi:
        if substring in x.name_cleaned and x.check_btype == 'Sản xuất bao bì':
            return 30
    return -1

@labeling_function(pre=[spacy_cn])
def company_sx_bao_bi_30(x):
    sx_bao_bi_cn = set(['bao_bì', 'nhãn_mác'])
    # if any(substring in x.company_name for substring in sx_bao_bi_cn):
    #     return 30
    for substring in sx_bao_bi_cn:
        if substring in x.company_name:
            return 30
    return -1

lfs = [sx_bao_bi_30, company_sx_bao_bi_30]

def get_lfs():
    return lfs 