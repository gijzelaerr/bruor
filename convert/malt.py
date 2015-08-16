from dbfpy import dbf

from recipe.models import Malt

file_ = "/home/gijs/.wine/drive_c/OLMSoft/BrouwVisie/Data/Mout.Dbf"


mapping = (
    ('name', 'MOUTNAAM'),
    ('country', 'HERKOMST'),
    ('dealer', 'LEVEREN'),
    ('kind', 'MOUTSOORT'),
    ('color', 'KLEUR'),
    ('gravity', 'POT_SG'),
    ('max_yield', 'OPBRENGST'),
    ('max_dump', 'STORTING'),
    ('moisture', 'VOCHT'),
    ('protein', 'EIWIT'),
    ('maisch', 'MAISCH'),
)

d = dbf.Dbf(file_)


for r in d:
    object = Malt()
    for to, from_ in mapping:
        value = r[from_]
        if type(value) == str:
            # looks like dbf can't handle unicode well
            value = value.decode(errors='ignore')
        setattr(object, to, value)
    object.save()
