# coding: utf-8

"""
EWK-related process definitions.

Some DY processes contain phasespace ranges in auxiliary fields. Each each is inclusive in the lower
bound and exclusive in the upper bound, i.e. (a, b) means a <= x < b:

- mll: dilepton invariant mass range
- ptll: dilepton pt range
- njets: number of extra jets on generator level (mostly NLO)
"""

__all__ = [
    "dy",
    "dy_m4to10",
    "dy_m10to50",
    "dy_m50toinf", "dy_m50toinf_0j", "dy_m50toinf_1j", "dy_m50toinf_2j", "dy_m50toinf_ge3j",
    "dy_m50toinf_3j", "dy_m50toinf_4j",
    "dy_m50toinf_1j_pt0to40", "dy_m50toinf_1j_pt40to100", "dy_m50toinf_1j_pt100to200", "dy_m50toinf_1j_pt200to400",
    "dy_m50toinf_1j_pt400to600", "dy_m50toinf_1j_pt600toinf",
    "dy_m50toinf_2j_pt0to40", "dy_m50toinf_2j_pt40to100", "dy_m50toinf_2j_pt100to200", "dy_m50toinf_2j_pt200to400",
    "dy_m50toinf_2j_pt400to600", "dy_m50toinf_2j_pt600toinf",
    "dy_0j", "dy_1j", "dy_2j",
    "dy_m50toinf_ht70to100", "dy_m50toinf_ht100to200", "dy_m50toinf_ht200to400",
    "dy_m50toinf_ht400to600", "dy_m50toinf_ht600to800", "dy_m50toinf_ht800to1200",
    "dy_m50toinf_ht1200to2500", "dy_m50toinf_ht2500toinf",
    "dy_pt0to50", "dy_pt50to100", "dy_pt100to250", "dy_pt250to400",
    "dy_pt400to650", "dy_pt650toinf",
    "z",
    "z_nunu",
    "z_nunu_ht100to200", "z_nunu_ht200to400", "z_nunu_ht400to600",
    "z_nunu_ht600to800", "z_nunu_ht800to1200", "z_nunu_ht1200to2500",
    "z_nunu_ht2500toinf",
    "z_qq",
    "z_qq_ht200to400", "z_qq_ht400to600", "z_qq_ht600to800", "z_qq_ht800toinf",
    "w",
    "w_taunu", "w_munu",
    "w_lnu",
    "w_lnu_ht70to100", "w_lnu_ht100to200", "w_lnu_ht200to400", "w_lnu_ht400to600",
    "w_lnu_ht600to800", "w_lnu_ht800to1200", "w_lnu_ht1200to2500", "w_lnu_ht2500toinf",
    "ewk",
    "ewk_wp_lnu_m50toinf", "ewk_wm_lnu_m50toinf", "ewk_z_ll_m50toinf",
    "vv",
    "zz",
    "zz_zqq_zll_m4toinf", "zz_zll_znunu_m4toinf", "zz_zll_zll_m4toinf", "zz_zqq_zqq", "zz_znunu_zqq",
    "wz", "wz_wlnu_zll_m4toinf", "wz_wqq_zll_m4toinf", "wz_wlnu_zqq",
    "ww",
    "ww_dl", "ww_sl", "ww_fh",
    "vvv",
    "zzz", "wzz", "wwz", "www",

]


from order import Process
from scinum import Number

import cmsdb.constants as const


#
# Drell-Yan
#

dy = Process(
    name="dy",
    id=50000,
    label="Drell-Yan",
    xsecs={13: Number(0.1)},  # TODO
)

# NNLO cross section, based on:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV?rev=28
# and for 13.6 TeV, based on:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV?rev=12

# if needed for scaling from NLO to NNLO:
# NLO cross section, based on GenXSecAnalyzer for
# DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
dy_m50toinf_nlo_13tev_xsec = Number(6421.0, {"tot": 11.25})

# if needed for scaling from LO to NNLO:
# LO cross section, based on GenXSecAnalyzer for DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
dy_m50toinf_lo_13tev_xsec = Number(5395.0, {"tot": 1.858})

# 13.6 TeV LO and NLO cross sections are based on GenXSecAnalyzer with CMSSW_13_0_13
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2 -n 5000000  # noqa
# or -c Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v1 when needed
dy_m4to10_nlo_13p6tev_xsec = Number(141600, {"tot": 79.81})  # xsdb: Number(141500, {"tot": 301.9})
dy_m10to50_nlo_13p6tev_xsec = Number(21170.0, {"tot": 18.38})  # xsdb: Number(20950.0, {"tot": 183.5})
dy_m50toinf_nlo_13p6tev_xsec = Number(6728.0, {"tot": 6.981})  # xsdb: Number(6688.0, {"tot": 83.99})

dy_m10to50_lo_13p6tev_xsec = Number(17410, {"tot": 2.393})
dy_m50toinf_lo_13p6tev_xsec = Number(5450, {"tot": 1.872})

dy_m50toinf = dy.add_process(
    name="dy_m50toinf",
    id=51100,
    xsecs={
        13: Number(6077.22, {
            "integration": 1.49,
            "scale": 0.02j,
            "pdf": 14.78,
        }),
        13.6: const.n_leps * Number(2091.7, {
            "scale": (0.008j, 0.013j),
            "pdf": 0.01j,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
    },
)

dy_k_factor_lo_to_nnlo = {
    13: dy_m50toinf.get_xsec(13) / dy_m50toinf_lo_13tev_xsec,
    13.6: dy_m50toinf.get_xsec(13.6) / dy_m50toinf_lo_13p6tev_xsec,
}
dy_k_factor_nlo_to_nnlo = {
    13: dy_m50toinf.get_xsec(13) / dy_m50toinf_nlo_13tev_xsec,
    13.6: dy_m50toinf.get_xsec(13.6) / dy_m50toinf_nlo_13p6tev_xsec,
}


dy_m4to10 = dy.add_process(
    name="dy_m4to10",
    id=51002,
    xsecs={
        13: Number(0.1),  # TODO
        13.6: dy_m4to10_nlo_13p6tev_xsec * dy_k_factor_nlo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 10.0),
    },
)
dy_m10to50 = dy.add_process(
    name="dy_m10to50",
    id=51001,
    xsecs={
        13: Number(0.1),  # TODO
        13.6: dy_m10to50_nlo_13p6tev_xsec * dy_k_factor_nlo_to_nnlo[13.6],
    },
    aux={
        "mll": (10.0, 50.0),
    },
)

#
# N-jet binned Drell-Yan (scaled to NNLO)
#

# 13.6 TeV xsecs based on XSDB for datasets DYto2L-4Jets_MLL-50_{i}J_TuneCP5_13p6TeV_madgraphMLM-pythia8
# e.g. https://xsdb-temp.app.cern.ch/xsdb/?columns=39911424&currentPage=0&pageSize=10&searchQuery=DAS%3DDYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8  # noqa
# 13 TeV: based on GenXSecAnalyzer
# for datasets DY{i}JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa

dy_m50toinf_0j = dy_m50toinf.add_process(
    name="dy_m50toinf_0j",
    id=51110,
    xsecs={
        # NLO xsec taken from https://xsdb-temp.app.cern.ch/xsdb/?columns=39911424&currentPage=0&pageSize=10&searchQuery=DAS%3DDYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  # noqa
        13.6: Number(5378, {"tot": 8.007}) * dy_k_factor_nlo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (0, 1),
    },
)

dy_m50toinf_1j = dy_m50toinf.add_process(
    name="dy_m50toinf_1j",
    id=51111,
    xsecs={
        13: Number(926.8, {
            "tot": 0.3597,
        }) * dy_k_factor_lo_to_nnlo[13],
        # 13.6: Number(1017, {"tot": 6.264}) * dy_k_factor_nlo_to_nnlo[13.6],
        13.6: Number(973.1, {"tot": 2.613}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
    },
)

dy_m50toinf_2j = dy_m50toinf.add_process(
    name="dy_m50toinf_2j",
    id=51112,
    xsecs={
        13: Number(294.5, {
            "tot": 0.1223,
        }) * dy_k_factor_lo_to_nnlo[13],
        # 13.6: Number(385.5, {"tot": 3.858}) * dy_k_factor_nlo_to_nnlo[13.6],
        13.6: Number(312.4, {"tot": 0.915}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
    },
)

dy_m50toinf_3j = dy_m50toinf.add_process(
    name="dy_m50toinf_3j",
    id=51113,
    xsecs={
        13: Number(86.53, {
            "tot": 0.03853,
        }) * dy_k_factor_lo_to_nnlo[13],
        13.6: Number(93.93, {"tot": 0.2858}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (3, 4),
    },
)

dy_m50toinf_4j = dy_m50toinf.add_process(
    name="dy_m50toinf_4j",
    id=51114,
    xsecs={
        13: Number(41.21, {
            "tot": 0.02392,
        }) * dy_k_factor_lo_to_nnlo[13],
        13.6: Number(45.43, {"tot": 0.1393}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (4, 5),
    },
)

dy_m50toinf_ge3j = dy_m50toinf.add_process(
    name="dy_m50toinf_ge3j",
    id=51115,
    aux={
        "mll": (50.0, const.inf),
        "njets": (3, const.inf),
    },
)

# based on GenXSecAnalyzer
# for DYJetsToLL_{i}J_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
dy_0j = dy.add_process(
    name="dy_0j",
    id=51200,
    xsecs={
        13: Number(5134.0, {
            "tot": 5.365,
        }),
    },
    aux={
        "njets": (0, 1),
    },
)

dy_1j = dy.add_process(
    name="dy_1j",
    id=51300,
    xsecs={
        13: Number(952.7, {
            "tot": 2.174,
        }),
    },
    aux={
        "njets": (1, 2),
    },
)

dy_2j = dy.add_process(
    name="dy_2j",
    id=51400,
    xsecs={
        13: Number(359.1, {
            "tot": 1.533,
        }),
    },
    aux={
        "njets": (2, 3),
    },
)

dy_m50toinf_1j_pt0to40 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt0to40",
    id=511110,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (0.0, 40.0),
    },
)

dy_m50toinf_1j_pt40to100 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt40to100",
    id=511111,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (40.0, 100.0),
    },
)

dy_m50toinf_1j_pt100to200 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt100to200",
    id=511112,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (100.0, 200.0),
    },
)

dy_m50toinf_1j_pt200to400 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt200to400",
    id=511113,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (200.0, 400.0),
    },
)

dy_m50toinf_1j_pt400to600 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt400to600",
    id=511114,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (400.0, 600.0),
    },
)

dy_m50toinf_1j_pt600toinf = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt600toinf",
    id=511115,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (600.0, const.inf),
    },
)

dy_m50toinf_2j_pt0to40 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt0to40",
    id=511120,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (0.0, 40.0),
    },
)

dy_m50toinf_2j_pt40to100 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt40to100",
    id=511121,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (40.0, 100.0),
    },
)

dy_m50toinf_2j_pt100to200 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt100to200",
    id=511122,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (100.0, 200.0),
    },
)

dy_m50toinf_2j_pt200to400 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt200to400",
    id=511123,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (200.0, 400.0),
    },
)

dy_m50toinf_2j_pt400to600 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt400to600",
    id=511124,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (400.0, 600.0),
    },
)

dy_m50toinf_2j_pt600toinf = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt600toinf",
    id=511125,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (600.0, const.inf),
    },
)

# LO cross sections, scaled to NNLO

# based on GenXSecAnalyzer
# for DYJetsToLL_M-50_HT-{i}to{j}_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
dy_m50toinf_ht70to100 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht70to100",
    id=51121,
    xsecs={
        13: Number(139.9, {"tot": 0.5747}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": [70.0, 100.0],
    },
)

dy_m50toinf_ht100to200 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht100to200",
    id=51122,
    xsecs={
        13: Number(140.1, {"tot": 0.5875}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": [100.0, 200.0],
    },
)

dy_m50toinf_ht200to400 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht200to400",
    id=51123,
    xsecs={
        13: Number(38.38, {"tot": 0.01628}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": [200.0, 400.0],
    },
)

dy_m50toinf_ht400to600 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht400to600",
    id=51124,
    xsecs={
        13: Number(5.212, {"tot": 0.003149}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": [400.0, 600.0],
    },
)

dy_m50toinf_ht600to800 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht600to800",
    id=51125,
    xsecs={
        13: Number(1.266, {"tot": 0.0007976}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": [600.0, 800.0],
    },
)

dy_m50toinf_ht800to1200 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht800to1200",
    id=51126,
    xsecs={
        13: Number(0.5684, {"tot": 0.0003515}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": [800.0, 1200.0],
    },
)

dy_m50toinf_ht1200to2500 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht1200to2500",
    id=51127,
    xsecs={
        13: Number(0.1332, {"tot": 0.00009084}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": [1200.0, 2500.0],
    },
)

dy_m50toinf_ht2500toinf = dy_m50toinf.add_process(
    name="dy_m50toinf_ht2500toinf",
    id=51128,
    xsecs={
        13: Number(0.002977, {"tot": 0.000003412}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": [2500.0, const.inf],
    },
)

# based on GenXSecAnalyzer
# for DYJetsToLL_LHEFilterPtZ-{i}To{j}_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
dy_pt0to50 = dy.add_process(
    name="dy_pt0to50",
    id=51510,
    xsecs={
        13: Number(1494.0, {
            "tot": 1.751,
        }),
    },
    aux={
        "ptll": (0.0, 50.0),
    },
)

dy_pt50to100 = dy.add_process(
    name="dy_pt50to100",
    id=51520,
    xsecs={
        13: Number(398.3, {
            "tot": 0.5600,
        }),
    },
    aux={
        "ptll": (50.0, 100.0),
    },
)

dy_pt100to250 = dy.add_process(
    name="dy_pt100to250",
    id=51530,
    xsecs={
        13: Number(96.58, {
            "tot": 0.1370,
        }),
    },
    aux={
        "ptll": (100.0, 250.0),
    },
)

dy_pt250to400 = dy.add_process(
    name="dy_pt250to400",
    id=51540,
    xsecs={
        13: Number(3.738, {
            "tot": 0.005305,
        }),
    },
    aux={
        "ptll": (250.0, 400.0),
    },
)

dy_pt400to650 = dy.add_process(
    name="dy_pt400to650",
    id=51550,
    xsecs={
        13: Number(0.5050, {
            "tot": 0.0008169,
        }),
    },
    aux={
        "ptll": (400.0, 650.0),
    },
)

dy_pt650toinf = dy.add_process(
    name="dy_pt650toinf",
    id=51560,
    xsecs={
        13: Number(0.04763, {
            "tot": 0.00007206,
        }),
    },
    aux={
        "ptll": (650.0, const.inf),
    },
)

#
# Z boson (no photon/DY)
#

z = Process(
    name="z",
    id=55000,
    label="Z + jets",
)

# Z -> neutrinos

z_nunu = z.add_process(
    name="z_nunu",
    id=55100,
    label=rf"{z.label} (Z $\rightarrow$ $\nu\nu$)",
)

# 13 TeV Xsecs based on GenXSecAnalyzer
# for ZJetsToNuNu_HT-{i}To{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
z_nunu_ht100to200 = z_nunu.add_process(
    name="z_nunu_ht100to200",
    id=55110,
    xsecs={
        13: Number(266.1, {
            "tot": 0.1117,
        }),
    },
)

z_nunu_ht200to400 = z_nunu.add_process(
    name="z_nunu_ht200to400",
    id=55120,
    xsecs={
        13: Number(73.00, {
            "tot": 0.04408,
        }),
    },
)

z_nunu_ht400to600 = z_nunu.add_process(
    name="z_nunu_ht400to600",
    id=55130,
    xsecs={
        13: Number(9.915, {
            "tot": 0.004229,
        }),
    },
)

z_nunu_ht600to800 = z_nunu.add_process(
    name="z_nunu_ht600to800",
    id=55140,
    xsecs={
        13: Number(2.409, {
            "tot": 0.001678,
        }),
    },
)

z_nunu_ht800to1200 = z_nunu.add_process(
    name="z_nunu_ht800to1200",
    id=55150,
    xsecs={
        13: Number(1.077, {
            "tot": 0.001295,
        }),
    },
)

z_nunu_ht1200to2500 = z_nunu.add_process(
    name="z_nunu_ht1200to2500",
    id=55160,
    xsecs={
        13: Number(0.2495, {
            "tot": 0.0007030,
        }),
    },
)

z_nunu_ht2500toinf = z_nunu.add_process(
    name="z_nunu_ht2500toinf",
    id=55170,
    xsecs={
        13: Number(0.005614, {
            "tot": 0.00001616,
        }),
    },
)

# Z -> quarks

# 13 TeV Xsecs based on GenXSecAnalyzer
# for ZJetsToQQ_HT-{i}to{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
z_qq = z.add_process(
    name="z_qq",
    id=55210,
    label=rf"{z.label} (Z $\rightarrow$ $\text{{q}}\overline{{\text{{q}}}}$)",
    xsecs={
        13: Number(0.1),  # TODO
    },
)

z_qq_ht200to400 = z_qq.add_process(
    name="z_qq_ht200to400",
    id=55210,
    xsecs={
        13: Number(1012.0, {
            "tot": 0.4260,
        }),
    },
)

z_qq_ht400to600 = z_qq.add_process(
    name="z_qq_ht400to600",
    id=55220,
    xsecs={
        13: Number(114.5, {
            "tot": 0.04884,
        }),
    },
)

z_qq_ht600to800 = z_qq.add_process(
    name="z_qq_ht600to800",
    id=55230,
    xsecs={
        13: Number(25.38, {
            "tot": 0.01088,
        }),
    },
)

z_qq_ht800toinf = z_qq.add_process(
    name="z_qq_ht800toinf",
    id=55240,
    xsecs={
        13: Number(12.92, {
            "tot": 0.005923,
        }),
    },
)


#
# W boson
#

w = Process(
    name="w",
    id=6000,
    label="W + jets",
    # TODO, or use w.set_xsec(13, w_lnu.get_xsec(13) / const.br_w["lep"]) below?
)


w_taunu = w.add_process(
    name="w_taunu",
    id=6010,
    label=rf"{w.label} ($W \rightarrow tau\nu$)",
)

w_munu = w.add_process(
    name="w_munu",
    id=6020,
    label=rf"{w.label} ($W \rightarrow mu\nu$)",
)


# NNLO cross section, based on:
# https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV?rev=27
# and for 13.6 TeV, based on:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV?rev=12

wm_lnu_xs_13p6 = const.n_leps * Number(9009.5, {
    "scale": (0.014j, 0.012j),
    "pdf": 0.008j,
})
wp_lnu_xs_13p6 = const.n_leps * Number(12122.5, {
    "scale": (0.011j, 0.014),
    "pdf": 0.007j,
})

w_lnu = w.add_process(
    name="w_lnu",
    id=6100,
    label=rf"{w.label} ($W \rightarrow l\nu$)",
    xsecs={
        13: const.n_leps * Number(20508.9, {
            "scale": (165.7, 88.2),
            "pdf": 770.9,
        }),
        # addition necessary due to absence of combined value
        13.6: wm_lnu_xs_13p6 + wp_lnu_xs_13p6,
    },
)


# LO cross section, needed for scaling to NNLO:
# based on GenXSecAnalyzer
# for WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa

w_lnu_lo_13tev_xsec = Number(54070.0, {"tot": 18.32})

# LO cross sections, scaled to NNLO

# ht bins based on GenXSecAnalyzer
# for WJetsToLNu_HT-{i}To{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
w_lnu_ht70to100 = w_lnu.add_process(
    name="w_lnu_ht70to100",
    id=6110,
    xsecs={
        13: Number(1270.0, {"tot": 0.5259}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
)

w_lnu_ht100to200 = w_lnu.add_process(
    name="w_lnu_ht100to200",
    id=6120,
    xsecs={
        13: Number(1254.0, {"tot": 0.5274}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
)

w_lnu_ht200to400 = w_lnu.add_process(
    name="w_lnu_ht200to400",
    id=6130,
    xsecs={
        13: Number(336.6, {"tot": 0.1528}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
)

w_lnu_ht400to600 = w_lnu.add_process(
    name="w_lnu_ht400to600",
    id=6140,
    xsecs={
        13: Number(45.21, {"tot": 0.02966}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
)

w_lnu_ht600to800 = w_lnu.add_process(
    name="w_lnu_ht600to800",
    id=6150,
    xsecs={
        13: Number(10.98, {"tot": 0.006997}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
)

w_lnu_ht800to1200 = w_lnu.add_process(
    name="w_lnu_ht800to1200",
    id=6160,
    xsecs={
        13: Number(4.927, {"tot": 0.003229}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
)

w_lnu_ht1200to2500 = w_lnu.add_process(
    name="w_lnu_ht1200to2500",
    id=6170,
    xsecs={
        13: Number(1.157, {"tot": 0.0007663}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
)

# this ht bin needs the command:
# ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
w_lnu_ht2500toinf = w_lnu.add_process(
    name="w_lnu_ht2500toinf",
    id=6180,
    xsecs={
        13: Number(0.02624, {"tot": 0.00002981}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
)

#
# EWK radiations
#

ewk = Process(
    name="ewk",
    id=7000,
    label="EWK",
    # TODO: Sum over the other? maybe with scaled w xsec to inclusive?
)

# based on GenXSecAnalyzer
# for EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
ewk_wp_lnu_m50toinf = ewk.add_process(
    name="ewk_wp_lnu_m50toinf",
    id=7100,
    xsecs={
        13: Number(39.07, {"tot": 0.006454}),
    },
)

# based on GenXSecAnalyzer
# for EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
ewk_wm_lnu_m50toinf = ewk.add_process(
    name="ewk_wm_lnu_m50toinf",
    id=7200,
    xsecs={
        13: Number(32.10, {"tot": 0.005308}),
    },
)

# based on GenXSecAnalyzer
# for EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
ewk_z_ll_m50toinf = ewk.add_process(
    name="ewk_z_ll_m50toinf",
    id=7300,
    xsecs={
        13: Number(6.206, {"tot": 0.002081}),
    },
)


#
# Di-boson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
    xsecs={13: Number(0.1)},  # updated below as the sum over WW, WZ, ZZ
)

# ZZ 13 TeV xsec values at NLO from https://arxiv.org/pdf/1105.0020.pdf v1
# old value before update:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(12.13) (LO)

zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        13: Number(15.99, {"scale": (0.037j, 0.026j)}),
        # 13.6 from GenXSecAnalyzer:
        13.6: Number(12.84, {
            "tot": 0.006035,  # xsdb: Number(12.75, {"tot": 0.0649})
        }),
    },
)

# based on GenXSecAnalyzer
# for ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
zz_zqq_zll_m4toinf = zz.add_process(
    name="zz_zqq_zll_m4toinf",
    id=8110,
    xsecs={
        13: Number(3.697, {"tot": 0.002713}),
    },
)

# looking at the generator config:
# https://raw.githubusercontent.com/cms-sw/genproductions/ce68f8a7ab05f530e0a99124088c08d1cc2bf355/bin/Powheg/production/2017/13TeV/ZZ/ZZ_2L2NU_NNPDF31_13TeV.input  # noqa
# it seems that there is a lepton mass cut of 4 GeV, like in the ZZTo2Q2L channel
# therefore values from GenXSecAnalyzer
# for ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
zz_zll_znunu_m4toinf = zz.add_process(
    name="zz_zll_znunu_m4toinf",
    id=8120,
    xsecs={
        13: Number(0.9738, {"tot": 0.0009971}),
    },
)

# looking at the generator config:
# https://raw.githubusercontent.com/cms-sw/genproductions/ce68f8a7ab05f530e0a99124088c08d1cc2bf355/bin/Powheg/production/2017/13TeV/ZZ/ZZ_4L_NNPDF31_13TeV.input  # noqa
# it seems that there is a lepton mass cut of 4 GeV, like in the ZZTo2Q2L channel
# therefore values from GenXSecAnalyzer
# from ZZTo4L_TuneCP5_13TeV_powheg_pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
zz_zll_zll_m4toinf = zz.add_process(
    name="zz_zll_zll_m4toinf",
    id=8130,
    xsecs={
        13: Number(1.325, {"tot": 0.00122}),
    },
)

# no additional cut found in generator card in MCM:
# dataset: /ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM  # noqa
# therefore, value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# for ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) -> value : Number(3.287, {"tot": 0.006298})
# also available, but not used here
zz_zqq_zqq = zz.add_process(
    name="zz_zqq_zqq",
    id=8140,
    xsecs={
        13: zz.get_xsec(13) * const.br_z["qq"] * const.br_z["qq"],  # value around 7.8
    },
)

# no branching ratio Z->nunu available, so taking values from GenXSecAnalyzer
# for ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
zz_znunu_zqq = zz.add_process(
    name="zz_znunu_zqq",
    id=8150,
    xsecs={
        13: Number(4.557, {"tot": 0.004843}),
    },
)

# WZ xsec values at NLO from https://arxiv.org/pdf/1105.0020.pdf v1
wp_z_xsec = {
    13: Number(28.55, {"scale": (0.041j, 0.032j)}),
}

wm_z_xsec = {
    13: Number(18.19, {"scale": (0.041j, 0.033j)}),
}

# old value before update:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(25.56) (LO)
wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        # as a remark, the W cross section calculation from
        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV?rev=28
        # shows a permille difference in the values calculated directly and the ones added from w+ and w-
        13: wp_z_xsec[13] + wm_z_xsec[13],
        # 13.6 from GenXSecAnalyzer:
        13.6: Number(29.17, {
            "tot": 0.005941,  # xsdb: Number(29.1, {"tot": 0.1318}),
        }),
    },
)

# looking at the generator config:
# https://github.com/cms-sw/genproductions/blob/2422e1837f93f875c54f8ace0f02d3dc962eca41/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/WZTo3LNu01j_5f_NLO_FXFX/WZTo3LNu01j_5f_NLO_FXFX_run_card.dat  # noqa
# it seems that there is a lepton mass cut of 4 GeV for leptons from Z, like in the ZZTo2Q2L channel
# therefore values from GenXSecAnalyzer
# for WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
wz_wlnu_zll_m4toinf = wz.add_process(
    name="wz_wlnu_zll_m4toinf",
    id=8210,
    xsecs={
        13: Number(5.218, {"tot": 0.00525}),
    },
)

# based on GenXSecAnalyzer
# for WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
wz_wqq_zll_m4toinf = wz.add_process(
    name="wz_wqq_zll_m4toinf",
    id=8220,
    xsecs={
        13: Number(6.431, {"tot": 0.007851}),
    },
)


# no additional cut found in generator card in MCM:
# dataset: /WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM  # noqa
# therefore, value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# for WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) -> value : Number(9.159, {"tot": 0.008259})
# also available, but not used here
wz_wlnu_zqq = wz.add_process(
    name="wz_wlnu_zqq",
    id=8230,
    xsecs={
        13: wz.get_xsec(13) * const.br_w["lep"] * const.br_z["qq"],  # value around 10.65
    },
)

# NNLO QCD from https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV?rev=28
# itself from https://arxiv.org/pdf/1408.5243.pdf v1

# old value before update:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(75.91) (LO)
ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        13: Number(118.7, {"scale": (0.025j, 0.022j)}),
        # 13.6 from GenXSecAnalyzer:
        13.6: Number(80.22, {
            "tot": 0.01677,  # xsdb: Number(80.23, {"tot": 0.3733})
        }),
    },
)

# update vv cross section
for cme in [13]:
    vv.set_xsec(cme, ww.get_xsec(cme) + wz.get_xsec(cme) + zz.get_xsec(cme))

# no additional cut found in generator card:
# https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/Powheg/production/2017/13TeV/WWTo2L2Nu_NNPDF31nnlo_13TeV/WWTo2L2Nu_NNPDF31nnlo_13TeV.input  # noqa
# therefore, value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8 (Summer20UL16, NLO) with Number(11.09, {"tot": 0.00704})
# also available, but not used here
ww_dl = ww.add_process(
    name="ww_dl",
    id=8310,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.dl,  # value around 12.6 for comparison to GenXSecAnalyzer NLO result
    },
)

# no additional cut found in generator card in MCM:
# dataset: /WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM  # noqa
# therefore, value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# for WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) -> value : Number(50.94, {"tot": 0.042})
# also available, but not used here
ww_sl = ww.add_process(
    name="ww_sl",
    id=8320,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.sl,  # value around 50.06 for comparison to GenXSecAnalyzer NLO result
    },
)

# no additional cut found in generator card in MCM:
# dataset: /WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM  # noqa
# therefore, value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# for WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) -> value : Number(51.53, {"tot": 0.04349})
# also available, but not used here
ww_fh = ww.add_process(
    name="ww_fh",
    id=8330,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.fh,  # value around 53.94 for comparison to GenXSecAnalyzer NLO result
    },
)


#
# Triple-boson
#

vvv = Process(
    name="vvv",
    id=9000,
    label="Triple-Boson",
    # xsecs set below as sum over individual processes
)

# based on GenXSecAnalyzer
# for ZZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO)
# remark: calculated xsec has lower error for sample without ext-1 as not all events were used for calculation of ext-1
# therefore the value for the sample without ext-1 is taken
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
zzz = vvv.add_process(
    name="zzz",
    id=9100,
    xsecs={
        13: Number(0.01476, {"tot": 2.347 * 10**(-6)}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.01591, {
            "tot": 0.000007828,
        }),
    },
)

# based on GenXSecAnalyzer
# for WZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
wzz = vvv.add_process(
    name="wzz",
    id=9200,
    xsecs={
        13: Number(0.05709, {"tot": 6.213 * 10**(-5)}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.06206, {
            "tot": 0.00003689,
        }),
    },
)

# based on GenXSecAnalyzer
# for WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
wwz = vvv.add_process(
    name="wwz",
    id=9300,
    xsecs={
        13: Number(0.1707, {"tot": 0.0001757}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.1851, {
            "tot": 0.00009482,
        }),
    },
)

# based on GenXSecAnalyzer
# for WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
www = vvv.add_process(
    name="www",
    id=9400,
    xsecs={
        13: Number(0.2158, {"tot": 0.0002479}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.2328, {
            "tot": 0.0001247,
        }),
    },
)

# update vvv cross section
for cme in [13]:
    vvv.set_xsec(cme, www.get_xsec(cme) + wwz.get_xsec(cme) + wzz.get_xsec(cme) + zzz.get_xsec(cme))
