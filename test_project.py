from project import wxtype, cigcalc, wxtypecolor

def test_wxtype():
    assert wxtype("700", "10+", "OVC") == "IFR"
    assert wxtype("3000", "8", "OVC") == "MVFR"
    assert wxtype("400", "2", "OVC") == "LIFR"
    assert wxtype("5000", "1", "OVC") == "IFR"
    assert wxtype("400", "8", "OVC") == "LIFR"
    assert wxtype("500", "2", "OVC") == "IFR"

def test_wxtypecolor():
    assert wxtypecolor("VFR")=="table-success"
    assert wxtypecolor(None)== "table-danger"
    assert wxtypecolor("IFR")== "table-danger"
    assert wxtypecolor("LIFR")== "table-danger"



def test_cigcalc():
    assert cigcalc([{"cover":None, "base":None}]) == None
    assert cigcalc([{"cover":"BKN", "base":600}]) == {"cover":"BKN", "base":600}
    assert cigcalc([{"cover":"FEW", "base":600}]) == None
    assert cigcalc([{"cover":"BKN", "base":600}]) == {"cover":"BKN", "base":600}
