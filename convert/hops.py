from dbfpy import dbf
from recipe.models import Hop

file_ = "/home/gijs/.wine/drive_c/OLMSoft/BrouwVisie/Data/Hop.Dbf"

mapping = (
    ('name', 'HOPNAAM'),
    ('country', 'LAND'),
    ('dealer', 'LEVEREN'),
    ('kind', 'HOPSOORT'),
    ('alpha_min', 'ALPHA_VAN'),
    ('alpha_max', 'ALPHA_TOT'),
    ('beta_min', 'BETA_VAN'),
    ('beta_max', 'BETA_TOT'),
    ('cohumulone_min', 'COHU_VAN'),
    ('cohumulone_max', 'COHU_TOT'),
    ('hopoil_min', 'OIL_VAN'),
    ('hopoil_max', 'OIL_TOT'),
    ('humulene_min', 'HUMU_VAN'),
    ('humulene_max', 'HUMU_TOT'),
    ('caryophyllene_min', 'CARO_VAN'),
    ('caryophyllene_max', 'CARO_TOT'),
    ('myrcene_min', 'MYCR_VAN'),
    ('myrcene_max', 'MYCR_TOT'),
    ('farnesene_min', 'FARN_VAN'),
    ('farnesene_max', 'FARN_TOT'),
    ('stability', 'HOP_STAB'),
    ('decay', 'HOUDFACT'),
    ('taste', 'SMAAK'),
)

d = dbf.Dbf(file_)


for r in d:
    object = Hop()
    for to, from_ in mapping:
        value = r[from_]
        if type(value) == str:
            # looks like dbf can't handle unicode well
            value = value.decode(errors='ignore')
        setattr(object, to, value)
    object.save()
