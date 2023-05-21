# import ssl
import torch
from functools import partial

# import nltk

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('punkt')

idx = torch.arange(1, 10)
print(idx[5:10])