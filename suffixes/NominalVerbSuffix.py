#-*- coding: cp1254 -*-

from . import Suffix

S11 = Suffix("-cAsInA",    "cas�na|�as�na|cesine|�esine",      None, True)
S4  = Suffix("-sUnUz",     "s�n�z|siniz|sunuz|s�n�z",          None, True)
S14 = Suffix("-(y)mU�",    "mu�|mi�|m��|m��",                  "y",  True)
S15 = Suffix("-(y)ken",    "ken",                              "y",  True)
S2  = Suffix("-sUn",       "s�n|sin|sun|s�n",                  None, True)
S5  = Suffix("-lAr",       "lar|ler",                          None, True)
S9  = Suffix("-nUz",       "n�z|niz|nuz|n�z",                  None, True)
S10 = Suffix("-DUr",       "t�r|tir|tur|t�r|d�r|dir|dur|d�r",  None, True)
S3  = Suffix("-(y)Uz",     "�z|iz|uz|�z",                      "y",  True)
S1  = Suffix("-(y)Um",     "�m|im|um|�m",                      "y",  True)
S12 = Suffix("-(y)DU",     "d�|di|du|d�|t�|ti|tu|t�",          "y",  True)
S13 = Suffix("-(y)sA",     "sa|se",                            "y",  True)
S6  = Suffix("-m",         "m",                                None, True)
S7  = Suffix("-n",         "n",                                None, True)
S8  = Suffix("-k",         "k",                                None, True)

# The order of the enum definition determines the priority of the suffix.
# For example, -(y)ken (S15 suffix) is  checked before -n (S7 suffix).
VALUES = (S11,S4,S14,S15,S2,S5,S9,S10,S3,S1,S12,S13,S6,S7,S8)