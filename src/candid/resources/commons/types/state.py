# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class State(str, enum.Enum):
    AA = "AA"
    AE = "AE"
    AP = "AP"
    AL = "AL"
    AK = "AK"
    AS = "AS"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DC = "DC"
    DE = "DE"
    FL = "FL"
    FM = "FM"
    GA = "GA"
    GU = "GU"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MH = "MH"
    MI = "MI"
    MN = "MN"
    MP = "MP"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    PR = "PR"
    PW = "PW"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VI = "VI"
    VT = "VT"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"
    _UNKNOWN = "__STATE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "State":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        aa: typing.Callable[[], T_Result],
        ae: typing.Callable[[], T_Result],
        ap: typing.Callable[[], T_Result],
        al: typing.Callable[[], T_Result],
        ak: typing.Callable[[], T_Result],
        as_: typing.Callable[[], T_Result],
        az: typing.Callable[[], T_Result],
        ar: typing.Callable[[], T_Result],
        ca: typing.Callable[[], T_Result],
        co: typing.Callable[[], T_Result],
        ct: typing.Callable[[], T_Result],
        dc: typing.Callable[[], T_Result],
        de: typing.Callable[[], T_Result],
        fl: typing.Callable[[], T_Result],
        fm: typing.Callable[[], T_Result],
        ga: typing.Callable[[], T_Result],
        gu: typing.Callable[[], T_Result],
        hi: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
        il: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        ia: typing.Callable[[], T_Result],
        ks: typing.Callable[[], T_Result],
        ky: typing.Callable[[], T_Result],
        la: typing.Callable[[], T_Result],
        me: typing.Callable[[], T_Result],
        md: typing.Callable[[], T_Result],
        ma: typing.Callable[[], T_Result],
        mh: typing.Callable[[], T_Result],
        mi: typing.Callable[[], T_Result],
        mn: typing.Callable[[], T_Result],
        mp: typing.Callable[[], T_Result],
        ms: typing.Callable[[], T_Result],
        mo: typing.Callable[[], T_Result],
        mt: typing.Callable[[], T_Result],
        ne: typing.Callable[[], T_Result],
        nv: typing.Callable[[], T_Result],
        nh: typing.Callable[[], T_Result],
        nj: typing.Callable[[], T_Result],
        nm: typing.Callable[[], T_Result],
        ny: typing.Callable[[], T_Result],
        nc: typing.Callable[[], T_Result],
        nd: typing.Callable[[], T_Result],
        oh: typing.Callable[[], T_Result],
        ok: typing.Callable[[], T_Result],
        or_: typing.Callable[[], T_Result],
        pa: typing.Callable[[], T_Result],
        pr: typing.Callable[[], T_Result],
        pw: typing.Callable[[], T_Result],
        ri: typing.Callable[[], T_Result],
        sc: typing.Callable[[], T_Result],
        sd: typing.Callable[[], T_Result],
        tn: typing.Callable[[], T_Result],
        tx: typing.Callable[[], T_Result],
        ut: typing.Callable[[], T_Result],
        vi: typing.Callable[[], T_Result],
        vt: typing.Callable[[], T_Result],
        va: typing.Callable[[], T_Result],
        wa: typing.Callable[[], T_Result],
        wv: typing.Callable[[], T_Result],
        wi: typing.Callable[[], T_Result],
        wy: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is State.AA:
            return aa()
        if self is State.AE:
            return ae()
        if self is State.AP:
            return ap()
        if self is State.AL:
            return al()
        if self is State.AK:
            return ak()
        if self is State.AS:
            return as_()
        if self is State.AZ:
            return az()
        if self is State.AR:
            return ar()
        if self is State.CA:
            return ca()
        if self is State.CO:
            return co()
        if self is State.CT:
            return ct()
        if self is State.DC:
            return dc()
        if self is State.DE:
            return de()
        if self is State.FL:
            return fl()
        if self is State.FM:
            return fm()
        if self is State.GA:
            return ga()
        if self is State.GU:
            return gu()
        if self is State.HI:
            return hi()
        if self is State.ID:
            return id()
        if self is State.IL:
            return il()
        if self is State.IN:
            return in_()
        if self is State.IA:
            return ia()
        if self is State.KS:
            return ks()
        if self is State.KY:
            return ky()
        if self is State.LA:
            return la()
        if self is State.ME:
            return me()
        if self is State.MD:
            return md()
        if self is State.MA:
            return ma()
        if self is State.MH:
            return mh()
        if self is State.MI:
            return mi()
        if self is State.MN:
            return mn()
        if self is State.MP:
            return mp()
        if self is State.MS:
            return ms()
        if self is State.MO:
            return mo()
        if self is State.MT:
            return mt()
        if self is State.NE:
            return ne()
        if self is State.NV:
            return nv()
        if self is State.NH:
            return nh()
        if self is State.NJ:
            return nj()
        if self is State.NM:
            return nm()
        if self is State.NY:
            return ny()
        if self is State.NC:
            return nc()
        if self is State.ND:
            return nd()
        if self is State.OH:
            return oh()
        if self is State.OK:
            return ok()
        if self is State.OR:
            return or_()
        if self is State.PA:
            return pa()
        if self is State.PR:
            return pr()
        if self is State.PW:
            return pw()
        if self is State.RI:
            return ri()
        if self is State.SC:
            return sc()
        if self is State.SD:
            return sd()
        if self is State.TN:
            return tn()
        if self is State.TX:
            return tx()
        if self is State.UT:
            return ut()
        if self is State.VI:
            return vi()
        if self is State.VT:
            return vt()
        if self is State.VA:
            return va()
        if self is State.WA:
            return wa()
        if self is State.WV:
            return wv()
        if self is State.WI:
            return wi()
        if self is State.WY:
            return wy()
        return _unknown_member(self._value_)
