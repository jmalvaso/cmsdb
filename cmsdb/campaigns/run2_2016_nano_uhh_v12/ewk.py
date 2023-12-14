# coding: utf-8

"""
Electroweak datasets for the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_uhh_v12 import campaign_run2_2016_nano_uhh_v12 as cpn


#
# Drell-Yan
#
cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14284445,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=73493454,
)

# jet binned, madgraph
# cpn.add_dataset(
#     name="dy_lep_m50_1j_madgraph",
#     id=14242968,
#     processes=[procs.dy_lep_m50_1j],
#     keys=[
#         "/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=51,
#     n_events=65903452,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_2j_madgraph",
#     id=14235404,
#     processes=[procs.dy_lep_m50_2j],
#     keys=[
#         "/DY2JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=19,
#     n_events=27099640,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_3j_madgraph",
#     id=14235548,
#     processes=[procs.dy_lep_m50_3j],
#     keys=[
#         "/DY3JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=15,
#     n_events=20165687,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_4j_madgraph",
#     id=14235551,
#     processes=[procs.dy_lep_m50_4j],
#     keys=[
#         "/DY4JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=21,
#     n_events=10872554,
# )
#

# jet binned, amcatnlo
cpn.add_dataset(
    name="dy_lep_0j_amcatnlo",
    id=14300634,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=76450315,
)

cpn.add_dataset(
    name="dy_lep_1j_amcatnlo",
    id=14300598,
    processes=[procs.dy_lep_1j],
    keys=[
        "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=82168430,
)

cpn.add_dataset(
    name="dy_lep_2j_amcatnlo",
    id=14212537,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=41724743,
)

# ht binned
# cpn.add_dataset(
#     name="dy_lep_m50_ht70to100_madgraph",
#     id=14235248,
#     processes=[procs.dy_lep_m50_ht70to100],
#     keys=[
#         "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=18,
#     n_events=12205958,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_ht100to200_madgraph",
#     id=14235412,
#     processes=[procs.dy_lep_m50_ht100to200],
#     keys=[
#         "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=22,
#     n_events=18648544,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_ht200to400_madgraph",
#     id=14235285,
#     processes=[procs.dy_lep_m50_ht200to400],
#     keys=[
#         "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=37,
#     n_events=12451701,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_ht400to600_madgraph",
#     id=14234754,
#     processes=[procs.dy_lep_m50_ht400to600],
#     keys=[
#         "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=17,
#     n_events=5384252,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_ht600to800_madgraph",
#     id=14234976,
#     processes=[procs.dy_lep_m50_ht600to800],
#     keys=[
#         "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=5118706,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_ht800to1200_madgraph",
#     id=14234833,
#     processes=[procs.dy_lep_m50_ht800to1200],
#     keys=[
#         "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=16,
#     n_events=4347168,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_ht1200to2500_madgraph",
#     id=14243239,
#     processes=[procs.dy_lep_m50_ht1200to2500],
#     keys=[
#         "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=4725936,
# )
#
# cpn.add_dataset(
#     name="dy_lep_m50_ht2500_madgraph",
#     id=14244972,
#     processes=[procs.dy_lep_m50_ht2500],
#     keys=[
#         "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=12,
#     n_events=1480047,
# )
#

# pt binned

cpn.add_dataset(
    name="dy_lep_pt0To50_amcatnlo",
    id=14338354,
    processes=[procs.dy_lep_pt0To50],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-0To50_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=100567109,
)

cpn.add_dataset(
    name="dy_lep_pt50To100_amcatnlo",
    id=14336830,
    processes=[procs.dy_lep_pt50To100],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=59792819,
)

cpn.add_dataset(
    name="dy_lep_pt100To250_amcatnlo",
    id=14337510,
    processes=[procs.dy_lep_pt100To250],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=38787711,
)

cpn.add_dataset(
    name="dy_lep_pt250To400_amcatnlo",
    id=14337403,
    processes=[procs.dy_lep_pt250To400],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=12318492,
)

cpn.add_dataset(
    name="dy_lep_pt400To650_amcatnlo",
    id=14338401,
    processes=[procs.dy_lep_pt400To650],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1980401,
)

cpn.add_dataset(
    name="dy_lep_pt650_amcatnlo",
    id=14338815,
    processes=[procs.dy_lep_pt650],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2018613,
)

#
# W boson production
#

# inclusive
cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14212767,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=82754918,
)

# ht binned
cpn.add_dataset(
    name="w_lnu_ht70To100_madgraph",
    id=14215006,
    processes=[procs.w_lnu_ht70To100],
    keys=[
        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=19439931,
)

cpn.add_dataset(
    name="w_lnu_ht100To200_madgraph",
    id=14215097,
    processes=[procs.w_lnu_ht100To200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=19753958,
)

cpn.add_dataset(
    name="w_lnu_ht200To400_madgraph",
    id=14214993,
    processes=[procs.w_lnu_ht200To400],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=15067621,
)

cpn.add_dataset(
    name="w_lnu_ht400To600_madgraph",
    id=14215048,
    processes=[procs.w_lnu_ht400To600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2115509,
)

cpn.add_dataset(
    name="w_lnu_ht600To800_madgraph",
    id=14215011,
    processes=[procs.w_lnu_ht600To800],
    keys=[
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2251807,
)

cpn.add_dataset(
    name="w_lnu_ht800To1200_madgraph",
    id=14215109,
    processes=[procs.w_lnu_ht800To1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2132228,
)

cpn.add_dataset(
    name="w_lnu_ht1200To2500_madgraph",
    id=14266357,
    processes=[procs.w_lnu_ht1200To2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2090561,
)

cpn.add_dataset(
    name="w_lnu_ht2500_madgraph",
    id=14237764,
    processes=[procs.w_lnu_ht2500],
    keys=[
        "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=709514,
)

#
# Z boson production
#

cpn.add_dataset(
    name="z_nunu_ht100To200_madgraph",
    id=14215073,
    processes=[procs.z_nunu_ht100To200],
    keys=[
        "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=7083216,
)

cpn.add_dataset(
    name="z_nunu_ht200To400_madgraph",
    id=14214912,
    processes=[procs.z_nunu_ht200To400],
    keys=[
        "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=6814106,
)

cpn.add_dataset(
    name="z_nunu_ht400To600_madgraph",
    id=14281550,
    processes=[procs.z_nunu_ht400To600],
    keys=[
        "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=6114046,
)

cpn.add_dataset(
    name="z_nunu_ht600To800_madgraph",
    id=14281420,
    processes=[procs.z_nunu_ht600To800],
    keys=[
        "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1881671,
)

cpn.add_dataset(
    name="z_nunu_ht800To1200_madgraph",
    id=14281563,
    processes=[procs.z_nunu_ht800To1200],
    keys=[
        "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=633500,
)

cpn.add_dataset(
    name="z_nunu_ht1200To2500_madgraph",
    id=14281209,
    processes=[procs.z_nunu_ht1200To2500],
    keys=[
        "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=115609,
)

cpn.add_dataset(
    name="z_nunu_ht2500_madgraph",
    id=14241375,
    processes=[procs.z_nunu_ht2500],
    keys=[
        "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=110461,
)

cpn.add_dataset(
    name="z_qq_ht200To400_madgraph",
    id=14285999,
    processes=[procs.z_qq_ht200To400],
    keys=[
        "/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=7285673,
)

cpn.add_dataset(
    name="z_qq_ht400To600_madgraph",
    id=14343844,
    processes=[procs.z_qq_ht400To600],
    keys=[
        "/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=6942718,
)

cpn.add_dataset(
    name="z_qq_ht600To800_madgraph",
    id=14255955,
    processes=[procs.z_qq_ht600To800],
    keys=[
        "/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=5500386,
)

cpn.add_dataset(
    name="z_qq_ht800_madgraph",
    id=14275730,
    processes=[procs.z_qq_ht800],
    keys=[
        "/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4388402,
)


#
# EWK
# (vector boson emissions)
#

cpn.add_dataset(
    name="ewk_wm_lnu_m50_madgraph",
    id=14215052,
    processes=[procs.ewk_wm_lnu_m50],
    keys=[
        "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2202000,
)

cpn.add_dataset(
    name="ewk_w_lnu_m50_madgraph",
    id=14216740,
    processes=[procs.ewk_wp_lnu_m50],
    keys=[
        "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2033000,
)

cpn.add_dataset(
    name="ewk_z_ll_m50_madgraph",
    id=14216471,
    processes=[procs.ewk_z_ll_m50],
    keys=[
        "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=453000,
)


#
# Di-boson
#

# ZZ
cpn.add_dataset(
    name="zz_pythia",
    id=14213491,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=1141000,
)

cpn.add_dataset(
    name="zz_qqll_m4_amcatnlo",
    id=14284244,
    processes=[procs.zz_qqll_m4],
    keys=[
        "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=13740600,
)

cpn.add_dataset(
    name="zz_llnunu_powheg",
    id=14212205,
    processes=[procs.zz_llnunu],
    keys=[
        "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=15928000,
)

cpn.add_dataset(
    name="zz_llll_powheg",
    id=14344450,
    processes=[procs.zz_llll],
    keys=[
        "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=52137000,
)

cpn.add_dataset(
    name="zz_qqqq_amcatnlo",
    id=14373200,
    processes=[procs.zz_qqqq],
    keys=[
        "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=1270030,
)

cpn.add_dataset(
    name="zz_nunuqq_amcatnlo",
    id=14373276,
    processes=[procs.zz_nunuqq],
    keys=[
        "/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2468807,
)


# WZ
cpn.add_dataset(
    name="wz_pythia",
    id=14214737,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=7584000,
)

cpn.add_dataset(
    name="wz_lllnu_amcatnlo",
    id=14212844,
    processes=[procs.wz_lllnu],
    keys=[
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=10441724,
)

cpn.add_dataset(
    name="wz_qqll_m4_amcatnlo",
    id=14283305,
    processes=[procs.wz_qqll_m4],
    keys=[
        "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=13526954,
)

cpn.add_dataset(
    name="wz_lnuqq_amcatnlo",
    id=14373428,
    processes=[procs.wz_lnuqq],
    keys=[
        "/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=3690271,
)

# WW
cpn.add_dataset(
    name="ww_pythia",
    id=14212245,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=15729000,
)

cpn.add_dataset(
    name="ww_lnuqq_amcatnlo",
    id=14373365,
    processes=[procs.ww_lnuqq],
    keys=[
        "/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=19976139,
)

cpn.add_dataset(
    name="ww_lnulnu_powheg",
    id=14215099,
    processes=[procs.ww_lnulnu],
    keys=[
        "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2900000,
)

cpn.add_dataset(
    name="ww_qqqq_amcatnlo",
    id=14373147,
    processes=[procs.ww_qqqq],
    keys=[
        "/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=19814659,
)

#
# Triple-boson
#

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14213248,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1 + 4,
    n_events=72000 + 4534000,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14212107,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1 + 5,
    n_events=137000 + 4554000,
)

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=14213247,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1 + 5,
    n_events=67000 + 4595000,
)

cpn.add_dataset(
    name="www_amcatnlo",
    id=14212167,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1 + 4,
    n_events=69000 + 4243000,
)
