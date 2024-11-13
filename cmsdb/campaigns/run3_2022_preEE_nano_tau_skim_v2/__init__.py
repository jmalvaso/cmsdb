from order import Campaign
#
# campaign
#

campaign_run3_2022_preEE_nano_tau_skim_v2 = Campaign(
    name="run3_2022_preEE_nano_tau_skim_v2",
    id=20221233,  # run 2 year 2022 ver 12 #33 is just for separation between different configs
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2022,
        "version": 14,
        "tag": "preEE",
        "run": 3,
        "custom": {
            "name": "run3_2022_preEE_nano_tau_skim_v2",
            "creator": "desy",
            "location": "/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2022"
        },
    },
)

import cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_v2.ewk
import cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_v2.data
import cmsdb.campaigns.run3_2022_preEE_nano_tau_skim_v2.top
