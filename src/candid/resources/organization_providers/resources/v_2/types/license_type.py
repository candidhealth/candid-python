# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LicenseType(str, enum.Enum):
    MD = "MD"
    NP = "NP"
    PA = "PA"
    LMFT = "LMFT"
    LCPC = "LCPC"
    LCSW = "LCSW"
    PMHNP = "PMHNP"
    FNP = "FNP"
    LPCC = "LPCC"
    DO = "DO"
    RD = "RD"
    SLP = "SLP"
    APRN = "APRN"
    LPC = "LPC"
    PHD = "PHD"
    PSYD = "PSYD"
    LMSW = "LMSW"
    LMHC = "LMHC"
    OTHER_MASTERS = "OTHER_MASTERS"
    BCBA = "BCBA"
    UNKNOWN = "UNKNOWN"
    RPH = "RPH"
    PHT = "PHT"
    LAC = "LAC"
    LMT = "LMT"
    DC = "DC"
    ND = "ND"
    MA = "MA"
    PT = "PT"
    IBCLC = "IBCLC"
    RN = "RN"
    DPT = "DPT"
    LCMHC = "LCMHC"
    CNM = "CNM"
    RNFA = "RNFA"
    ACSW = "ACSW"
    APC = "APC"
    BCABA = "BCABA"
    BHA = "BHA"
    OD = "OD"
    DPM = "DPM"
    DA = "DA"
    DDS = "DDS"
    DEH = "DEH"
    DMD = "DMD"
    PTA = "PTA"
    LCADC = "LCADC"
    LCAT = "LCAT"
    LCMHCS = "LCMHCS"
    LCMHCA = "LCMHCA"
    LCSWA = "LCSWA"
    LICSW = "LICSW"
    LISW = "LISW"
    LMFTS = "LMFTS"
    LMFTA = "LMFTA"
    LPCI = "LPCI"
    LSCSW = "LSCSW"
    MHCA = "MHCA"
    MHT = "MHT"
    RBT = "RBT"
    RCSWI = "RCSWI"
    RHMCI = "RHMCI"
    LPN = "LPN"
    OTD = "OTD"
    OMS = "OMS"
    MFTA = "MFTA"
    APCC = "APCC"
    DNP = "DNP"
    AGNPBC = "AGNPBC"
    ANP = "ANP"
    FNPPP = "FNPPP"
    LCSWR = "LCSWR"
    ALC = "ALC"
    RMFTI = "RMFTI"
    LAMFT = "LAMFT"
    LPCA = "LPCA"
    LSWI = "LSWI"
    CSW = "CSW"
    CPC = "CPC"
    LGMFT = "LGMFT"
    LLPC = "LLPC"
    PLPC = "PLPC"
    PLMFT = "PLMFT"
    LMHCA = "LMHCA"
    CIT = "CIT"
    CT = "CT"
    MFT = "MFT"
    LSW = "LSW"
    PLMHP = "PLMHP"
    PCMSW = "PCMSW"
    LMHP = "LMHP"
    OTRL = "OTR/L"
    RPA = "RPA"
    COTA = "COTA"
    CRNP = "CRNP"
    _UNKNOWN = "__LICENSETYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "LicenseType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        md: typing.Callable[[], T_Result],
        np: typing.Callable[[], T_Result],
        pa: typing.Callable[[], T_Result],
        lmft: typing.Callable[[], T_Result],
        lcpc: typing.Callable[[], T_Result],
        lcsw: typing.Callable[[], T_Result],
        pmhnp: typing.Callable[[], T_Result],
        fnp: typing.Callable[[], T_Result],
        lpcc: typing.Callable[[], T_Result],
        do: typing.Callable[[], T_Result],
        rd: typing.Callable[[], T_Result],
        slp: typing.Callable[[], T_Result],
        aprn: typing.Callable[[], T_Result],
        lpc: typing.Callable[[], T_Result],
        phd: typing.Callable[[], T_Result],
        psyd: typing.Callable[[], T_Result],
        lmsw: typing.Callable[[], T_Result],
        lmhc: typing.Callable[[], T_Result],
        other_masters: typing.Callable[[], T_Result],
        bcba: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        rph: typing.Callable[[], T_Result],
        pht: typing.Callable[[], T_Result],
        lac: typing.Callable[[], T_Result],
        lmt: typing.Callable[[], T_Result],
        dc: typing.Callable[[], T_Result],
        nd: typing.Callable[[], T_Result],
        ma: typing.Callable[[], T_Result],
        pt: typing.Callable[[], T_Result],
        ibclc: typing.Callable[[], T_Result],
        rn: typing.Callable[[], T_Result],
        dpt: typing.Callable[[], T_Result],
        lcmhc: typing.Callable[[], T_Result],
        cnm: typing.Callable[[], T_Result],
        rnfa: typing.Callable[[], T_Result],
        acsw: typing.Callable[[], T_Result],
        apc: typing.Callable[[], T_Result],
        bcaba: typing.Callable[[], T_Result],
        bha: typing.Callable[[], T_Result],
        od: typing.Callable[[], T_Result],
        dpm: typing.Callable[[], T_Result],
        da: typing.Callable[[], T_Result],
        dds: typing.Callable[[], T_Result],
        deh: typing.Callable[[], T_Result],
        dmd: typing.Callable[[], T_Result],
        pta: typing.Callable[[], T_Result],
        lcadc: typing.Callable[[], T_Result],
        lcat: typing.Callable[[], T_Result],
        lcmhcs: typing.Callable[[], T_Result],
        lcmhca: typing.Callable[[], T_Result],
        lcswa: typing.Callable[[], T_Result],
        licsw: typing.Callable[[], T_Result],
        lisw: typing.Callable[[], T_Result],
        lmfts: typing.Callable[[], T_Result],
        lmfta: typing.Callable[[], T_Result],
        lpci: typing.Callable[[], T_Result],
        lscsw: typing.Callable[[], T_Result],
        mhca: typing.Callable[[], T_Result],
        mht: typing.Callable[[], T_Result],
        rbt: typing.Callable[[], T_Result],
        rcswi: typing.Callable[[], T_Result],
        rhmci: typing.Callable[[], T_Result],
        lpn: typing.Callable[[], T_Result],
        otd: typing.Callable[[], T_Result],
        oms: typing.Callable[[], T_Result],
        mfta: typing.Callable[[], T_Result],
        apcc: typing.Callable[[], T_Result],
        dnp: typing.Callable[[], T_Result],
        agnpbc: typing.Callable[[], T_Result],
        anp: typing.Callable[[], T_Result],
        fnppp: typing.Callable[[], T_Result],
        lcswr: typing.Callable[[], T_Result],
        alc: typing.Callable[[], T_Result],
        rmfti: typing.Callable[[], T_Result],
        lamft: typing.Callable[[], T_Result],
        lpca: typing.Callable[[], T_Result],
        lswi: typing.Callable[[], T_Result],
        csw: typing.Callable[[], T_Result],
        cpc: typing.Callable[[], T_Result],
        lgmft: typing.Callable[[], T_Result],
        llpc: typing.Callable[[], T_Result],
        plpc: typing.Callable[[], T_Result],
        plmft: typing.Callable[[], T_Result],
        lmhca: typing.Callable[[], T_Result],
        cit: typing.Callable[[], T_Result],
        ct: typing.Callable[[], T_Result],
        mft: typing.Callable[[], T_Result],
        lsw: typing.Callable[[], T_Result],
        plmhp: typing.Callable[[], T_Result],
        pcmsw: typing.Callable[[], T_Result],
        lmhp: typing.Callable[[], T_Result],
        otrl: typing.Callable[[], T_Result],
        rpa: typing.Callable[[], T_Result],
        cota: typing.Callable[[], T_Result],
        crnp: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is LicenseType.MD:
            return md()
        if self is LicenseType.NP:
            return np()
        if self is LicenseType.PA:
            return pa()
        if self is LicenseType.LMFT:
            return lmft()
        if self is LicenseType.LCPC:
            return lcpc()
        if self is LicenseType.LCSW:
            return lcsw()
        if self is LicenseType.PMHNP:
            return pmhnp()
        if self is LicenseType.FNP:
            return fnp()
        if self is LicenseType.LPCC:
            return lpcc()
        if self is LicenseType.DO:
            return do()
        if self is LicenseType.RD:
            return rd()
        if self is LicenseType.SLP:
            return slp()
        if self is LicenseType.APRN:
            return aprn()
        if self is LicenseType.LPC:
            return lpc()
        if self is LicenseType.PHD:
            return phd()
        if self is LicenseType.PSYD:
            return psyd()
        if self is LicenseType.LMSW:
            return lmsw()
        if self is LicenseType.LMHC:
            return lmhc()
        if self is LicenseType.OTHER_MASTERS:
            return other_masters()
        if self is LicenseType.BCBA:
            return bcba()
        if self is LicenseType.UNKNOWN:
            return unknown()
        if self is LicenseType.RPH:
            return rph()
        if self is LicenseType.PHT:
            return pht()
        if self is LicenseType.LAC:
            return lac()
        if self is LicenseType.LMT:
            return lmt()
        if self is LicenseType.DC:
            return dc()
        if self is LicenseType.ND:
            return nd()
        if self is LicenseType.MA:
            return ma()
        if self is LicenseType.PT:
            return pt()
        if self is LicenseType.IBCLC:
            return ibclc()
        if self is LicenseType.RN:
            return rn()
        if self is LicenseType.DPT:
            return dpt()
        if self is LicenseType.LCMHC:
            return lcmhc()
        if self is LicenseType.CNM:
            return cnm()
        if self is LicenseType.RNFA:
            return rnfa()
        if self is LicenseType.ACSW:
            return acsw()
        if self is LicenseType.APC:
            return apc()
        if self is LicenseType.BCABA:
            return bcaba()
        if self is LicenseType.BHA:
            return bha()
        if self is LicenseType.OD:
            return od()
        if self is LicenseType.DPM:
            return dpm()
        if self is LicenseType.DA:
            return da()
        if self is LicenseType.DDS:
            return dds()
        if self is LicenseType.DEH:
            return deh()
        if self is LicenseType.DMD:
            return dmd()
        if self is LicenseType.PTA:
            return pta()
        if self is LicenseType.LCADC:
            return lcadc()
        if self is LicenseType.LCAT:
            return lcat()
        if self is LicenseType.LCMHCS:
            return lcmhcs()
        if self is LicenseType.LCMHCA:
            return lcmhca()
        if self is LicenseType.LCSWA:
            return lcswa()
        if self is LicenseType.LICSW:
            return licsw()
        if self is LicenseType.LISW:
            return lisw()
        if self is LicenseType.LMFTS:
            return lmfts()
        if self is LicenseType.LMFTA:
            return lmfta()
        if self is LicenseType.LPCI:
            return lpci()
        if self is LicenseType.LSCSW:
            return lscsw()
        if self is LicenseType.MHCA:
            return mhca()
        if self is LicenseType.MHT:
            return mht()
        if self is LicenseType.RBT:
            return rbt()
        if self is LicenseType.RCSWI:
            return rcswi()
        if self is LicenseType.RHMCI:
            return rhmci()
        if self is LicenseType.LPN:
            return lpn()
        if self is LicenseType.OTD:
            return otd()
        if self is LicenseType.OMS:
            return oms()
        if self is LicenseType.MFTA:
            return mfta()
        if self is LicenseType.APCC:
            return apcc()
        if self is LicenseType.DNP:
            return dnp()
        if self is LicenseType.AGNPBC:
            return agnpbc()
        if self is LicenseType.ANP:
            return anp()
        if self is LicenseType.FNPPP:
            return fnppp()
        if self is LicenseType.LCSWR:
            return lcswr()
        if self is LicenseType.ALC:
            return alc()
        if self is LicenseType.RMFTI:
            return rmfti()
        if self is LicenseType.LAMFT:
            return lamft()
        if self is LicenseType.LPCA:
            return lpca()
        if self is LicenseType.LSWI:
            return lswi()
        if self is LicenseType.CSW:
            return csw()
        if self is LicenseType.CPC:
            return cpc()
        if self is LicenseType.LGMFT:
            return lgmft()
        if self is LicenseType.LLPC:
            return llpc()
        if self is LicenseType.PLPC:
            return plpc()
        if self is LicenseType.PLMFT:
            return plmft()
        if self is LicenseType.LMHCA:
            return lmhca()
        if self is LicenseType.CIT:
            return cit()
        if self is LicenseType.CT:
            return ct()
        if self is LicenseType.MFT:
            return mft()
        if self is LicenseType.LSW:
            return lsw()
        if self is LicenseType.PLMHP:
            return plmhp()
        if self is LicenseType.PCMSW:
            return pcmsw()
        if self is LicenseType.LMHP:
            return lmhp()
        if self is LicenseType.OTRL:
            return otrl()
        if self is LicenseType.RPA:
            return rpa()
        if self is LicenseType.COTA:
            return cota()
        if self is LicenseType.CRNP:
            return crnp()
        return _unknown_member(self._value_)
