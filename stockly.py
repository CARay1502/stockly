import yfinance as yf
import streamlit as st
import pandas as pd 
from pandas_datareader import data as pdr
import requests 
from pathlib import Path
from streamlit_lottie import st_lottie
from PIL import Image
from io import StringIO

# --- PAGE CONFIG --- 
st.set_page_config(
    page_title="Stockly",
    page_icon="chart_with_upwards_trend",
    layout="centered",
)
# --- PATH SETTINGS & CSS FILE LOAD--- 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

yf.pdr_override()   #  NO IDEA WHAT THIS IS LOL

# --- LANDING PAGE --- 
st.subheader("Stock Data AI Aggregator! Relevant Data & News...") 
social_media= {"Instagram": "https://www.instagram.com/stock.ly23/"}

#--- SIDE BAR BIO --- 
with st.sidebar:
    st.header("Welcome to Stockly!")
    st.subheader("Investing made easy!") 
    st.write(
        """
        We are a FinTech startup located in Charlotte, NC. Devoted to making stock data & analysis easy and efficient!
        """
    )
    st.button=social_media
    st.divider()
    st.caption("Navigate over to our Test Data Engine")
    st.lottie("https://lottie.host/0cb10a6d-aa93-409e-b6b6-5d035ba87e40/aa4qVv390m.json")

# Your plain text with security data
security_text = """
AACG|ATA Creativity Global - American Depositary Shares, each representing two common shares|G|N|N|100|N|N
AACI|Armada Acquisition Corp. I - Common Stock|G|N|N|100|N|N
AACIU|Armada Acquisition Corp. I - Unit|G|N|N|100|N|N
AACIW|Armada Acquisition Corp. I - Warrant|G|N|N|100|N|N
AADI|Aadi Bioscience, Inc. - Common Stock|S|N|N|100|N|N
AADR|AdvisorShares Dorsey Wright ADR ETF|G|N|N|100|Y|N
AAL|American Airlines Group, Inc. - Common Stock|Q|N|N|100|N|N
AAME|Atlantic American Corporation - Common Stock|G|N|N|100|N|N
AAOI|Applied Optoelectronics, Inc. - Common Stock|G|N|N|100|N|N
AAON|AAON, Inc. - Common Stock|Q|N|N|100|N|N
AAPB|GraniteShares 1.75x Long AAPL Daily ETF|G|N|N|100|Y|N
AAPD|Direxion Daily AAPL Bear 1X Shares|G|N|N|100|Y|N
AAPL|Apple Inc. - Common Stock|Q|N|N|100|N|N
AAPU|Direxion Daily AAPL Bull 1.5X Shares|G|N|N|100|Y|N
AAXJ|iShares MSCI All Country Asia ex Japan ETF|G|N|N|100|Y|N
ABAT|American Battery Technology Company - Common Stock|S|N|N|100|N|N
ABCB|Ameris Bancorp - Common Stock|Q|N|N|100|N|N
ABCL|AbCellera Biologics Inc. - Common Shares|Q|N|N|100|N|N
ABCM|Abcam plc - American Depositary Shares|Q|N|N|100|N|N
ABEO|Abeona Therapeutics Inc. - Common Stock|S|N|N|100|N|N
ABIO|ARCA biopharma, Inc. - Common Stock|S|N|N|100|N|N
ABL|Abacus Life, Inc. - Class A Common Stock|S|N|N|100|N|N
ABLLW|Abacus Life, Inc. - Warrant|S|N|N|100|N|N
ABLV|Able View Global Inc. - Class B Ordinary Shares|S|N|N|100|N|N
ABLVW|Able View Global Inc. - Warrant|S|N|N|100|N|N
ABNB|Airbnb, Inc. - Class A Common Stock|Q|N|N|100|N|N
ABOS|Acumen Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
ABSI|Absci Corporation - Common Stock|Q|N|N|100|N|N
ABUS|Arbutus Biopharma Corporation - Common Stock|Q|N|N|100|N|N
ABVC|ABVC BioPharma, Inc. - Common Stock|S|N|N|100|N|N
ACAB|Atlantic Coastal Acquisition Corp. II - Class A Common Stock|G|N|N|100|N|N
ACABU|Atlantic Coastal Acquisition Corp. II - Unit|G|N|N|100|N|N
ACABW|Atlantic Coastal Acquisition Corp. II - Warrant|G|N|N|100|N|N
ACAC|Acri Capital Acquisition Corporation - Class A Common Stock|S|N|N|100|N|N
ACACU|Acri Capital Acquisition Corporation - Unit|S|N|N|100|N|N
ACACW|Acri Capital Acquisition Corporation - Warrant|S|N|N|100|N|N
ACAD|ACADIA Pharmaceuticals Inc. - Common Stock|Q|N|N|100|N|N
ACAH|Atlantic Coastal Acquisition Corp. - Class A Common Stock|S|N|E|100|N|N
ACAHU|Atlantic Coastal Acquisition Corp. - Unit|S|N|E|100|N|N
ACAHW|Atlantic Coastal Acquisition Corp. - Warrant|S|N|E|100|N|N
ACAX|Alset Capital Acquisition Corp. - Class A Common Stock|G|N|D|100|N|N
ACAXR|Alset Capital Acquisition Corp. - Right|G|N|D|100|N|N
ACAXU|Alset Capital Acquisition Corp. - Unit|G|N|D|100|N|N
ACAXW|Alset Capital Acquisition Corp. - Warrant|G|N|D|100|N|N
ACB|Aurora Cannabis Inc. - Common Shares|S|N|D|100|N|N
ACBA|Ace Global Business Acquisition Limited - Ordinary Shares|S|N|N|100|N|N
ACBAU|Ace Global Business Acquisition Limited - Unit|S|N|N|100|N|N
ACBAW|Ace Global Business Acquisition Limited - Warrant|S|N|N|100|N|N
ACCD|Accolade, Inc. - common stock|Q|N|N|100|N|N
ACDC|ProFrac Holding Corp. - Class A Common Stock|Q|N|N|100|N|N
ACDCW|ProFrac Holding Corp. - Warrant|Q|N|N|100|N|N
ACER|Acer Therapeutics Inc. - Common Stock|S|N|D|100|N|N
ACET|Adicet Bio, Inc. - Common Stock|G|N|N|100|N|N
ACGL|Arch Capital Group Ltd. - Common Stock|Q|N|N|100|N|N
ACGLN|Arch Capital Group Ltd. - Depositary Shares, each Representing a 1/1,000th Interest in a 4.550% Non-Cumulative Preferred Share, Series G|Q|N|N|100|N|N
ACGLO|Arch Capital Group Ltd. - Depositary Shares Each Representing 1/1,000th Interest in a Share of5.45% Non-Cumulative Preferred Shares, Series F|Q|N|N|100|N|N
ACHC|Acadia Healthcare Company, Inc. - Common Stock|Q|N|N|100|N|N
ACHL|Achilles Therapeutics plc - American Depositary Shares|Q|N|D|100|N|N
ACHV|Achieve Life Sciences, Inc.  - Common Shares|S|N|N|100|N|N
ACIC|American Coastal Insurance Corporation - Common Stock|S|N|N|100|N|N
ACIU|AC Immune SA - Common Stock|G|N|N|100|N|N
ACIW|ACI Worldwide, Inc. - Common Stock|Q|N|N|100|N|N
ACLS|Axcelis Technologies, Inc. - Common Stock|Q|N|N|100|N|N
ACLX|Arcellx, Inc. - Common Stock|Q|N|N|100|N|N
ACMR|ACM Research, Inc. - Class A Common Stock|G|N|N|100|N|N
ACNB|ACNB Corporation - Common Stock|S|N|N|100|N|N
ACNT|Ascent Industries Co. - Common Stock|G|N|N|100|N|N
ACON|Aclarion, Inc. - Common Stock|S|N|D|100|N|N
ACONW|Aclarion, Inc. - Warrant|S|N|D|100|N|N
ACOR|Acorda Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
ACRS|Aclaris Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
ACRV|Acrivon Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
ACRX|AcelRx Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
ACST|Acasti Pharma, Inc.  - Class A Common Stock|S|N|N|100|N|N
ACT|Enact Holdings, Inc. - Common Stock|Q|N|N|100|N|N
ACTG|Acacia Research Corporation - Common Stock|Q|N|N|100|N|N
ACVA|ACV Auctions Inc. - Class A Common Stock|Q|N|N|100|N|N
ACWI|iShares MSCI ACWI ETF|G|N|N|100|Y|N
ACWX|iShares MSCI ACWI ex U.S. ETF|G|N|N|100|Y|N
ACXP|Acurx Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
ADAG|Adagene Inc. - ADS, each representing 1.25 ordinary shares|G|N|N|100|N|N
ADAP|Adaptimmune Therapeutics plc - American Depositary Shares|Q|N|D|100|N|N
ADBE|Adobe Inc. - Common Stock|Q|N|N|100|N|N
ADD|Color Star Technology Co., Ltd. - Class A Ordinary Shares|S|N|N|100|N|N
ADEA|Adeia Inc.  - Common Stock|Q|N|N|100|N|N
ADES|Advanced Emissions Solutions, Inc. - Common Stock|G|N|N|100|N|N
ADI|Analog Devices, Inc. - Common Stock|Q|N|N|100|N|N
ADIL|Adial Pharmaceuticals, Inc - Common Stock|S|N|N|100|N|N
ADMA|ADMA Biologics Inc - Common Stock|G|N|N|100|N|N
ADN|Advent Technologies Holdings, Inc. - Class A Common Stock|S|N|D|100|N|N
ADNWW|Advent Technologies Holdings, Inc. - Warrant|S|N|N|100|N|N
ADOC|Edoc Acquisition Corp. - Class A Ordinary Share|S|N|D|100|N|N
ADOCR|Edoc Acquisition Corp. - Right|S|N|N|100|N|N
ADOCW|Edoc Acquisition Corp. - Warrant|S|N|N|100|N|N
ADP|Automatic Data Processing, Inc. - Common Stock|Q|N|N|100|N|N
ADPT|Adaptive Biotechnologies Corporation - Common Stock|Q|N|D|100|N|N
ADSE|ADS-TEC ENERGY PLC - Ordinary Shares|S|N|N|100|N|N
ADSEW|ADS-TEC ENERGY PLC - Warrant|S|N|N|100|N|N
ADSK|Autodesk, Inc. - Common Stock|Q|N|N|100|N|N
ADTH|AdTheorent Holding Company, Inc. - Common Stock|S|N|N|100|N|N
ADTHW|AdTheorent Holding Company, Inc. - Warrants|S|N|N|100|N|N
ADTN|ADTRAN Holdings, Inc. - Common Stock|Q|N|N|100|N|N
ADTX|Aditxt, Inc. - Common Stock|S|N|D|100|N|N
ADUS|Addus HomeCare Corporation - Common Stock|Q|N|N|100|N|N
ADV|Advantage Solutions Inc.  - Class A Common Stock|Q|N|N|100|N|N
ADVM|Adverum Biotechnologies, Inc. - Common Stock|S|N|N|100|N|N
ADVWW|Advantage Solutions Inc.  - Warrant|Q|N|N|100|N|N
ADXN|Addex Therapeutics Ltd - American Depositary Shares|S|N|D|100|N|N
AEAE|AltEnergy Acquisition Corp. - Class A Common Stock|G|N|D|100|N|N
AEAEU|AltEnergy Acquisition Corp. - Unit|G|N|N|100|N|N
AEAEW|AltEnergy Acquisition Corp. - Warrant|G|N|N|100|N|N
AEHL|Antelope Enterprise Holdings Limited - Class A Ordinary Shares|S|N|N|100|N|N
AEHR|Aehr Test Systems - Common Stock|S|N|N|100|N|N
AEI|Alset Inc. - Common Stock|S|N|N|100|N|N
AEIS|Advanced Energy Industries, Inc. - Common Stock|Q|N|N|100|N|N
AEMD|Aethlon Medical, Inc. - Common Stock|S|N|D|100|N|N
AENT|Alliance Entertainment Holding Corporation - common stock|S|N|E|100|N|N
AENTW|Alliance Entertainment Holding Corporation - Warrants|S|N|E|100|N|N
AEP|American Electric Power Company, Inc. - Common Stock|Q|N|N|100|N|N
AEY|ADDvantage Technologies Group, Inc. - Common Stock|S|N|D|100|N|N
AEYE|AudioEye, Inc. - Common Stock|S|N|N|100|N|N
AEZS|Aeterna Zentaris Inc. - Common Stock|S|N|N|100|N|N
AFAR|Aura FAT Projects Acquisition Corp - Class A Ordinary Shares|G|N|N|100|N|N
AFARU|Aura FAT Projects Acquisition Corp - Unit|G|N|N|100|N|N
AFARW|Aura FAT Projects Acquisition Corp - Warrant|G|N|N|100|N|N
AFBI|Affinity Bancshares, Inc. - Common Stock|S|N|N|100|N|N
AFCG|AFC Gamma, Inc. - Common Stock|G|N|N|100|N|N
AFIB|Acutus Medical, Inc. - Common Stock|Q|N|D|100|N|N
AFMD|Affimed N.V. - Common Stock|S|N|D|100|N|N
AFRI|Forafric Global PLC - Ordinary Shares|S|N|N|100|N|N
AFRIW|Forafric Global PLC - Warrants|S|N|N|100|N|N
AFRM|Affirm Holdings, Inc. - Class A Common Stock|Q|N|N|100|N|N
AFYA|Afya Limited - Class A Common Shares|Q|N|N|100|N|N
AGAE|Allied Gaming & Entertainment Inc. - Common Stock|S|N|N|100|N|N
AGBA|AGBA Group Holding Limited - Ordinary Share|S|N|D|100|N|N
AGBAW|AGBA Group Holding Limited - Warrant|S|N|N|100|N|N
AGEN|Agenus Inc. - Common Stock|S|N|N|100|N|N
AGFY|Agrify Corporation - Common Stock|S|N|E|100|N|N
AGIL|AgileThought, Inc. - Class A Common Stock|S|N|D|100|N|N
AGILW|AgileThought, Inc. - Warrant|S|N|N|100|N|N
AGIO|Agios Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
AGLE|Aeglea BioTherapeutics, Inc. - Common Stock|S|N|N|100|N|N
AGMH|AGM Group Holdings Inc. - Class A Ordinary Shares|S|N|E|100|N|N
AGNC|AGNC Investment Corp. - Common Stock|Q|N|N|100|N|N
AGNCL|AGNC Investment Corp. - Depositary Shares Each Representing a 1/1,000th Interest in a Share of 7.75% Series G Fixed-Rate Reset Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
AGNCM|AGNC Investment Corp. - Depositary Shares rep 6.875% Series D Fixed-to-Floating Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
AGNCN|AGNC Investment Corp. - Depositary Shares Each Representing a 1/1,000th Interest in a Share of 7.00% Series C Fixed-To-Floating Rate Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
AGNCO|AGNC Investment Corp. - Depositary Shares, each representing a 1/1,000th interest in a share of Series E Fixed-to-Floating Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
AGNCP|AGNC Investment Corp. - Depositary Shares Each Representing a 1/1,000th Interest in a Share of 6.125% Series F Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
AGNG|Global X Aging Population ETF|G|N|N|100|Y|N
AGRI|AgriFORCE  Growing Systems Ltd. - Common Shares|S|N|D|100|N|N
AGRIW|AgriFORCE  Growing Systems Ltd. - Warrant|S|N|N|100|N|N
AGRX|Agile Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
AGYS|Agilysys, Inc. - Common Stock|Q|N|N|100|N|N
AGZD|WisdomTree Interest Rate Hedged U.S. Aggregate Bond Fund|G|N|N|100|Y|N
AHCO|AdaptHealth Corp.  - Common Stock|S|N|N|100|N|N
AHG|Akso Health Group - American Depositary Shares|S|N|N|100|N|N
AHI|Advanced Health Intelligence Ltd. - American Depositary Shares|S|N|N|100|N|N
AIA|iShares Asia 50 ETF|G|N|N|100|Y|N
AIB|AIB Acquisition Corporation - Class A Ordinary Shares|G|N|D|100|N|N
AIBBR|AIB Acquisition Corporation - Right|G|N|D|100|N|N
AIBBU|AIB Acquisition Corporation - Unit|G|N|D|100|N|N
AIH|Aesthetic Medical International Holdings Group Ltd. - American Depositary Shares|S|N|D|100|N|N
AIHS|Senmiao Technology Limited - Common Stock|S|N|D|100|N|N
AIMAU|Aimfinity Investment Corp. I - Unit|G|N|N|100|N|N
AIMAW|Aimfinity Investment Corp. I - Warrant|G|N|N|100|N|N
AIMBU|Aimfinity Investment Corp. I - Subunit|G|N|N|100|N|N
AIMD|Ainos, Inc. - common stock|S|N|D|100|N|N
AIMDW|Ainos, Inc. - warrants|S|N|N|100|N|N
AIP|Arteris, Inc.  - Common Stock|G|N|N|100|N|N
AIQ|Global X Artificial Intelligence & Technology ETF|G|N|N|100|Y|N
AIRG|Airgain, Inc. - Common Stock|S|N|N|100|N|N
AIRR|First Trust RBA American Industrial Renaissance ETF|G|N|N|100|Y|N
AIRS|AirSculpt Technologies, Inc. - Common Stock|G|N|N|100|N|N
AIRT|Air T, Inc. - Common Stock|G|N|N|100|N|N
AIRTP|Air T, Inc. - Trust Preferred Securities|G|N|N|100|N|N
AIXI|XIAO-I Corporation - American Depositary Shares|G|N|N|100|N|N
AKAM|Akamai Technologies, Inc. - Common Stock|Q|N|N|100|N|N
AKAN|Akanda Corp. - Common Shares|S|N|D|100|N|N
AKBA|Akebia Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
AKLI|Akili, Inc. - Common Stock|S|N|N|100|N|N
AKRO|Akero Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
AKTS|Akoustis Technologies, Inc. - Common Stock|S|N|N|100|N|N
AKTX|Akari Therapeutics Plc - American Depositary Shares|S|N|N|100|N|N
AKU|Akumin Inc. - Common Shares|S|N|D|100|N|N
AKYA|Akoya BioSciences, Inc. - Common Stock|Q|N|N|100|N|N
ALAR|Alarum Technologies Ltd. - American Depositary Shares|S|N|N|100|N|N
ALBT|Avalon GloboCare Corp. - Common Stock|S|N|N|100|N|N
ALCO|Alico, Inc. - Common Stock|Q|N|N|100|N|N
ALCY|Alchemy Investments Acquisition Corp 1 - Class A Ordinary Shares|G|N|N|100|N|N
ALCYU|Alchemy Investments Acquisition Corp 1 - Units|G|N|N|100|N|N
ALCYW|Alchemy Investments Acquisition Corp 1 - Warrants|G|N|N|100|N|N
ALDX|Aldeyra Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
ALEC|Alector, Inc. - Common Stock|Q|N|N|100|N|N
ALGM|Allegro MicroSystems, Inc. - Common Stock|Q|N|N|100|N|N
ALGN|Align Technology, Inc. - Common Stock|Q|N|N|100|N|N
ALGS|Aligos Therapeutics, Inc. - Common stock|Q|N|D|100|N|N
ALGT|Allegiant Travel Company - Common Stock|Q|N|N|100|N|N
ALHC|Alignment Healthcare, Inc. - Common Stock|Q|N|N|100|N|N
ALIM|Alimera Sciences, Inc. - Common Stock|G|N|N|100|N|N
ALKS|Alkermes plc - Ordinary Shares|Q|N|N|100|N|N
ALKT|Alkami Technology, Inc. - Common Stock|Q|N|N|100|N|N
ALLK|Allakos Inc. - Common Stock|Q|N|N|100|N|N
ALLO|Allogene Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
ALLR|Allarity Therapeutics, Inc. - Common stock|S|N|N|100|N|N
ALLT|Allot Ltd. - Ordinary Shares|Q|N|N|100|N|N
ALNT|Allient Inc. - Common Stock|G|N|N|100|N|N
ALNY|Alnylam Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
ALOR|ALSP Orchid Acquisition Corporation I - Class A Ordinary Share|G|N|D|100|N|N
ALORU|ALSP Orchid Acquisition Corporation I - Unit|G|N|D|100|N|N
ALORW|ALSP Orchid Acquisition Corporation I - Warrant|G|N|D|100|N|N
ALOT|AstroNova, Inc. - Common Stock|G|N|N|100|N|N
ALPN|Alpine Immune Sciences, Inc. - Common Stock|G|N|N|100|N|N
ALPP|Alpine 4 Holdings, Inc. - Class A Common Stock|S|N|N|100|N|N
ALRM|Alarm.com Holdings, Inc. - Common Stock|Q|N|N|100|N|N
ALRN|Aileron Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
ALRS|Alerus Financial Corporation - Common Stock|S|N|N|100|N|N
ALSA|Alpha Star Acquisition Corporation - Ordinary Shares|G|N|N|100|N|N
ALSAR|Alpha Star Acquisition Corporation - Rights|G|N|N|100|N|N
ALSAU|Alpha Star Acquisition Corporation - Units|G|N|N|100|N|N
ALSAW|Alpha Star Acquisition Corporation - Warrants|G|N|N|100|N|N
ALT|Altimmune, Inc. - Common Stock|G|N|N|100|N|N
ALTI|AlTi Global, Inc. - Class A Common Stock|S|N|N|100|N|N
ALTO|Alto Ingredients, Inc. - Common Stock|S|N|N|100|N|N
ALTR|Altair Engineering Inc. - Class A Common Stock|Q|N|N|100|N|N
ALTU|Altitude Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
ALTUU|Altitude Acquisition Corp. - Unit|S|N|N|100|N|N
ALTUW|Altitude Acquisition Corp. - Warrant|S|N|N|100|N|N
ALTY|Global X Alternative Income ETF|G|N|N|100|Y|N
ALVO|Alvotech - Ordinary Shares|G|N|N|100|N|N
ALVOW|Alvotech - Warrant|G|N|N|100|N|N
ALVR|AlloVir, Inc. - Common Stock|Q|N|N|100|N|N
ALXO|ALX Oncology Holdings Inc. - Common Stock|Q|N|N|100|N|N
ALYA|Alithya Group inc. - Class A subordinate voting shares|S|N|N|100|N|N
ALZN|Alzamend Neuro, Inc. - Common Stock|S|N|D|100|N|N
AMAL|Amalgamated Financial Corp. - Common Stock|G|N|N|100|N|N
AMAM|Ambrx Biopharma Inc. - Common Stock|Q|N|N|100|N|N
AMAT|Applied Materials, Inc. - Common Stock|Q|N|N|100|N|N
AMBA|Ambarella, Inc. - Ordinary Shares|Q|N|N|100|N|N
AMCX|AMC Networks Inc. - Class A Common Stock|Q|N|N|100|N|N
AMD|Advanced Micro Devices, Inc. - Common Stock|Q|N|N|100|N|N
AMDS|GraniteShares 1x Short AMD Daily ETF|G|N|N|100|Y|N
AMED|Amedisys Inc - Common Stock|Q|N|N|100|N|N
AMEH|Apollo Medical Holdings, Inc. - Common Stock|S|N|N|100|N|N
AMGN|Amgen Inc. - Common Stock|Q|N|N|100|N|N
AMID|Argent Mid Cap ETF|G|N|N|100|Y|N
AMKR|Amkor Technology, Inc. - Common Stock|Q|N|N|100|N|N
AMLI|American Lithium Corp. - Common Stock|S|N|N|100|N|N
AMLX|Amylyx Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
AMNB|American National Bankshares, Inc. - Common Stock|Q|N|N|100|N|N
AMPG|Amplitech Group, Inc. - Common Stock|S|N|N|100|N|N
AMPGW|Amplitech Group, Inc. - Warrants|S|N|N|100|N|N
AMPH|Amphastar Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
AMPL|Amplitude, Inc. - Class A Common Stock|S|N|N|100|N|N
AMRK|A-Mark Precious Metals, Inc. - Common Stock|Q|N|N|100|N|N
AMRN|Amarin Corporation plc - American Depositary Shares, each representing one Ordinary Share|G|N|N|100|N|N
AMSC|American Superconductor Corporation - Common Stock|Q|N|N|100|N|N
AMSF|AMERISAFE, Inc. - Common Stock|Q|N|N|100|N|N
AMST|Amesite Inc. - Common Stock|S|N|N|100|N|N
AMSWA|American Software, Inc. - Class A Common Stock|Q|N|N|100|N|N
AMTI|Applied Molecular Transport Inc. - common stock|S|N|D|100|N|N
AMTX|Aemetis, Inc - Common Stock|G|N|N|100|N|N
AMWD|American Woodmark Corporation - Common Stock|Q|N|N|100|N|N
AMZD|Direxion Daily AMZN Bear 1X Shares|G|N|N|100|Y|N
AMZN|Amazon.com, Inc. - Common Stock|Q|N|N|100|N|N
AMZU|Direxion Daily AMZN Bull 1.5X Shares|G|N|N|100|Y|N
ANAB|AnaptysBio, Inc. - Common Stock|Q|N|N|100|N|N
ANDE|The Andersons, Inc. - Common Stock|Q|N|N|100|N|N
ANEB|Anebulo Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
ANGH|Anghami Inc. - Ordinary Shares|G|N|D|100|N|N
ANGHW|Anghami Inc. - Warrants|S|N|N|100|N|N
ANGI|Angi Inc. - Class A Common Stock|Q|N|N|100|N|N
ANGL|VanEck Fallen Angel High Yield Bond ETF|G|N|N|100|Y|N
ANGO|AngioDynamics, Inc. - Common Stock|Q|N|N|100|N|N
ANIK|Anika Therapeutics Inc. - Common Stock|Q|N|N|100|N|N
ANIP|ANI Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
ANIX|Anixa Biosciences, Inc. - Common Stock|S|N|N|100|N|N
ANL|Adlai Nortye Ltd. - American Depositary Shares|G|N|N|100|N|N
ANNX|Annexon, Inc. - common stock|Q|N|N|100|N|N
ANSS|ANSYS, Inc. - Common Stock|Q|N|N|100|N|N
ANTE|AirNet Technology Inc. - American Depositary Shares, each representing one ordinary shares|S|N|N|100|N|N
ANTX|AN2 Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
ANY|Sphere 3D Corp. - Common Shares|S|N|N|100|N|N
AOGO|Arogo Capital Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
AOGOU|Arogo Capital Acquisition Corp. - Unit|G|N|N|100|N|N
AOGOW|Arogo Capital Acquisition Corp. - Warrant|G|N|N|100|N|N
AONC|American Oncology Network, Inc. - Class A Common Stock|S|N|N|100|N|N
AONCW|American Oncology Network, Inc. - Warrant|S|N|N|100|N|N
AOSL|Alpha and Omega Semiconductor Limited - Common Shares|Q|N|N|100|N|N
AOTG|AOT Growth and Innovation ETF|G|N|N|100|Y|N
AOUT|American Outdoor Brands, Inc. - Common Stock|Q|N|N|100|N|N
APA|APA Corporation - Common Stock|Q|N|N|100|N|N
APAC|StoneBridge Acquisition Corporation - Class A Ordinary Shares|S|N|D|100|N|N
APACU|StoneBridge Acquisition Corporation - Unit|S|N|D|100|N|N
APACW|StoneBridge Acquisition Corporation - Warrant|S|N|D|100|N|N
APCX|AppTech Payments Corp. - Common stock|S|N|N|100|N|N
APCXW|AppTech Payments Corp. - Warrant|S|N|N|100|N|N
APDN|Applied DNA Sciences, Inc. - Common Stock|S|N|N|100|N|N
APEI|American Public Education, Inc. - Common Stock|Q|N|N|100|N|N
APGE|Apogee Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
API|Agora, Inc. - ADS|Q|N|N|100|N|N
APLD|Applied Digital Corporation - Common Stock|Q|N|N|100|N|N
APLM|Apollomics Inc. - Class A Ordinary Shares|S|N|N|100|N|N
APLMW|Apollomics Inc. - Warrant|S|N|N|100|N|N
APLS|Apellis Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
APLT|Applied Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
APM|Aptorum Group Limited - Class A Ordinary Shares|S|N|N|100|N|N
APOG|Apogee Enterprises, Inc. - Common Stock|Q|N|N|100|N|N
APP|Applovin Corporation - Class A Common Stock|Q|N|N|100|N|N
APPF|AppFolio, Inc. - Class A Common Stock|G|N|N|100|N|N
APPN|Appian Corporation - Class A Common Stock|G|N|N|100|N|N
APPS|Digital Turbine, Inc. - Common Stock|S|N|N|100|N|N
APRE|Aprea Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
APRN|Blue Apron Holdings, Inc. - Class A Common Stock|G|N|N|100|N|N
APTM|Alpha Partners Technology Merger Corp. - Class A Ordinary Shares|S|N|N|100|N|N
APTMU|Alpha Partners Technology Merger Corp. - Unit|S|N|N|100|N|N
APTMW|Alpha Partners Technology Merger Corp. - Warrant|S|N|N|100|N|N
APTO|Aptose Biosciences, Inc. - Common Shares|S|N|N|100|N|N
APVO|Aptevo Therapeutics Inc. - Common Stock|S|N|D|100|N|N
APWC|Asia Pacific Wire & Cable Corporation Limited  - Common shares, Par value .01 per share|S|N|N|100|N|N
APXI|APx Acquisition Corp. I - Class A Ordinary Share|G|N|N|100|N|N
APXIU|APx Acquisition Corp. I - Unit|G|N|N|100|N|N
APXIW|APx Acquisition Corp. I - Warrant|G|N|D|100|N|N
APYX|Apyx Medical Corporation - Common Stock|Q|N|N|100|N|N
AQB|AquaBounty Technologies, Inc. - Common Stock|S|N|D|100|N|N
AQMS|Aqua Metals, Inc. - Common Stock|S|N|N|100|N|N
AQST|Aquestive Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
AQU|Aquaron Acquisition Corp. - Common Stock|S|N|N|100|N|N
AQUNR|Aquaron Acquisition Corp. - Rights|S|N|N|100|N|N
AQUNU|Aquaron Acquisition Corp. - Units|S|N|N|100|N|N
AQWA|Global X Clean Water ETF|G|N|N|100|Y|N
ARAV|Aravive, Inc. - Common Stock|Q|N|D|100|N|N
ARAY|Accuray Incorporated - Common Stock|Q|N|N|100|N|N
ARBB|ARB IOT Group Limited - Ordinary Shares|S|N|N|100|N|N
ARBE|Arbe Robotics Ltd. - Ordinary Shares|S|N|N|100|N|N
ARBEW|Arbe Robotics Ltd. - Warrant|S|N|N|100|N|N
ARBK|Argo Blockchain plc - American Depositary Shares|Q|N|N|100|N|N
ARBKL|Argo Blockchain plc - 8.75% Senior Notes due 2026|G|N|N|100|N|N
ARCB|ArcBest Corporation - Common Stock|Q|N|N|100|N|N
ARCC|Ares Capital Corporation - Closed End Fund|Q|N|N|100|N|N
ARCE|Arco Platform Limited - Class A Common Shares|Q|N|N|100|N|N
ARCT|Arcturus Therapeutics Holdings Inc. - Common Stock|G|N|N|100|N|N
ARDX|Ardelyx, Inc. - Common Stock|G|N|N|100|N|N
AREB|American Rebel Holdings, Inc. - Common Stock|S|N|N|100|N|N
AREBW|American Rebel Holdings, Inc. - warrants|S|N|N|100|N|N
AREC|American Resources Corporation - Class A Common Stock|S|N|N|100|N|N
ARGX|argenx SE - American Depositary Shares|Q|N|N|100|N|N
ARHS|Arhaus, Inc. - Class A Common Stock|Q|N|N|100|N|N
ARIZ|Arisz Acquisition Corp. - Common Stock|G|N|N|100|N|N
ARIZR|Arisz Acquisition Corp. - Right|G|N|N|100|N|N
ARIZU|Arisz Acquisition Corp. - Unit|G|N|N|100|N|N
ARIZW|Arisz Acquisition Corp. - Warrant|G|N|N|100|N|N
ARKO|ARKO Corp. - Common Stock|S|N|N|100|N|N
ARKOW|ARKO Corp. - Warrant|S|N|N|100|N|N
ARKR|Ark Restaurants Corp. - Common Stock|G|N|N|100|N|N
ARLP|Alliance Resource Partners, L.P. - Common Units Representing Limited Partnership Interests|Q|N|N|100|N|N
ARM|Arm Holdings plc - American Depositary Shares|Q|N|N|100|N|N
AROW|Arrow Financial Corporation - Common Stock|Q|N|N|100|N|N
ARQQ|Arqit Quantum Inc. - Ordinary Shares|S|N|N|100|N|N
ARQQW|Arqit Quantum Inc. - Warrants|S|N|N|100|N|N
ARQT|Arcutis Biotherapeutics, Inc. - Common stock|Q|N|N|100|N|N
ARRW|Arrowroot Acquisition Corp. - Class A common stock|S|N|N|100|N|N
ARRWU|Arrowroot Acquisition Corp. - Unit|S|N|N|100|N|N
ARRWW|Arrowroot Acquisition Corp. - Warrant|S|N|N|100|N|N
ARRY|Array Technologies, Inc. - Common Stock|G|N|N|100|N|N
ARTE|Artemis Strategic Investment Corporation - Class A Common Stock|G|N|D|100|N|N
ARTEU|Artemis Strategic Investment Corporation - Unit|G|N|N|100|N|N
ARTEW|Artemis Strategic Investment Corporation - Warrant|G|N|N|100|N|N
ARTL|Artelo Biosciences, Inc. - Common Stock|S|N|N|100|N|N
ARTLW|Artelo Biosciences, Inc. - Warrant|S|N|N|100|N|N
ARTNA|Artesian Resources Corporation - Class A Non-Voting Common Stock|Q|N|N|100|N|N
ARTW|Art's-Way Manufacturing Co., Inc. - Common Stock|S|N|N|100|N|N
ARVL|Arrival - Ordinary Shares|Q|N|E|100|N|N
ARVN|Arvinas, Inc. - Common Stock|Q|N|N|100|N|N
ARVR|First Trust Indxx Metaverse ETF|G|N|N|100|Y|N
ARWR|Arrowhead Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
ARYD|ARYA Sciences Acquisition Corp IV - Class A Ordinary Shares|S|N|N|100|N|N
ASCA|A SPAC I Acquisition Corp. - Class A Ordinary Share|S|N|N|100|N|N
ASCAR|A SPAC I Acquisition Corp. - Right|S|N|N|100|N|N
ASCAU|A SPAC I Acquisition Corp. - Unit|S|N|N|100|N|N
ASCAW|A SPAC I Acquisition Corp. - Warrant|S|N|N|100|N|N
ASCB|A SPAC II Acquisition Corp. - Ordinary Shares, Class A Common Stock|G|N|N|100|N|N
ASCBR|A SPAC II Acquisition Corp. - Right|G|N|N|100|N|N
ASCBU|A SPAC II Acquisition Corp. - Unit|G|N|N|100|N|N
ASCBW|A SPAC II Acquisition Corp. - Warrant|G|N|N|100|N|N
ASET|FlexShares Real Assets Allocation Index Fund|G|N|N|100|Y|N
ASLE|AerSale Corporation - Common Stock|S|N|N|100|N|N
ASLN|ASLAN Pharmaceuticals Limited - American Depositary Shares|S|N|N|100|N|N
ASMB|Assembly Biosciences, Inc. - Common Stock|Q|N|D|100|N|N
ASML|ASML Holding N.V. - New York Registry Shares|Q|N|N|100|N|N
ASND|Ascendis Pharma A/S - American Depositary Shares|Q|N|N|100|N|N
ASNS|Actelis Networks, Inc. - Common Stock|S|N|D|100|N|N
ASO|Academy Sports and Outdoors, Inc. - Common Stock|Q|N|N|100|N|N
ASPA|Abri SPAC I, Inc. - Common Stock|S|N|D|100|N|N
ASPAU|Abri SPAC I, Inc. - Unit|S|N|D|100|N|N
ASPAW|Abri SPAC I, Inc. - Warrant|S|N|D|100|N|N
ASPI|ASP Isotopes Inc. - Common Stock|S|N|N|100|N|N
ASPS|Altisource Portfolio Solutions S.A. - Common Stock|Q|N|N|100|N|N
ASRT|Assertio Holdings, Inc. - Common Stock|S|N|N|100|N|N
ASRV|AmeriServ Financial Inc. - Common Stock|G|N|N|100|N|N
ASST|Asset Entities Inc. - Class B Common Stock|S|N|D|100|N|N
ASTC|Astrotech Corporation - Common Stock|S|N|N|100|N|N
ASTE|Astec Industries, Inc. - Common Stock|Q|N|N|100|N|N
ASTI|Ascent Solar Technologies, Inc - Common Stock|S|N|N|100|N|N
ASTL|Algoma Steel Group Inc. - Common Shares|G|N|N|100|N|N
ASTLW|Algoma Steel Group Inc. - Warrant|G|N|N|100|N|N
ASTR|Astra Space, Inc. - Class A Common Stock|S|N|N|100|N|N
ASTS|AST SpaceMobile, Inc. - Class A Common Stock|Q|N|N|100|N|N
ASTSW|AST SpaceMobile, Inc. - Warrant|Q|N|N|100|N|N
ASUR|Asure Software Inc - Common Stock|S|N|N|100|N|N
ASYS|Amtech Systems, Inc. - Common Stock|Q|N|N|100|N|N
ATAI|ATAI Life Sciences N.V. - Common Shares|G|N|N|100|N|N
ATAK|Aurora Technology Acquisition Corp. - Class A Ordinary Shares|G|N|N|100|N|N
ATAKR|Aurora Technology Acquisition Corp. - Rights|G|N|N|100|N|N
ATAKU|Aurora Technology Acquisition Corp. - Unit|G|N|N|100|N|N
ATAKW|Aurora Technology Acquisition Corp. - Warrants|G|N|D|100|N|N
ATAT|Atour Lifestyle Holdings Limited - American Depositary Shares|Q|N|N|100|N|N
ATCOL|Atlas Corp. - 7.125% Notes due 2027|G|N|N|100|N|N
ATEC|Alphatec Holdings, Inc. - Common Stock|Q|N|N|100|N|N
ATER|Aterian, Inc. - Common Stock|S|N|D|100|N|N
ATEX|Anterix Inc. - Common Stock|S|N|N|100|N|N
ATHA|Athira Pharma, Inc. - Common Stock|Q|N|N|100|N|N
ATHE|Alterity Therapeutics Limited - American Depositary Shares|S|N|N|100|N|N
ATHX|Athersys, Inc. - Common Stock|S|N|D|100|N|N
ATIF|ATIF Holdings Limited - Ordinary Shares|S|N|N|100|N|N
ATLC|Atlanticus Holdings Corporation - Common Stock|Q|N|N|100|N|N
ATLCL|Atlanticus Holdings Corporation - 6.125% Senior Notes due 2026|G|N|N|100|N|N
ATLCP|Atlanticus Holdings Corporation - 7.625% Series B Cumulative Perpetual Preferred Stock, no par value per share|Q|N|N|100|N|N
ATLO|Ames National Corporation - Common Stock|S|N|N|100|N|N
ATLX|Atlas Lithium Corporation - Common Stock|S|N|N|100|N|N
ATMC|AlphaTime Acquisition Corp - Ordinary Shares|G|N|N|100|N|N
ATMCR|AlphaTime Acquisition Corp - Right|G|N|N|100|N|N
ATMCU|AlphaTime Acquisition Corp - Unit|G|N|N|100|N|N
ATMCW|AlphaTime Acquisition Corp - Warrant|G|N|N|100|N|N
ATMV|AlphaVest Acquisition Corp - Ordinary Shares|G|N|N|100|N|N
ATMVR|AlphaVest Acquisition Corp - Right|G|N|N|100|N|N
ATMVU|AlphaVest Acquisition Corp - Unit|G|N|N|100|N|N
ATNF|180 Life Sciences Corp. - Common Stock|S|N|D|100|N|N
ATNFW|180 Life Sciences Corp. - Warrant|S|N|N|100|N|N
ATNI|ATN International, Inc. - Common Stock|Q|N|N|100|N|N
ATOM|Atomera Incorporated - Common Stock|S|N|N|100|N|N
ATOS|Atossa Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
ATPC|Agape ATP Corporation - Common Stock|S|N|N|100|N|N
ATRA|Atara Biotherapeutics, Inc. - Common Stock|Q|N|N|100|N|N
ATRC|AtriCure, Inc. - Common Stock|G|N|N|100|N|N
ATRI|Atrion Corporation - Common Stock|Q|N|N|100|N|N
ATRO|Astronics Corporation - Common Stock|Q|N|N|100|N|N
ATSG|Air Transport Services Group, Inc - Common Stock|Q|N|N|100|N|N
ATXG|Addentax Group Corp. - Common Stock|S|N|N|100|N|N
ATXI|Avenue Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
ATXS|Astria Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
AUBN|Auburn National Bancorporation, Inc. - Common Stock|G|N|N|100|N|N
AUDC|AudioCodes Ltd. - Ordinary Shares|Q|N|N|100|N|N
AUGX|Augmedix, Inc. - Common Stock|S|N|N|100|N|N
AUID|authID Inc. - Common Stock|S|N|N|100|N|N
AUPH|Aurinia Pharmaceuticals Inc - Common Shares|G|N|N|100|N|N
AUR|Aurora Innovation, Inc.  - Class A Common Stock|Q|N|N|100|N|N
AURA|Aura Biosciences, Inc. - Common Stock|G|N|N|100|N|N
AUROW|Aurora Innovation, Inc.  - Warrant|Q|N|N|100|N|N
AUTL|Autolus Therapeutics plc - American Depositary Shares|Q|N|N|100|N|N
AUUD|Auddia Inc. - Common Stock|S|N|D|100|N|N
AUUDW|Auddia Inc. - Warrants|S|N|N|100|N|N
AUVI|Applied UV, Inc. - Common Stock|S|N|D|100|N|N
AUVIP|Applied UV, Inc. - 10.5% Series A Cumulative Perpetual Preferred Stock, $0.0001 par value per share|S|N|N|100|N|N
AVAH|Aveanna Healthcare Holdings Inc. - Common Stock|Q|N|N|100|N|N
AVAV|AeroVironment, Inc. - Common Stock|Q|N|N|100|N|N
AVDL|Avadel Pharmaceuticals plc - American Depositary Shares each representing one Ordinary Share|G|N|N|100|N|N
AVDX|AvidXchange Holdings, Inc. - Common Stock|Q|N|N|100|N|N
AVGO|Broadcom Inc. - Common Stock|Q|N|N|100|N|N
AVGR|Avinger, Inc. - Common Stock|S|N|D|100|N|N
AVHI|Achari Ventures Holdings Corp. I - Common Stock|G|N|D|100|N|N
AVHIU|Achari Ventures Holdings Corp. I - Unit|G|N|D|100|N|N
AVHIW|Achari Ventures Holdings Corp. I - Warrant|G|N|D|100|N|N
AVID|Avid Technology, Inc. - Common Stock|Q|N|N|100|N|N
AVIR|Atea Pharmaceuticals, Inc. - common stock|Q|N|N|100|N|N
AVNW|Aviat Networks, Inc. - Common Stock|Q|N|N|100|N|N
AVO|Mission Produce, Inc. - Common Stock|Q|N|N|100|N|N
AVPT|AvePoint, Inc. - Class A Common Stock|Q|N|N|100|N|N
AVPTW|AvePoint, Inc. - Warrant|Q|N|N|100|N|N
AVRO|AVROBIO, Inc. - Common Stock|Q|N|N|100|N|N
AVT|Avnet, Inc. - Common Stock|Q|N|N|100|N|N
AVTA|Avantax, Inc. - Common Stock|Q|N|N|100|N|N
AVTE|Aerovate Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
AVTX|Avalo Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
AVXL|Anavex Life Sciences Corp. - Common Stock|Q|N|N|100|N|N
AWH|Aspira Women's Health Inc. - Common Stock|S|N|N|100|N|N
AWIN|AERWINS Technologies Inc. - Common Stock|G|N|D|100|N|N
AWINW|AERWINS Technologies Inc. - Warrant|S|N|N|100|N|N
AWRE|Aware, Inc. - Common Stock|G|N|N|100|N|N
AXDX|Accelerate Diagnostics, Inc. - Common Stock|S|N|N|100|N|N
AXGN|Axogen, Inc. - Common Stock|S|N|N|100|N|N
AXLA|Axcella Health Inc. - Common Stock|G|N|D|100|N|N
AXNX|Axonics, Inc. - Common Stock|Q|N|N|100|N|N
AXON|Axon Enterprise, Inc. - Common Stock|Q|N|N|100|N|N
AXSM|Axsome Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
AXTI|AXT Inc - Common Stock|Q|N|N|100|N|N
AY|Atlantica Sustainable Infrastructure plc - Ordinary Shares|Q|N|N|100|N|N
AYRO|AYRO, Inc. - Common Stock|S|N|N|100|N|N
AYTU|Aytu BioPharma, Inc.  - Common Stock|S|N|N|100|N|N
AZ|A2Z Smart Technologies Corp. - Common Shares|S|N|N|100|N|N
AZN|AstraZeneca PLC - American Depositary Shares|Q|N|N|100|N|N
AZPN|Aspen Technology, Inc. - Common Stock|Q|N|N|100|N|N
AZTA|Azenta, Inc. - Common Stock|Q|N|N|100|N|N
BABX|GraniteShares 1.75x Long BABA Daily ETF|G|N|N|100|Y|N
BACK|IMAC Holdings, Inc. - Common Stock|S|N|N|100|N|N
BAER|Bridger Aerospace Group Holdings, Inc. - Common Stock|G|N|N|100|N|N
BAERW|Bridger Aerospace Group Holdings, Inc. - Warrant|G|N|N|100|N|N
BAFN|BayFirst Financial Corp. - Common Stock|S|N|N|100|N|N
BAND|Bandwidth Inc. - Class A Common Stock|Q|N|N|100|N|N
BANF|BancFirst Corporation - Common Stock|Q|N|N|100|N|N
BANFP|BancFirst Corporation - 7.2% Cumulative Trust Preferred Securities|Q|N|N|100|N|N
BANL|CBL International Limited - Ordinary Shares|S|N|N|100|N|N
BANR|Banner Corporation - Common Stock|Q|N|N|100|N|N
BANX|ArrowMark Financial Corp. - Closed End Fund|Q|N|N|100|N|N
BAOS|Baosheng Media Group Holdings Limited - Ordinary shares|S|N|N|100|N|N
BASE|Couchbase, Inc. - Common Stock|Q|N|N|100|N|N
BATRA|Atlanta Braves Holdings, Inc. - Series A Common Stock|Q|N|N|100|N|N
BATRK|Atlanta Braves Holdings, Inc. - Series C Common Stock|Q|N|N|100|N|N
BBCP|Concrete Pumping Holdings, Inc.  - Common Stock|S|N|N|100|N|N
BBGI|Beasley Broadcast Group, Inc. - Class A Common Stock|G|N|N|100|N|N
BBH|VanEck Biotech ETF|G|N|N|100|Y|N
BBIO|BridgeBio Pharma, Inc. - Common Stock|Q|N|N|100|N|N
BBLG|Bone Biologics Corp - Common Stock|S|N|D|100|N|N
BBLGW|Bone Biologics Corp - warrants|S|N|N|100|N|N
BBSI|Barrett Business Services, Inc. - Common Stock|Q|N|N|100|N|N
BCAB|BioAtla, Inc. - Common Stock|G|N|N|100|N|N
BCAL|Southern California Bancorp - Common Stock|S|N|N|100|N|N
BCAN|BYND Cannasoft Enterprises Inc. - Common Stock|S|N|N|100|N|N
BCBP|BCB Bancorp, Inc. (NJ) - Common Stock|G|N|N|100|N|N
BCDA|BioCardia, Inc. - Common Stock|S|N|D|100|N|N
BCDAW|BioCardia, Inc. - Warrant|S|N|D|100|N|N
BCEL|Atreca, Inc. - Class A Common Stock|Q|N|D|100|N|N
BCLI|Brainstorm Cell Therapeutics Inc. - Common Stock|S|N|N|100|N|N
BCML|BayCom Corp - Common Stock|Q|N|N|100|N|N
BCOV|Brightcove Inc. - Common Stock|Q|N|N|100|N|N
BCOW|1895 Bancorp of Wisconsin, Inc. - Common Stock|S|N|N|100|N|N
BCPC|Balchem Corporation - Common Stock|Q|N|N|100|N|N
BCRX|BioCryst Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
BCSA|Blockchain Coinvestors Acquisition Corp. I - Class A Ordinary Shares|G|N|N|100|N|N
BCSAU|Blockchain Coinvestors Acquisition Corp. I - Unit|G|N|N|100|N|N
BCSAW|Blockchain Coinvestors Acquisition Corp. I - Warrant|G|N|N|100|N|N
BCTX|BriaCell Therapeutics Corp. - Common Shares|S|N|N|100|N|N
BCTXW|BriaCell Therapeutics Corp. - Warrant|S|N|N|100|N|N
BCYC|Bicycle Therapeutics plc - American Depositary Shares|Q|N|N|100|N|N
BDGS|Bridges Capital Tactical ETF|G|N|N|100|Y|N
BDRX|Biodexa Pharmaceuticals plc - American Depositary Shares|S|N|N|100|N|N
BDSX|Biodesix, Inc. - Common Stock|G|N|N|100|N|N
BDTX|Black Diamond Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
BEAM|Beam Therapeutics Inc. - Common Stock|Q|N|N|100|N|N
BEAT|Heartbeam, Inc. - Common Stock|S|N|N|100|N|N
BEATW|Heartbeam, Inc. - Warrant|S|N|N|100|N|N
BECN|Beacon Roofing Supply, Inc. - Common Stock|Q|N|N|100|N|N
BEEM|Beam Global - Common Stock|S|N|D|100|N|N
BEEMW|Beam Global - Warrant|S|N|D|100|N|N
BELFA|Bel Fuse Inc. - Class A Common Stock|Q|N|N|100|N|N
BELFB|Bel Fuse Inc. - Class B Common Stock|Q|N|N|100|N|N
BENF|Beneficient - Class A Common Stock|G|N|N|100|N|N
BENFW|Beneficient - Warrant|S|N|N|100|N|N
BETR|Better Home & Finance Holding Company - Class A Common Stock|G|N|N|100|N|N
BETRW|Better Home & Finance Holding Company - Warrant|S|N|N|100|N|N
BETS|Bit Brother Limited - Class A Ordinary Shares|S|N|D|100|N|N
BFC|Bank First Corporation - Common Stock|S|N|N|100|N|N
BFI|BurgerFi International Inc - Common Stock|G|N|N|100|N|N
BFIIW|BurgerFi International Inc - Warrant|G|N|N|100|N|N
BFIN|BankFinancial Corporation - Common Stock|Q|N|N|100|N|N
BFIT|Global X Health & Wellness ETF|G|N|N|100|Y|N
BFRG|Bullfrog AI Holdings, Inc. - Common Stock|S|N|N|100|N|N
BFRGW|Bullfrog AI Holdings, Inc. - Warrants|S|N|N|100|N|N
BFRI|Biofrontera Inc. - Common Stock|S|N|N|100|N|N
BFRIW|Biofrontera Inc. - Warrants|S|N|N|100|N|N
BFST|Business First Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
BGC|BGC Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
BGFV|Big 5 Sporting Goods Corporation - Common Stock|Q|N|N|100|N|N
BGLC|BioNexus Gene Lab Corp - Common stock|S|N|N|100|N|N
BGNE|BeiGene, Ltd. - American Depositary Shares|Q|N|N|100|N|N
BGRN|iShares USD Green Bond ETF|G|N|N|100|Y|N
BGXX|Bright Green Corporation - Common Stock|S|N|D|100|N|N
BHAC|Crixus BH3 Acquisition Company - Class A Common Stock|G|N|D|100|N|N
BHACU|Crixus BH3 Acquisition Company - Units|G|N|N|100|N|N
BHACW|Crixus BH3 Acquisition Company - Warrants|G|N|N|100|N|N
BHAT|Blue Hat Interactive Entertainment Technology - Ordinary Shares|S|N|N|100|N|N
BHF|Brighthouse Financial, Inc. - Common Stock|Q|N|N|100|N|N
BHFAL|Brighthouse Financial, Inc. - Junior Subordinated Debentures due 2058|Q|N|N|100|N|N
BHFAM|Brighthouse Financial, Inc. - Depositary shares each representing a 1/1,000th Interest in a Share of 4.625% Non-Cumulative Preferred Stock, Series D|Q|N|N|100|N|N
BHFAN|Brighthouse Financial, Inc. - depositary shares, each representing a 1/1,000th interest in a share of 5.375% Non-Cumulative Preferred Stock, Series C|Q|N|N|100|N|N
BHFAO|Brighthouse Financial, Inc. - Depositary Shares, each representing a 1/1,000th interest in a share of 6.750% Non-Cumulative Preferred Stock, Series B|Q|N|N|100|N|N
BHFAP|Brighthouse Financial, Inc. - Depositary Shares 6.6% Non-Cumulative Preferred Stock, Series A|Q|N|N|100|N|N
BHRB|Burke & Herbert Financial Services Corp. - Common Stock|S|N|N|100|N|N
BIAF|bioAffinity Technologies, Inc. - Common Stock|S|N|N|100|N|N
BIAFW|bioAffinity Technologies, Inc. - Warrant|S|N|N|100|N|N
BIB|ProShares Ultra Nasdaq Biotechnology|G|N|N|100|Y|N
BIDU|Baidu, Inc. - American Depositary Shares, each representing 8 ordinary share|Q|N|N|100|N|N
BIGB|Roundhill BIG Bank ETF|G|N|N|100|Y|N
BIGC|BigCommerce Holdings, Inc. - Series 1 Common Stock|G|N|N|100|N|N
BIGT|Roundhill BIG Tech ETF|G|N|N|100|Y|N
BIIB|Biogen Inc. - Common Stock|Q|N|N|100|N|N
BILI|Bilibili Inc. - American Depositary Shares|Q|N|N|100|N|N
BIMI|BIMI International Medical Inc. - Common Stock|S|N|E|100|N|N
BIOC|Biocept, Inc. - Common Stock|S|N|D|100|N|N
BIOL|Biolase, Inc. - Common Stock|S|N|N|100|N|N
BIOR|Biora Therapeutics, Inc.  - Common Stock|G|N|N|100|N|N
BIOX|Bioceres Crop Solutions Corp. - Ordinary Shares|Q|N|N|100|N|N
BIRD|Allbirds, Inc. - Class A Common Stock|Q|N|N|100|N|N
BIS|ProShares UltraShort Nasdaq Biotechnology|G|N|N|100|Y|N
BITF|Bitfarms Ltd. - Common Stock|G|N|N|100|N|N
BITS|Global X Blockchain & Bitcoin Strategy ETF|G|N|N|100|Y|N
BIVI|BioVie Inc. - Common stock|S|N|N|100|N|N
BJDX|Bluejay Diagnostics, Inc. - Common Stock|S|N|N|100|N|N
BJK|VanEck Gaming ETF|G|N|N|100|Y|N
BJRI|BJ's Restaurants, Inc. - Common Stock|Q|N|N|100|N|N
BKCC|BlackRock Capital Investment Corporation - Closed End Fund|Q|N|N|100|N|N
BKCH|Global X Blockchain ETF|G|N|N|100|Y|N
BKIV|BNY Mellon Innovators ETF|G|N|N|100|Y|N
BKNG|Booking Holdings Inc. - Common Stock|Q|N|N|100|N|N
BKR|Baker Hughes Company - Common Stock|Q|N|N|100|N|N
BKWO|BNY Mellon Women's Opportunities ETF|G|N|N|100|Y|N
BKYI|BIO-key International, Inc. - Common Stock|S|N|D|100|N|N
BL|BlackLine, Inc. - Common Stock|Q|N|N|100|N|N
BLAC|Bellevue Life Sciences Acquisition Corp. - Common Stock|S|N|D|100|N|N
BLACR|Bellevue Life Sciences Acquisition Corp. - Rights|S|N|D|100|N|N
BLACU|Bellevue Life Sciences Acquisition Corp. - Unit|S|N|D|100|N|N
BLACW|Bellevue Life Sciences Acquisition Corp. - Warrant|S|N|D|100|N|N
BLBD|Blue Bird Corporation - Common Stock|G|N|N|100|N|N
BLBX|Blackboxstocks Inc. - Common Stock|S|N|N|100|N|N
BLCN|Siren Nasdaq NexGen Economy ETF|G|N|N|100|Y|N
BLDE|Blade Air Mobility, Inc. - Class A Common Stock|S|N|N|100|N|N
BLDEW|Blade Air Mobility, Inc. - Warrants|S|N|N|100|N|N
BLDP|Ballard Power Systems, Inc. - Common Shares|G|N|N|100|N|N
BLEU|bleuacacia ltd - Class A Ordinary Shares|G|N|D|100|N|N
BLEUR|bleuacacia ltd - Rights|G|N|D|100|N|N
BLEUU|bleuacacia ltd - Units|G|N|D|100|N|N
BLEUW|bleuacacia ltd - Warrants|G|N|D|100|N|N
BLFS|BioLife Solutions, Inc. - Common Stock|S|N|N|100|N|N
BLFY|Blue Foundry Bancorp - Common Stock|Q|N|N|100|N|N
BLIN|Bridgeline Digital, Inc. - Common Stock|S|N|D|100|N|N
BLKB|Blackbaud, Inc. - Common Stock|Q|N|N|100|N|N
BLLD|JPMorgan Sustainable Infrastructure ETF|G|N|N|100|Y|N
BLMN|Bloomin' Brands, Inc. - Common Stock|Q|N|N|100|N|N
BLNK|Blink Charging Co. - Common Stock|S|N|N|100|N|N
BLRX|BioLineRx Ltd. - American Depositary Shares|S|N|N|100|N|N
BLTE|Belite Bio, Inc - American Depositary Shares|S|N|N|100|N|N
BLUE|bluebird bio, Inc. - Common Stock|Q|N|N|100|N|N
BLZE|Backblaze, Inc. - Class A Common Stock|G|N|N|100|N|N
BMBL|Bumble Inc. - common stock|Q|N|N|100|N|N
BMEA|Biomea Fusion, Inc. - Common Stock|Q|N|N|100|N|N
BMR|Beamr Imaging Ltd. - Ordinary Share|S|N|N|100|N|N
BMRA|Biomerica, Inc. - Common Stock|S|N|N|100|N|N
BMRC|Bank of Marin Bancorp - Common Stock|S|N|N|100|N|N
BMRN|BioMarin Pharmaceutical Inc. - Common Stock|Q|N|N|100|N|N
BND|Vanguard Total Bond Market ETF|G|N|N|100|Y|N
BNDW|Vanguard Total World Bond ETF|G|N|N|100|Y|N
BNDX|Vanguard Total International Bond ETF|G|N|N|100|Y|N
BNGO|Bionano Genomics, Inc. - Common Stock|S|N|N|100|N|N
BNIX|Bannix Acquisition Corp. - Common Stock|S|N|N|100|N|N
BNIXR|Bannix Acquisition Corp. - Right|S|N|N|100|N|N
BNIXW|Bannix Acquisition Corp. - Warrant|S|N|N|100|N|N
BNMV|BitNile Metaverse, Inc. - Common Stock|S|N|D|100|N|N
BNOX|Bionomics Limited - American Depository Shares|G|N|N|100|N|N
BNR|Burning Rock Biotech Limited - American Depositary Shares|G|N|N|100|N|N
BNRG|Brenmiller Energy Ltd - Ordinary Shares|S|N|D|100|N|N
BNTC|Benitec Biopharma Inc. - Common Stock|S|N|N|100|N|N
BNTX|BioNTech SE - American Depositary Shares|Q|N|N|100|N|N
BOCN|Blue Ocean Acquisition Corp - Class A Ordinary Shares|G|N|N|100|N|N
BOCNU|Blue Ocean Acquisition Corp - Units|G|N|N|100|N|N
BOCNW|Blue Ocean Acquisition Corp - Warrants|G|N|N|100|N|N
BOF|BranchOut Food Inc. - Common Stock|S|N|N|100|N|N
BOKF|BOK Financial Corporation - Common Stock|Q|N|N|100|N|N
BOLT|Bolt Biotherapeutics, Inc. - Common Stock|Q|N|N|100|N|N
BON|Bon Natural Life Limited - Ordinary Shares|S|N|D|100|N|N
BOOM|DMC Global Inc. - Common Stock|Q|N|N|100|N|N
BOSC|B.O.S. Better Online Solutions - Ordinary Shares|S|N|N|100|N|N
BOTJ|Bank of the James Financial Group, Inc. - Common Stock|S|N|N|100|N|N
BOTZ|Global X Robotics & Artificial Intelligence ETF|G|N|N|100|Y|N
BOWN|Bowen Acquisition Corp - Ordinary Shares|G|N|N|100|N|N
BOWNR|Bowen Acquisition Corp - Rights|G|N|N|100|N|N
BOWNU|Bowen Acquisition Corp - Unit|G|N|N|100|N|N
BOXL|Boxlight Corporation - Class A Common Stock|S|N|N|100|N|N
BPMC|Blueprint Medicines Corporation - Common Stock|Q|N|N|100|N|N
BPOP|Popular, Inc. - Common Stock|Q|N|N|100|N|N
BPOPM|Popular, Inc. - Popular Capital Trust II - 6.125% Cumulative Monthly Income Trust Preferred Securities|Q|N|N|100|N|N
BPRN|Princeton Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
BPTH|Bio-Path Holdings, Inc. - Common Stock|S|N|D|100|N|N
BPTS|Biophytis SA - American Depositary Share|S|N|D|100|N|N
BPYPM|Brookfield Property Partners L.P. - 6.25% Class A Cumulative Redeemable Preferred Units, Series 1|Q|N|N|100|N|N
BPYPN|Brookfield Property Partners L.P. - 5.750% Class A Cumulative Redeemable Perpetual Preferred Units, Series 3|Q|N|N|100|N|N
BPYPO|Brookfield Property Partners L.P. - 6.375% Class A Cumulative Redeemable Perpetual Preferred Units, Series 2|Q|N|N|100|N|N
BPYPP|Brookfield Property Partners L.P. - 6.50% Class A Cumulative Redeemable Perpetual Preferred Units|Q|N|N|100|N|N
BRAC|Broad Capital Acquisition Corp - Common Stock|G|N|N|100|N|N
BRACR|Broad Capital Acquisition Corp - Rights|G|N|N|100|N|N
BRACU|Broad Capital Acquisition Corp - Units|G|N|N|100|N|N
BRAG|Bragg Gaming Group Inc. - Common Shares|Q|N|N|100|N|N
BREA|Brera Holdings PLC - Class B Ordinary Shares|S|N|N|100|N|N
BREZ|Breeze Holdings Acquisition Corp. - Common Stock|S|N|N|100|N|N
BREZR|Breeze Holdings Acquisition Corp. - Right|S|N|N|100|N|N
BREZW|Breeze Holdings Acquisition Corp. - Warrant|S|N|N|100|N|N
BRFH|Barfresh Food Group Inc. - Common Stock|S|N|D|100|N|N
BRID|Bridgford Foods Corporation - Common Stock|G|N|N|100|N|N
BRKH|BurTech Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
BRKHU|BurTech Acquisition Corp. - Unit|G|N|N|100|N|N
BRKHW|BurTech Acquisition Corp. - Warrants|G|N|N|100|N|N
BRKL|Brookline Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
BRKR|Bruker Corporation - Common Stock|Q|N|N|100|N|N
BRLI|Brilliant Acquisition Corporation - Ordinary Shares|S|N|D|100|N|N
BRLIR|Brilliant Acquisition Corporation - Rights|S|N|D|100|N|N
BRLIU|Brilliant Acquisition Corporation - Unit|S|N|D|100|N|N
BRLIW|Brilliant Acquisition Corporation - Warrants|S|N|D|100|N|N
BRLT|Brilliant Earth Group, Inc. - Class A Common Stock|G|N|N|100|N|N
BRNY|Burney U.S. Factor Rotation ETF|G|N|N|100|Y|N
BROG|Brooge Energy Limited  - Ordinary Shares|S|N|N|100|N|N
BROGW|Brooge Energy Limited  - Warrant|S|N|N|100|N|N
BRP|BRP Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
BRQS|Borqs Technologies, Inc.  - Ordinary Shares|S|N|D|100|N|N
BRSH|Bruush Oral Care Inc. - Common Stock|S|N|D|100|N|N
BRSHW|Bruush Oral Care Inc. - Warrant|S|N|D|100|N|N
BRTX|BioRestorative Therapies, Inc. - Common Stock|S|N|N|100|N|N
BRY|Berry Corporation (bry) - Common Stock|Q|N|N|100|N|N
BRZE|Braze, Inc. - Class A Common Stock|Q|N|N|100|N|N
BSBK|Bogota Financial Corp. - Common Stock|S|N|N|100|N|N
BSCN|Invesco BulletShares 2023 Corporate Bond ETF|G|N|N|100|Y|N
BSCO|Invesco BulletShares 2024 Corporate Bond ETF|G|N|N|100|Y|N
BSCP|Invesco BulletShares 2025 Corporate Bond ETF|G|N|N|100|Y|N
BSCQ|Invesco BulletShares 2026 Corporate Bond ETF|G|N|N|100|Y|N
BSCR|Invesco BulletShares 2027 Corporate Bond ETF|G|N|N|100|Y|N
BSCS|Invesco BulletShares 2028 Corporate Bond ETF|G|N|N|100|Y|N
BSCT|Invesco BulletShares 2029 Corporate Bond ETF|G|N|N|100|Y|N
BSCU|Invesco BulletShares 2030 Corporate Bond ETF|G|N|N|100|Y|N
BSCV|Invesco BulletShares 2031 Corporate Bond ETF|G|N|N|100|Y|N
BSCW|Invesco BulletShares 2032 Corporate Bond ETF|G|N|N|100|Y|N
BSCX|Invesco BulletShares 2033 Corporate Bond ETF|G|N|N|100|Y|N
BSET|Bassett Furniture Industries, Incorporated - Common Stock|Q|N|N|100|N|N
BSFC|Blue Star Foods Corp. - Common stock|S|N|D|100|N|N
BSGM|BioSig Technologies, Inc. - Common Stock|S|N|D|100|N|N
BSJN|Invesco BulletShares 2023 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSJO|Invesco BulletShares 2024 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSJP|Invesco BulletShares 2025 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSJQ|Invesco BulletShares 2026 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSJR|Invesco BulletShares 2027 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSJS|Invesco BulletShares 2028 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSJT|Invesco BulletShares 2029 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSJU|Invesco BulletShares 2030 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSJV|Invesco BulletShares 2031 High Yield Corporate Bond ETF|G|N|N|100|Y|N
BSMN|Invesco BulletShares 2023 Municipal Bond ETF|G|N|N|100|Y|N
BSMO|Invesco BulletShares 2024 Municipal Bond ETF|G|N|N|100|Y|N
BSMP|Invesco BulletShares 2025 Municipal Bond ETF|G|N|N|100|Y|N
BSMQ|Invesco BulletShares 2026 Municipal Bond ETF|G|N|N|100|Y|N
BSMR|Invesco BulletShares 2027 Municipal Bond ETF|G|N|N|100|Y|N
BSMS|Invesco BulletShares 2028 Municipal Bond ETF|G|N|N|100|Y|N
BSMT|Invesco BulletShares 2029 Municipal Bond ETF|G|N|N|100|Y|N
BSMU|Invesco BulletShares 2030 Municipal Bond ETF|G|N|N|100|Y|N
BSMV|Invesco BulletShares 2031 Municipal Bond ETF|G|N|N|100|Y|N
BSMW|Invesco BulletShares 2032 Municipal Bond ETF|G|N|N|100|Y|N
BSQR|BSQUARE Corporation - Common Stock|S|N|N|100|N|N
BSRR|Sierra Bancorp - Common Stock|Q|N|N|100|N|N
BSSX|Invesco BulletShares 2033 Municipal Bond ETF|G|N|N|100|Y|N
BSVN|Bank7 Corp. - Common stock|Q|N|N|100|N|N
BSVO|EA Bridgeway Omni Small-Cap Value ETF|G|N|N|100|Y|N
BSY|Bentley Systems, Incorporated - Class B Common Stock|Q|N|N|100|N|N
BTAI|BioXcel Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
BTBD|BT Brands, Inc. - Common Stock|S|N|N|100|N|N
BTBDW|BT Brands, Inc. - Warrant|S|N|N|100|N|N
BTBT|Bit Digital, Inc. - Ordinary Share|S|N|N|100|N|N
BTCS|BTCS Inc. - Common Stock|S|N|N|100|N|N
BTCT|BTC Digital Ltd. - Ordinary Shares|S|N|N|100|N|N
BTCTW|BTC Digital Ltd. - Warrant|S|N|N|100|N|N
BTCY|Biotricity, Inc. - Common Stock|S|N|D|100|N|N
BTDR|Bitdeer Technologies Group - Ordinary Shares|S|N|N|100|N|N
BTEC|Principal Healthcare Innovators ETF|G|N|N|100|Y|N
BTF|Valkyrie Bitcoin and Ether Strategy ETF|G|N|N|100|Y|N
BTM|Bitcoin Depot Inc. - Class A Common Stock|S|N|N|100|N|N
BTMD|Biote Corp. - Class A common stock|G|N|N|100|N|N
BTMWW|Bitcoin Depot Inc. - Warrant|S|N|N|100|N|N
BTOG|Bit Origin Limited - Ordinary Shares|S|N|N|100|N|N
BTTX|Better Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
BUG|Global X Cybersecurity ETF|G|N|N|100|Y|N
BUJA|Bukit Jalil Global Acquisition 1 Ltd. - Ordinary Shares|S|N|N|100|N|N
BUJAR|Bukit Jalil Global Acquisition 1 Ltd. - Rights|S|N|N|100|N|N
BUJAU|Bukit Jalil Global Acquisition 1 Ltd. - Unit|S|N|N|100|N|N
BUJAW|Bukit Jalil Global Acquisition 1 Ltd. - Warrants|S|N|N|100|N|N
BULD|Pacer BlueStar Engineering the Future ETF|G|N|N|100|Y|N
BUSE|First Busey Corporation - Common Stock|Q|N|N|100|N|N
BVFL|BV Financial, Inc. - Common Stock|S|N|N|100|N|N
BVS|Bioventus Inc. - Class A Common Stock|Q|N|N|100|N|N
BWAQ|Blue World Acquisition Corporation - Class A ordinary shares|G|N|N|100|N|N
BWAQR|Blue World Acquisition Corporation - Right|G|N|N|100|N|N
BWAQU|Blue World Acquisition Corporation - Unit|G|N|N|100|N|N
BWAQW|Blue World Acquisition Corporation - Warrant|G|N|N|100|N|N
BWAY|BrainsWay Ltd. - American Depositary Shares|G|N|N|100|N|N
BWB|Bridgewater Bancshares, Inc. - Common Stock|S|N|N|100|N|N
BWBBP|Bridgewater Bancshares, Inc. - Depositary Shares, Each Representing a 1/100th Interest in a Share of 5.875% Non-Cumulative Perpetual Preferred Stock, Series A|S|N|N|100|N|N
BWEN|Broadwind, Inc. - Common Stock|S|N|N|100|N|N
BWFG|Bankwell Financial Group, Inc. - Common Stock|G|N|N|100|N|N
BWMN|Bowman Consulting Group Ltd. - Common Stock|G|N|N|100|N|N
BWMX|Betterware de Mexico, S.A.P.I. de C.V. - Ordinary Shares|S|N|N|100|N|N
BWV|Blue Water Biotech, Inc. - Common Stock|S|N|H|100|N|N
BXRX|Baudax Bio, Inc. - Common stock|S|N|D|100|N|N
BYFC|Broadway Financial Corporation - Common Stock|S|N|D|100|N|N
BYND|Beyond Meat, Inc. - Common stock|Q|N|N|100|N|N
BYNO|byNordic Acquisition Corporation - Class A Common Stock|G|N|N|100|N|N
BYNOU|byNordic Acquisition Corporation - Units|G|N|N|100|N|N
BYNOW|byNordic Acquisition Corporation - Warrant|G|N|N|100|N|N
BYOB|SoFi Be Your Own Boss ETF|G|N|N|100|Y|N
BYRN|Byrna Technologies, Inc. - Common Stock|S|N|N|100|N|N
BYSI|BeyondSpring, Inc. - Ordinary Shares|S|N|D|100|N|N
BYTS|BYTE Acquisition Corp. - Class A Ordinary Shares|S|N|N|100|N|N
BYTSU|BYTE Acquisition Corp. - Units|S|N|N|100|N|N
BYTSW|BYTE Acquisition Corp. - Warrants|S|N|N|100|N|N
BZ|KANZHUN LIMITED - American Depository Shares|Q|N|N|100|N|N
BZFD|BuzzFeed, Inc. - Class A Common Stock|G|N|D|100|N|N
BZFDW|BuzzFeed, Inc. - Warrant|S|N|N|100|N|N
BZUN|Baozun Inc. - American Depositary Shares|Q|N|N|100|N|N
CAAS|China Automotive Systems, Inc. - Common Stock|S|N|N|100|N|N
CABA|Cabaletta Bio, Inc. - Common Stock|Q|N|N|100|N|N
CAC|Camden National Corporation - Common Stock|Q|N|N|100|N|N
CACC|Credit Acceptance Corporation - Common Stock|Q|N|N|100|N|N
CACG|ClearBridge All Cap Growth ESG ETF|G|N|N|100|Y|N
CACO|Caravelle International Group - Ordinary Shares|S|N|D|100|N|N
CADL|Candel Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
CAFG|Pacer US Small Cap Cash Cows Growth Leaders ETF|G|N|N|100|Y|N
CAKE|The Cheesecake Factory Incorporated - Common Stock|Q|N|N|100|N|N
CALB|California BanCorp - Common Stock|Q|N|N|100|N|N
CALC|CalciMedica, Inc. - Common Stock|S|N|N|100|N|N
CALM|Cal-Maine Foods, Inc. - Common Stock|Q|N|N|100|N|N
CALT|Calliditas Therapeutics AB - American Depositary Shares|Q|N|N|100|N|N
CALY|BlackRock Short-Term California Muni Bond ETF|G|N|N|100|Y|N
CAMP|CalAmp Corp. - Common Stock|Q|N|D|100|N|N
CAMT|Camtek Ltd. - Ordinary Shares|G|N|N|100|N|N
CAN|Canaan Inc. - American Depositary Shares|G|N|N|100|N|N
CANC|Tema Oncology ETF|G|N|N|100|Y|N
CAPR|Capricor Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
CAR|Avis Budget Group, Inc. - Common Stock|Q|N|N|100|N|N
CARA|Cara Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
CARE|Carter Bankshares, Inc. - Common Stock|Q|N|N|100|N|N
CARG|CarGurus, Inc. - Class A Common Stock|Q|N|N|100|N|N
CARM|Carisma Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
CART|Maplebear Inc. - Common Stock|Q|N|N|100|N|N
CARV|Carver Bancorp, Inc. - Common Stock|S|N|N|100|N|N
CARZ|First Trust S-Network Electric & Future Vehicle Ecosystem ETF|G|N|N|100|Y|N
CASA|Casa Systems, Inc. - Common Stock|Q|N|D|100|N|N
CASH|Pathward Financial, Inc. - Common Stock|Q|N|N|100|N|N
CASI|CASI Pharmaceuticals, Inc. - Ordinary Shares|S|N|N|100|N|N
CASS|Cass Information Systems, Inc - Common Stock|Q|N|N|100|N|N
CASY|Caseys General Stores, Inc. - Common Stock|Q|N|N|100|N|N
CATC|Cambridge Bancorp - Common Stock|S|N|N|100|N|N
CATH|Global X S&P 500 Catholic Values ETF|G|N|N|100|Y|N
CATY|Cathay General Bancorp - Common Stock|Q|N|N|100|N|N
CBAN|Colony Bankcorp, Inc. - Common Stock|G|N|N|100|N|N
CBAT|CBAK Energy Technology, Inc. - Common Stock|S|N|D|100|N|N
CBAY|CymaBay Therapeutics Inc. - Common Stock|Q|N|N|100|N|N
CBFV|CB Financial Services, Inc. - Common Stock|G|N|N|100|N|N
CBIO|Catalyst Biosciences, Inc.  - Common Stock|S|N|D|100|N|N
CBNK|Capital Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
CBRG|Chain Bridge I - Class A Ordinary Shares|G|N|N|100|N|N
CBRGU|Chain Bridge I - Units|G|N|N|100|N|N
CBRL|Cracker Barrel Old Country Store, Inc. - Common Stock|Q|N|N|100|N|N
CBSH|Commerce Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
CBUS|Cibus, Inc. - Class A Common Stock|S|N|N|100|N|N
CCAP|Crescent Capital BDC, Inc. - Common Stock|G|N|N|100|N|N
CCB|Coastal Financial Corporation - Common Stock|Q|N|N|100|N|N
CCBG|Capital City Bank Group - Common Stock|Q|N|N|100|N|N
CCCC|C4 Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
CCCS|CCC Intelligent Solutions Holdings Inc. - Common Stock|Q|N|N|100|N|N
CCD|Calamos Dynamic Convertible & Income Fund - Closed End Fund|Q|N|N|100|N|N
CCEP|Coca-Cola Europacific Partners plc - Ordinary Shares|Q|N|N|100|N|N
CCG|Cheche Group Inc. - Class A Ordinary Shares|S|N|N|100|N|N
CCGWW|Cheche Group Inc. - Warrant|S|N|N|100|N|N
CCLD|CareCloud, Inc. - Common Stock|G|N|N|100|N|N
CCLDO|CareCloud, Inc. - 8.75% Series B Cumulative Redeemable Perpetual Preferred Stock|G|N|N|100|N|N
CCLDP|CareCloud, Inc. - 11% Series A Cumulative Redeemable Perpetual Preferred Stock|G|N|N|100|N|N
CCLP|CSI Compressco LP - common units|Q|N|N|100|N|N
CCNE|CNB Financial Corporation - Common Stock|Q|N|N|100|N|N
CCNEP|CNB Financial Corporation - Depositary shares, each representing a 1/40th ownership interest in a share of 7.125% Series A Fixed- Rate Non-Cumulative Perpetual Preferred Stock|Q|N|N|100|N|N
CCOI|Cogent Communications Holdings, Inc. - Common Stock|Q|N|N|100|N|N
CCRN|Cross Country Healthcare, Inc. - Common Stock|Q|N|N|100|N|N
CCSI|Consensus Cloud Solutions, Inc. - Common Stock|Q|N|N|100|N|N
CCSO|Carbon Collective Climate Solutions U.S. Equity ETF|G|N|N|100|Y|N
CCTS|Cactus Acquisition Corp. 1 Limited - Class A Ordinary Share|G|N|D|100|N|N
CCTSU|Cactus Acquisition Corp. 1 Limited - Unit|G|N|D|100|N|N
CCTSW|Cactus Acquisition Corp. 1 Limited - Warrant|G|N|D|100|N|N
CD|Chindata Group Holdings Limited - American Depositary Shares|Q|N|N|100|N|N
CDAQ|Compass Digital Acquisition Corp. - Class A Ordinary Shares|G|N|N|100|N|N
CDAQU|Compass Digital Acquisition Corp. - Unit|G|N|N|100|N|N
CDAQW|Compass Digital Acquisition Corp. - Warrant|G|N|N|100|N|N
CDC|VictoryShares US EQ Income Enhanced Volatility Wtd ETF|G|N|N|100|Y|N
CDIO|Cardio Diagnostics Holdings Inc. - Common stock|S|N|D|100|N|N
CDIOW|Cardio Diagnostics Holdings Inc. - Warrant|S|N|N|100|N|N
CDL|VictoryShares US Large Cap High Div Volatility Wtd ETF|G|N|N|100|Y|N
CDLX|Cardlytics, Inc. - Common Stock|G|N|N|100|N|N
CDMO|Avid Bioservices, Inc. - Common Stock|S|N|N|100|N|N
CDNA|CareDx, Inc. - Common Stock|G|N|N|100|N|N
CDNS|Cadence Design Systems, Inc. - Common Stock|Q|N|N|100|N|N
CDRO|Codere Online Luxembourg, S.A. - Ordinary Shares|S|N|N|100|N|N
CDROW|Codere Online Luxembourg, S.A. - Warrants|S|N|N|100|N|N
CDT|Conduit Pharmaceuticals Inc.  - Common Stock|G|N|N|100|N|N
CDTTW|Conduit Pharmaceuticals Inc.  - Warrant|S|N|N|100|N|N
CDTX|Cidara Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
CDW|CDW Corporation - Common Stock|Q|N|N|100|N|N
CDXC|ChromaDex Corporation - Common Stock|S|N|N|100|N|N
CDXS|Codexis, Inc. - Common Stock|Q|N|N|100|N|N
CDZI|Cadiz, Inc. - Common Stock|G|N|N|100|N|N
CDZIP|Cadiz, Inc. - Depositary Shares|G|N|N|100|N|N
CEAD|CEA Industries Inc. - Common Stock|S|N|D|100|N|N
CEADW|CEA Industries Inc. - Warrant|S|N|N|100|N|N
CECO|CECO Environmental Corp. - Common Stock|Q|N|N|100|N|N
CEFA|Global X S&P Catholic Values Developed ex-U.S. ETF|G|N|N|100|Y|N
CEG|Constellation Energy Corporation - Common Stock|Q|N|N|100|N|N
CELC|Celcuity Inc. - Common Stock|S|N|N|100|N|N
CELH|Celsius Holdings, Inc. - Common Stock|S|N|N|100|N|N
CELU|Celularity Inc. - Class A Common Stock|S|N|D|100|N|N
CELUW|Celularity Inc. - Warrant|S|N|N|100|N|N
CELZ|Creative Medical Technology Holdings, Inc. - Common Stock|S|N|N|100|N|N
CENN|Cenntro Electric Group Limited - Ordinary Shares|S|N|D|100|N|N
CENT|Central Garden & Pet Company - Common Stock|Q|N|N|100|N|N
CENTA|Central Garden & Pet Company - Class A Common Stock Nonvoting|Q|N|N|100|N|N
CENX|Century Aluminum Company - Common Stock|Q|N|N|100|N|N
CERE|Cerevel Therapeutics Holdings, Inc. - Common Stock|S|N|N|100|N|N
CERS|Cerus Corporation - Common Stock|G|N|N|100|N|N
CERT|Certara, Inc. - Common Stock|Q|N|N|100|N|N
CETU|Cetus Capital Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
CETUR|Cetus Capital Acquisition Corp. - Right to receive 1/6 of one share of Class A Common Stock|S|N|N|100|N|N
CETUU|Cetus Capital Acquisition Corp. - Unit|S|N|N|100|N|N
CETUW|Cetus Capital Acquisition Corp. - Warrant|S|N|N|100|N|N
CETX|Cemtrex Inc. - Common Stock|S|N|N|100|N|N
CETXP|Cemtrex Inc. - Series 1 Preferred Stock|S|N|D|100|N|N
CETY|Clean Energy Technologies, Inc. - Common Stock|S|N|N|100|N|N
CEVA|CEVA, Inc. - Common Stock|Q|N|N|100|N|N
CFA|VictoryShares US 500 Volatility Wtd ETF|G|N|N|100|Y|N
CFB|CrossFirst Bankshares, Inc. - Common Stock|Q|N|N|100|N|N
CFBK|CF Bankshares Inc. - Common Stock|S|N|N|100|N|N
CFFE|CF Acquisition Corp. VIII - Class A Common Stock|S|N|N|100|N|N
CFFEU|CF Acquisition Corp. VIII - Unit|S|N|N|100|N|N
CFFEW|CF Acquisition Corp. VIII - Warrant|S|N|N|100|N|N
CFFI|C&F Financial Corporation - Common Stock|Q|N|N|100|N|N
CFFN|Capitol Federal Financial, Inc. - Common Stock|Q|N|N|100|N|N
CFFS|CF Acquisition Corp. VII - Class A Common Stock|S|N|N|100|N|N
CFFSU|CF Acquisition Corp. VII - Unit|G|N|N|100|N|N
CFFSW|CF Acquisition Corp. VII - Warrant|S|N|N|100|N|N
CFIV|CF Acquisition Corp. IV - Class A common stock|S|N|N|100|N|N
CFIVU|CF Acquisition Corp. IV - Unit|S|N|N|100|N|N
CFIVW|CF Acquisition Corp. IV - Warrant|S|N|N|100|N|N
CFLT|Confluent, Inc. - Class A Common Stock|Q|N|N|100|N|N
CFO|VictoryShares US 500 Enhanced Volatility Wtd ETF|G|N|N|100|Y|N
CFRX|ContraFect Corporation - Common Stock|S|N|D|100|N|N
CFSB|CFSB Bancorp, Inc. - Common Stock|S|N|N|100|N|N
CG|The Carlyle Group Inc. - Common Stock|Q|N|N|100|N|N
CGABL|The Carlyle Group Inc. - 4.625% Subordinated Notes due 2061|Q|N|N|100|N|N
CGBD|Carlyle Secured Lending, Inc. - Closed End Fund|Q|N|N|100|N|N
CGC|Canopy Growth Corporation - Common Shares|Q|N|D|100|N|N
CGEM|Cullinan Oncology, Inc. - Common Stock|Q|N|N|100|N|N
CGEN|Compugen Ltd. - Ordinary Shares|S|N|N|100|N|N
CGNT|Cognyte Software Ltd. - Ordinary Shares|Q|N|N|100|N|N
CGNX|Cognex Corporation - Common Stock|Q|N|N|100|N|N
CGO|Calamos Global Total Return Fund - Closed End Fund|Q|N|N|100|N|N
CGTX|Cognition Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
CHB|Global X China Biotech Innovation ETF|G|N|N|100|Y|N
CHCI|Comstock Holding Companies, Inc. - Class A Common Stock|S|N|N|100|N|N
CHCO|City Holding Company - Common Stock|Q|N|N|100|N|N
CHDN|Churchill Downs, Incorporated - Common Stock|Q|N|N|100|N|N
CHEA|Chenghe Acquisition Co. - Class A Ordinary Share|G|N|N|100|N|N
CHEAU|Chenghe Acquisition Co. - Unit|G|N|N|100|N|N
CHEF|The Chefs' Warehouse, Inc. - Common Stock|Q|N|N|100|N|N
CHEK|Check-Cap Ltd. - Ordinary Share|S|N|N|100|N|N
CHI|Calamos Convertible Opportunities and Income Fund - Closed End Fund|Q|N|N|100|N|N
CHK|Chesapeake Energy Corporation - Common Stock|Q|N|N|100|N|N
CHKEL|Chesapeake Energy Corporation - Class C Warrants|Q|N|N|100|N|N
CHKEW|Chesapeake Energy Corporation - Class A Warrants|S|N|N|100|N|N
CHKEZ|Chesapeake Energy Corporation - Class B Warrants|S|N|N|100|N|N
CHKP|Check Point Software Technologies Ltd. - Ordinary Shares|Q|N|N|100|N|N
CHMG|Chemung Financial Corp  - Common Stock|Q|N|N|100|N|N
CHNA|Loncar China BioPharma ETF|G|N|N|100|Y|N
CHNR|China Natural Resources, Inc. - Common Shares|S|N|N|100|N|N
CHPS|Xtrackers Semiconductor Select Equity ETF|G|N|N|100|Y|N
CHRD|Chord Energy Corporation - Common Stock|Q|N|N|100|N|N
CHRS|Coherus BioSciences, Inc. - Common Stock|G|N|N|100|N|N
CHRW|C.H. Robinson Worldwide, Inc. - Common Stock|Q|N|N|100|N|N
CHSCL|CHS Inc - Class B Cumulative Redeemable Preferred Stock, Series 4|Q|N|N|100|N|N
CHSCM|CHS Inc - Class B Reset Rate Cumulative Redeemable Preferred Stock, Series 3|Q|N|N|100|N|N
CHSCN|CHS Inc - Preferred Class B Series 2 Reset Rate|Q|N|N|100|N|N
CHSCO|CHS Inc - Class B Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
CHSCP|CHS Inc - 8%  Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
CHSN|Chanson International Holding - Class A Ordinary Shares|S|N|N|100|N|N
CHTR|Charter Communications, Inc. - Class A Common Stock|Q|N|N|100|N|N
CHUY|Chuy's Holdings, Inc. - Common Stock|Q|N|N|100|N|N
CHW|Calamos Global Dynamic Income Fund - Closed End Fund|Q|N|N|100|N|N
CHX|ChampionX Corporation - Common Stock|Q|N|N|100|N|N
CHY|Calamos Convertible and High Income Fund - Closed End Fund|Q|N|N|100|N|N
CIBR|First Trust NASDAQ Cybersecurity ETF|G|N|N|100|Y|N
CID|VictoryShares International High Div Volatility Wtd ETF|G|N|N|100|Y|N
CIFR|Cipher Mining Inc. - Common Stock|Q|N|N|100|N|N
CIFRW|Cipher Mining Inc. - Warrant|Q|N|N|100|N|N
CIGI|Colliers International Group Inc.  - Subordinate Voting Shares|Q|N|N|100|N|N
CIL|VictoryShares International Volatility Wtd ETF|G|N|N|100|Y|N
CINF|Cincinnati Financial Corporation - Common Stock|Q|N|N|100|N|N
CING|Cingulate Inc. - Common Stock|S|N|D|100|N|N
CINGW|Cingulate Inc. - Warrants|S|N|D|100|N|N
CIRC|JPMorgan Sustainable Consumption ETF|G|N|N|100|Y|N
CISO|CISO Global, Inc. - Common Stock|S|N|D|100|N|N
CISS|C3is Inc. - Common Stock|S|N|D|100|N|N
CITE|Cartica Acquisition Corp - Class A Ordinary Shares|G|N|D|100|N|N
CITEU|Cartica Acquisition Corp - Unit|G|N|N|100|N|N
CITEW|Cartica Acquisition Corp - Warrant|G|N|N|100|N|N
CIVB|Civista Bancshares, Inc.  - Common Stock|S|N|N|100|N|N
CIZ|VictoryShares Developed Enhanced Volatility Wtd ETF|G|N|N|100|Y|N
CIZN|Citizens Holding Company - Common Stock|G|N|N|100|N|N
CJET|Chijet Motor Company, Inc. - Ordinary Shares|G|N|N|100|N|N
CJJD|China Jo-Jo Drugstores, Inc. - Ordinary Shares|S|N|D|100|N|N
CKPT|Checkpoint Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
CLAR|Clarus Corporation - Common Stock|Q|N|N|100|N|N
CLAY|Chavant Capital Acquisition Corp. - Ordinary Shares|S|N|D|100|N|N
CLAYU|Chavant Capital Acquisition Corp. - Unit|S|N|D|100|N|N
CLAYW|Chavant Capital Acquisition Corp. - Warrants|S|N|D|100|N|N
CLBK|Columbia Financial, Inc. - Common Stock|Q|N|N|100|N|N
CLBT|Cellebrite DI Ltd. - Ordinary Shares|Q|N|N|100|N|N
CLBTW|Cellebrite DI Ltd. - Warrants|Q|N|N|100|N|N
CLDX|Celldex Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
CLEU|China Liberal Education Holdings Limited - Ordinary Shares|S|N|D|100|N|N
CLFD|Clearfield, Inc. - Common Stock|G|N|N|100|N|N
CLGN|CollPlant Biotechnologies Ltd. - Ordinary Shares|G|N|N|100|N|N
CLIN|Clean Earth Acquisitions Corp. - Class A Common Stock|G|N|N|100|N|N
CLINR|Clean Earth Acquisitions Corp. - Right|G|N|N|100|N|N
CLINU|Clean Earth Acquisitions Corp. - Unit|G|N|N|100|N|N
CLINW|Clean Earth Acquisitions Corp. - Warrant|G|N|D|100|N|N
CLIR|ClearSign Technologies Corporation - Common Stock|S|N|N|100|N|N
CLLS|Cellectis S.A. - American Depositary Shares|G|N|N|100|N|N
CLMB|Climb Global Solutions, Inc. - Common Stock|G|N|N|100|N|N
CLMT|Calumet Specialty Products Partners, L.P. - Common units representing limited partner interests|Q|N|N|100|N|N
CLNE|Clean Energy Fuels Corp. - Common Stock|Q|N|N|100|N|N
CLNN|Clene Inc. - Common Stock|S|N|D|100|N|N
CLNNW|Clene Inc. - Warrant|S|N|N|100|N|N
CLOA|BlackRock AAA CLO ETF|G|N|N|100|Y|N
CLOE|Clover Leaf Capital Corp. - Class A Common Stock|S|N|D|100|N|N
CLOER|Clover Leaf Capital Corp. - Rights|S|N|N|100|N|N
CLOEU|Clover Leaf Capital Corp. - Unit|S|N|N|100|N|N
CLOU|Global X Cloud Computing ETF|G|N|N|100|Y|N
CLOV|Clover Health Investments, Corp.  - Class A Common stock|Q|N|N|100|N|N
CLPS|CLPS Incorporation - Common Stock|G|N|N|100|N|N
CLPT|ClearPoint Neuro Inc. - Common Stock|S|N|N|100|N|N
CLRB|Cellectar Biosciences, Inc. - Common Stock|S|N|D|100|N|N
CLRC|ClimateRock - Class A Ordinary Shares|G|N|N|100|N|N
CLRCR|ClimateRock - Right|G|N|N|100|N|N
CLRCU|ClimateRock - Unit|G|N|N|100|N|N
CLRCW|ClimateRock - Warrant|G|N|N|100|N|N
CLRG|IQ U.S. Large Cap ETF|G|N|N|100|Y|N
CLRO|ClearOne, Inc. - Common Stock|S|N|D|100|N|N
CLSA|Cabana Target Leading Sector Aggressive ETF|G|N|N|100|Y|N
CLSC|Cabana Target Leading Sector Conservative ETF|G|N|N|100|Y|N
CLSD|Clearside Biomedical, Inc. - Common Stock|G|N|D|100|N|N
CLSK|CleanSpark, Inc. - Common Stock|S|N|N|100|N|N
CLSM|Cabana Target Leading Sector Moderate ETF|G|N|N|100|Y|N
CLST|Catalyst Bancorp, Inc. - common stock|S|N|N|100|N|N
CLVR|Clever Leaves Holdings Inc. - Common Shares|S|N|N|100|N|N
CLVRW|Clever Leaves Holdings Inc. - Warrant|S|N|N|100|N|N
CLWT|Euro Tech Holdings Company Limited - Ordinary Shares|S|N|N|100|N|N
CMAX|CareMax, Inc. - Class A Common Stock|Q|N|N|100|N|N
CMAXW|CareMax, Inc. - Warrant|Q|N|N|100|N|N
CMBM|Cambium Networks Corporation - Ordinary Shares|G|N|N|100|N|N
CMCA|Capitalworks Emerging Markets Acquisition Corp - Class A Ordinary Shares|G|N|D|100|N|N
CMCAU|Capitalworks Emerging Markets Acquisition Corp - Unit|G|N|N|100|N|N
CMCAW|Capitalworks Emerging Markets Acquisition Corp - Warrant|G|N|N|100|N|N
CMCO|Columbus McKinnon Corporation - Common Stock|Q|N|N|100|N|N
CMCSA|Comcast Corporation - Class A Common Stock|Q|N|N|100|N|N
CMCT|Creative Media & Community Trust Corporation - Common Stock|G|N|N|100|N|N
CME|CME Group Inc. - Class A Common Stock|Q|N|N|100|N|N
CMLS|Cumulus Media Inc. - Class A Common Stock|G|N|N|100|N|N
CMMB|Chemomab Therapeutics Ltd.  - American Depositary Shares|S|N|N|100|N|N
CMND|Clearmind Medicine Inc. - Common Shares|S|N|D|100|N|N
CMPO|CompoSecure, Inc.  - Class A Common Stock|G|N|N|100|N|N
CMPOW|CompoSecure, Inc.  - Warrant|G|N|N|100|N|N
CMPR|Cimpress plc - Ordinary Shares|Q|N|N|100|N|N
CMPS|COMPASS Pathways Plc - American Depository Shares|Q|N|N|100|N|N
CMPX|Compass Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
CMRA|Comera Life Sciences Holdings, Inc. - Common stock|S|N|D|100|N|N
CMRAW|Comera Life Sciences Holdings, Inc. - Warrant|S|N|D|100|N|N
CMRX|Chimerix, Inc. - Common Stock|G|N|N|100|N|N
CMTL|Comtech Telecommunications Corp. - Common Stock|Q|N|N|100|N|N
CNCR|Range Cancer Therapeutics ETF|G|N|N|100|Y|N
CNDT|Conduent Incorporated - Common Stock|Q|N|N|100|N|N
CNET|ZW Data Action Technologies Inc. - Common Stock|S|N|N|100|N|N
CNEY|CN Energy Group Inc. - Class A Ordinary Shares|S|N|D|100|N|N
CNFR|Conifer Holdings, Inc. - Common Stock|G|N|N|100|N|N
CNFRZ|Conifer Holdings, Inc. - 9.75% Senior Unsecured Notes due 2028|G|N|N|100|N|N
CNGL|Canna-Global Acquisition Corp - Class A Common Stock|S|N|N|100|N|N
CNGLU|Canna-Global Acquisition Corp - Unit|S|N|N|100|N|N
CNGLW|Canna-Global Acquisition Corp - Warrant|S|N|N|100|N|N
CNOB|ConnectOne Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
CNOBP|ConnectOne Bancorp, Inc. - Depositary Shares (each representing a 1/40th interest in a share of 5.25% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock, Series A, par value $0.00 per share)|Q|N|N|100|N|N
CNSL|Consolidated Communications Holdings, Inc. - Common Stock|Q|N|N|100|N|N
CNSP|CNS Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
CNTA|Centessa Pharmaceuticals plc - American Depositary Shares|Q|N|N|100|N|N
CNTB|Connect Biopharma Holdings Limited - American Depositary Shares|G|N|D|100|N|N
CNTG|Centogene N.V. - Common Shares|G|N|D|100|N|N
CNTX|Context Therapeutics Inc. - Common Stock|S|N|N|100|N|N
CNTY|Century Casinos, Inc. - Common Stock|S|N|N|100|N|N
CNVS|Cineverse Corp. - Class A Common Stock|S|N|N|100|N|N
CNXA|Connexa Sports Technologies Inc. - Common Stock|S|N|D|100|N|N
CNXC|Concentrix Corporation - Common Stock|Q|N|N|100|N|N
CNXN|PC Connection, Inc. - Common Stock|Q|N|N|100|N|N
COCH|Envoy Medical, Inc. - Class A Common Stock|S|N|N|100|N|N
COCHW|Envoy Medical, Inc. - Warrant|S|N|N|100|N|N
COCO|The Vita Coco Company, Inc. - Common Stock|Q|N|N|100|N|N
COCP|Cocrystal Pharma, Inc. - Common Stock|S|N|N|100|N|N
CODA|Coda Octopus Group, Inc. - Common stock|S|N|N|100|N|N
CODX|Co-Diagnostics, Inc. - Common Stock|S|N|N|100|N|N
COEP|Coeptis Therapeutics Holdings, Inc. - Common Stock|S|N|D|100|N|N
COEPW|Coeptis Therapeutics Holdings, Inc. - Warrants|S|N|D|100|N|N
COFS|ChoiceOne Financial Services, Inc. - Common Stock|S|N|N|100|N|N
COGT|Cogent Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
COHU|Cohu, Inc. - Common Stock|Q|N|N|100|N|N
COIN|Coinbase Global, Inc. - Class A Common Stock|Q|N|N|100|N|N
COKE|Coca-Cola Consolidated, Inc. - Common Stock|Q|N|N|100|N|N
COLB|Columbia Banking System, Inc. - Common Stock|Q|N|N|100|N|N
COLL|Collegium Pharmaceutical, Inc. - Common Stock|Q|N|N|100|N|N
COLM|Columbia Sportswear Company - Common Stock|Q|N|N|100|N|N
COMM|CommScope Holding Company, Inc. - Common Stock|Q|N|N|100|N|N
COMS|COMSovereign Holding Corp. - Common Stock|S|N|E|100|N|N
COMSP|COMSovereign Holding Corp. - 9.25% Series A Cumulative Redeemable Perpetual Preferred Stock|S|N|H|100|N|N
COMSW|COMSovereign Holding Corp. - Warrants|S|N|E|100|N|N
COMT|iShares GSCI Commodity Dynamic Roll Strategy ETF|G|N|N|100|Y|N
CONL|GraniteShares 1.5x COIN Daily ETF|G|N|N|100|Y|N
CONN|Conn's, Inc. - Common Stock|Q|N|N|100|N|N
CONX|CONX Corp. - Class A Common Stock|S|N|D|100|N|N
CONXU|CONX Corp. - Unit|S|N|D|100|N|N
CONXW|CONX Corp. - Warrant|S|N|D|100|N|N
COO|The Cooper Companies, Inc.  - Common Stock|Q|N|N|100|N|N
COOL|Corner Growth Acquisition Corp. - Class A Ordinary Shares|S|N|N|100|N|N
COOLU|Corner Growth Acquisition Corp. - Unit|S|N|N|100|N|N
COOLW|Corner Growth Acquisition Corp. - Warrant|S|N|N|100|N|N
COOP|Mr. Cooper Group Inc. - Common Stock|S|N|N|100|N|N
COPJ|Sprott Junior Copper Miners ETF|G|N|N|100|Y|N
CORT|Corcept Therapeutics Incorporated - Common Stock|S|N|N|100|N|N
COSM|Cosmos Health Inc. - Common Stock|S|N|N|100|N|N
COST|Costco Wholesale Corporation - Common Stock|Q|N|N|100|N|N
COWG|Pacer US Large Cap Cash Cows Growth Leaders ETF|G|N|N|100|Y|N
COWS|Amplify Cash Flow Dividend Leaders ETF|G|N|N|100|Y|N
COYA|Coya Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
CPHC|Canterbury Park Holding Corporation - Common Stock|G|N|N|100|N|N
CPIX|Cumberland Pharmaceuticals Inc. - Common Stock|Q|N|N|100|N|N
CPLP|Capital Product Partners L.P. - common units representing limited partner interests|Q|N|N|100|N|N
CPOP|Pop Culture Group Co., Ltd - Class A Ordinary Shares|S|N|D|100|N|N
CPRT|Copart, Inc. - Common Stock|Q|N|N|100|N|N
CPRX|Catalyst Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
CPSH|CPS Technologies Corp. - Common Stock|S|N|N|100|N|N
CPSI|Computer Programs and Systems, Inc. - Common Stock|Q|N|N|100|N|N
CPSS|Consumer Portfolio Services, Inc. - Common Stock|G|N|N|100|N|N
CPTN|Cepton, Inc. - Common Stock|S|N|N|100|N|N
CPTNW|Cepton, Inc. - Warrant|S|N|N|100|N|N
CPZ|Calamos Long/Short Equity & Dynamic Income Trust - Closed End Fund|Q|N|N|100|N|N
CRAI|CRA International,Inc. - Common Stock|Q|N|N|100|N|N
CRBP|Corbus Pharmaceuticals Holdings, Inc. - Common Stock|S|N|N|100|N|N
CRBU|Caribou Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
CRCT|Cricut, Inc. - Class A common stock|Q|N|N|100|N|N
CRDF|Cardiff Oncology, Inc. - Common Stock|S|N|N|100|N|N
CRDL|Cardiol Therapeutics Inc. - Class A Common Shares|S|N|N|100|N|N
CRDO|Credo Technology Group Holding Ltd - Ordinary Shares|Q|N|N|100|N|N
CREG|Smart Powerr Corp. - Common Stock|S|N|N|100|N|N
CRESW|Cresud S.A.C.I.F. y A. - Warrant|S|N|N|100|N|N
CRESY|Cresud S.A.C.I.F. y A. - American Depositary Shares, each representing ten shares of Common Stock|Q|N|N|100|N|N
CREX|Creative Realities, Inc. - Common Stock|S|N|N|100|N|N
CREXW|Creative Realities, Inc. - Warrant|S|N|N|100|N|N
CRGE|Charge Enterprises, Inc. - Common Stock|G|N|D|100|N|N
CRGO|Freightos Limited - Ordinary shares|S|N|N|100|N|N
CRGOW|Freightos Limited - Warrants|S|N|N|100|N|N
CRIS|Curis, Inc. - Common Stock|S|N|N|100|N|N
CRKN|Crown Electrokinetics Corp. - Common Stock|S|N|N|100|N|N
CRMD|CorMedix Inc. - Common Stock|G|N|N|100|N|N
CRMT|America's Car-Mart, Inc. - Common Stock|Q|N|N|100|N|N
CRNC|Cerence Inc. - Common Stock|Q|N|N|100|N|N
CRNT|Ceragon Networks Ltd. - Ordinary Shares|Q|N|N|100|N|N
CRNX|Crinetics Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
CRON|Cronos Group Inc. - Common Share|G|N|N|100|N|N
CROX|Crocs, Inc. - Common Stock|Q|N|N|100|N|N
CRSP|CRISPR Therapeutics AG - Common Shares|G|N|N|100|N|N
CRSR|Corsair Gaming, Inc. - Common Stock|Q|N|N|100|N|N
CRTO|Criteo S.A. - American Depositary Shares|Q|N|N|100|N|N
CRUS|Cirrus Logic, Inc. - Common Stock|Q|N|N|100|N|N
CRVL|CorVel Corp. - Common Stock|Q|N|N|100|N|N
CRVO|CervoMed Inc. - Common Stock|S|N|N|100|N|N
CRVS|Corvus Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
CRWD|CrowdStrike Holdings, Inc. - Class A Common Stock|Q|N|N|100|N|N
CRWS|Crown Crafts, Inc. - Common Stock|S|N|N|100|N|N
CSA|VictoryShares US Small Cap Volatility Wtd ETF|G|N|N|100|Y|N
CSB|VictoryShares US Small Cap High Div Volatility Wtd ETF|G|N|N|100|Y|N
CSBR|Champions Oncology, Inc. - Common Stock|S|N|N|100|N|N
CSCO|Cisco Systems, Inc. - Common Stock|Q|N|N|100|N|N
CSF|VictoryShares US Discovery Enhanced Volatility Wtd ETF|G|N|N|100|Y|N
CSGP|CoStar Group, Inc. - Common Stock|Q|N|N|100|N|N
CSGS|CSG Systems International, Inc. - Common Stock|Q|N|N|100|N|N
CSIQ|Canadian Solar Inc. - Common Shares|Q|N|N|100|N|N
CSLM|CSLM Acquisition Corp. - Class A Ordinary Share|S|N|N|100|N|N
CSLMR|CSLM Acquisition Corp. - Right|S|N|N|100|N|N
CSLMU|CSLM Acquisition Corp. - Unit|S|N|N|100|N|N
CSLMW|CSLM Acquisition Corp. - Warrant|S|N|D|100|N|N
CSLR|Complete Solaria, Inc. - Common Stock|G|N|N|100|N|N
CSLRW|Complete Solaria, Inc. - Warrant|S|N|N|100|N|N
CSML|IQ U.S. Small Cap ETF|G|N|N|100|Y|N
CSPI|CSP Inc. - Common Stock|G|N|N|100|N|N
CSQ|Calamos Strategic Total Return Fund - Closed End Fund|Q|N|N|100|N|N
CSSE|Chicken Soup for the Soul Entertainment, Inc. - Class A Common Stock|G|N|D|100|N|N
CSSEL|Chicken Soup for the Soul Entertainment, Inc. - Warrant|G|N|N|100|N|N
CSSEN|Chicken Soup for the Soul Entertainment, Inc. - 9.50% Notes due 2025|G|N|N|100|N|N
CSSEP|Chicken Soup for the Soul Entertainment, Inc. - 9.75% Series A Cumulative Redeemable Perpetual Preferred Stock|G|N|N|100|N|N
CSTE|Caesarstone Ltd. - Ordinary Shares|Q|N|N|100|N|N
CSTL|Castle Biosciences, Inc. - Common stock|G|N|N|100|N|N
CSTR|CapStar Financial Holdings, Inc. - Common Stock|Q|N|N|100|N|N
CSWC|Capital Southwest Corporation - Common Stock|Q|N|N|100|N|N
CSWCZ|Capital Southwest Corporation - 7.75% Notes due 2028|Q|N|N|100|N|N
CSWI|CSW Industrials, Inc. - Common Stock|Q|N|N|100|N|N
CSX|CSX Corporation - Common Stock|Q|N|N|100|N|N
CTAS|Cintas Corporation - Common Stock|Q|N|N|100|N|N
CTBI|Community Trust Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
CTCX|Carmell Therapeutics Corporation - Class A Common Stock|S|N|N|100|N|N
CTCXW|Carmell Therapeutics Corporation - Warrant|S|N|N|100|N|N
CTEC|Global X CleanTech ETF|G|N|N|100|Y|N
CTG|Computer Task Group, Incorporated - Common Stock|Q|N|N|100|N|N
CTHR|Charles & Colvard Ltd. - Common Stock|S|N|D|100|N|N
CTKB|Cytek Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
CTLP|Cantaloupe, Inc. - Common Stock|Q|N|N|100|N|N
CTMX|CytomX Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
CTNT|Cheetah Net Supply Chain Service Inc. - Class A Common Stock|S|N|N|100|N|N
CTRM|Castor Maritime Inc. - Common Shares|S|N|D|100|N|N
CTRN|Citi Trends, Inc. - Common Stock|Q|N|N|100|N|N
CTSH|Cognizant Technology Solutions Corporation - Class A Common Stock|Q|N|N|100|N|N
CTSO|Cytosorbents Corporation - Common Stock|S|N|N|100|N|N
CTXR|Citius Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
CUBA|The Herzfeld Caribbean Basin Fund, Inc. - Closed End Fund|S|N|N|100|N|N
CUE|Cue Biopharma, Inc. - Common Stock|S|N|N|100|N|N
CUEN|Cuentas, Inc. - Common Stock|S|N|D|100|N|N
CUENW|Cuentas, Inc. - Warrant|S|N|D|100|N|N
CULL|Cullman Bancorp, Inc. - Common Stock|S|N|N|100|N|N
CURI|CuriosityStream Inc.  - Class A Common Stock|S|N|D|100|N|N
CURIW|CuriosityStream Inc.  - Warrant|S|N|N|100|N|N
CUTR|Cutera, Inc. - Common Stock|Q|N|N|100|N|N
CVAC|CureVac N.V. - Ordinary Shares|G|N|N|100|N|N
CVBF|CVB Financial Corporation - Common Stock|Q|N|N|100|N|N
CVCO|Cavco Industries, Inc. - Common Stock|Q|N|N|100|N|N
CVCY|Central Valley Community Bancorp - Common Stock|S|N|N|100|N|N
CVGI|Commercial Vehicle Group, Inc. - Common Stock|Q|N|N|100|N|N
CVGW|Calavo Growers, Inc. - Common Stock|Q|N|N|100|N|N
CVKD|Cadrenal Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
CVLG|Covenant Logistics Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
CVLT|Commvault Systems, Inc. - Common Stock|Q|N|N|100|N|N
CVLY|Codorus Valley Bancorp, Inc - Common Stock|G|N|N|100|N|N
CVRX|CVRx, Inc. - Common Stock|Q|N|N|100|N|N
CVV|CVD Equipment Corporation - Common Stock|S|N|N|100|N|N
CWBC|Community West Bancshares - Common Stock|G|N|N|100|N|N
CWBR|CohBar, Inc. - Common Stock|S|N|N|100|N|N
CWCO|Consolidated Water Co. Ltd. - Ordinary Shares|Q|N|N|100|N|N
CWD|CaliberCos Inc. - Class A Common Stock|S|N|N|100|N|N
CWST|Casella Waste Systems, Inc. - Class A Common Stock|Q|N|N|100|N|N
CXAI|CXApp Inc. - Class A Common Stock|S|N|N|100|N|N
CXAIW|CXApp Inc. - Warrant|S|N|N|100|N|N
CXDO|Crexendo, Inc. - Common Stock|S|N|N|100|N|N
CXSE|WisdomTree China ex-State-Owned Enterprises Fund|G|N|N|100|Y|N
CYAN|Cyanotech Corporation - Common Stock|S|N|D|100|N|N
CYBR|CyberArk Software Ltd. - Ordinary Shares|Q|N|N|100|N|N
CYCC|Cyclacel Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
CYCCP|Cyclacel Pharmaceuticals, Inc. - 6% Convertible Preferred Stock|S|N|N|100|N|N
CYCN|Cyclerion Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
CYN|Cyngn Inc. - Common stock|S|N|D|100|N|N
CYRX|CryoPort, Inc. - Common Stock|S|N|N|100|N|N
CYT|Cyteir Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
CYTH|Cyclo Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
CYTHW|Cyclo Therapeutics, Inc. - Warrant|S|N|N|100|N|N
CYTK|Cytokinetics, Incorporated - Common Stock|Q|N|N|100|N|N
CYTO|Altamira Therapeutics Ltd. - Common Shares|S|N|D|100|N|N
CZFS|Citizens Financial Services, Inc. - Common Stock|S|N|N|100|N|N
CZNC|Citizens & Northern Corp - Common Stock|S|N|N|100|N|N
CZR|Caesars Entertainment, Inc. - Common Stock|Q|N|N|100|N|N
CZWI|Citizens Community Bancorp, Inc. - Common Stock|G|N|N|100|N|N
DADA|Dada Nexus Limited - American Depositary Shares|Q|N|N|100|N|N
DAIO|Data I/O Corporation - Common Stock|S|N|N|100|N|N
DAKT|Daktronics, Inc. - Common Stock|Q|N|N|100|N|N
DALI|First Trust Dorsey Wright DALI 1 ETF|G|N|N|100|Y|N
DALN|DallasNews Corporation - Series A Common Stock|S|N|N|100|N|N
DAPP|VanEck Digital Transformation ETF|G|N|N|100|Y|N
DARE|Dare Bioscience, Inc. - Common Stock|S|N|D|100|N|N
DASH|DoorDash, Inc. - Common Stock|Q|N|N|100|N|N
DATS|DatChat, Inc. - Common Stock|S|N|N|100|N|N
DATSW|DatChat, Inc. - Series A Warrant|S|N|N|100|N|N
DAVE|Dave Inc.  - Class A Common Stock|G|N|N|100|N|N
DAVEW|Dave Inc.  - Warrants|G|N|N|100|N|N
DAWN|Day One Biopharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
DAX|Global X DAX Germany ETF|G|N|N|100|Y|N
DBGI|Digital Brands Group, Inc. - Common Stock|S|N|N|100|N|N
DBGIW|Digital Brands Group, Inc. - Warrant|S|N|N|100|N|N
DBVT|DBV Technologies S.A. - American Depositary Shares|Q|N|N|100|N|N
DBX|Dropbox, Inc. - Class A Common Stock|Q|N|N|100|N|N
DCBO|Docebo Inc. - Common Shares|Q|N|N|100|N|N
DCFC|Tritium DCFC Limited - Ordinary Shares|G|N|N|100|N|N
DCFCW|Tritium DCFC Limited - Warrant|G|N|N|100|N|N
DCGO|DocGo Inc. - Common Stock|S|N|N|100|N|N
DCOM|Dime Community Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
DCOMP|Dime Community Bancshares, Inc. - Fixed-Rate Non-Cumulative Perpetual Preferred Stock, Series A|Q|N|N|100|N|N
DCPH|Deciphera Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
DCTH|Delcath Systems, Inc. - Common Stock|S|N|N|100|N|N
DDI|DoubleDown Interactive Co., Ltd. - American Depository Shares|Q|N|N|100|N|N
DDIV|First Trust Dorsey Wright Momentum & Dividend ETF|G|N|N|100|Y|N
DDOG|Datadog, Inc. - Class A Common Stock|Q|N|N|100|N|N
DECA|Denali Capital Acquisition Corp. - Class A Ordinary Shares|G|N|N|100|N|N
DECAU|Denali Capital Acquisition Corp. - Unit|G|N|N|100|N|N
DECAW|Denali Capital Acquisition Corp. - Warrant|G|N|N|100|N|N
DEMZ|Democratic Large Cap Core ETF|G|N|N|100|Y|N
DENN|Denny's Corporation - Common Stock|S|N|N|100|N|N
DERM|Journey Medical Corporation - Common Stock|S|N|N|100|N|N
DFLI|Dragonfly Energy Holdings Corp - Common Stock|G|N|N|100|N|N
DFLIW|Dragonfly Energy Holdings Corp - Warrant|S|N|N|100|N|N
DGHI|Digihost Technology Inc. - Common Subordinate Voting Shares|S|N|N|100|N|N
DGICA|Donegal Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
DGICB|Donegal Group, Inc. - Class B Common Stock|Q|N|N|100|N|N
DGII|Digi International Inc. - Common Stock|Q|N|N|100|N|N
DGLY|Digital Ally, Inc. - Common Stock|S|N|N|100|N|N
DGRE|WisdomTree Emerging Markets Quality Dividend Growth Fund|G|N|N|100|Y|N
DGRS|WisdomTree U.S. SmallCap Quality Dividend Growth Fund|G|N|N|100|Y|N
DGRW|WisdomTree U.S. Quality Dividend Growth Fund|G|N|N|100|Y|N
DH|Definitive Healthcare Corp. - Class A Common Stock|Q|N|N|100|N|N
DHAC|Digital Health Acquisition Corp. - Common Stock|G|N|D|100|N|N
DHACU|Digital Health Acquisition Corp. - Unit|G|N|D|100|N|N
DHACW|Digital Health Acquisition Corp. - Warrant|G|N|D|100|N|N
DHC|Diversified Healthcare Trust  - Common Shares of Beneficial Interest|Q|N|N|100|N|N
DHCA|DHC Acquisition Corp. - Class A ordinary share|S|N|N|100|N|N
DHCAU|DHC Acquisition Corp. - Unit|S|N|N|100|N|N
DHCAW|DHC Acquisition Corp. - Warrant|S|N|N|100|N|N
DHCNI|Diversified Healthcare Trust  - 5.625% Senior Notes due 2042|Q|N|N|100|N|N
DHCNL|Diversified Healthcare Trust  - 6.25% Senior Notes Due 2046|Q|N|N|100|N|N
DHIL|Diamond Hill Investment Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
DIBS|1stdibs.com, Inc. - Common Stock|G|N|N|100|N|N
DIOD|Diodes Incorporated - Common Stock|Q|N|N|100|N|N
DISA|Disruptive Acquisition Corporation I - Class A Ordinary Shares|S|N|D|100|N|N
DISAU|Disruptive Acquisition Corporation I - Unit|S|N|D|100|N|N
DISAW|Disruptive Acquisition Corporation I - Warrant|S|N|D|100|N|N
DISH|DISH Network Corporation - Class A Common Stock|Q|N|N|100|N|N
DIST|Distoken Acquisition Corporation - Ordinary Shares|G|N|N|100|N|N
DISTR|Distoken Acquisition Corporation - Right|G|N|N|100|N|N
DISTW|Distoken Acquisition Corporation - Warrant|G|N|N|100|N|N
DIVD|Altrius Global Dividend ETF|G|N|N|100|Y|N
DJCO|Daily Journal Corp. (S.C.) - Common Stock|S|N|N|100|N|N
DKDCA|Data Knights Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
DKDCU|Data Knights Acquisition Corp. - Unit|S|N|N|100|N|N
DKDCW|Data Knights Acquisition Corp. - Warrant|S|N|N|100|N|N
DKNG|DraftKings Inc. - Class A Common Stock|Q|N|N|100|N|N
DLHC|DLH Holdings Corp. - Common Stock|S|N|N|100|N|N
DLO|DLocal Limited - Class A Common Shares|Q|N|N|100|N|N
DLPN|Dolphin Entertainment, Inc. - Common Stock|S|N|N|100|N|N
DLTH|Duluth Holdings Inc. - Class B Common Stock|Q|N|N|100|N|N
DLTR|Dollar Tree, Inc. - Common Stock|Q|N|N|100|N|N
DMAC|DiaMedica Therapeutics Inc. - Common Stock|S|N|N|100|N|N
DMAQ|Deep Medicine Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
DMAQR|Deep Medicine Acquisition Corp. - Rights|S|N|N|100|N|N
DMAT|Global X Disruptive Materials ETF|G|N|N|100|Y|N
DMK|DMK Pharmaceuticals Corporation - Common Stock|S|N|D|100|N|N
DMLP|Dorchester Minerals, L.P. - Common Units Representing Limited Partnership Interests|Q|N|N|100|N|N
DMRC|Digimarc Corporation - Common Stock|Q|N|N|100|N|N
DMTK|DermTech, Inc. - Common Stock|S|N|N|100|N|N
DMXF|iShares ESG Advanced MSCI EAFE ETF|G|N|N|100|Y|N
DNLI|Denali Therapeutics Inc. - Common Stock|Q|N|N|100|N|N
DNTH|Dianthus Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
DNUT|Krispy Kreme, Inc. - Common Stock|Q|N|N|100|N|N
DOCU|DocuSign, Inc. - Common Stock|Q|N|N|100|N|N
DOGZ|Dogness (International) Corporation - Class A Common Stock|S|N|D|100|N|N
DOMH|Dominari Holdings Inc. - Common Stock|S|N|N|100|N|N
DOMO|Domo, Inc. - Class B Common Stock|G|N|N|100|N|N
DOOO|BRP Inc. - Common Subordinate Voting Shares|Q|N|N|100|N|N
DORM|Dorman Products, Inc. - Common Stock|Q|N|N|100|N|N
DOX|Amdocs Limited - Ordinary Shares|Q|N|N|100|N|N
DOYU|DouYu International Holdings Limited - American Depositary Shares|Q|N|N|100|N|N
DPCS|DP Cap Acquisition Corp I - Class A Ordinary Shares|G|N|D|100|N|N
DPCSU|DP Cap Acquisition Corp I - Unit|G|N|D|100|N|N
DPCSW|DP Cap Acquisition Corp I - Warrants|G|N|D|100|N|N
DPRO|Draganfly Inc. - Common Shares|S|N|D|100|N|N
DRCT|Direct Digital Holdings, Inc. - Class A Common Stock|S|N|N|100|N|N
DRCTW|Direct Digital Holdings, Inc. - Warrant|S|N|N|100|N|N
DRIO|DarioHealth Corp. - Common Stock|S|N|N|100|N|N
DRIV|Global X Autonomous & Electric Vehicles ETF|G|N|N|100|Y|N
DRMA|Dermata Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
DRMAW|Dermata Therapeutics, Inc. - Warrant|S|N|N|100|N|N
DRRX|DURECT Corporation - Common Stock|S|N|N|100|N|N
DRS|Leonardo DRS, Inc. - Common Stock|Q|N|N|100|N|N
DRTS|Alpha Tau Medical Ltd. - Ordinary Shares|S|N|N|100|N|N
DRTSW|Alpha Tau Medical Ltd. - Warrant|S|N|N|100|N|N
DRUG|Bright Minds Biosciences Inc. - common stock|S|N|N|100|N|N
DRVN|Driven Brands Holdings Inc. - Common Stock|Q|N|N|100|N|N
DSGN|Design Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
DSGR|Distribution Solutions Group, Inc. - Common Stock|Q|N|N|100|N|N
DSGX|The Descartes Systems Group Inc. - Common Stock|Q|N|N|100|N|N
DSKE|Daseke, Inc. - Common Stock|S|N|N|100|N|N
DSP|Viant Technology Inc. - common stock|Q|N|N|100|N|N
DSWL|Deswell Industries, Inc. - Common Shares|G|N|N|100|N|N
DTCK|Davis Commodities Limited - Ordinary Shares|S|N|N|100|N|N
DTI|Drilling Tools International Corporation  - Common Stock|S|N|N|100|N|N
DTIL|Precision BioSciences, Inc. - Common Stock|Q|N|D|100|N|N
DTSS|Datasea Inc. - Common Stock|S|N|D|100|N|N
DTST|Data Storage Corporation - Common Stock|S|N|N|100|N|N
DTSTW|Data Storage Corporation - Warrant|S|N|N|100|N|N
DUET|DUET Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
DUETU|DUET Acquisition Corp. - Unit|G|N|N|100|N|N
DUETW|DUET Acquisition Corp. - Warrant|G|N|N|100|N|N
DUNE|Dune Acquisition Corporation - Class A Common Stock|S|N|N|100|N|N
DUNEU|Dune Acquisition Corporation - Unit|S|N|N|100|N|N
DUNEW|Dune Acquisition Corporation - Warrant|S|N|N|100|N|N
DUO|Fangdd Network Group Ltd. - American Depositary Shares|G|N|N|100|N|N
DUOL|Duolingo, Inc. - Class A Common Stock|Q|N|N|100|N|N
DUOT|Duos Technologies Group, Inc. - Common Stock|S|N|N|100|N|N
DVAL|BrandywineGLOBAL-Dynamic US Large Cap Value ETF|G|N|N|100|Y|N
DVAX|Dynavax Technologies Corporation - Common Stock|Q|N|N|100|N|N
DVLU|First Trust Dorsey Wright Momentum & Value ETF|G|N|N|100|Y|N
DVOL|First Trust Dorsey Wright Momentum & Low Volatility ETF|G|N|N|100|Y|N
DVY|iShares Select Dividend ETF|G|N|N|100|Y|N
DWAC|Digital World Acquisition Corp. - Class A Common Stock|G|N|E|100|N|N
DWACU|Digital World Acquisition Corp. - Units|G|N|E|100|N|N
DWACW|Digital World Acquisition Corp. - Warrants|G|N|E|100|N|N
DWAS|Invesco Dorsey Wright SmallCap Momentum ETF|G|N|N|100|Y|N
DWAW|AdvisorShares Dorsey Wright FSM All Cap World ETF|G|N|N|100|Y|N
DWSH|AdvisorShares Dorsey Wright Short ETF|G|N|N|100|Y|N
DWSN|Dawson Geophysical Company - Common Stock|Q|N|N|100|N|N
DWUS|AdvisorShares Dorsey Wright FSM US Core ETF|G|N|N|100|Y|N
DXCM|DexCom, Inc. - Common Stock|Q|N|N|100|N|N
DXGE|WisdomTree Germany Hedged Equity Fund|G|N|N|100|Y|N
DXJS|WisdomTree Japan Hedged SmallCap Equity Fund|G|N|N|100|Y|N
DXLG|Destination XL Group, Inc. - Common Stock|G|N|N|100|N|N
DXPE|DXP Enterprises, Inc. - Common Stock|Q|N|N|100|N|N
DXR|Daxor Corporation - Closed End Fund|S|N|N|100|N|N
DXYN|The Dixie Group, Inc. - Common Stock|G|N|D|100|N|N
DYAI|Dyadic International, Inc. - Common Stock|S|N|N|100|N|N
DYN|Dyne Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
DYNT|Dynatronics Corporation - Common Stock|S|N|D|100|N|N
DYTA|SGI Dynamic Tactical ETF|G|N|N|100|Y|N
DZSI|DZS Inc. - Common Stock|S|N|E|100|N|N
EA|Electronic Arts Inc. - Common Stock|Q|N|N|100|N|N
EAC|Edify Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
EACPU|Edify Acquisition Corp. - Units|S|N|N|100|N|N
EACPW|Edify Acquisition Corp. - Warrant|S|N|N|100|N|N
EAR|Eargo, Inc. - Common Stock|Q|N|N|100|N|N
EAST|Eastside Distilling, Inc. - Common Stock|S|N|N|100|N|N
EBAY|eBay Inc. - Common Stock|Q|N|N|100|N|N
EBC|Eastern Bankshares, Inc. - Common Stock|Q|N|N|100|N|N
EBIX|Ebix, Inc. - Common Stock|Q|N|N|100|N|N
EBIZ|Global X E-commerce ETF|G|N|N|100|Y|N
EBMT|Eagle Bancorp Montana, Inc. - Common Stock|G|N|N|100|N|N
EBON|Ebang International Holdings Inc. - Class A Ordinary Shares|Q|N|N|100|N|N
EBTC|Enterprise Bancorp Inc - Common Stock|Q|N|N|100|N|N
ECBK|ECB Bancorp, Inc. - Common Stock|S|N|N|100|N|N
ECOR|electroCore, Inc. - Common Stock|S|N|N|100|N|N
ECOW|Pacer Emerging Markets Cash Cows 100 ETF|G|N|N|100|Y|N
ECPG|Encore Capital Group Inc - Common Stock|Q|N|N|100|N|N
ECX|ECARX Holdings Inc. - Class A Ordinary shares|G|N|N|100|N|N
ECXWW|ECARX Holdings Inc. - Warrants|S|N|N|100|N|N
EDAP|EDAP TMS S.A. - American Depositary Shares, each representing One Ordinary Share|G|N|N|100|N|N
EDBL|Edible Garden AG Incorporated - Common Stock|S|N|N|100|N|N
EDBLW|Edible Garden AG Incorporated - Warrant|S|N|N|100|N|N
EDIT|Editas Medicine, Inc. - Common Stock|Q|N|N|100|N|N
EDOC|Global X Telemedicine & Digital Health ETF|G|N|N|100|Y|N
EDRY|EuroDry Ltd. - Common Shares|S|N|N|100|N|N
EDSA|Edesa Biotech, Inc. - Common Shares|S|N|D|100|N|N
EDTK|Skillful Craftsman Education Technology Limited - Ordinary Share|S|N|N|100|N|N
EDUC|Educational Development Corporation - Common Stock|G|N|N|100|N|N
EDUT|Global X Education ETF|G|N|N|100|Y|N
EEFT|Euronet Worldwide, Inc. - Common Stock|Q|N|N|100|N|N
EEIQ|EpicQuest Education Group International Limited - Common Stock|S|N|N|100|N|N
EEMA|iShares MSCI Emerging Markets Asia ETF|G|N|N|100|Y|N
EFAS|Global X MSCI SuperDividend EAFE ETF|G|N|N|100|Y|N
EFHT|EF Hutton Acquisition Corporation I - Common Stock|G|N|N|100|N|N
EFHTR|EF Hutton Acquisition Corporation I - Rights|G|N|N|100|N|N
EFHTW|EF Hutton Acquisition Corporation I - Warrant|G|N|N|100|N|N
EFOI|Energy Focus, Inc. - Common Stock|S|N|N|100|N|N
EFRA|iShares Environmental Infrastructure and Industrials ETF|G|N|N|100|Y|N
EFSC|Enterprise Financial Services Corporation - Common Stock|Q|N|N|100|N|N
EFSCP|Enterprise Financial Services Corporation - Depositary Shares Each Representing a 1/40th Interest in a Share of 5% Fixed Rate Non-Cumulative Perpetual Preferred Stock, Series A|Q|N|N|100|N|N
EFTR|eFFECTOR Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
EFTRW|eFFECTOR Therapeutics, Inc. - Warrant|S|N|N|100|N|N
EGAN|eGain Corporation - Common Stock|S|N|N|100|N|N
EGBN|Eagle Bancorp, Inc. - Common Stock|S|N|N|100|N|N
EGHT|8x8 Inc - Common stock|Q|N|N|100|N|N
EGIO|Edgio, Inc. - Common Stock|Q|N|D|100|N|N
EGLX|Enthusiast Gaming Holdings Inc. - Common Stock|S|N|D|100|N|N
EGRX|Eagle Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
EH|EHang Holdings Limited - ADS|G|N|N|100|N|N
EHTH|eHealth, Inc. - Common Stock|Q|N|N|100|N|N
EIGR|Eiger BioPharmaceuticals, Inc. - Common Stock|G|N|D|100|N|N
EJH|E-Home Household Service Holdings Limited - Ordinary shares|S|N|N|100|N|N
EKG|First Trust Nasdaq Lux Digital Health Solutions ETF|G|N|N|100|Y|N
EKSO|Ekso Bionics Holdings, Inc. - Common Stock|S|N|D|100|N|N
ELBM|Electra Battery Materials Corporation - Common Stock|S|N|D|100|N|N
ELDN|Eledon Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
ELEV|Elevation Oncology, Inc. - Common stock|Q|N|D|100|N|N
ELSE|Electro-Sensors, Inc. - Common Stock|S|N|N|100|N|N
ELTK|Eltek Ltd. - Ordinary Shares|S|N|N|100|N|N
ELTX|Elicio Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
ELUT|Elutia, Inc. - Class A Common Stock|S|N|D|100|N|N
ELVA|Electrovaya Inc. - Common Shares|S|N|N|100|N|N
ELVN|Enliven Therapeutics, Inc.  - Common Stock|Q|N|N|100|N|N
ELWS|Earlyworks Co., Ltd. - American Depositary Shares|S|N|N|100|N|N
ELYM|Eliem Therapeutics, Inc - Common Stock|G|N|N|100|N|N
EM|Smart Share Global Limited - American Depositary Shares|Q|N|D|100|N|N
EMB|iShares J.P. Morgan USD Emerging Markets Bond ETF|G|N|N|100|Y|N
EMBC|Embecta Corp. - Common Stock|Q|N|N|100|N|N
EMCB|WisdomTree Emerging Markets Corporate Bond Fund|G|N|N|100|Y|N
EMCG|Embrace Change Acquisition Corp - Ordinary Shares|G|N|N|100|N|N
EMCGR|Embrace Change Acquisition Corp - Rights|G|N|N|100|N|N
EMCGU|Embrace Change Acquisition Corp - Units|G|N|N|100|N|N
EMCGW|Embrace Change Acquisition Corp - Warrants|G|N|N|100|N|N
EMIF|iShares Emerging Markets Infrastructure ETF|G|N|N|100|Y|N
EMKR|EMCORE Corporation - Common Stock|G|N|D|100|N|N
EML|Eastern Company (The) - Common Stock|G|N|N|100|N|N
EMLD|FTAC Emerald Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
EMLDU|FTAC Emerald Acquisition Corp. - Unit|G|N|N|100|N|N
EMLDW|FTAC Emerald Acquisition Corp. - Warrant|G|N|N|100|N|N
EMXC|iShares MSCI Emerging Markets ex China ETF|G|N|N|100|Y|N
EMXF|iShares ESG Advanced MSCI EM ETF|G|N|N|100|Y|N
ENCP|Energem Corp - Class A Ordinary Shares|G|N|D|100|N|N
ENCPU|Energem Corp - Unit|G|N|D|100|N|N
ENCPW|Energem Corp - Warrant|G|N|D|100|N|N
ENER|Accretion Acquisition Corp. - Common Stock|G|N|N|100|N|N
ENERR|Accretion Acquisition Corp. - Right|G|N|N|100|N|N
ENERU|Accretion Acquisition Corp. - Unit|G|N|N|100|N|N
ENERW|Accretion Acquisition Corp. - Warrant|G|N|N|100|N|N
ENG|ENGlobal Corporation - Common Stock|S|N|D|100|N|N
ENLT|Enlight Renewable Energy Ltd. - Ordinary Shares|Q|N|N|100|N|N
ENLV|Enlivex Therapeutics Ltd. - Ordinary Shares|S|N|N|100|N|N
ENPH|Enphase Energy, Inc. - Common Stock|G|N|N|100|N|N
ENSC|Ensysce Biosciences, Inc. - Common Stock|S|N|N|100|N|N
ENSG|The Ensign Group, Inc. - Common Stock|Q|N|N|100|N|N
ENTA|Enanta Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
ENTG|Entegris, Inc. - Common Stock|Q|N|N|100|N|N
ENTX|Entera Bio Ltd. - Ordinary Shares|S|N|D|100|N|N
ENVB|Enveric Biosciences, Inc.  - Common Stock|S|N|N|100|N|N
ENVX|Enovix Corporation - Common Stock|Q|N|N|100|N|N
ENZL|iShares MSCI New Zealand ETF|G|N|N|100|Y|N
EOLS|Evolus, Inc. - Common Stock|G|N|N|100|N|N
EOSE|Eos Energy Enterprises, Inc. - Common Stock|S|N|N|100|N|N
EOSEW|Eos Energy Enterprises, Inc. - Warrant|S|N|N|100|N|N
EPIX|ESSA Pharma Inc. - Common Stock|S|N|N|100|N|N
EPOW|Sunrise New Energy Co., Ltd - Ordinary Shares|S|N|N|100|N|N
EPSN|Epsilon Energy Ltd. - Common Shares|G|N|N|100|N|N
EQ|Equillium, Inc. - Common Stock|S|N|D|100|N|N
EQIX|Equinix, Inc. - Common Stock|Q|N|N|100|N|N
EQRR|ProShares Equities for Rising Rates ETF|G|N|N|100|Y|N
EQRX|EQRx, Inc.  - Common Stock|G|N|N|100|N|N
EQRXW|EQRx, Inc.  - Warrant|G|N|N|100|N|N
ERAS|Erasca, Inc. - Common Stock|Q|N|N|100|N|N
ERET|iShares Environmentally Aware Real Estate ETF|G|N|N|100|Y|N
ERIC|Ericsson - American Depositary Shares each representing 1 underlying Class B share|Q|N|N|100|N|N
ERIE|Erie Indemnity Company - Class A Common Stock|Q|N|N|100|N|N
ERII|Energy Recovery, Inc. - Common Stock|Q|N|N|100|N|N
ERNA|Eterna Therapeutics Inc. - Common Stock|S|N|D|100|N|N
ESAC|ESGEN Acquisition Corporation - Class A Ordinary Shares|G|N|D|100|N|N
ESACU|ESGEN Acquisition Corporation - Unit|G|N|D|100|N|N
ESACW|ESGEN Acquisition Corporation - Warrants|G|N|D|100|N|N
ESCA|Escalade, Incorporated - Common Stock|G|N|N|100|N|N
ESEA|Euroseas Ltd. - Common Stock|S|N|N|100|N|N
ESGD|iShares ESG Aware MSCI EAFE ETF|G|N|N|100|Y|N
ESGE|iShares ESG Aware MSCI EM ETF|G|N|N|100|Y|N
ESGL|ESGL Holdings Limited - Class A Ordinary Shares|G|N|N|100|N|N
ESGLW|ESGL Holdings Limited - Warrants|G|N|N|100|N|N
ESGR|Enstar Group Limited - Ordinary Shares|Q|N|N|100|N|N
ESGRO|Enstar Group Limited - Depository Shares 7.00% Perpetual Non-Cumulative Preference Shares, Series E|Q|N|N|100|N|N
ESGRP|Enstar Group Limited - Depositary Shares Each Representing 1/1000th of an interest in Preference Shares|Q|N|N|100|N|N
ESGU|iShares ESG Aware MSCI USA ETF|G|N|N|100|Y|N
ESHA|ESH Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
ESHAR|ESH Acquisition Corp. - Right|G|N|N|100|N|N
ESLA|Estrella Immunopharma, Inc. - Common Stock|S|N|D|100|N|N
ESLAW|Estrella Immunopharma, Inc. - Warrant|S|N|N|100|N|N
ESLT|Elbit Systems Ltd. - Ordinary Shares|Q|N|N|100|N|N
ESMV|iShares ESG MSCI USA Min Vol Factor ETF|G|N|N|100|Y|N
ESOA|Energy Services of America Corporation - Common Stock|S|N|N|100|N|N
ESPO|VanEck Video Gaming and eSports ETF|G|N|N|100|Y|N
ESPR|Esperion Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
ESQ|Esquire Financial Holdings, Inc. - Common Stock|S|N|N|100|N|N
ESSA|ESSA Bancorp, Inc. - common stock|Q|N|N|100|N|N
ESTA|Establishment Labs Holdings Inc. - Common Shares|S|N|N|100|N|N
ETAO|Etao International Co., Ltd. - Ordinary Shares|S|N|D|100|N|N
ETEC|iShares Breakthrough Environmental Solutions ETF|G|N|N|100|Y|N
ETNB|89bio, Inc. - Common Stock|G|N|N|100|N|N
ETON|Eton Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
ETSY|Etsy, Inc. - Common Stock|Q|N|N|100|N|N
EUDA|Euda Health Holdings Limited - Ordinary Shares|S|N|N|100|N|N
EUDAW|Euda Health Holdings Limited - Warrant|S|N|N|100|N|N
EUFN|iShares MSCI Europe Financials ETF|G|N|N|100|Y|N
EVAX|Evaxion Biotech A/S - American Depositary Share|S|N|D|100|N|N
EVBG|Everbridge, Inc. - Common Stock|G|N|N|100|N|N
EVCM|EverCommerce Inc. - Common Stock|Q|N|N|100|N|N
EVER|EverQuote, Inc. - Class A Common Stock|G|N|N|100|N|N
EVGN|Evogene Ltd. - Ordinary Shares|S|N|D|100|N|N
EVGO|EVgo Inc. - Common Stock|Q|N|D|100|N|N
EVGOW|EVgo Inc. - Warrants, each whole warrant exercisable for one share of Class A Common Stock at an exercise price of $11.50|Q|N|D|100|N|N
EVGR|Evergreen Corporation - Class A Ordinary Share|G|N|N|100|N|N
EVGRU|Evergreen Corporation - Unit|G|N|N|100|N|N
EVGRW|Evergreen Corporation - Warrant|G|N|N|100|N|N
EVLO|Evelo Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
EVLV|Evolv Technologies Holdings, Inc. - Class A Common Stock|S|N|N|100|N|N
EVLVW|Evolv Technologies Holdings, Inc. - Warrant|S|N|N|100|N|N
EVMT|Invesco Electric Vehicle Metals Commodity Strategy No K-1 ETF|G|N|N|100|Y|N
EVO|Evotec SE - American Depositary Shares each representing 1/2 of one ordinary share|Q|N|N|100|N|N
EVOK|Evoke Pharma, Inc. - Common Stock|S|N|D|100|N|N
EVRG|Evergy, Inc. - Common Stock|Q|N|N|100|N|N
EVTV|Envirotech Vehicles, Inc. - Common stock|S|N|E|100|N|N
EWBC|East West Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
EWCZ|European Wax Center, Inc. - Class A Common Stock|Q|N|N|100|N|N
EWEB|Global X Emerging Markets Internet & E-commerce ETF|G|N|N|100|Y|N
EWJV|iShares MSCI Japan Value ETF|G|N|N|100|Y|N
EWTX|Edgewise Therapeutics, Inc. - Common Stock|Q|N|D|100|N|N
EWZS|iShares MSCI Brazil Small-Cap ETF|G|N|N|100|Y|N
EXAI|Exscientia Plc - American Depositary Shares|Q|N|N|100|N|N
EXAS|Exact Sciences Corporation - Common Stock|S|N|N|100|N|N
EXC|Exelon Corporation - Common Stock|Q|N|N|100|N|N
EXEL|Exelixis, Inc. - Common Stock|Q|N|N|100|N|N
EXFY|Expensify, Inc. - Class A Common Stock|Q|N|N|100|N|N
EXLS|ExlService Holdings, Inc. - Common Stock|Q|N|N|100|N|N
EXPD|Expeditors International of Washington, Inc. - Common Stock|Q|N|N|100|N|N
EXPE|Expedia Group, Inc. - Common Stock|Q|N|N|100|N|N
EXPI|eXp World Holdings, Inc. - Common Stock|G|N|N|100|N|N
EXPO|Exponent, Inc. - Common Stock|Q|N|N|100|N|N
EXTR|Extreme Networks, Inc. - Common Stock|Q|N|N|100|N|N
EYE|National Vision Holdings, Inc. - Common Stock|Q|N|N|100|N|N
EYEN|Eyenovia, Inc. - Common Stock|S|N|N|100|N|N
EYPT|EyePoint Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
EZFL|EzFill Holdings, Inc. - Common Stock|S|N|D|100|N|N
EZGO|EZGO Technologies Ltd. - Ordinary Shares|S|N|N|100|N|N
EZPW|EZCORP, Inc. - Class A Non-Voting Common Stock|Q|N|N|100|N|N
FA|First Advantage Corporation - Common Stock|Q|N|N|100|N|N
FAAR|First Trust Alternative Absolute Return Strategy ETF|G|N|N|100|Y|N
FAB|First Trust Multi Cap Value AlphaDEX Fund|G|N|N|100|Y|N
FAD|First Trust Multi Cap Growth AlphaDEX Fund|G|N|N|100|Y|N
FALN|iShares Fallen Angels USD Bond ETF|G|N|N|100|Y|N
FAMI|Farmmi, INC. - Ordinary Shares|S|N|N|100|N|N
FANG|Diamondback Energy, Inc. - Common Stock|Q|N|N|100|N|N
FANH|Fanhua Inc. - American depositary shares, each representing 20 ordinary shares|Q|N|N|100|N|N
FARM|Farmer Brothers Company - Common Stock|Q|N|N|100|N|N
FARO|FARO Technologies, Inc. - Common Stock|Q|N|N|100|N|N
FAST|Fastenal Company - Common Stock|Q|N|N|100|N|N
FAT|FAT Brands Inc. - Common Stock|S|N|N|100|N|N
FATBB|FAT Brands Inc. - Class B Common Stock|S|N|N|100|N|N
FATBP|FAT Brands Inc. - 8.25% Series B Cumulative Preferred Stock|S|N|N|100|N|N
FATBW|FAT Brands Inc. - Warrant|S|N|N|100|N|N
FATE|Fate Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
FATP|Fat Projects Acquisition Corp - Class A Ordinary Share|G|N|D|100|N|N
FATPU|Fat Projects Acquisition Corp - Unit|G|N|D|100|N|N
FATPW|Fat Projects Acquisition Corp - Warrant|G|N|D|100|N|N
FAZE|FaZe Holdings Inc. - Common Stock|S|N|D|100|N|N
FAZEW|FaZe Holdings Inc. - Warrant|S|N|N|100|N|N
FBIO|Fortress Biotech, Inc. - Common Stock|S|N|D|100|N|N
FBIOP|Fortress Biotech, Inc. - 9.375% Series A Cumulative Redeemable Perpetual Preferred Stock|S|N|N|100|N|N
FBIZ|First Business Financial Services, Inc. - Common Stock|Q|N|N|100|N|N
FBL|GraniteShares 1.5x Long Meta Daily ETF|G|N|N|100|Y|N
FBMS|The First Bancshares, Inc. - Common Stock|G|N|N|100|N|N
FBNC|First Bancorp - Common Stock|Q|N|N|100|N|N
FBOT|Fidelity Disruptive Automation ETF|G|N|N|100|Y|N
FBRX|Forte Biosciences, Inc.  - Common Stock|S|N|D|100|N|N
FBYD|Falcon's Beyond Global, Inc. - Class A Common Stock|G|N|N|100|N|N
FBYDP|Falcon's Beyond Global, Inc. - 8% Series A Preferred Stock|G|N|N|100|N|N
FBYDW|Falcon's Beyond Global, Inc. - Warrants|S|N|N|100|N|N
FBZ|First Trust Brazil AlphaDEX Fund|G|N|N|100|Y|N
FCA|First Trust China AlphaDEX Fund|G|N|N|100|Y|N
FCAL|First Trust California Municipal High income ETF|G|N|N|100|Y|N
FCAP|First Capital, Inc. - Common Stock|S|N|N|100|N|N
FCBC|First Community Bankshares, Inc. - Common Stock|Q|N|N|100|N|N
FCCO|First Community Corporation - Common Stock|S|N|N|100|N|N
FCEF|First Trust Income Opportunities ETF|G|N|N|100|Y|N
FCEL|FuelCell Energy, Inc. - Common Stock|G|N|N|100|N|N
FCFS|FirstCash Holdings, Inc. - Common Stock|Q|N|N|100|N|N
FCNCA|First Citizens BancShares, Inc. - Class A Common Stock|Q|N|N|100|N|N
FCNCO|First Citizens BancShares, Inc. - 5.625% Non-Cumulative Perpetual Preferred Stock, Series C|Q|N|N|100|N|N
FCNCP|First Citizens BancShares, Inc. - Depositary Shares Each Representing a 1/40th Interest in a Share of 5.375% Non-Cumulative Perpetual Preferred Stock, Series A|Q|N|N|100|N|N
FCUV|Focus Universal Inc. - Common Stock|G|N|N|100|N|N
FCVT|First Trust SSI Strategic Convertible Securities ETF|G|N|N|100|Y|N
FDBC|Fidelity D & D Bancorp, Inc. - Common Stock|G|N|N|100|N|N
FDCF|Fidelity Disruptive Communications ETF|G|N|N|100|Y|N
FDFF|Fidelity Disruptive Finance ETF|G|N|N|100|Y|N
FDIF|Fidelity Disruptors ETF|G|N|N|100|Y|N
FDIG|Fidelity Crypto Industry and Digital Payments ETF|G|N|N|100|Y|N
FDIV|MarketDesk Focused U.S. Dividend ETF|G|N|N|100|Y|N
FDMT|4D Molecular Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
FDNI|First Trust Dow Jones International Internet ETF|G|N|N|100|Y|N
FDT|First Trust Developed Markets Ex-US AlphaDEX Fund|G|N|N|100|Y|N
FDTS|First Trust Developed Markets ex-US Small Cap AlphaDEX Fund|G|N|N|100|Y|N
FDTX|Fidelity Disruptive Technology ETF|G|N|N|100|Y|N
FDUS|Fidus Investment Corporation - Closed End Fund|Q|N|N|100|N|N
FEAM|5E Advanced Materials, Inc. - Common Stock|Q|N|N|100|N|N
FEIM|Frequency Electronics, Inc. - Common Stock|G|N|N|100|N|N
FELE|Franklin Electric Co., Inc. - Common Stock|Q|N|N|100|N|N
FEM|First Trust Emerging Markets AlphaDEX Fund|G|N|N|100|Y|N
FEMB|First Trust Emerging Markets Local Currency Bond ETF|G|N|N|100|Y|N
FEMS|First Trust Emerging Markets Small Cap AlphaDEX Fund|G|N|N|100|Y|N
FEMY|Femasys Inc. - Common Stock|S|N|N|100|N|N
FENC|Fennec Pharmaceuticals Inc. - Common Stock|S|N|N|100|N|N
FEP|First Trust Europe AlphaDEX Fund|G|N|N|100|Y|N
FEPI|REX FANG & Innovation Equity Premium Income ETF|G|N|N|100|Y|N
FEUZ|First Trust Eurozone AlphaDEX ETF|G|N|N|100|Y|N
FEX|First Trust Large Cap Core AlphaDEX Fund|G|N|N|100|Y|N
FEXD|Fintech Ecosystem Development Corp. - Class A Common Stock|G|N|D|100|N|N
FEXDR|Fintech Ecosystem Development Corp. - Right|G|N|D|100|N|N
FEXDU|Fintech Ecosystem Development Corp. - Units|G|N|D|100|N|N
FEXDW|Fintech Ecosystem Development Corp. - Warrant|G|N|D|100|N|N
FFBC|First Financial Bancorp. - Common Stock|Q|N|N|100|N|N
FFIC|Flushing Financial Corporation - Common Stock|Q|N|N|100|N|N
FFIE|Faraday Future Intelligent Electric Inc. - Common Stock|S|N|N|100|N|N
FFIEW|Faraday Future Intelligent Electric Inc. - Warrant|S|N|N|100|N|N
FFIN|First Financial Bankshares, Inc. - Common Stock|Q|N|N|100|N|N
FFIV|F5, Inc. - Common Stock|Q|N|N|100|N|N
FFNW|First Financial Northwest, Inc. - Common Stock|Q|N|N|100|N|N
FGBI|First Guaranty Bancshares, Inc. - Common Stock|G|N|N|100|N|N
FGBIP|First Guaranty Bancshares, Inc. - 6.75% Series A Fixed-Rate Non-Cumulative Perpetual Preferred Stock|G|N|N|100|N|N
FGEN|FibroGen, Inc - Common Stock|Q|N|N|100|N|N
FGF|FG Financial Group, Inc.  - Common Stock|G|N|N|100|N|N
FGFPP|FG Financial Group, Inc.  - 8.00% Cumulative Series A Preferred Stock|G|N|N|100|N|N
FGI|FGI Industries Ltd. - Ordinary Shares|S|N|N|100|N|N
FGIWW|FGI Industries Ltd. - warrant|S|N|N|100|N|N
FGM|First Trust Germany AlphaDEX Fund|G|N|N|100|Y|N
FHB|First Hawaiian, Inc. - Common Stock|Q|N|N|100|N|N
FHLT|Future Health ESG Corp. - Common stock|S|N|D|100|N|N
FHLTU|Future Health ESG Corp. - Unit|S|N|N|100|N|N
FHLTW|Future Health ESG Corp. - Warrant|S|N|N|100|N|N
FHTX|Foghorn Therapeutics Inc. - Common Stock|G|N|N|100|N|N
FIAC|Focus Impact Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
FIACU|Focus Impact Acquisition Corp. - Unit|G|N|N|100|N|N
FIACW|Focus Impact Acquisition Corp. - Warrant|G|N|N|100|N|N
FIBK|First Interstate BancSystem, Inc. - Common Stock|Q|N|N|100|N|N
FICS|First Trust International Developed Capital Strength ETF|G|N|N|100|Y|N
FICV|Frontier Investment Corp - Class A Ordinary Shares|S|N|N|100|N|N
FICVU|Frontier Investment Corp - Units|S|N|N|100|N|N
FICVW|Frontier Investment Corp - Warrants|S|N|N|100|N|N
FID|First Trust S&P International Dividend Aristocrats ETF|G|N|N|100|Y|N
FINW|FinWise Bancorp - Common Stock|G|N|N|100|N|N
FINX|Global X FinTech ETF|G|N|N|100|Y|N
FIP|FTAI Infrastructure Inc. - Common Stock|Q|N|N|100|N|N
FISI|Financial Institutions, Inc. - Common Stock|Q|N|N|100|N|N
FITB|Fifth Third Bancorp - Common Stock|Q|N|N|100|N|N
FITBI|Fifth Third Bancorp - Depositary Share repstg 1/1000th Ownership Interest Perp Pfd Series I|Q|N|N|100|N|N
FITBO|Fifth Third Bancorp - Depositary Shares each representing a 1/1000th ownership interest in a share of Non-Cumulative Perpetual Preferred Stock, Series K|Q|N|N|100|N|N
FITBP|Fifth Third Bancorp - Depositary Shares each representing 1/40th share of Fifth Third 6.00% Non-Cumulative Perpetual Class B Preferred Stock, Series A|Q|N|N|100|N|N
FIVE|Five Below, Inc. - Common Stock|Q|N|N|100|N|N
FIVN|Five9, Inc. - Common Stock|G|N|N|100|N|N
FIXD|First Trust TCW Opportunistic Fixed Income ETF|G|N|N|100|Y|N
FIXT|Procure Disaster Recovery Strategy ETF|G|N|N|100|Y|N
FIXX|Homology Medicines, Inc. - Common Stock|Q|N|N|100|N|N
FIZZ|National Beverage Corp. - Common Stock|Q|N|N|100|N|N
FJP|First Trust Japan AlphaDEX Fund|G|N|N|100|Y|N
FKU|First Trust United Kingdom AlphaDEX Fund|G|N|N|100|Y|N
FKWL|Franklin Wireless Corp. - common stock|S|N|N|100|N|N
FLEX|Flex Ltd. - Ordinary Shares|Q|N|N|100|N|N
FLFV|Feutune Light Acquisition Corporation - Class A Common Stock|G|N|N|100|N|N
FLFVR|Feutune Light Acquisition Corporation - Right|G|N|N|100|N|N
FLFVU|Feutune Light Acquisition Corporation - Unit|G|N|N|100|N|N
FLFVW|Feutune Light Acquisition Corporation - Warrant|G|N|N|100|N|N
FLGC|Flora Growth Corp. - Common Stock|S|N|N|100|N|N
FLGT|Fulgent Genetics, Inc. - Common Stock|G|N|N|100|N|N
FLIC|The First of Long Island Corporation - Common Stock|S|N|N|100|N|N
FLJ|FLJ Group Limited - American Depositary Shares|G|N|D|100|N|N
FLL|Full House Resorts, Inc. - Common Stock|S|N|N|100|N|N
FLN|First Trust Latin America AlphaDEX Fund|G|N|N|100|Y|N
FLNC|Fluence Energy, Inc. - Class A Common Stock|Q|N|N|100|N|N
FLNT|Fluent, Inc. - Common Stock|G|N|D|100|N|N
FLUX|Flux Power Holdings, Inc. - Common Stock|S|N|N|100|N|N
FLWS|1-800-FLOWERS.COM, Inc. - Class A Common Stock|Q|N|N|100|N|N
FLXS|Flexsteel Industries, Inc. - Common Stock|Q|N|N|100|N|N
FLYW|Flywire Corporation - Voting Common Stock|Q|N|N|100|N|N
FMAO|Farmers & Merchants Bancorp, Inc. - Common Stock|S|N|N|100|N|N
FMB|First Trust Managed Municipal ETF|G|N|N|100|Y|N
FMBH|First Mid Bancshares, Inc. - Common Stock|G|N|N|100|N|N
FMED|Fidelity Disruptive Medicine ETF|G|N|N|100|Y|N
FMET|Fidelity Metaverse ETF|G|N|N|100|Y|N
FMHI|First Trust Municipal High Income ETF|G|N|N|100|Y|N
FMNB|Farmers National Banc Corp. - Common Stock|S|N|N|100|N|N
FMST|Foremost Lithium Resource & Technology Ltd. - Common stock|S|N|N|100|N|N
FMSTW|Foremost Lithium Resource & Technology Ltd. - Warrant|S|N|N|100|N|N
FNCB|FNCB Bancorp Inc. - Common Stock|S|N|N|100|N|N
FNCH|Finch Therapeutics Group, Inc. - Common Stock|Q|N|N|100|N|N
FNGR|FingerMotion, Inc. - common stock|S|N|N|100|N|N
FNK|First Trust Mid Cap Value AlphaDEX Fund|G|N|N|100|Y|N
FNKO|Funko, Inc. - Class A Common Stock|Q|N|N|100|N|N
FNLC|First Bancorp, Inc (ME) - Common Stock|Q|N|N|100|N|N
FNVT|Finnovate Acquisition Corp. - Class A Ordinary Shares|G|N|H|100|N|N
FNVTU|Finnovate Acquisition Corp. - Units|G|N|E|100|N|N
FNVTW|Finnovate Acquisition Corp. - Warrants|G|N|E|100|N|N
FNWB|First Northwest Bancorp - Common Stock|G|N|N|100|N|N
FNWD|Finward Bancorp - common stock|S|N|N|100|N|N
FNX|First Trust Mid Cap Core AlphaDEX Fund|G|N|N|100|Y|N
FNY|First Trust Mid Cap Growth AlphaDEX Fund|G|N|N|100|Y|N
FOLD|Amicus Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
FONR|Fonar Corporation - Common Stock|S|N|N|100|N|N
FORA|Forian Inc. - Common Stock|S|N|N|100|N|N
FORD|Forward Industries, Inc. - Common Stock|S|N|D|100|N|N
FORL|Four Leaf Acquisition Corporation - Class A Common Stock|S|N|N|100|N|N
FORLU|Four Leaf Acquisition Corporation - Unit|S|N|N|100|N|N
FORLW|Four Leaf Acquisition Corporation - Warrants|S|N|N|100|N|N
FORM|FormFactor, Inc. - Common Stock|Q|N|N|100|N|N
FORR|Forrester Research, Inc. - Common Stock|Q|N|N|100|N|N
FORTY|Formula Systems (1985) Ltd. - American Depositary Shares|Q|N|N|100|N|N
FOSL|Fossil Group, Inc. - Common Stock|Q|N|N|100|N|N
FOSLL|Fossil Group, Inc. - 7% Senior Notes due 2026|Q|N|N|100|N|N
FOX|Fox Corporation - Class B Common Stock|Q|N|N|100|N|N
FOXA|Fox Corporation - Class A Common Stock|Q|N|N|100|N|N
FOXF|Fox Factory Holding Corp. - Common Stock|Q|N|N|100|N|N
FPA|First Trust Asia Pacific Ex-Japan AlphaDEX Fund|G|N|N|100|Y|N
FPAY|FlexShopper, Inc. - Common Stock|S|N|N|100|N|N
FPXE|First Trust IPOX Europe Equity Opportunities ETF|G|N|N|100|Y|N
FPXI|First Trust International Equity Opportunities ETF|G|N|N|100|Y|N
FRAF|Franklin Financial Services Corporation - Common Stock|S|N|N|100|N|N
FRBA|First Bank  - Common Stock|G|N|N|100|N|N
FRBN|Forbion European Acquisition Corp. - Class A Ordinary Shares|G|N|N|100|N|N
FRBNU|Forbion European Acquisition Corp. - Units|G|N|N|100|N|N
FRBNW|Forbion European Acquisition Corp. - Warrants|G|N|N|100|N|N
FREE|Whole Earth Brands, Inc. - Class A Common Stock|S|N|N|100|N|N
FREEW|Whole Earth Brands, Inc. - Warrant|S|N|N|100|N|N
FREQ|Frequency Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
FRES|Fresh2 Group Limited - American Depositary Shares|S|N|D|100|N|N
FRGI|Fiesta Restaurant Group, Inc. - Common Stock|Q|N|N|100|N|N
FRGT|Freight Technologies, Inc. - Ordinary Shares|S|N|D|100|N|N
FRHC|Freedom Holding Corp. - Common Stock|S|N|N|100|N|N
FRLA|Fortune Rise Acquisition Corporation - Class A Common Stock|G|N|D|100|N|N
FRLAU|Fortune Rise Acquisition Corporation - Units|G|N|D|100|N|N
FRLAW|Fortune Rise Acquisition Corporation - Warrant|G|N|D|100|N|N
FRLN|Freeline Therapeutics Holdings plc - ADSs|S|N|N|100|N|N
FRME|First Merchants Corporation - Common Stock|Q|N|N|100|N|N
FRMEP|First Merchants Corporation - Depository Shares, each representing a 1/100th interest in a share of 7.50% Non-Cumulative Perpetual Preferred Stock, A|Q|N|N|100|N|N
FROG|JFrog Ltd. - Ordinary shares|Q|N|N|100|N|N
FRPH|FRP Holdings, Inc. - Common Stock|Q|N|N|100|N|N
FRPT|Freshpet, Inc. - Common Stock|G|N|N|100|N|N
FRSH|Freshworks Inc. - Class A Common Stock|Q|N|N|100|N|N
FRST|Primis Financial Corp. - Common Stock|G|N|N|100|N|N
FRSX|Foresight Autonomous Holdings Ltd. - American Depositary Shares|S|N|N|100|N|N
FRTX|Fresh Tracks Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
FRZA|Forza X1, Inc. - Common Stock|S|N|D|100|N|N
FSBC|Five Star Bancorp - Common Stock|Q|N|N|100|N|N
FSBW|FS Bancorp, Inc. - Common Stock|S|N|N|100|N|N
FSEA|First Seacoast Bancorp, Inc. - Common Stock|S|N|N|100|N|N
FSFG|First Savings Financial Group, Inc. - Common Stock|S|N|N|100|N|N
FSLR|First Solar, Inc. - Common Stock|Q|N|N|100|N|N
FSRX|FinServ Acquisition Corp. II - Class A Common Stock|S|N|N|100|N|N
FSRXU|FinServ Acquisition Corp. II - Unit|S|N|N|100|N|N
FSRXW|FinServ Acquisition Corp. II - Warrant|S|N|N|100|N|N
FSTR|L.B. Foster Company - Common Stock|Q|N|N|100|N|N
FSV|FirstService Corporation - Common Shares|Q|N|N|100|N|N
FSZ|First Trust Switzerland AlphaDEX Fund|G|N|N|100|Y|N
FTA|First Trust Large Cap Value AlphaDEX Fund|G|N|N|100|Y|N
FTAG|First Trust Indxx Global Agriculture ETF|G|N|N|100|Y|N
FTAI|FTAI Aviation Ltd. - Common Stock|Q|N|N|100|N|N
FTAIM|FTAI Aviation Ltd. - 9.500% Fixed-Rate Reset Series D Cumulative Perpetual Redeemable Preferred Shares|Q|N|N|100|N|N
FTAIN|FTAI Aviation Ltd. - 8.25% Fixed-Rate Reset Series C Cumulative Perpetual Redeemable Preferred Shares|Q|N|N|100|N|N
FTAIO|FTAI Aviation Ltd. - 8.00% Fixed-to-Floating Rate Series B Cumulative Perpetual Redeemable Preferred Shares|Q|N|N|100|N|N
FTAIP|FTAI Aviation Ltd. - 8.25% Fixed-to-Floating Rate Series A Cumulative Perpetual Redeemable Preferred Shares|Q|N|N|100|N|N
FTC|First Trust Large Cap Growth AlphaDEX Fund|G|N|N|100|Y|N
FTCI|FTC Solar, Inc. - Common Stock|G|N|N|100|N|N
FTCS|First Trust Capital Strength ETF|G|N|N|100|Y|N
FTDR|Frontdoor, Inc. - Common Stock|Q|N|N|100|N|N
FTDS|First Trust Dividend Strength ETF|G|N|N|100|Y|N
FTEK|Fuel Tech, Inc. - Common Stock|S|N|N|100|N|N
FTEL|Fitell Corporation - Ordinary Shares|S|N|N|100|N|N
FTFT|Future FinTech Group Inc. - Common Stock|S|N|N|100|N|N
FTGC|First Trust Global Tactical Commodity Strategy Fund|G|N|N|100|Y|N
FTGS|First Trust Growth Strength ETF|G|N|N|100|Y|N
FTHI|First Trust BuyWrite Income ETF|G|N|N|100|Y|N
FTHM|Fathom Holdings Inc. - Common Stock|S|N|N|100|N|N
FTII|FutureTech II Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
FTIIU|FutureTech II Acquisition Corp. - Unit|G|N|N|100|N|N
FTIIW|FutureTech II Acquisition Corp. - Warrant|G|N|N|100|N|N
FTLF|FitLife Brands, Inc. - Common Stock|S|N|N|100|N|N
FTNT|Fortinet, Inc. - Common Stock|Q|N|N|100|N|N
FTQI|First Trust Nasdaq BuyWrite Income ETF|G|N|N|100|Y|N
FTRE|Fortrea Holdings Inc. - Common Stock|Q|N|N|100|N|N
FTRI|First Trust Indxx Global Natural Resources Income ETF|G|N|N|100|Y|N
FTSL|First Trust Senior Loan Fund|G|N|N|100|Y|N
FTSM|First Trust Enhanced Short Maturity ETF|G|N|N|100|Y|N
FTXG|First Trust Nasdaq Food & Beverage ETF|G|N|N|100|Y|N
FTXH|First Trust Nasdaq Pharmaceuticals ETF|G|N|N|100|Y|N
FTXL|First Trust Nasdaq Semiconductor ETF|G|N|N|100|Y|N
FTXN|First Trust Nasdaq Oil & Gas ETF|G|N|N|100|Y|N
FTXO|First Trust Nasdaq Bank ETF|G|N|N|100|Y|N
FTXR|First Trust Nasdaq Transportation ETF|G|N|N|100|Y|N
FULC|Fulcrum Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
FULT|Fulton Financial Corporation - Common Stock|Q|N|N|100|N|N
FULTP|Fulton Financial Corporation - Depositary Shares Each Representing a 1/40th Interest in a Share of Fixed Rate Non-Cumulative Perpetual Preferred Stock, Series A|Q|N|N|100|N|N
FUNC|First United Corporation - Common Stock|Q|N|N|100|N|N
FUND|Sprott Focus Trust, Inc. - Closed End Fund|Q|N|N|100|N|N
FUSB|First US Bancshares, Inc. - Common Stock|S|N|N|100|N|N
FUSN|Fusion Pharmaceuticals Inc. - Common Shares|Q|N|N|100|N|N
FUTU|Futu Holdings Limited - American Depositary Shares|G|N|N|100|N|N
FUV|Arcimoto, Inc. - Common Stock|G|N|N|100|N|N
FV|First Trust Dorsey Wright Focus 5 ETF|G|N|N|100|Y|N
FVC|First Trust Dorsey Wright Dynamic Focus 5 ETF|G|N|N|100|Y|N
FVCB|FVCBankcorp, Inc. - Common Stock|S|N|N|100|N|N
FWBI|First Wave BioPharma, Inc. - Common Stock|S|N|D|100|N|N
FWONA|Liberty Media Corporation - Series A Liberty Formula One Common Stock|Q|N|N|100|N|N
FWONK|Liberty Media Corporation - Series C Liberty Formula One Common Stock|Q|N|N|100|N|N
FWRD|Forward Air Corporation - Common Stock|Q|N|N|100|N|N
FWRG|First Watch Restaurant Group, Inc. - Common Stock|Q|N|N|100|N|N
FXNC|First National Corporation - Common Stock|S|N|N|100|N|N
FYBR|Frontier Communications Parent, Inc. - Common Stock|Q|N|N|100|N|N
FYC|First Trust Small Cap Growth AlphaDEX Fund|G|N|N|100|Y|N
FYT|First Trust Small Cap Value AlphaDEX Fund|G|N|N|100|Y|N
FYX|First Trust Small Cap Core AlphaDEX Fund|G|N|N|100|Y|N
GABC|German American Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
GAIA|Gaia, Inc. - Class A Common Stock|G|N|N|100|N|N
GAIN|Gladstone Investment Corporation - Business Development Company|Q|N|N|100|N|N
GAINL|Gladstone Investment Corporation - 8.00% Notes due 2028|Q|N|N|100|N|N
GAINN|Gladstone Investment Corporation - 5.00% Notes Due 2026|Q|N|N|100|N|N
GAINZ|Gladstone Investment Corporation - 4.875% Notes due 2028|Q|N|N|100|N|N
GALT|Galectin Therapeutics Inc. - Common Stock|S|N|N|100|N|N
GAMB|Gambling.com Group Limited - Ordinary Shares|G|N|N|100|N|N
GAMC|Golden Arrow Merger Corp. - Class A Common Stock|S|N|N|100|N|N
GAMCU|Golden Arrow Merger Corp. - Unit|S|N|N|100|N|N
GAMCW|Golden Arrow Merger Corp. - Warrant|S|N|N|100|N|N
GAME|GameSquare Holdings, Inc. - Common stock|S|N|N|100|N|N
GAN|GAN Limited - Ordinary Shares|S|N|N|100|N|N
GANX|Gain Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
GASS|StealthGas, Inc. - common stock|Q|N|N|100|N|N
GATE|Marblegate Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
GATEU|Marblegate Acquisition Corp. - Unit|S|N|N|100|N|N
GATEW|Marblegate Acquisition Corp. - Warrant|S|N|N|100|N|N
GBBK|Global Blockchain Acquisition Corp. - Common Stock|G|N|N|100|N|N
GBBKR|Global Blockchain Acquisition Corp. - Right|G|N|N|100|N|N
GBBKW|Global Blockchain Acquisition Corp. - Warrant|G|N|N|100|N|N
GBDC|Golub Capital BDC, Inc. - Closed End Fund|Q|N|N|100|N|N
GBIO|Generation Bio Co. - Common stock|Q|N|N|100|N|N
GBNH|Greenbrook TMS Inc. - Common Shares|S|N|D|100|N|N
GBNY|Generations Bancorp NY, Inc. - Common Stock|S|N|N|100|N|N
GCBC|Greene County Bancorp, Inc. - Common Stock|S|N|N|100|N|N
GCMG|GCM Grosvenor Inc. - Class A Common Stock|G|N|N|100|N|N
GCMGW|GCM Grosvenor Inc. - Warrant|G|N|N|100|N|N
GCT|GigaCloud Technology Inc - Class A Ordinary Shares|G|N|N|100|N|N
GCTK|GlucoTrack, Inc. - Common Stock|S|N|D|100|N|N
GDC|GD Culture Group Limited - Common Stock|S|N|N|100|N|N
GDEN|Golden Entertainment, Inc. - Common Stock|G|N|N|100|N|N
GDEV|GDEV Inc. - Ordinary Shares|G|N|N|100|N|N
GDEVW|GDEV Inc. - Warrant|G|N|N|100|N|N
GDHG|Golden Heaven Group Holdings Ltd.  - Class A Ordinary Shares|S|N|N|100|N|N
GDNR|Gardiner Healthcare Acquisitions Corp. - Common Stock|G|N|H|100|N|N
GDNRU|Gardiner Healthcare Acquisitions Corp. - Unit|G|N|H|100|N|N
GDNRW|Gardiner Healthcare Acquisitions Corp. - Warrant|G|N|H|100|N|N
GDRX|GoodRx Holdings, Inc. - Class A Common Stock|Q|N|N|100|N|N
GDS|GDS Holdings Limited - American Depositary Shares|G|N|N|100|N|N
GDST|Goldenstone Acquisition Limited - Common Stock|S|N|N|100|N|N
GDSTR|Goldenstone Acquisition Limited - Rights|S|N|N|100|N|N
GDSTU|Goldenstone Acquisition Limited - Units|S|N|N|100|N|N
GDSTW|Goldenstone Acquisition Limited - Warrants|S|N|N|100|N|N
GDTC|CytoMed Therapeutics Limited - Ordinary Shares|S|N|N|100|N|N
GDYN|Grid Dynamics Holdings, Inc. - Class A Common Stock|S|N|N|100|N|N
GECC|Great Elm Capital Corp. - Closed End Fund|G|N|N|100|N|N
GECCM|Great Elm Capital Corp. - 6.75% Notes Due 2025|G|N|N|100|N|N
GECCO|Great Elm Capital Corp. - 5.875% Notes due 2026|G|N|N|100|N|N
GECCZ|Great Elm Capital Corp. - 8.75% Notes due 2028|G|N|N|100|N|N
GEG|Great Elm Group, Inc.  - Common Stock|Q|N|N|100|N|N
GEGGL|Great Elm Group, Inc.  - 7.25% Notes due 2027|G|N|N|100|N|N
GEHC|GE HealthCare Technologies Inc. - Common Stock|Q|N|N|100|N|N
GEN|Gen Digital Inc. - Common Stock|Q|N|N|100|N|N
GENE|Genetic Technologies Ltd - American Depositary Shares|S|N|D|100|N|N
GENK|GEN Restaurant Group, Inc. - Class A Common Stock|G|N|N|100|N|N
GEOS|Geospace Technologies Corporation - Common Stock|Q|N|N|100|N|N
GERN|Geron Corporation - Common Stock|Q|N|N|100|N|N
GEVO|Gevo, Inc. - Common Stock|S|N|N|100|N|N
GFAI|Guardforce AI Co., Limited - Ordinary Shares|S|N|N|100|N|N
GFAIW|Guardforce AI Co., Limited - Warrant|S|N|N|100|N|N
GFGF|Guru Favorite Stocks ETF|G|N|N|100|Y|N
GFS|GlobalFoundries Inc. - Ordinary Share|Q|N|N|100|N|N
GGAL|Grupo Financiero Galicia S.A. - American Depositary Shares, Class B Shares underlying|S|N|N|100|N|N
GGE|Green Giant Inc. - Common Stock|S|N|D|100|N|N
GGLL|Direxion Daily GOOGL Bull 1.5X Shares|G|N|N|100|Y|N
GGLS|Direxion Daily GOOGL Bear 1X Shares|G|N|N|100|Y|N
GGR|Gogoro Inc. - Ordinary Shares|Q|N|N|100|N|N
GGROW|Gogoro Inc. - Warrant|Q|N|N|100|N|N
GH|Guardant Health, Inc. - Common Stock|Q|N|N|100|N|N
GHIX|Gores Holdings IX, Inc. - Class A Common Stock|G|N|N|100|N|N
GHIXU|Gores Holdings IX, Inc. - Unit|G|N|N|100|N|N
GHIXW|Gores Holdings IX, Inc. - Warrant|G|N|N|100|N|N
GHRS|GH Research PLC - Ordinary Shares|G|N|N|100|N|N
GHSI|Guardion Health Sciences, Inc. - Common Stock|S|N|N|100|N|N
GIA|GigCapital 5, Inc. - Common Stock|G|N|N|100|N|N
GIFI|Gulf Island Fabrication, Inc. - Common Stock|Q|N|N|100|N|N
GIGM|GigaMedia Limited - Ordinary Shares|S|N|N|100|N|N
GIII|G-III Apparel Group, LTD. - Common Stock|Q|N|N|100|N|N
GILD|Gilead Sciences, Inc. - Common Stock|Q|N|N|100|N|N
GILT|Gilat Satellite Networks Ltd. - Ordinary Shares|Q|N|N|100|N|N
GIPR|Generation Income Properties Inc. - Common stock|S|N|N|100|N|N
GIPRW|Generation Income Properties Inc. - Warrant|S|N|N|100|N|N
GLAD|Gladstone Capital Corporation - Closed End Fund|Q|N|N|100|N|N
GLADZ|Gladstone Capital Corporation - 7.75% Notes due 2028|Q|N|N|100|N|N
GLBE|Global-E Online Ltd. - ordinary shares|Q|N|N|100|N|N
GLBS|Globus Maritime Limited - Common Stock|S|N|N|100|N|N
GLBZ|Glen Burnie Bancorp - Common Stock|S|N|N|100|N|N
GLDD|Great Lakes Dredge & Dock Corporation - Common Stock|Q|N|N|100|N|N
GLDI|Credit Suisse X-Links Gold Shares Covered Call ETNs due February 2, 2033|G|N|N|100|N|N
GLG|TD Holdings, Inc. - Common Stock|S|N|D|100|N|N
GLLI|Globalink Investment Inc. - Common Stock|G|N|N|100|N|N
GLLIR|Globalink Investment Inc. - Rights|G|N|N|100|N|N
GLLIU|Globalink Investment Inc. - Units|G|N|N|100|N|N
GLLIW|Globalink Investment Inc. - Warrants|G|N|N|100|N|N
GLMD|Galmed Pharmaceuticals Ltd. - Ordinary Shares|S|N|D|100|N|N
GLNG|Golar LNG Limited - Common Shares|Q|N|N|100|N|N
GLPG|Galapagos NV - American Depositary Shares|Q|N|N|100|N|N
GLPI|Gaming and Leisure Properties, Inc. - Common Stock|Q|N|N|100|N|N
GLRE|Greenlight Reinsurance, Ltd. - Class A Ordinary Shares|Q|N|N|100|N|N
GLSI|Greenwich LifeSciences, Inc. - Common stock|S|N|N|100|N|N
GLST|Global Star Acquisition, Inc. - Class A Common Stock|G|N|N|100|N|N
GLSTR|Global Star Acquisition, Inc. - Right|G|N|N|100|N|N
GLSTU|Global Star Acquisition, Inc. - Unit|G|N|N|100|N|N
GLSTW|Global Star Acquisition, Inc. - Warrants|G|N|N|100|N|N
GLTO|Galecto, Inc. - Common Stock|Q|N|D|100|N|N
GLUE|Monte Rosa Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
GLYC|GlycoMimetics, Inc. - Common Stock|G|N|N|100|N|N
GMAB|Genmab A/S - American Depositary Shares|Q|N|N|100|N|N
GMBL|Esports Entertainment Group Inc. - Common Stock|S|N|D|100|N|N
GMBLP|Esports Entertainment Group Inc. - 10.0% Series A Cumulative Redeemable Convertible Preferred Stock|S|N|N|100|N|N
GMBLW|Esports Entertainment Group Inc. - Warrant|S|N|N|100|N|N
GMBLZ|Esports Entertainment Group Inc. - Warrant|S|N|N|100|N|N
GMDA|Gamida Cell Ltd. - Ordinary Shares|G|N|N|100|N|N
GMFI|Aetherium Acquisition Corp. - Class A Common Stock|G|N|H|100|N|N
GMFIU|Aetherium Acquisition Corp. - Unit|G|N|H|100|N|N
GMFIW|Aetherium Acquisition Corp. - Warrant|G|N|H|100|N|N
GMGI|Golden Matrix Group, Inc. - Common Stock|S|N|N|100|N|N
GMM|Global Mofy Metaverse Limited - Ordinary Shares|S|N|N|100|N|N
GNFT|GENFIT S.A. - American Depositary Shares|Q|N|N|100|N|N
GNLN|Greenlane Holdings, Inc. - Class A Common Stock|G|N|D|100|N|N
GNLX|Genelux Corporation - Common Stock|S|N|N|100|N|N
GNMA|iShares GNMA Bond ETF|G|N|N|100|Y|N
GNOM|Global X Genomics & Biotechnology ETF|G|N|N|100|Y|N
GNPX|Genprex, Inc. - Common Stock|S|N|D|100|N|N
GNSS|Genasys Inc. - Common Stock|S|N|N|100|N|N
GNTA|Genenta Science S.p.A. - American Depositary Shares|S|N|N|100|N|N
GNTX|Gentex Corporation - Common Stock|Q|N|N|100|N|N
GO|Grocery Outlet Holding Corp. - Common Stock|Q|N|N|100|N|N
GOCO|GoHealth, Inc. - Class A Common Stock|S|N|N|100|N|N
GODN|Golden Star Acquisition Corporation - Ordinary Shares|G|N|N|100|N|N
GODNR|Golden Star Acquisition Corporation - Rights|G|N|N|100|N|N
GODNU|Golden Star Acquisition Corporation - Unit|G|N|N|100|N|N
GOEV|Canoo Inc.  - Class A Common Stock|S|N|D|100|N|N
GOEVW|Canoo Inc.  - Warrant|S|N|N|100|N|N
GOGL|Golden Ocean Group Limited - Common Stock|Q|N|N|100|N|N
GOGO|Gogo Inc. - Common Stock|Q|N|N|100|N|N
GOOD|Gladstone Commercial Corporation - Real Estate Investment Trust|Q|N|N|100|N|N
GOODN|Gladstone Commercial Corporation - 6.625% Series E Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
GOODO|Gladstone Commercial Corporation - 6.00% Series G Cumulative Redeemable Preferred Stock, par value $0.001 per share|Q|N|N|100|N|N
GOOG|Alphabet Inc. - Class C Capital Stock|Q|N|N|100|N|N
GOOGL|Alphabet Inc. - Class A Common Stock|Q|N|N|100|N|N
GOSS|Gossamer Bio, Inc. - Common Stock|Q|N|N|100|N|N
GOVI|Invesco Equal Weight 0-30 Year Treasury ETF|G|N|N|100|Y|N
GOVX|GeoVax Labs, Inc. - Common Stock|S|N|D|100|N|N
GOVXW|GeoVax Labs, Inc. - Warrants|S|N|N|100|N|N
GP|GreenPower Motor Company Inc. - Common Shares|S|N|N|100|N|N
GPAC|Global Partner Acquisition Corp II - Class A Ordinary Share|S|N|N|100|N|N
GPACU|Global Partner Acquisition Corp II - Unit|S|N|N|100|N|N
GPACW|Global Partner Acquisition Corp II - Warrant|S|N|N|100|N|N
GPAK|Gamer Pakistan Inc. - Common Stock|S|N|N|100|N|N
GPCR|Structure Therapeutics Inc. - American Depositary Shares|G|N|N|100|N|N
GPP|Green Plains Partners LP - Common Units|G|N|N|100|N|N
GPRE|Green Plains, Inc. - Common Stock|Q|N|N|100|N|N
GPRO|GoPro, Inc. - Class A Common Stock|Q|N|N|100|N|N
GRAB|Grab Holdings Limited - Class A Ordinary Shares|Q|N|N|100|N|N
GRABW|Grab Holdings Limited - Warrant|Q|N|N|100|N|N
GRCL|Gracell Biotechnologies Inc. - American Depositary Shares|Q|N|N|100|N|N
GREE|Greenidge Generation Holdings Inc. - Class A Common Stock|Q|N|N|100|N|N
GREEL|Greenidge Generation Holdings Inc. - 8.50% Senior Notes due 2026|Q|N|N|100|N|N
GRFS|Grifols, S.A. - American Depositary Shares|Q|N|N|100|N|N
GRI|GRI Bio, Inc. - Common Stock|S|N|N|100|N|N
GRID|First Trust NASDAQ Clean Edge Smart Grid Infrastructure Index Fund|G|N|N|100|Y|N
GRIN|Grindrod Shipping Holdings Ltd. - Ordinary Shares|Q|N|N|100|N|N
GRNQ|Greenpro Capital Corp. - Common Stock|S|N|N|100|N|N
GRNR|Global X Green Building ETF|G|N|N|100|Y|N
GROM|Grom Social Enterprises Inc. - Common Stock|S|N|N|100|N|N
GROMW|Grom Social Enterprises Inc. - Warrants|S|N|N|100|N|N
GROW|U.S. Global Investors, Inc. - Class A Common Stock|S|N|N|100|N|N
GRPH|Graphite Bio, Inc. - Common Stock|G|N|N|100|N|N
GRPN|Groupon, Inc. - Common Stock|Q|N|N|100|N|N
GRRR|Gorilla Technology Group Inc. - Ordinary shares|S|N|N|100|N|N
GRRRW|Gorilla Technology Group Inc. - Warrant|S|N|N|100|N|N
GRTS|Gritstone bio, Inc. - Common Stock|Q|N|N|100|N|N
GRTX|Galera Therapeutics, Inc. - Common Stock|G|N|D|100|N|N
GRVY|GRAVITY Co., Ltd. - American depositary shares, each representing one common share.|G|N|N|100|N|N
GRWG|GrowGeneration Corp. - Common Stock|S|N|N|100|N|N
GSBC|Great Southern Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
GSD|Global Systems Dynamics Inc. - Common Stock|S|N|H|100|N|N
GSDWU|Global Systems Dynamics Inc. - Unit|S|N|H|100|N|N
GSDWW|Global Systems Dynamics Inc. - Warrant|S|N|H|100|N|N
GSHD|Goosehead Insurance, Inc. - Class A Common Stock|Q|N|N|100|N|N
GSIT|GSI Technology, Inc. - Common Stock|Q|N|N|100|N|N
GSM|Ferroglobe PLC - Ordinary Shares|S|N|N|100|N|N
GSMG|Glory Star New Media Group Holdings Limited - Ordinary Share|S|N|D|100|N|N
GSMGW|Glory Star New Media Group Holdings Limited - Warrant|S|N|N|100|N|N
GSUN|Golden Sun Education Group Limited - Class A Ordinary Shares|S|N|D|100|N|N
GT|The Goodyear Tire & Rubber Company - Common Stock|Q|N|N|100|N|N
GTAC|Global Technology Acquisition Corp. I - Class A Ordinary Shares|G|N|D|100|N|N
GTACU|Global Technology Acquisition Corp. I - Unit|G|N|D|100|N|N
GTACW|Global Technology Acquisition Corp. I - Warrant|G|N|D|100|N|N
GTBP|GT Biopharma, Inc. - Common Stock|S|N|D|100|N|N
GTEC|Greenland Technologies Holding Corporation - Ordinary Shares|S|N|N|100|N|N
GTH|Genetron Holdings Limited - American Depositary Shares|G|N|D|100|N|N
GTHX|G1 Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
GTIM|Good Times Restaurants Inc. - Common Stock|S|N|N|100|N|N
GTLB|GitLab Inc. - Class A Common Stock|Q|N|N|100|N|N
GTR|WisdomTree Target Range Fund|G|N|N|100|Y|N
GTX|Garrett Motion Inc. - Common Stock|Q|N|N|100|N|N
GURE|Gulf Resources, Inc. - Common Stock|Q|N|N|100|N|N
GV|Visionary Education Technology Holdings Group Inc. - Common Shares|S|N|D|100|N|N
GVP|GSE Systems, Inc. - Common Stock|S|N|D|100|N|N
GWAV|Greenwave Technology Solutions, Inc. - Common Stock|S|N|D|100|N|N
GWRS|Global Water Resources, Inc. - common stock|G|N|N|100|N|N
GXTG|Global X Thematic Growth ETF|G|N|N|100|Y|N
GYRO|Gyrodyne , LLC - Common Stock|S|N|N|100|N|N
HA|Hawaiian Holdings, Inc. - Common Stock|Q|N|N|100|N|N
HAFC|Hanmi Financial Corporation - Common Stock|Q|N|N|100|N|N
HAIA|Healthcare AI Acquisition Corp. - Class A Ordinary Shares|S|N|N|100|N|N
HAIAU|Healthcare AI Acquisition Corp. - Units|S|N|N|100|N|N
HAIAW|Healthcare AI Acquisition Corp. - Warrants|S|N|N|100|N|N
HAIN|The Hain Celestial Group, Inc. - Common Stock|Q|N|N|100|N|N
HALL|Hallmark Financial Services, Inc. - Common Stock|G|N|D|100|N|N
HALO|Halozyme Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
HARP|Harpoon Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
HAS|Hasbro, Inc. - Common Stock|Q|N|N|100|N|N
HAYN|Haynes International, Inc. - Common Stock|Q|N|N|100|N|N
HBAN|Huntington Bancshares Incorporated - Common Stock|Q|N|N|100|N|N
HBANL|Huntington Bancshares Incorporated - Depositary Shares, Each Representing a 1/40th Interest in a Share of 6.875% Series J Non-Cumulative Perpetual Preferred Stock|Q|N|N|100|N|N
HBANM|Huntington Bancshares Incorporated - Depositary Shares each representing a 1/1000th interest in a share of Huntington Series I Preferred Stock|Q|N|N|100|N|N
HBANP|Huntington Bancshares Incorporated - Depositary Shares 4.500% Series H Non-Cumulative Perpetual Preferred Stock|Q|N|N|100|N|N
HBCP|Home Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
HBIO|Harvard Bioscience, Inc. - Common Stock|G|N|N|100|N|N
HBNC|Horizon Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
HBT|HBT Financial, Inc. - Common Stock|Q|N|N|100|N|N
HCAT|Health Catalyst, Inc - Common stock|Q|N|N|100|N|N
HCCI|Heritage-Crystal Clean, Inc. - Common Stock|Q|N|N|100|N|N
HCDI|Harbor Custom Development, Inc. - Common Stock|S|N|D|100|N|N
HCDIP|Harbor Custom Development, Inc. - 8.0% Series A Cumulative Convertible Preferred Stock, no par value|S|N|D|100|N|N
HCDIW|Harbor Custom Development, Inc. - Warrant|S|N|D|100|N|N
HCDIZ|Harbor Custom Development, Inc. - Warrant|S|N|D|100|N|N
HCKT|The Hackett Group, Inc. - Common Stock|Q|N|N|100|N|N
HCM|HUTCHMED (China) Limited - American Depositary Shares|Q|N|N|100|N|N
HCMA|HCM Acquisition Corp - Class A Ordinary Shares|G|N|D|100|N|N
HCMAU|HCM Acquisition Corp - Unit|G|N|N|100|N|N
HCMAW|HCM Acquisition Corp - Warrant|G|N|N|100|N|N
HCOW|Amplify Cash Flow High Income ETF|G|N|N|100|Y|N
HCP|HashiCorp, Inc. - Class A Common Stock|Q|N|N|100|N|N
HCSG|Healthcare Services Group, Inc. - Common Stock|Q|N|N|100|N|N
HCTI|Healthcare Triangle, Inc. - Common Stock|S|N|N|100|N|N
HCVI|Hennessy Capital Investment Corp. VI - Class A Common Stock|G|N|N|100|N|N
HCVIU|Hennessy Capital Investment Corp. VI - Unit|G|N|N|100|N|N
HCVIW|Hennessy Capital Investment Corp. VI - Warrant|G|N|N|100|N|N
HCWB|HCW Biologics Inc. - Common Stock|G|N|N|100|N|N
HDSN|Hudson Technologies, Inc. - Common Stock|S|N|N|100|N|N
HEAR|Turtle Beach Corporation - Common Stock|G|N|N|100|N|N
HEES|H&E Equipment Services, Inc. - Common Stock|Q|N|N|100|N|N
HELE|Helen of Troy Limited - Common Stock|Q|N|N|100|N|N
HEPA|Hepion Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
HEPS|D-Market Electronic Services & Trading - American Depositary Shares|Q|N|N|100|N|N
HERD|Pacer Cash Cows Fund of Funds ETF|G|N|N|100|Y|N
HERO|Global X Video Games & Esports ETF|G|N|N|100|Y|N
HEWG|iShares Currency Hedged MSCI Germany ETF|G|N|N|100|Y|N
HFBL|Home Federal Bancorp, Inc. of Louisiana - Common Stock|S|N|N|100|N|N
HFFG|HF Foods Group Inc. - Common Stock|S|N|N|100|N|N
HFWA|Heritage Financial Corporation - Common Stock|Q|N|N|100|N|N
HGBL|Heritage Global Inc. - Common Stock|S|N|N|100|N|N
HHGC|HHG Capital Corporation - Ordinary Shares|S|N|N|100|N|N
HHGCR|HHG Capital Corporation - Rights|S|N|N|100|N|N
HHGCU|HHG Capital Corporation - Units|S|N|N|100|N|N
HHGCW|HHG Capital Corporation - Warrant|S|N|N|100|N|N
HHRS|Hammerhead Energy Inc. - Class A Common Stock|S|N|N|100|N|N
HHS|Harte-Hanks, Inc. - Common Stock|G|N|N|100|N|N
HIBB|Hibbett, Inc. - Common Stock|Q|N|N|100|N|N
HIFS|Hingham Institution for Savings - Common Stock|G|N|N|100|N|N
HIHO|Highway Holdings Limited - Common Stock|S|N|N|100|N|N
HIMX|Himax Technologies, Inc. - American depositary shares, each of which represents two ordinary shares.|Q|N|N|100|N|N
HISF|First Trust High Income Strategic Focus ETF|G|N|N|100|Y|N
HITI|High Tide Inc. - Common Shares|S|N|N|100|N|N
HIVE|HIVE Digital Technologies Ltd - Common Shares|S|N|N|100|N|N
HKIT|Hitek Global Inc. - Ordinary Share|S|N|N|100|N|N
HLAL|Wahed FTSE USA Shariah ETF|G|N|N|100|Y|N
HLIT|Harmonic Inc. - Common Stock|Q|N|N|100|N|N
HLMN|Hillman Solutions Corp. - Common Stock|G|N|N|100|N|N
HLNE|Hamilton Lane Incorporated - Class A Common Stock|Q|N|N|100|N|N
HLP|Hongli Group Inc. - Ordinary Shares|S|N|N|100|N|N
HLTH|Cue Health Inc. - Common Stock|Q|N|D|100|N|N
HLVX|HilleVax, Inc. - Common Stock|Q|N|N|100|N|N
HMNF|HMN Financial, Inc. - Common Stock|G|N|N|100|N|N
HMST|HomeStreet, Inc. - Common Stock|Q|N|N|100|N|N
HNDL|Strategy Shares Nasdaq 7HANDL Index ETF|G|N|N|100|Y|N
HNNA|Hennessy Advisors, Inc. - Common Stock|G|N|N|100|N|N
HNNAZ|Hennessy Advisors, Inc. - 4.875% Notes due 2026|G|N|N|100|N|N
HNRG|Hallador Energy Company - Common Stock|S|N|N|100|N|N
HNST|The Honest Company, Inc. - Common Stock|Q|N|N|100|N|N
HNVR|Hanover Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
HOFT|Hooker Furnishings Corporation - Common Stock|Q|N|N|100|N|N
HOFV|Hall of Fame Resort & Entertainment Company - Common Stock|S|N|N|100|N|N
HOFVW|Hall of Fame Resort & Entertainment Company - Warrant|S|N|N|100|N|N
HOLI|Hollysys Automation Technologies, Ltd. - Common Stock|Q|N|N|100|N|N
HOLO|MicroCloud Hologram Inc. - Ordinary Shares|S|N|N|100|N|N
HOLOW|MicroCloud Hologram Inc. - Warrant|S|N|N|100|N|N
HOLX|Hologic, Inc. - Common Stock|Q|N|N|100|N|N
HON|Honeywell International Inc. - Common Stock|Q|N|N|100|N|N
HONE|HarborOne Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
HOOD|Robinhood Markets, Inc. - Class A Common Stock|Q|N|N|100|N|N
HOOK|HOOKIPA Pharma Inc. - Common Stock|Q|N|D|100|N|N
HOPE|Hope Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
HOTH|Hoth Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
HOUR|Hour Loop, Inc. - common stock|S|N|N|100|N|N
HOVNP|Hovnanian Enterprises Inc - Depositary Share representing 1/1000th of 7.625% Series A Preferred Stock|G|N|N|100|N|N
HOWL|Werewolf Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
HPCO|Hempacco Co., Inc. - Common Stock|S|N|D|100|N|N
HPK|HighPeak Energy, Inc. - Common Stock|G|N|N|100|N|N
HPKEW|HighPeak Energy, Inc. - Warrant|G|N|N|100|N|N
HPLT|Home Plate Acquisition Corporation - Class A Common Stock|S|N|D|100|N|N
HPLTU|Home Plate Acquisition Corporation - Unit|S|N|N|100|N|N
HPLTW|Home Plate Acquisition Corporation - Warrant|S|N|N|100|N|N
HQI|HireQuest, Inc. - Common Stock|S|N|N|100|N|N
HQY|HealthEquity, Inc. - Common Stock|Q|N|N|100|N|N
HRMY|Harmony Biosciences Holdings, Inc. - Common Stock|G|N|N|100|N|N
HROW|Harrow, Inc. - Common Stock|G|N|N|100|N|N
HROWL|Harrow, Inc. - 8.625% senior notes due 2026|G|N|N|100|N|N
HROWM|Harrow, Inc. - 11.875% Senior Notes due 2027|G|N|N|100|N|N
HRTX|Heron Therapeutics, Inc.   - Common Stock|S|N|N|100|N|N
HRYU|Hanryu Holdings, Inc. - Common Stock|S|N|N|100|N|N
HRZN|Horizon Technology Finance Corporation - Common Stock|Q|N|N|100|N|N
HSAI|Hesai Group - American Depositary Share, each ADS represents one Class B ordinary share|Q|N|N|100|N|N
HSCS|Heart Test Laboratories, Inc. - Common Stock|S|N|D|100|N|N
HSCSW|Heart Test Laboratories, Inc. - Warrant|S|N|D|100|N|N
HSDT|Helius Medical Technologies, Inc. - Class A Common Stock|S|N|N|100|N|N
HSIC|Henry Schein, Inc. - Common Stock|Q|N|N|100|N|N
HSII|Heidrick & Struggles International, Inc. - Common Stock|Q|N|N|100|N|N
HSON|Hudson Global, Inc. - Common Stock|Q|N|N|100|N|N
HSPO|Horizon Space Acquisition I Corp. - Ordinary Shares|G|N|N|100|N|N
HSPOR|Horizon Space Acquisition I Corp. - Right|G|N|N|100|N|N
HSPOU|Horizon Space Acquisition I Corp. - Unit|G|N|N|100|N|N
HSPOW|Horizon Space Acquisition I Corp. - Warrant|G|N|N|100|N|N
HST|Host Hotels & Resorts, Inc. - Common Stock|Q|N|N|100|N|N
HSTM|HealthStream, Inc. - Common Stock|Q|N|N|100|N|N
HTBI|HomeTrust Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
HTBK|Heritage Commerce Corp - Common Stock|Q|N|N|100|N|N
HTCR|Heartcore Enterprises, Inc. - Common Stock|S|N|N|100|N|N
HTHT|H World Group Limited - American Depositary Shares|Q|N|N|100|N|N
HTIA|Healthcare Trust, Inc. - 7.375% Series A Cumulative Redeemable Perpetual Preferred Stock|G|N|N|100|N|N
HTIBP|Healthcare Trust, Inc. - 7.125% Series B Cumulative Redeemable Perpetual Preferred Stock|G|N|N|100|N|N
HTLD|Heartland Express, Inc. - Common Stock|Q|N|N|100|N|N
HTLF|Heartland Financial USA, Inc. - Common Stock|Q|N|N|100|N|N
HTLFP|Heartland Financial USA, Inc. - Depositary Shares, each representing a 1/400th ownership interest in a share of 7.00% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock, Series E|Q|N|N|100|N|N
HTOO|Fusion Fuel Green PLC - Ordinary Shares|G|N|N|100|N|N
HTOOW|Fusion Fuel Green PLC - Warrant|G|N|N|100|N|N
HTZ|Hertz Global Holdings, Inc - Common Stock|Q|N|N|100|N|N
HTZWW|Hertz Global Holdings, Inc - Warrant|Q|N|N|100|N|N
HUBC|Hub Cyber Security Ltd. - Ordinary Shares|G|N|D|100|N|N
HUBCW|Hub Cyber Security Ltd. - Warrant expiring 2/27/28|S|N|N|100|N|N
HUBCZ|Hub Cyber Security Ltd. - Warrant|G|N|N|100|N|N
HUBG|Hub Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
HUDA|Hudson Acquisition I Corp. - Common Stock|G|N|E|100|N|N
HUDAR|Hudson Acquisition I Corp. - Right|G|N|E|100|N|N
HUDAU|Hudson Acquisition I Corp. - Unit|G|N|E|100|N|N
HUDI|Huadi International Group Co., Ltd. - Ordinary Shares|S|N|N|100|N|N
HUGE|FSD Pharma Inc. - Class B Subordinate Voting Shares|S|N|N|100|N|N
HUIZ|Huize Holding Limited - American Depositary Shares|G|N|N|100|N|N
HUMA|Humacyte, Inc. - Common Stock|Q|N|N|100|N|N
HUMAW|Humacyte, Inc. - Warrant|Q|N|N|100|N|N
HURC|Hurco Companies, Inc. - Common Stock|Q|N|N|100|N|N
HURN|Huron Consulting Group Inc. - Common Stock|Q|N|N|100|N|N
HUT|Hut 8 Mining Corp. - Common Shares|Q|N|N|100|N|N
HWBK|Hawthorn Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
HWC|Hancock Whitney Corporation - Common Stock|Q|N|N|100|N|N
HWCPZ|Hancock Whitney Corporation - 6.25% Subordinated Notes due 2060|Q|N|N|100|N|N
HWEL|Healthwell Acquisition Corp. I - Class A Common Stock|S|N|N|100|N|N
HWELU|Healthwell Acquisition Corp. I - Unit|S|N|N|100|N|N
HWELW|Healthwell Acquisition Corp. I - Warrant|S|N|N|100|N|N
HWKN|Hawkins, Inc. - Common Stock|Q|N|N|100|N|N
HYDR|Global X Hydrogen ETF|G|N|N|100|Y|N
HYFM|Hydrofarm Holdings Group, Inc. - Common Stock|Q|N|N|100|N|N
HYLS|First Trust Tactical High Yield ETF|G|N|N|100|Y|N
HYMC|Hycroft Mining Holding Corporation - Class A Common Stock|S|N|D|100|N|N
HYMCL|Hycroft Mining Holding Corporation - Warrants|S|N|N|100|N|N
HYMCW|Hycroft Mining Holding Corporation - Warrant|S|N|N|100|N|N
HYPR|Hyperfine, Inc.  - Class A Common Stock|G|N|N|100|N|N
HYW|Hywin Holdings Ltd. - American Depositary Shares|G|N|N|100|N|N
HYXF|iShares ESG Advanced High Yield Corporate Bond ETF|G|N|N|100|Y|N
HYZD|WisdomTree Interest Rate Hedged High Yield Bond Fund|G|N|N|100|Y|N
HYZN|Hyzon Motors Inc. - Class A Common Stock|Q|N|N|100|N|N
HYZNW|Hyzon Motors Inc. - Warrant|Q|N|N|100|N|N
IAC|IAC Inc. - Common Stock|Q|N|N|100|N|N
IART|Integra LifeSciences Holdings Corporation - Common Stock|Q|N|N|100|N|N
IAS|Integral Ad Science Holding Corp. - Common Stock|Q|N|N|100|N|N
IBB|iShares Biotechnology ETF|G|N|N|100|Y|N
IBBQ|Invesco Nasdaq Biotechnology ETF|G|N|N|100|Y|N
IBCP|Independent Bank Corporation - Common Stock|Q|N|N|100|N|N
IBEX|IBEX Limited - Common Share|G|N|N|100|N|N
IBKR|Interactive Brokers Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
IBOC|International Bancshares Corporation - Common Stock|Q|N|N|100|N|N
IBOT|VanEck Robotics ETF|G|N|N|100|Y|N
IBRX|ImmunityBio, Inc. - Common Stock|Q|N|N|100|N|N
IBTD|iShares iBonds Dec 2023 Term Treasury ETF|G|N|N|100|Y|N
IBTE|iShares iBonds Dec 2024 Term Treasury ETF|G|N|N|100|Y|N
IBTF|iShares iBonds Dec 2025 Term Treasury ETF|G|N|N|100|Y|N
IBTG|iShares iBonds Dec 2026 Term Treasury ETF|G|N|N|100|Y|N
IBTH|iShares iBonds Dec 2027 Term Treasury ETF|G|N|N|100|Y|N
IBTI|iShares iBonds Dec 2028 Term Treasury ETF|G|N|N|100|Y|N
IBTJ|iShares iBonds Dec 2029 Term Treasury ETF|G|N|N|100|Y|N
IBTK|iShares iBonds Dec 2030 Term Treasury ETF|G|N|N|100|Y|N
IBTL|iShares iBonds Dec 2031 Term Treasury ETF|G|N|N|100|Y|N
IBTM|iShares iBonds Dec 2032 Term Treasury ETF|G|N|N|100|Y|N
IBTO|iShares iBonds Dec 2033 Term Treasury ETF|G|N|N|100|Y|N
IBTX|Independent Bank Group, Inc - Common Stock|Q|N|N|100|N|N
ICAD|icad inc. - Common Stock|S|N|N|100|N|N
ICCC|ImmuCell Corporation - Common Stock|S|N|N|100|N|N
ICCH|ICC Holdings, Inc. - Common Stock|S|N|N|100|N|N
ICCM|IceCure Medical Ltd. - Ordinary Shares|S|N|N|100|N|N
ICCT|iCoreConnect Inc. - Common stock|S|N|N|100|N|N
ICFI|ICF International, Inc. - Common Stock|Q|N|N|100|N|N
ICG|Intchains Group Limited - American Depositary Shares|S|N|N|100|N|N
ICHR|Ichor Holdings - Ordinary Shares|Q|N|N|100|N|N
ICLK|iClick Interactive Asia Group Limited - American Depositary Shares|G|N|N|100|N|N
ICLN|iShares Global Clean Energy ETF|G|N|N|100|Y|N
ICLR|ICON plc - Ordinary Shares|Q|N|N|100|N|N
ICMB|Investcorp Credit Management BDC, Inc. - Common Stock|Q|N|N|100|N|N
ICOP|iShares Copper and Metals Mining ETF|G|N|N|100|Y|N
ICPT|Intercept Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
ICU|SeaStar Medical Holding Corporation - Common Stock|S|N|D|100|N|N
ICUCW|SeaStar Medical Holding Corporation - Warrant|S|N|D|100|N|N
ICUI|ICU Medical, Inc. - Common Stock|Q|N|N|100|N|N
ICVX|Icosavax, Inc. - Common Stock|Q|N|N|100|N|N
IDAI|T Stamp Inc. - Class A Common Stock|S|N|N|100|N|N
IDCC|InterDigital, Inc. - Common Stock|Q|N|N|100|N|N
IDEX|Ideanomics, Inc. - Common Stock|S|N|N|100|N|N
IDN|Intellicheck, Inc. - Common Stock|G|N|N|100|N|N
IDXX|IDEXX Laboratories, Inc. - Common Stock|Q|N|N|100|N|N
IDYA|IDEAYA Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
IEF|iShares 7-10 Year Treasury Bond ETF|G|N|N|100|Y|N
IEI|iShares 3-7 Year Treasury Bond ETF|G|N|N|100|Y|N
IEP|Icahn Enterprises L.P. - Depositary Units representing Limited Partner Interests|Q|N|N|100|N|N
IESC|IES Holdings, Inc. - Common Stock|G|N|N|100|N|N
IEUS|iShares MSCI Europe Small-Cap ETF|G|N|N|100|Y|N
IFBD|Infobird Co., Ltd - Ordinary Shares|S|N|D|100|N|N
IFGL|iShares International Developed Real Estate ETF|G|N|N|100|Y|N
IFRX|InflaRx N.V. - Common Stock|Q|N|N|100|N|N
IFV|First Trust Dorsey Wright International Focus 5 ETF|G|N|N|100|Y|N
IGF|iShares Global Infrastructure ETF|G|N|N|100|Y|N
IGIB|iShares 5-10 Year Investment Grade Corporate Bond ETF|G|N|N|100|Y|N
IGIC|International General Insurance Holdings Ltd. - Ordinary Shares|S|N|N|100|N|N
IGMS|IGM Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
IGOV|iShares International Treasury Bond ETF|G|N|N|100|Y|N
IGSB|iShares 1-5 Year Investment Grade Corporate Bond ETF|G|N|N|100|Y|N
IGTA|Inception Growth Acquisition Limited - Common Stock|G|N|N|100|N|N
IGTAR|Inception Growth Acquisition Limited - Rights|G|N|N|100|N|N
IGTAU|Inception Growth Acquisition Limited - Units|G|N|N|100|N|N
IGTAW|Inception Growth Acquisition Limited - Warrants|G|N|N|100|N|N
IHRT|iHeartMedia, Inc. - Class A Common Stock|Q|N|N|100|N|N
IHYF|Invesco High Yield Bond Factor ETF|G|N|N|100|Y|N
III|Information Services Group, Inc. - Common Stock|G|N|N|100|N|N
IIIV|i3 Verticals, Inc. - Common Stock|Q|N|N|100|N|N
IINN|Inspira Technologies Oxy B.H.N. Ltd. - Ordinary Shares|S|N|N|100|N|N
IINNW|Inspira Technologies Oxy B.H.N. Ltd. - Warrant|S|N|N|100|N|N
IJT|iShares S&P SmallCap 600 Growth ETF|G|N|N|100|Y|N
IKNA|Ikena Oncology, Inc. - Common Stock|G|N|N|100|N|N
IKT|Inhibikase Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
ILAG|Intelligent Living Application Group Inc. - Ordinary Shares|S|N|N|100|N|N
ILIT|iShares Lithium Miners and Producers ETF|G|N|N|100|Y|N
ILMN|Illumina, Inc. - Common Stock|Q|N|N|100|N|N
ILPT|Industrial Logistics Properties Trust - Common Shares of Beneficial Interest|Q|N|N|100|N|N
IMAB|I-MAB - American Depositary Shares|G|N|N|100|N|N
IMACW|IMAC Holdings, Inc. - Warrant|S|N|N|100|N|N
IMAQ|International Media Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
IMAQR|International Media Acquisition Corp. - Rights|S|N|N|100|N|N
IMAQU|International Media Acquisition Corp. - Unit|S|N|N|100|N|N
IMAQW|International Media Acquisition Corp. - Warrants|S|N|N|100|N|N
IMCC|IM Cannabis Corp. - Common Shares|S|N|D|100|N|N
IMCR|Immunocore Holdings plc - American Depositary Shares|Q|N|N|100|N|N
IMCV|iShares Morningstar Mid-Cap Value ETF|G|N|N|100|Y|N
IMGN|ImmunoGen, Inc. - Common Stock|Q|N|N|100|N|N
IMKTA|Ingles Markets, Incorporated - Class A Common Stock|Q|N|N|100|N|N
IMMP|Immutep Limited - American Depositary Shares|G|N|N|100|N|N
IMMR|Immersion Corporation - Common Stock|Q|N|N|100|N|N
IMMX|Immix Biopharma, Inc. - Common Stock|S|N|N|100|N|N
IMNM|Immunome, Inc. - Common Stock|S|N|N|100|N|N
IMNN|Imunon, Inc. - Common Stock|S|N|N|100|N|N
IMOS|ChipMOS TECHNOLOGIES INC. - American Depositary Shares|Q|N|N|100|N|N
IMPL|Impel Pharmaceuticals Inc. - Common Stock|G|N|D|100|N|N
IMPP|Imperial Petroleum Inc. - Common Shares|S|N|N|100|N|N
IMPPP|Imperial Petroleum Inc. - 8.75% Series A Cumulative Redeemable Perpetual Preferred Shares|S|N|N|100|N|N
IMRN|Immuron Limited - American Depositary Shares|S|N|N|100|N|N
IMRX|Immuneering Corporation - Class A Common Stock|G|N|N|100|N|N
IMTE|Integrated Media Technology Limited - Ordinary Shares|S|N|D|100|N|N
IMTX|Immatics N.V. - Ordinary Shares|S|N|N|100|N|N
IMTXW|Immatics N.V. - Warrants|S|N|N|100|N|N
IMUX|Immunic, Inc.  - Common Stock|Q|N|N|100|N|N
IMVT|Immunovant, Inc.  - Common Stock|Q|N|N|100|N|N
IMXI|International Money Express, Inc. - Common Stock|S|N|N|100|N|N
INAB|IN8bio, Inc. - Common Stock|G|N|N|100|N|N
INAQ|Insight Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
INAQU|Insight Acquisition Corp. - Unit|G|N|N|100|N|N
INAQW|Insight Acquisition Corp. - Warrant|S|N|N|100|N|N
INBK|First Internet Bancorp - Common Stock|Q|N|N|100|N|N
INBKZ|First Internet Bancorp - Fixed-to-Floating Rate Subordinated Notes Due 2029|Q|N|N|100|N|N
INBS|Intelligent Bio Solutions Inc.  - Common Stock|S|N|N|100|N|N
INBX|Inhibrx, Inc. - Common Stock|G|N|N|100|N|N
INCR|Intercure Ltd. - ordinary shares|G|N|N|100|N|N
INCY|Incyte Corporation - Common Stock|Q|N|N|100|N|N
INDB|Independent Bank Corp. - Common Stock|Q|N|N|100|N|N
INDI|indie Semiconductor, Inc. - Class A Common Stock|S|N|N|100|N|N
INDIW|indie Semiconductor, Inc. - Warrant|S|N|N|100|N|N
INDP|Indaptus Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
INDV|Indivior PLC - Ordinary Shares|Q|N|N|100|N|N
INDY|iShares India 50 ETF|G|N|N|100|Y|N
INFN|Infinera Corporation - Common Stock|Q|N|N|100|N|N
INFR|ClearBridge Sustainable Infrastructure ETF|G|N|N|100|Y|N
INGN|Inogen, Inc - Common Stock|Q|N|N|100|N|N
INKT|MiNK Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
INM|InMed Pharmaceuticals Inc. - Common Shares|S|N|D|100|N|N
INMB|INmune Bio Inc. - Common stock|S|N|N|100|N|N
INMD|InMode Ltd.  - Ordinary Shares|Q|N|N|100|N|N
INNV|InnovAge Holding Corp. - Common Stock|Q|N|N|100|N|N
INO|Inovio Pharmaceuticals, Inc. - Common Stock|Q|N|D|100|N|N
INOD|Innodata Inc. - Common Stock|G|N|N|100|N|N
INPX|Inpixon  - Common Stock|S|N|D|100|N|N
INSE|Inspired Entertainment, Inc. - Common Stock|S|N|N|100|N|N
INSG|Inseego Corp. - Common Stock|Q|N|D|100|N|N
INSM|Insmed Incorporated - Common Stock|Q|N|N|100|N|N
INTA|Intapp, Inc. - Common Stock|Q|N|N|100|N|N
INTC|Intel Corporation - Common Stock|Q|N|N|100|N|N
INTE|Integral Acquisition Corporation 1 - Class A Common Stock|G|N|D|100|N|N
INTEU|Integral Acquisition Corporation 1 - Unit|G|N|D|100|N|N
INTEW|Integral Acquisition Corporation 1 - Warrant|G|N|D|100|N|N
INTG|The Intergroup Corporation - Common Stock|S|N|N|100|N|N
INTR|Inter & Co. Inc. - Class A Common Shares|Q|N|N|100|N|N
INTS|Intensity Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
INTU|Intuit Inc. - Common Stock|Q|N|N|100|N|N
INTZ|Intrusion Inc. - Common Stock|S|N|D|100|N|N
INVA|Innoviva, Inc. - Common Stock|Q|N|D|100|N|N
INVE|Identiv, Inc. - Common Stock|S|N|N|100|N|N
INVO|INVO BioScience, Inc. - Common Stock|S|N|D|100|N|N
INVZ|Innoviz Technologies Ltd. - Ordinary shares|S|N|N|100|N|N
INVZW|Innoviz Technologies Ltd. - Warrant|S|N|N|100|N|N
INZY|Inozyme Pharma, Inc. - Common Stock|Q|N|N|100|N|N
IOAC|Innovative International Acquisition Corp. - Class A Ordinary Shares|G|N|D|100|N|N
IOACU|Innovative International Acquisition Corp. - Unit|G|N|D|100|N|N
IOACW|Innovative International Acquisition Corp. - Warrants|G|N|D|100|N|N
IOBT|IO Biotech, Inc. - Common Stock|Q|N|N|100|N|N
IONM|Assure Holdings Corp. - Common Stock|S|N|D|100|N|N
IONR|ioneer Ltd - American Depositary Shares|S|N|N|100|N|N
IONS|Ionis Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
IOSP|Innospec Inc. - Common Stock|Q|N|N|100|N|N
IOVA|Iovance Biotherapeutics, Inc. - Common Stock|G|N|N|100|N|N
IPA|ImmunoPrecise Antibodies Ltd. - Common Stock|G|N|N|100|N|N
IPAR|Inter Parfums, Inc. - Common Stock|Q|N|N|100|N|N
IPDN|Professional Diversity Network, Inc. - Common Stock|S|N|N|100|N|N
IPGP|IPG Photonics Corporation - Common Stock|Q|N|N|100|N|N
IPHA|Innate Pharma S.A. - American Depositary Shares|Q|N|N|100|N|N
IPKW|Invesco International BuyBack Achievers ETF|G|N|N|100|Y|N
IPSC|Century Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
IPW|iPower Inc. - Common Stock|S|N|D|100|N|N
IPWR|Ideal Power Inc. - Common Stock|S|N|N|100|N|N
IPX|IperionX Limited - American Depositary Share|S|N|N|100|N|N
IPXX|Inflection Point Acquisition Corp. II - Class A Ordinary Shares|G|N|N|100|N|N
IPXXU|Inflection Point Acquisition Corp. II - Unit|G|N|N|100|N|N
IPXXW|Inflection Point Acquisition Corp. II - Warrant|G|N|N|100|N|N
IQ|iQIYI, Inc. - American Depositary Shares|Q|N|N|100|N|N
IRAA|Iris Acquisition Corp - Class A Common Stock|S|N|N|100|N|N
IRAAU|Iris Acquisition Corp - Units|S|N|N|100|N|N
IRAAW|Iris Acquisition Corp - Warrant|S|N|N|100|N|N
IRBT|iRobot Corporation - Common Stock|Q|N|N|100|N|N
IRDM|Iridium Communications Inc - Common Stock|Q|N|N|100|N|N
IREN|Iris Energy Limited - Ordinary Shares|Q|N|N|100|N|N
IRIX|IRIDEX Corporation - Common Stock|G|N|N|100|N|N
IRMD|iRadimed Corporation - Common Stock|S|N|N|100|N|N
IRON|Disc Medicine, Inc. - Common Stock|G|N|N|100|N|N
IROQ|IF Bancorp, Inc. - Common Stock|S|N|N|100|N|N
IRTC|iRhythm Technologies, Inc. - Common Stock|Q|N|N|100|N|N
IRWD|Ironwood Pharmaceuticals, Inc. - Class A Common Stock|Q|N|N|100|N|N
ISHG|iShares 1-3 Year International Treasury Bond ETF|G|N|N|100|Y|N
ISHP|First Trust S-Network E-Commerce ETF|G|N|N|100|Y|N
ISPC|iSpecimen Inc. - Common Stock|S|N|D|100|N|N
ISPO|Inspirato Incorporated - Class A Common Stock|G|N|D|100|N|N
ISPOW|Inspirato Incorporated - Warrant|G|N|D|100|N|N
ISPR|Ispire Technology Inc. - Common Stock|S|N|N|100|N|N
ISRG|Intuitive Surgical, Inc. - Common Stock|Q|N|N|100|N|N
ISRL|Israel Acquisitions Corp - Class A Ordinary Shares|G|N|N|100|N|N
ISRLU|Israel Acquisitions Corp - Unit|G|N|N|100|N|N
ISRLW|Israel Acquisitions Corp - Warrant|G|N|N|100|N|N
ISSC|Innovative Solutions and Support, Inc. - Common Stock|Q|N|N|100|N|N
ISTB|iShares Core 1-5 Year USD Bond ETF|G|N|N|100|Y|N
ISTR|Investar Holding Corporation - Common Stock|G|N|N|100|N|N
ISUN|iSun, Inc. - Common Stock|S|N|D|100|N|N
ITAQ|Industrial Tech Acquisitions II, Inc. - Class A Common Stock|S|N|D|100|N|N
ITAQU|Industrial Tech Acquisitions II, Inc. - Units|S|N|D|100|N|N
ITAQW|Industrial Tech Acquisitions II, Inc. - Warrants|S|N|D|100|N|N
ITCI|Intra-Cellular Therapies Inc. - Common Stock|Q|N|N|100|N|N
ITI|Iteris, Inc. - Common Stock|S|N|N|100|N|N
ITIC|Investors Title Company - Common Stock|Q|N|N|100|N|N
ITOS|iTeos Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
ITRI|Itron, Inc. - Common Stock|Q|N|N|100|N|N
ITRM|Iterum Therapeutics plc - Ordinary Share|S|N|D|100|N|N
ITRN|Ituran Location and Control Ltd. - Ordinary Shares|Q|N|N|100|N|N
IUS|Invesco RAFI Strategic US ETF|G|N|N|100|Y|N
IUSB|iShares Core Total USD Bond Market ETF|G|N|N|100|Y|N
IUSG|iShares Core S&P U.S. Growth ETF|G|N|N|100|Y|N
IUSV|iShares Core S&P U.S. Value ETF|G|N|N|100|Y|N
IVA|Inventiva S.A. - American Depository Shares|G|N|N|100|N|N
IVAC|Intevac, Inc. - Common Stock|Q|N|N|100|N|N
IVCA|Investcorp India Acquisition Corp. - Class A Ordinary Shares|G|N|N|100|N|N
IVCAU|Investcorp India Acquisition Corp. - Unit|G|N|N|100|N|N
IVCAW|Investcorp India Acquisition Corp. - Warrant|G|N|N|100|N|N
IVCB|Investcorp Europe Acquisition Corp I - Class A Ordinary Shares|G|N|N|100|N|N
IVCBU|Investcorp Europe Acquisition Corp I - Unit|G|N|N|100|N|N
IVCBW|Investcorp Europe Acquisition Corp I - Warrant|G|N|N|100|N|N
IVCP|Swiftmerge Acquisition Corp. - Class A Ordinary Share|S|N|N|100|N|N
IVCPU|Swiftmerge Acquisition Corp. - Unit|S|N|N|100|N|N
IVCPW|Swiftmerge Acquisition Corp. - Warrants|S|N|N|100|N|N
IVDA|Iveda Solutions, Inc. - Common Stock|S|N|D|100|N|N
IVDAW|Iveda Solutions, Inc. - Warrant|S|N|N|100|N|N
IVEG|iShares Emergent Food and AgTech Multisector ETF|G|N|N|100|Y|N
IVP|Inspire Veterinary Partners, Inc. - Class A Common Stock|S|N|N|100|N|N
IVVD|Invivyd, Inc. - Common Stock|G|N|N|100|N|N
IWTR|iShares MSCI Water Management Multisector ETF|G|N|N|100|Y|N
IXAQ|IX Acquisition Corp. - Class A Ordinary Share|G|N|D|100|N|N
IXAQU|IX Acquisition Corp. - Unit|G|N|N|100|N|N
IXAQW|IX Acquisition Corp. - Warrant|G|N|N|100|N|N
IXHL|Incannex Healthcare Limited - American Depositary Shares|G|N|N|100|N|N
IXUS|iShares Core MSCI Total International Stock ETF|G|N|N|100|Y|N
IZEA|IZEA Worldwide, Inc. - Common Stock|S|N|N|100|N|N
IZM|ICZOOM Group Inc. - Class A Ordinary Shares|S|N|N|100|N|N
JACK|Jack In The Box Inc. - Common Stock|Q|N|N|100|N|N
JAGX|Jaguar Health, Inc. - Common Stock|S|N|D|100|N|N
JAKK|JAKKS Pacific, Inc. - Common Stock|Q|N|N|100|N|N
JAMF|Jamf Holding Corp. - Common Stock|Q|N|N|100|N|N
JAN|JanOne Inc. - Common Stock|S|N|D|100|N|N
JANX|Janux Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
JAQC|Jupiter Acquisition Corporation - Common stock|S|N|N|100|N|N
JAQCU|Jupiter Acquisition Corporation - Units|S|N|N|100|N|N
JAQCW|Jupiter Acquisition Corporation - Warrants|S|N|N|100|N|N
JAZZ|Jazz Pharmaceuticals plc - Ordinary Shares|Q|N|N|100|N|N
JBHT|J.B. Hunt Transport Services, Inc. - Common Stock|Q|N|N|100|N|N
JBLU|JetBlue Airways Corporation - Common Stock|Q|N|N|100|N|N
JBSS|John B. Sanfilippo & Son, Inc. - Common Stock|Q|N|N|100|N|N
JCSE|JE Cleantech Holdings Limited - Ordinary Shares|S|N|D|100|N|N
JCTCF|Jewett-Cameron Trading Company - Common Shares|S|N|N|100|N|N
JD|JD.com, Inc. - American Depositary Shares|Q|N|N|100|N|N
JEPQ|JPMorgan Nasdaq Equity Premium Income ETF|G|N|N|100|Y|N
JEWL|Adamas One Corp. - Common Stock|S|N|E|100|N|N
JFBR|Jeffs' Brands Ltd - Ordinary Shares|S|N|D|100|N|N
JFBRW|Jeffs' Brands Ltd - Warrant|S|N|N|100|N|N
JFIN|Jiayin Group Inc. - American Depositary Shares|G|N|N|100|N|N
JFU|9F Inc. - American Depositary Shares|G|N|N|100|N|N
JG|Aurora Mobile Limited - American Depositary Shares|S|N|D|100|N|N
JGGC|Jaguar Global Growth Corporation I - Class A Ordinary Shares|G|N|N|100|N|N
JGGCR|Jaguar Global Growth Corporation I - Right|G|N|N|100|N|N
JGGCU|Jaguar Global Growth Corporation I - Unit|G|N|N|100|N|N
JGGCW|Jaguar Global Growth Corporation I - Warrant|G|N|D|100|N|N
JGLO|JPMorgan Global Select Equity ETF|G|N|N|100|Y|N
JIVE|JPMorgan International Value ETF|G|N|N|100|Y|N
JJSF|J & J Snack Foods Corp. - Common Stock|Q|N|N|100|N|N
JKHY|Jack Henry & Associates, Inc. - Common Stock|Q|N|N|100|N|N
JMSB|John Marshall Bancorp, Inc. - Common Stock|S|N|N|100|N|N
JNVR|Janover Inc. - Common Stock|S|N|N|100|N|N
JOAN|JOANN, Inc. - common stock|G|N|D|100|N|N
JOET|Virtus Terranova U.S. Quality Momentum ETF|G|N|N|100|Y|N
JOUT|Johnson Outdoors Inc. - Class A Common Stock|Q|N|N|100|N|N
JPEF|JPMorgan Equity Focus ETF|G|N|N|100|Y|N
JRSH|Jerash Holdings (US), Inc. - Common Stock|S|N|N|100|N|N
JRVR|James River Group Holdings, Ltd. - Common Shares|Q|N|N|100|N|N
JSM|Navient Corporation - 6% Senior Notes due December 15, 2043|Q|N|N|100|N|N
JSMD|Janus Henderson Small/Mid Cap Growth Alpha ETF|G|N|N|100|Y|N
JSML|Janus Henderson Small Cap Growth Alpha ETF|G|N|N|100|Y|N
JSPR|Jasper Therapeutics, Inc. - Class A Common Stock|S|N|N|100|N|N
JSPRW|Jasper Therapeutics, Inc. - Warrant|S|N|N|100|N|N
JTAI|Jet.AI Inc. - Common Stock|G|N|N|100|N|N
JTAIW|Jet.AI Inc. - Warrant|S|N|N|100|N|N
JTAIZ|Jet.AI Inc. - Merger Consideration Warrants|G|N|N|100|N|N
JTEK|JPMorgan U.S. Tech Leaders ETF|G|N|N|100|Y|N
JVA|Coffee Holding Co., Inc. - Common Stock|S|N|N|100|N|N
JWEL|Jowell Global Ltd. - Ordinary Shares|S|N|D|100|N|N
JXJT|JX Luxventure Limited - Common Stock|S|N|N|100|N|N
JYD|Jayud Global Logistics Limited - Class A Ordinary Shares|S|N|N|100|N|N
JYNT|The Joint Corp. - Common Stock|S|N|N|100|N|N
JZ|Jianzhi Education Technology Group Company Limited - American Depositary Shares|Q|N|D|100|N|N
JZXN|Jiuzi Holdings, Inc. - Ordinary Shares|S|N|N|100|N|N
KA|Kineta, Inc. - Common Stock|S|N|N|100|N|N
KACL|Kairous Acquisition Corp. Limited - Ordinary Shares|G|N|D|100|N|N
KACLR|Kairous Acquisition Corp. Limited - Rights|G|N|D|100|N|N
KACLU|Kairous Acquisition Corp. Limited - Unit|G|N|D|100|N|N
KACLW|Kairous Acquisition Corp. Limited - Warrants|G|N|D|100|N|N
KALA|KALA BIO, Inc. - Common Stock|S|N|N|100|N|N
KALU|Kaiser Aluminum Corporation - Common Stock|Q|N|N|100|N|N
KALV|KalVista Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
KARO|Karooooo Ltd. - Ordinary shares|S|N|N|100|N|N
KAVL|Kaival Brands Innovations Group, Inc. - Common Stock|S|N|D|100|N|N
KBNT|Kubient, Inc. - Common Stock|S|N|H|100|N|N
KBNTW|Kubient, Inc. - Warrant|S|N|E|100|N|N
KBWB|Invesco KBW Bank ETF|G|N|N|100|Y|N
KBWD|Invesco KBW High Dividend Yield Financial ETF|G|N|N|100|Y|N
KBWP|Invesco KBW Property & Casualty Insurance ETF|G|N|N|100|Y|N
KBWR|Invesco KBW Regional Banking ETF|G|N|N|100|Y|N
KBWY|Invesco KBW Premium Yield Equity REIT ETF|G|N|N|100|Y|N
KC|Kingsoft Cloud Holdings Limited - American Depositary Shares|Q|N|N|100|N|N
KDP|Keurig Dr Pepper Inc. - Common Stock|Q|N|N|100|N|N
KE|Kimball Electronics, Inc. - Common Stock|Q|N|N|100|N|N
KEJI|Global X China Innovation ETF|G|N|N|100|Y|N
KELYA|Kelly Services, Inc. - Class A Common Stock|Q|N|N|100|N|N
KELYB|Kelly Services, Inc. - Class B Common Stock|Q|N|N|100|N|N
KEQU|Kewaunee Scientific Corporation - Common Stock|G|N|N|100|N|N
KERN|Akerna Corp. - Common Stock|S|N|D|100|N|N
KERNW|Akerna Corp. - Warrant|S|N|D|100|N|N
KFFB|Kentucky First Federal Bancorp - Common Stock|G|N|N|100|N|N
KFRC|Kforce, Inc. - Common Stock|Q|N|N|100|N|N
KGEI|Kolibri Global Energy Inc. - Common stock|S|N|N|100|N|N
KHC|The Kraft Heinz Company - Common Stock|Q|N|N|100|N|N
KIDS|OrthoPediatrics Corp. - Common Stock|G|N|N|100|N|N
KINS|Kingstone Companies, Inc - Common Stock|S|N|N|100|N|N
KIRK|Kirkland's, Inc. - Common Stock|Q|N|N|100|N|N
KITT|Nauticus Robotics, Inc. - Common stock|S|N|N|100|N|N
KITTW|Nauticus Robotics, Inc. - Warrant|S|N|N|100|N|N
KLAC|KLA Corporation  - Common Stock|Q|N|N|100|N|N
KLIC|Kulicke and Soffa Industries, Inc. - Common Stock|Q|N|N|100|N|N
KLTR|Kaltura, Inc. - Common Stock|Q|N|N|100|N|N
KLXE|KLX Energy Services Holdings, Inc.  - Common Stock|Q|N|N|100|N|N
KMDA|Kamada Ltd. - Ordinary Shares|Q|N|N|100|N|N
KNDI|Kandi Technologies Group, Inc. - Common Stock|Q|N|N|100|N|N
KNGZ|First Trust S&P 500 Diversified Dividend Aristocrats ETF|G|N|N|100|Y|N
KNSA|Kiniksa Pharmaceuticals, Ltd. - Class A Common Stock|Q|N|N|100|N|N
KNTE|Kinnate Biopharma Inc. - Common Stock|Q|N|N|100|N|N
KOD|Kodiak Sciences Inc - Common Stock|G|N|N|100|N|N
KOPN|Kopin Corporation - Common Stock|S|N|N|100|N|N
KOSS|Koss Corporation - Common Stock|S|N|N|100|N|N
KPLT|Katapult Holdings, Inc. - Common Stock|G|N|N|100|N|N
KPLTW|Katapult Holdings, Inc. - Warrant|G|N|N|100|N|N
KPRX|Kiora Pharmaceuticals, Inc.  - Common Stock|S|N|D|100|N|N
KPTI|Karyopharm Therapeutics Inc. - Common Stock|Q|N|N|100|N|N
KRKR|36Kr Holdings Inc. - American Depositary Shares|G|N|N|100|N|N
KRMA|Global X Conscious Companies ETF|G|N|N|100|Y|N
KRMD|KORU Medical Systems, Inc. - Common Stock|S|N|N|100|N|N
KRNL|Kernel Group Holdings, Inc. - Class A Ordinary Shares|S|N|N|100|N|N
KRNLU|Kernel Group Holdings, Inc. - Units|S|N|N|100|N|N
KRNLW|Kernel Group Holdings, Inc. - Warrants|S|N|N|100|N|N
KRNT|Kornit Digital Ltd. - Ordinary Shares|Q|N|N|100|N|N
KRNY|Kearny Financial - Common Stock|Q|N|N|100|N|N
KRON|Kronos Bio, Inc. - Common Stock|Q|N|N|100|N|N
KROP|Global X AgTech & Food Innovation ETF|G|N|N|100|Y|N
KROS|Keros Therapeutics, Inc. - common stock|G|N|N|100|N|N
KRT|Karat Packaging Inc. - Common Stock|Q|N|N|100|N|N
KRTX|Karuna Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
KRUS|Kura Sushi USA, Inc. - Class A Common Stock|G|N|N|100|N|N
KRYS|Krystal Biotech, Inc. - Common Stock|G|N|N|100|N|N
KSCP|Knightscope, Inc. - Class A Common Stock|G|N|N|100|N|N
KTCC|Key Tronic Corporation - Common Stock|G|N|N|100|N|N
KTOS|Kratos Defense & Security Solutions, Inc. - Common Stock|Q|N|N|100|N|N
KTRA|Kintara Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
KTTA|Pasithea Therapeutics Corp. - Common Stock|S|N|D|100|N|N
KTTAW|Pasithea Therapeutics Corp. - Warrant|S|N|N|100|N|N
KURA|Kura Oncology, Inc. - Common Stock|Q|N|N|100|N|N
KVAC|Keen Vision Acquisition Corporation - Ordinary Shares|G|N|N|100|N|N
KVACU|Keen Vision Acquisition Corporation - Units|G|N|N|100|N|N
KVACW|Keen Vision Acquisition Corporation - Warrant|G|N|N|100|N|N
KVHI|KVH Industries, Inc. - Common Stock|Q|N|N|100|N|N
KVSA|Khosla Ventures Acquisition Co. - Class A Common Stock|S|N|D|100|N|N
KWE|KWESST Micro Systems Inc. - common stock, no R/S concurrent with offering|S|N|N|100|N|N
KWESW|KWESST Micro Systems Inc. - warrant|S|N|N|100|N|N
KXIN|Kaixin Auto Holdings - Ordinary Shares|S|N|N|100|N|N
KYCH|Keyarch Acquisition Corporation - Ordinary Shares|S|N|N|100|N|N
KYCHR|Keyarch Acquisition Corporation - Rights|S|N|N|100|N|N
KYCHU|Keyarch Acquisition Corporation - Unit|S|N|N|100|N|N
KYCHW|Keyarch Acquisition Corporation - Warrant|S|N|N|100|N|N
KYMR|Kymera Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
KZIA|Kazia Therapeutics Limited - American Depositary Shares|S|N|N|100|N|N
KZR|Kezar Life Sciences, Inc. - Common Stock|Q|N|N|100|N|N
LAB|Standard BioTools Inc. - Common Stock|Q|N|N|100|N|N
LABP|Landos Biopharma, Inc. - Common Stock|S|N|N|100|N|N
LAES|SEALSQ Corp - Ordinary Shares|G|N|D|100|N|N
LAKE|Lakeland Industries, Inc. - Common Stock|G|N|N|100|N|N
LAMR|Lamar Advertising Company - Class A Common Stock|Q|N|N|100|N|N
LANC|Lancaster Colony Corporation - Common Stock|Q|N|N|100|N|N
LAND|Gladstone Land Corporation - Common Stock|G|N|N|100|N|N
LANDM|Gladstone Land Corporation - 5.00% Series D Cumulative Term Preferred Stock|G|N|N|100|N|N
LANDO|Gladstone Land Corporation - 6.00% Series B Cumulative Redeemable Preferred Stock|G|N|N|100|N|N
LANDP|Gladstone Land Corporation - 6.00% Series C Cumulative Redeemable Preferred Stock|G|N|N|100|N|N
LARK|Landmark Bancorp Inc. - Common Stock|G|N|N|100|N|N
LASE|Laser Photonics Corporation - Common Stock|S|N|D|100|N|N
LASR|nLIGHT, Inc. - Common Stock|Q|N|N|100|N|N
LATG|LatAmGrowth SPAC - Class A Ordinary Shares|G|N|N|100|N|N
LATGU|LatAmGrowth SPAC - Units|G|N|N|100|N|N
LAUR|Laureate Education, Inc. - Common Stock|Q|N|N|100|N|N
LAZR|Luminar Technologies, Inc.  - Class A Common Stock|Q|N|N|100|N|N
LAZY|Lazydays Holdings, Inc. - Common Stock|S|N|N|100|N|N
LBAI|Lakeland Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
LBBB|Lakeshore Acquisition II Corp. - Ordinary Shares|G|N|N|100|N|N
LBBBR|Lakeshore Acquisition II Corp. - Rights|G|N|N|100|N|N
LBBBU|Lakeshore Acquisition II Corp. - Unit|G|N|N|100|N|N
LBBBW|Lakeshore Acquisition II Corp. - Warrants|G|N|N|100|N|N
LBC|Luther Burbank Corporation - Common Stock|Q|N|N|100|N|N
LBPH|Longboard Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
LBRDA|Liberty Broadband Corporation - Class A Common Stock|Q|N|N|100|N|N
LBRDK|Liberty Broadband Corporation - Class C Common Stock|Q|N|N|100|N|N
LBRDP|Liberty Broadband Corporation - Series A Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
LBTYA|Liberty Global plc - Class A Ordinary Shares|Q|N|N|100|N|N
LBTYB|Liberty Global plc - Class B Ordinary Shares|Q|N|N|100|N|N
LBTYK|Liberty Global plc - Class C Ordinary Shares|Q|N|N|100|N|N
LCA|Landcadia Holdings IV, Inc. - Class A Common Stock|S|N|N|100|N|N
LCAA|L Catterton Asia Acquisition Corp - Class A Ordinary Shares|S|N|N|100|N|N
LCAAU|L Catterton Asia Acquisition Corp - Units|S|N|N|100|N|N
LCAAW|L Catterton Asia Acquisition Corp - Warrant|S|N|N|100|N|N
LCAHU|Landcadia Holdings IV, Inc. - Units|S|N|N|100|N|N
LCAHW|Landcadia Holdings IV, Inc. - Warrant|S|N|N|100|N|N
LCFY|Locafy Limited - Ordinary Share|S|N|D|100|N|N
LCFYW|Locafy Limited - Warrant|S|N|D|100|N|N
LCID|Lucid Group, Inc. - Common Stock|Q|N|N|100|N|N
LCNB|LCNB Corporation - Common Stock|S|N|N|100|N|N
LCUT|Lifetime Brands, Inc. - Common Stock|Q|N|N|100|N|N
LDEM|iShares ESG MSCI EM Leaders ETF|G|N|N|100|Y|N
LDSF|First Trust Low Duration Strategic Focus ETF|G|N|N|100|Y|N
LDWY|Lendway, Inc. - Common Stock|S|N|N|100|N|N
LE|Lands' End, Inc. - Common Stock|S|N|N|100|N|N
LECO|Lincoln Electric Holdings, Inc. - Common Shares|Q|N|N|100|N|N
LEDS|SemiLEDS Corporation - Common Stock|S|N|D|100|N|N
LEE|Lee Enterprises, Incorporated - Common Stock|Q|N|N|100|N|N
LEGH|Legacy Housing Corporation - Common Stock|Q|N|D|100|N|N
LEGN|Legend Biotech Corporation - American Depositary Shares|Q|N|N|100|N|N
LEGR|First Trust Indxx Innovative Transaction & Process ETF|G|N|N|100|Y|N
LESL|Leslie's, Inc. - Common Stock|Q|N|N|100|N|N
LEXX|Lexaria Bioscience Corp. - Common Stock|S|N|N|100|N|N
LEXXW|Lexaria Bioscience Corp. - Warrant|S|N|N|100|N|N
LFCR|Lifecore Biomedical, Inc. - Common Stock|Q|N|E|100|N|N
LFLY|Leafly Holdings, Inc. - Common Stock|S|N|N|100|N|N
LFLYW|Leafly Holdings, Inc. - Warrant|S|N|N|100|N|N
LFMD|LifeMD, Inc. - Common Stock|G|N|N|100|N|N
LFMDP|LifeMD, Inc. - 8.875% Series A Cumulative Perpetual Preferred Stock|G|N|N|100|N|N
LFST|LifeStance Health Group, Inc. - Common Stock|Q|N|N|100|N|N
LFUS|Littelfuse, Inc. - Common Stock|Q|N|N|100|N|N
LFVN|Lifevantage Corporation - Common Stock|S|N|N|100|N|N
LGHL|Lion Group Holding Ltd. - American Depositary Share|S|N|N|100|N|N
LGHLW|Lion Group Holding Ltd. - Warrant|S|N|N|100|N|N
LGIH|LGI Homes, Inc. - Common Stock|Q|N|N|100|N|N
LGMK|LogicMark, Inc. - Common Stock|S|N|N|100|N|N
LGND|Ligand Pharmaceuticals Incorporated - Common Stock|G|N|N|100|N|N
LGO|Largo Inc. - Common Shares|Q|N|N|100|N|N
LGRO|Level Four Large Cap Growth Active ETF|G|N|N|100|Y|N
LGST|Semper Paratus Acquisition Corporation - Class A Ordinary Shares|G|N|N|100|N|N
LGSTU|Semper Paratus Acquisition Corporation - Unit|G|N|N|100|N|N
LGSTW|Semper Paratus Acquisition Corporation - Warrant|G|N|N|100|N|N
LGVC|LAMF Global Ventures Corp. I - Class A Ordinary Shares|G|N|N|100|N|N
LGVCU|LAMF Global Ventures Corp. I - Unit|G|N|N|100|N|N
LGVCW|LAMF Global Ventures Corp. I - Warrant|G|N|N|100|N|N
LGVN|Longeveron Inc. - common stock|S|N|N|100|N|N
LI|Li Auto Inc. - American Depositary Shares|Q|N|N|100|N|N
LIAN|LianBio - American Depositary Shares|G|N|N|100|N|N
LIBY|Liberty Resources Acquisition Corp. - Class A Common Stock|G|N|D|100|N|N
LIBYU|Liberty Resources Acquisition Corp. - Unit|G|N|D|100|N|N
LIBYW|Liberty Resources Acquisition Corp. - Warrant|G|N|D|100|N|N
LICN|Lichen China Limited - Class A Ordinary Shares|S|N|N|100|N|N
LIDR|AEye, Inc. - Class A Common Stock|S|N|D|100|N|N
LIDRW|AEye, Inc. - Warrant|S|N|D|100|N|N
LIFE|aTyr Pharma, Inc. - Common Stock|S|N|N|100|N|N
LIFW|MSP Recovery, Inc. - Class A Common Stock|G|N|D|100|N|N
LIFWW|MSP Recovery, Inc. - Warrant|G|N|D|100|N|N
LIFWZ|MSP Recovery, Inc. - Warrant|G|N|D|100|N|N
LILA|Liberty Latin America Ltd. - Class A Common Stock|Q|N|N|100|N|N
LILAK|Liberty Latin America Ltd. - Class C Common Stock|Q|N|N|100|N|N
LILM|Lilium N.V. - Class A Ordinary Shares|Q|N|N|100|N|N
LILMW|Lilium N.V. - Warrants|Q|N|N|100|N|N
LINC|Lincoln Educational Services Corporation - Common Stock|Q|N|N|100|N|N
LIND|Lindblad Expeditions Holdings Inc.  - Common Stock|S|N|N|100|N|N
LINK|Interlink Electronics, Inc. - Common Stock|S|N|N|100|N|N
LIPO|Lipella Pharmaceuticals Inc. - Common Stock|S|N|N|100|N|N
LIQT|LiqTech International, Inc. - Common Stock|S|N|N|100|N|N
LITE|Lumentum Holdings Inc. - Common Stock|Q|N|N|100|N|N
LITM|Snow Lake Resources Ltd. - Common Shares|S|N|N|100|N|N
LITP|Sprott Lithium Miners ETF|G|N|N|100|Y|N
LIVB|LIV Capital Acquisition Corp. II - Class A Ordinary Shares|G|N|N|100|N|N
LIVBU|LIV Capital Acquisition Corp. II - Unit|G|N|N|100|N|N
LIVBW|LIV Capital Acquisition Corp. II - Warrants|G|N|N|100|N|N
LIVE|Live Ventures Incorporated - Common Stock|S|N|N|100|N|N
LIVN|LivaNova PLC - Ordinary Shares|Q|N|N|100|N|N
LIXT|Lixte Biotechnology Holdings, Inc. - Common Stock|S|N|N|100|N|N
LIXTW|Lixte Biotechnology Holdings, Inc. - Warrants|S|N|N|100|N|N
LIZI|LIZHI INC. - American Depositary Shares|S|N|N|100|N|N
LKCO|Luokung Technology Corp - Ordinary Shares|S|N|N|100|N|N
LKFN|Lakeland Financial Corporation - Common Stock|Q|N|N|100|N|N
LKQ|LKQ Corporation - Common Stock|Q|N|N|100|N|N
LLYVA|Liberty Media Corporation - Series A Liberty Live Common Stock|Q|N|N|100|N|N
LLYVK|Liberty Media Corporation - Series C Liberty Live Common Stock|Q|N|N|100|N|N
LMAT|LeMaitre Vascular, Inc. - Common Stock|G|N|N|100|N|N
LMB|Limbach Holdings, Inc. - Common Stock|S|N|N|100|N|N
LMBS|First Trust Low Duration Opportunities ETF|G|N|N|100|Y|N
LMDX|LumiraDx Limited - Common stock|G|N|D|100|N|N
LMDXW|LumiraDx Limited - Warrant|G|N|N|100|N|N
LMFA|LM Funding America, Inc. - Common Stock|S|N|D|100|N|N
LMNR|Limoneira Co - Common Stock|Q|N|N|100|N|N
LNKB|LINKBANCORP, Inc. - Common Stock|S|N|N|100|N|N
LNSR|LENSAR, Inc. - Common Stock|S|N|N|100|N|N
LNT|Alliant Energy Corporation - Common Stock|Q|N|N|100|N|N
LNTH|Lantheus Holdings, Inc. - Common Stock|G|N|N|100|N|N
LNW|Light & Wonder, Inc.  - Common Stock|Q|N|N|100|N|N
LNZA|LanzaTech Global, Inc. - Common Stock|S|N|N|100|N|N
LNZAW|LanzaTech Global, Inc. - Warrant|S|N|N|100|N|N
LOAN|Manhattan Bridge Capital, Inc - Common Stock|S|N|N|100|N|N
LOCO|El Pollo Loco Holdings, Inc. - Common Stock|Q|N|N|100|N|N
LOGI|Logitech International S.A. - Registered Shares|Q|N|N|100|N|N
LOOP|Loop Industries, Inc. - Common Stock|G|N|N|100|N|N
LOPE|Grand Canyon Education, Inc. - Common Stock|Q|N|N|100|N|N
LOVE|The Lovesac Company - Common Stock|G|N|E|100|N|N
LPCN|Lipocine Inc. - Common Stock|S|N|N|100|N|N
LPLA|LPL Financial Holdings Inc. - Common Stock|Q|N|N|100|N|N
LPRO|Open Lending Corporation - Common Stock|G|N|N|100|N|N
LPSN|LivePerson, Inc. - Common Stock|Q|N|N|100|N|N
LPTH|LightPath Technologies, Inc. - Class A Common Stock|S|N|N|100|N|N
LPTX|Leap Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
LQDA|Liquidia Corporation - Common Stock|S|N|N|100|N|N
LQDT|Liquidity Services, Inc. - Common Stock|Q|N|N|100|N|N
LQR|LQR House Inc. - Common Stock|S|N|N|100|N|N
LRCX|Lam Research Corporation - Common Stock|Q|N|N|100|N|N
LRE|Lead Real Estate Co., Ltd - American Depositary Shares|G|N|N|100|N|N
LRFC|Logan Ridge Finance Corporation - Common Stock|Q|N|N|100|N|N
LRGE|ClearBridge Large Cap Growth ESG ETF|G|N|N|100|Y|N
LRHC|La Rosa Holdings Corp. - Common Stock|S|N|N|100|N|N
LRMR|Larimar Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
LRND|IQ U.S. Large Cap R&D Leaders ETF|G|N|N|100|Y|N
LSAK|Lesaka Technologies, Inc. - Common Stock|Q|N|N|100|N|N
LSBK|Lake Shore Bancorp, Inc. - Common Stock|G|N|N|100|N|N
LSCC|Lattice Semiconductor Corporation - Common Stock|Q|N|N|100|N|N
LSDI|Lucy Scientific Discovery Inc. - Common Stock|S|N|D|100|N|N
LSEA|Landsea Homes Corporation - Common Stock|S|N|N|100|N|N
LSEAW|Landsea Homes Corporation - Warrant|S|N|N|100|N|N
LSTA|Lisata Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
LSTR|Landstar System, Inc. - Common Stock|Q|N|N|100|N|N
LSXMA|Liberty Media Corporation - Series A Liberty SiriusXM Common Stock|Q|N|N|100|N|N
LSXMB|Liberty Media Corporation - Series B Liberty SiriusXM Common Stock|Q|N|N|100|N|N
LSXMK|Liberty Media Corporation - Series C Liberty SiriusXM Common Stock|Q|N|N|100|N|N
LTBR|Lightbridge Corporation - Common Stock|S|N|N|100|N|N
LTRN|Lantern Pharma Inc. - Common Stock|S|N|N|100|N|N
LTRPA|Liberty TripAdvisor Holdings, Inc. - Series A Common Stock|Q|N|D|100|N|N
LTRPB|Liberty TripAdvisor Holdings, Inc. - Series B Common Stock|Q|N|N|100|N|N
LTRX|Lantronix, Inc. - Common Stock|S|N|N|100|N|N
LTRY|Lottery.com, Inc. - Common Stock|G|N|N|100|N|N
LTRYW|Lottery.com, Inc. - Warrant|G|N|N|100|N|N
LUCD|Lucid Diagnostics Inc. - Common Stock|G|N|N|100|N|N
LUCY|Innovative Eyewear, Inc. - Common Stock|S|N|D|100|N|N
LUCYW|Innovative Eyewear, Inc. - Warrants|S|N|N|100|N|N
LULU|lululemon athletica inc. - Common Stock|Q|N|N|100|N|N
LUMO|Lumos Pharma, Inc. - Common Stock|G|N|N|100|N|N
LUNA|Luna Innovations Incorporated - Common Stock|S|N|N|100|N|N
LUNG|Pulmonx Corporation - Common Stock|Q|N|N|100|N|N
LUNR|Intuitive Machines, Inc. - Class A Common Stock|G|N|N|100|N|N
LUNRW|Intuitive Machines, Inc. - Warrants|S|N|N|100|N|N
LUXH|LuxUrban Hotels Inc. - Common Stock|S|N|N|100|N|N
LVHD|Franklin U.S. Low Volatility High Dividend Index ETF|G|N|N|100|Y|N
LVLU|Lulu's Fashion Lounge Holdings, Inc. - Common Stock|G|N|N|100|N|N
LVO|LiveOne, Inc. - Common Stock|S|N|N|100|N|N
LVOX|LiveVox Holdings, Inc. - Class A Common Stock|Q|N|N|100|N|N
LVOXU|LiveVox Holdings, Inc. - Unit|Q|N|N|100|N|N
LVOXW|LiveVox Holdings, Inc. - Warrant|Q|N|N|100|N|N
LVRO|Lavoro Limited - Class A Ordinary Shares|G|N|N|100|N|N
LVROW|Lavoro Limited - Warrant|G|N|N|100|N|N
LVTX|LAVA Therapeutics N.V. - Ordinary Shares|Q|N|N|100|N|N
LWAY|Lifeway Foods, Inc. - Common Stock|G|N|N|100|N|N
LWLG|Lightwave Logic, Inc. - Common Stock|S|N|N|100|N|N
LX|LexinFintech Holdings Ltd. - American Depositary Shares|Q|N|N|100|N|N
LXEH|Lixiang Education Holding Co., Ltd. - American Depositary Shares|G|N|D|100|N|N
LXRX|Lexicon Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
LYEL|Lyell Immunopharma, Inc. - Common Stock|Q|N|N|100|N|N
LYFT|Lyft, Inc. - Class A Common Stock|Q|N|N|100|N|N
LYRA|Lyra Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
LYT|Lytus Technologies Holdings PTV. Ltd. - Common Shares|S|N|D|100|N|N
LYTS|LSI Industries Inc. - Common Stock|Q|N|N|100|N|N
LZ|LegalZoom.com, Inc. - Common Stock|Q|N|N|100|N|N
LZRD|Parabla Innovation ETF|G|N|N|100|Y|N
MACA|Moringa Acquisition Corp - Class A Ordinary Shares|S|N|D|100|N|N
MACAU|Moringa Acquisition Corp - Units|S|N|D|100|N|N
MACAW|Moringa Acquisition Corp - Warrant|S|N|D|100|N|N
MACK|Merrimack Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
MAMA|Mama's Creations, Inc. - Common Stock|S|N|N|100|N|N
MANH|Manhattan Associates, Inc. - Common Stock|Q|N|N|100|N|N
MAPS|WM Technology, Inc. - Class A Common Stock|Q|N|N|100|N|N
MAPSW|WM Technology, Inc. - Warrants|Q|N|N|100|N|N
MAQC|Maquia Capital Acquisition Corporation - Class A Common Stock|S|N|N|100|N|N
MAQCU|Maquia Capital Acquisition Corporation - Unit|S|N|N|100|N|N
MAQCW|Maquia Capital Acquisition Corporation - Warrant|S|N|N|100|N|N
MAR|Marriott International - Class A Common Stock|Q|N|N|100|N|N
MARA|Marathon Digital Holdings, Inc. - Common Stock|S|N|N|100|N|N
MARK|Remark Holdings, Inc. - Common Stock|S|N|D|100|N|N
MARPS|Marine Petroleum Trust - Units of Beneficial Interest|S|N|N|100|N|N
MARX|Mars Acquisition Corp. - Ordinary Shares|G|N|N|100|N|N
MARXR|Mars Acquisition Corp. - Rights|G|N|N|100|N|N
MARXU|Mars Acquisition Corp. - Unit|G|N|N|100|N|N
MASI|Masimo Corporation - Common Stock|Q|N|N|100|N|N
MASS|908 Devices Inc. - Common Stock|G|N|N|100|N|N
MAT|Mattel, Inc. - Common Stock|Q|N|N|100|N|N
MATH|Metalpha Technology Holding Limited - Ordinary Shares|S|N|E|100|N|N
MATW|Matthews International Corporation - Class A Common Stock|Q|N|N|100|N|N
MAXI|Simplify Bitcoin Strategy PLUS Income ETF|G|N|N|100|Y|N
MAXN|Maxeon Solar Technologies, Ltd. - Ordinary Shares|Q|N|N|100|N|N
MAYS|J. W. Mays, Inc. - Common Stock|S|N|N|100|N|N
MBB|iShares MBS ETF|G|N|N|100|Y|N
MBCN|Middlefield Banc Corp. - Common Stock|S|N|N|100|N|N
MBIN|Merchants Bancorp - Common Stock|S|N|N|100|N|N
MBINM|Merchants Bancorp - Depositary Shares, Each Representing a 1/40th Interest in a Share of 8.25% Fixed-Rate Reset Series D Non-Cumulative Perpetual Preferred Stock|S|N|N|100|N|N
MBINN|Merchants Bancorp - Depositary Shares 6.00% Fixed Rate Series C Non-Cumulative Perpetual Preferred Stock|S|N|N|100|N|N
MBINO|Merchants Bancorp - Depositary Shares Each Representing a 1/40th Interest in a Share of Series B Fixed-to-Floating Rate|S|N|N|100|N|N
MBINP|Merchants Bancorp - 7.00% Fixed-to-Floating Rate Series A Non-Cumulative Perpetual Preferred Stock|S|N|N|100|N|N
MBIO|Mustang Bio, Inc. - Common Stock|S|N|N|100|N|N
MBLY|Mobileye Global Inc. - Class A Common Stock|Q|N|N|100|N|N
MBNKP|Medallion Bank - Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock, Series F|S|N|N|100|N|N
MBOT|Microbot Medical Inc.  - Common Stock|S|N|N|100|N|N
MBRX|Moleculin Biotech, Inc. - Common Stock|S|N|D|100|N|N
MBTC|Nocturne Acquisition Corporation - Ordinary Shares|S|N|N|100|N|N
MBTCR|Nocturne Acquisition Corporation - Right|S|N|N|100|N|N
MBTCU|Nocturne Acquisition Corporation - Unit|S|N|N|100|N|N
MBUU|Malibu Boats, Inc. - Common Stock|G|N|N|100|N|N
MBWM|Mercantile Bank Corporation - Common Stock|Q|N|N|100|N|N
MCAA|Mountain & Co. I Acquisition Corp. - Class A Ordinary Shares|G|N|D|100|N|N
MCAAU|Mountain & Co. I Acquisition Corp. - Unit|G|N|N|100|N|N
MCAAW|Mountain & Co. I Acquisition Corp. - Warrant|G|N|N|100|N|N
MCAC|Monterey Capital Acquisition Corporation - Class A Common Stock|G|N|N|100|N|N
MCACR|Monterey Capital Acquisition Corporation - Rights|G|N|N|100|N|N
MCACU|Monterey Capital Acquisition Corporation - Unit|G|N|N|100|N|N
MCACW|Monterey Capital Acquisition Corporation - Warrants|G|N|N|100|N|N
MCAF|Mountain Crest Acquisition Corp. IV - Common Stock|S|N|N|100|N|N
MCAFR|Mountain Crest Acquisition Corp. IV - Rights|S|N|N|100|N|N
MCAFU|Mountain Crest Acquisition Corp. IV - Unit|S|N|N|100|N|N
MCAG|Mountain Crest Acquisition Corp. V - Common Stock|G|N|D|100|N|N
MCAGR|Mountain Crest Acquisition Corp. V - Right|G|N|D|100|N|N
MCAGU|Mountain Crest Acquisition Corp. V - Unit|G|N|D|100|N|N
MCBC|Macatawa Bank Corporation - Common Stock|Q|N|N|100|N|N
MCBS|MetroCity Bankshares, Inc. - Common Stock|Q|N|N|100|N|N
MCFT|MasterCraft Boat Holdings, Inc. - Common Stock|G|N|N|100|N|N
MCHI|iShares MSCI China ETF|G|N|N|100|Y|N
MCHP|Microchip Technology Incorporated - Common Stock|Q|N|N|100|N|N
MCHX|Marchex, Inc. - Class B Common Stock|Q|N|N|100|N|N
MCOM|micromobility.com Inc. - Class A Common Stock|S|N|D|100|N|N
MCOMW|micromobility.com Inc. - Warrant|S|N|D|100|N|N
MCRB|Seres Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
MCRI|Monarch Casino & Resort, Inc. - Common Stock|Q|N|N|100|N|N
MCSE|Martin Currie Sustainable International Equity ETF|G|N|N|100|Y|N
MCVT|Mill City Ventures III, Ltd. - Common Stock|S|N|N|100|N|N
MDAI|Spectral AI, Inc. - Class A Common Stock|S|N|N|100|N|N
MDAIW|Spectral AI, Inc. - Warrants|S|N|N|100|N|N
MDB|MongoDB, Inc. - Class A Common Stock|G|N|N|100|N|N
MDBH|MDB Capital Holdings, LLC - Class A common |S|N|N|100|N|N
MDCP|VictoryShares THB Mid Cap ESG ETF|G|N|N|100|Y|N
MDGL|Madrigal Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
MDGS|Medigus Ltd. - American Depositary Shares|S|N|N|100|N|N
MDIA|Mediaco Holding Inc. - Class A Common Stock|S|N|D|100|N|N
MDIV|Multi-Asset Diversified Income Index Fund|G|N|N|100|Y|N
MDJH|MDJM LTD - Ordinary Shares|S|N|N|100|N|N
MDLZ|Mondelez International, Inc. - Class A Common Stock|Q|N|N|100|N|N
MDNA|Medicenna Therapeutics Corp. - Common Shares|S|N|D|100|N|N
MDRR|Medalist Diversified REIT, Inc. - Common Stock|S|N|N|100|N|N
MDRRP|Medalist Diversified REIT, Inc. - Series A Cumulative Redeemable Preferred Stock|S|N|N|100|N|N
MDRX|Veradigm Inc. - common stock|Q|N|E|100|N|N
MDVL|MedAvail Holdings, Inc.  - Common Stock|S|N|N|100|N|N
MDWD|MediWound Ltd. - Ordinary Shares|G|N|N|100|N|N
MDWT|Midwest Holding Inc. - Common Stock|S|N|N|100|N|N
MDXG|MiMedx Group, Inc - Common Stock|S|N|N|100|N|N
MDXH|MDxHealth SA - American Depositary Shares|S|N|N|100|N|N
ME|23andMe Holding Co. - Common Stock|Q|N|N|100|N|N
MEDP|Medpace Holdings, Inc. - Common Stock|Q|N|N|100|N|N
MEDS|TRxADE HEALTH, Inc. - Common Stock|S|N|N|100|N|N
MEDX|Horizon Kinetics Medical ETF|G|N|N|100|Y|N
MEGL|Magic Empire Global Limited - Ordinary Shares|S|N|N|100|N|N
MEIP|MEI Pharma, Inc. - Common Stock|S|N|N|100|N|N
MELI|MercadoLibre, Inc. - Common Stock|Q|N|N|100|N|N
MEOH|Methanex Corporation - Common Stock|Q|N|N|100|N|N
MERC|Mercer International Inc. - Common Stock|Q|N|N|100|N|N
MESA|Mesa Air Group, Inc. - Common Stock|Q|N|N|100|N|N
MESO|Mesoblast Limited - American Depositary Shares|Q|N|N|100|N|N
META|Meta Platforms, Inc. - Class A Common Stock|Q|N|N|100|N|N
METC|Ramaco Resources, Inc. - Class A Common Stock|Q|N|N|100|N|N
METCB|Ramaco Resources, Inc. - Class B Common Stock|Q|N|N|100|N|N
METCL|Ramaco Resources, Inc. - 9.00% Senior Notes due 2026|Q|N|N|100|N|N
MF|Missfresh Limited - American Depositary Shares|S|N|D|100|N|N
MFH|Mercurity Fintech Holding Inc. - American Ordinary Shares|S|N|N|100|N|N
MFIC|MidCap Financial Investment Corporation - Closed End Fund|Q|N|N|100|N|N
MFIN|Medallion Financial Corp. - Common Stock|Q|N|N|100|N|N
MFLX|First Trust Flexible Municipal High Income ETF|G|N|N|100|Y|N
MGAM|Mobile Global Esports Inc. - Common Stock|S|N|D|100|N|N
MGEE|MGE Energy Inc. - Common Stock|Q|N|N|100|N|N
MGIC|Magic Software Enterprises Ltd. - Ordinary Shares|Q|N|N|100|N|N
MGIH|Millennium Group International Holdings Limited - Ordinary Shares|S|N|N|100|N|N
MGNI|Magnite, Inc. - Common Stock|Q|N|N|100|N|N
MGNX|MacroGenics, Inc. - Common Stock|Q|N|N|100|N|N
MGOL|MGO Global Inc. - Common Stock|S|N|N|100|N|N
MGPI|MGP Ingredients, Inc. - Common Stock|Q|N|N|100|N|N
MGRC|McGrath RentCorp - Common Stock|Q|N|N|100|N|N
MGRM|Monogram Orthopaedics Inc. - Common Stock|S|N|N|100|N|N
MGRX|Mangoceuticals, Inc. - Common Stock|S|N|N|100|N|N
MGTX|MeiraGTx Holdings plc - Ordinary Shares|Q|N|N|100|N|N
MGYR|Magyar Bancorp, Inc. - Common Stock|G|N|N|100|N|N
MHLD|Maiden Holdings, Ltd. - Common Stock|S|N|N|100|N|N
MHUA|Meihua International Medical Technologies Co., Ltd. - Ordinary Shares|G|N|N|100|N|N
MICS|The Singing Machine Company, Inc. - Common Stock|S|N|N|100|N|N
MIDD|The Middleby Corporation - Common Stock|Q|N|N|100|N|N
MIGI|Mawson Infrastructure Group Inc. - Common Stock|S|N|D|100|N|N
MILN|Global X Millennial Consumer ETF|G|N|N|100|Y|N
MIND|MIND Technology, Inc. - Common Stock|S|N|D|100|N|N
MINDP|MIND Technology, Inc. - Series A 9.00% Series A Cumulative Preferred Stock|S|N|N|100|N|N
MINM|Minim, Inc. - Common Stock|S|N|E|100|N|N
MIRA|MIRA Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
MIRM|Mirum Pharmaceuticals, Inc. - common stock|G|N|N|100|N|N
MIRO|Miromatrix Medical Inc. - Common Stock|S|N|N|100|N|N
MIST|Milestone Pharmaceuticals Inc. - Common Shares|Q|N|N|100|N|N
MITA|Coliseum Acquisition Corp. - Class A Ordinary Share|S|N|D|100|N|N
MITAU|Coliseum Acquisition Corp. - Unit|S|N|N|100|N|N
MITAW|Coliseum Acquisition Corp. - Warrant|S|N|N|100|N|N
MITK|Mitek Systems, Inc. - Common Stock|S|N|E|100|N|N
MKAM|MKAM ETF|G|N|N|100|Y|N
MKSI|MKS Instruments, Inc. - Common Stock|Q|N|N|100|N|N
MKTW|MarketWise, Inc. - Class A Common Stock|G|N|N|100|N|N
MKTX|MarketAxess Holdings, Inc. - Common Stock|Q|N|N|100|N|N
MLAB|Mesa Laboratories, Inc. - Common Stock|Q|N|N|100|N|N
MLCO|Melco Resorts & Entertainment Limited - American Depositary Shares |Q|N|N|100|N|N
MLEC|Moolec Science SA - Ordinary shares|S|N|N|100|N|N
MLECW|Moolec Science SA - Warrant|S|N|N|100|N|N
MLGO|MicroAlgo, Inc. - Ordinary Shares|S|N|N|100|N|N
MLKN|MillerKnoll, Inc. - Common Stock|Q|N|N|100|N|N
MLTX|MoonLake Immunotherapeutics - Class A Ordinary Shares|S|N|N|100|N|N
MLYS|Mineralys Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
MMAT|Meta Materials Inc. - Common Stock|S|N|D|100|N|N
MMLP|Martin Midstream Partners L.P. - Common Units Representing Limited Partnership Interests|Q|N|N|100|N|N
MMSI|Merit Medical Systems, Inc. - Common Stock|Q|N|N|100|N|N
MMV|MultiMetaVerse Holdings Limited - Class A Ordinary Share|S|N|D|100|N|N
MMVWW|MultiMetaVerse Holdings Limited - Warrant|S|N|N|100|N|N
MMYT|MakeMyTrip Limited - Ordinary Shares|Q|N|N|100|N|N
MNDO|MIND C.T.I. Ltd. - Ordinary Shares|G|N|N|100|N|N
MNDY|monday.com Ltd. - Ordinary Shares|Q|N|N|100|N|N
MNKD|MannKind Corporation - Common Stock|G|N|N|100|N|N
MNMD|Mind Medicine (MindMed) Inc. - Common Shares|Q|N|N|100|N|N
MNOV|MediciNova, Inc. - Common Stock|G|N|D|100|N|N
MNPR|Monopar Therapeutics Inc. - Common Stock|S|N|D|100|N|N
MNRO|Monro, Inc.  - Common Stock|Q|N|N|100|N|N
MNSB|MainStreet Bancshares, Inc. - Common Stock|S|N|N|100|N|N
MNSBP|MainStreet Bancshares, Inc. - Depositary Shares|S|N|N|100|N|N
MNST|Monster Beverage Corporation - Common Stock|Q|N|N|100|N|N
MNTK|Montauk Renewables, Inc. - Common Stock|S|N|N|100|N|N
MNTS|Momentus Inc. - Class A Common Stock|Q|N|N|100|N|N
MNTSW|Momentus Inc. - Warrant|Q|N|N|100|N|N
MNTX|Manitex International, Inc. - common stock|S|N|N|100|N|N
MNY|MoneyHero Limited - Class A Ordinary Shares|G|N|N|100|N|N
MNYWW|MoneyHero Limited - Warrants|G|N|N|100|N|N
MOB|Mobilicom Limited - American Depositary Shares|S|N|N|100|N|N
MOBBW|Mobilicom Limited - Warrants|S|N|N|100|N|N
MOBQ|Mobiquity Technologies, Inc. - common stock|S|N|D|100|N|N
MOBQW|Mobiquity Technologies, Inc. - warrant|S|N|D|100|N|N
MOBV|Mobiv Acquisition Corp - Class A Common Stock|G|N|N|100|N|N
MOBVU|Mobiv Acquisition Corp - Unit|G|N|N|100|N|N
MOBVW|Mobiv Acquisition Corp - Warrant|G|N|N|100|N|N
MODD|Modular Medical, Inc. - common stock|S|N|N|100|N|N
MODL|VictoryShares WestEnd U.S. Sector ETF|G|N|N|100|Y|N
MODV|ModivCare Inc. - Common Stock|Q|N|N|100|N|N
MOFG|MidWestOne Financial Group, Inc. - Common Stock|Q|N|N|100|N|N
MOGO|Mogo Inc. - Common Shares|S|N|N|100|N|N
MOLN|Molecular Partners AG - American Depositary Shares|Q|N|N|100|N|N
MOMO|Hello Group Inc.  - American Depositary Shares|Q|N|N|100|N|N
MOND|Mondee Holdings, Inc. - Class A Common Stock|G|N|N|100|N|N
MOR|MorphoSys AG - American Depositary Shares|Q|N|N|100|N|N
MORF|Morphic Holding, Inc. - Common Stock|G|N|N|100|N|N
MORN|Morningstar, Inc. - Common Stock|Q|N|N|100|N|N
MOTS|Motus GI Holdings, Inc. - Common Stock|S|N|D|100|N|N
MOVE|Movano Inc. - Common Stock|S|N|N|100|N|N
MOXC|Moxian (BVI) Inc  - Ordinary Shares|S|N|N|100|N|N
MPAA|Motorcar Parts of America, Inc. - Common Stock|Q|N|N|100|N|N
MPB|Mid Penn Bancorp - Common Stock|G|N|N|100|N|N
MPWR|Monolithic Power Systems, Inc. - Common Stock|Q|N|N|100|N|N
MQ|Marqeta, Inc. - Class A Common Stock|Q|N|N|100|N|N
MRAI|Marpai, Inc. - Class A Common Stock|S|N|D|100|N|N
MRAM|Everspin Technologies, Inc. - Common Stock|G|N|N|100|N|N
MRBK|Meridian Corporation - Common Stock|Q|N|N|100|N|N
MRCC|Monroe Capital Corporation - Closed End Fund|Q|N|N|100|N|N
MRCY|Mercury Systems Inc - Common Stock|Q|N|N|100|N|N
MREO|Mereo BioPharma Group plc - American Depositary Shares|S|N|N|100|N|N
MRIN|Marin Software Incorporated - Common Stock|G|N|D|100|N|N
MRKR|Marker Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
MRM|MEDIROM Healthcare Technologies Inc. - American Depositary Share|S|N|N|100|N|N
MRNA|Moderna, Inc. - Common Stock|Q|N|N|100|N|N
MRND|IQ U.S. Mid Cap R&D Leaders ETF|G|N|N|100|Y|N
MRNS|Marinus Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
MRSN|Mersana Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
MRTN|Marten Transport, Ltd. - Common Stock|Q|N|N|100|N|N
MRTX|Mirati Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
MRUS|Merus N.V. - Common Shares|G|N|N|100|N|N
MRVI|Maravai LifeSciences Holdings, Inc. - Class A common stock|Q|N|N|100|N|N
MRVL|Marvell Technology, Inc. - Common Stock|Q|N|N|100|N|N
MSBI|Midland States Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
MSBIP|Midland States Bancorp, Inc. - Depositary Shares Each Representing a 1/40th Interest in a Share of 7.750% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock, Series A|Q|N|N|100|N|N
MSEX|Middlesex Water Company - Common Stock|Q|N|N|100|N|N
MSFD|Direxion Daily MSFT Bear 1X Shares|G|N|N|100|Y|N
MSFT|Microsoft Corporation - Common Stock|Q|N|N|100|N|N
MSFU|Direxion Daily MSFT Bull 1.5X Shares|G|N|N|100|Y|N
MSGM|Motorsport Games Inc. - Class A Common Stock|S|N|N|100|N|N
MSS|Maison Solutions Inc. - Class A Common Stock|S|N|N|100|N|N
MSSA|Metal Sky Star Acquisition Corporation - Ordinary shares|G|N|N|100|N|N
MSSAR|Metal Sky Star Acquisition Corporation - Right|G|N|N|100|N|N
MSSAU|Metal Sky Star Acquisition Corporation - Unit|G|N|N|100|N|N
MSSAW|Metal Sky Star Acquisition Corporation - Warrant|G|N|N|100|N|N
MSTR|MicroStrategy Incorporated - Class A Common Stock|Q|N|N|100|N|N
MTC|MMTec, Inc. - Common Shares|S|N|D|100|N|N
MTCH|Match Group, Inc. - Common Stock|Q|N|N|100|N|N
MTEK|Maris-Tech Ltd. - ordinary shares|S|N|D|100|N|N
MTEKW|Maris-Tech Ltd. - Warrants|S|N|N|100|N|N
MTEM|Molecular Templates, Inc. - Common Stock|S|N|N|100|N|N
MTEX|Mannatech, Incorporated - Common Stock|Q|N|N|100|N|N
MTLS|Materialise NV - American Depositary Shares|Q|N|N|100|N|N
MTRX|Matrix Service Company - Common Stock|Q|N|N|100|N|N
MTRY|Monterey Innovation Acquisition Corp. - Common Stock|G|N|D|100|N|N
MTRYU|Monterey Innovation Acquisition Corp. - Unit|G|N|N|100|N|N
MTRYW|Monterey Innovation Acquisition Corp. - Warrant|G|N|N|100|N|N
MTSI|MACOM Technology Solutions Holdings, Inc. - Common Stock|Q|N|N|100|N|N
MTTR|Matterport, Inc. - Class A Common Stock|G|N|N|100|N|N
MU|Micron Technology, Inc. - Common Stock|Q|N|N|100|N|N
MULN|Mullen Automotive, Inc. - Common Stock|S|N|D|100|N|N
MVBF|MVB Financial Corp. - Common Stock|S|N|N|100|N|N
MVIS|MicroVision, Inc. - Common Stock|G|N|N|100|N|N
MVLA|Movella Holdings Inc. - Common Stock|G|N|D|100|N|N
MVLAW|Movella Holdings Inc. - Warrant|S|N|N|100|N|N
MVST|Microvast Holdings, Inc. - Common Stock|Q|N|N|100|N|N
MVSTW|Microvast Holdings, Inc. - Warrant|Q|N|N|100|N|N
MXCT|MaxCyte, Inc. - Common Stock|Q|N|N|100|N|N
MXL|MaxLinear, Inc - Common Stock|Q|N|N|100|N|N
MYFW|First Western Financial, Inc. - Common Stock|Q|N|N|100|N|N
MYGN|Myriad Genetics, Inc. - Common Stock|Q|N|N|100|N|N
MYMD|MyMD Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
MYNA|Mynaric AG - American Depository Shares|Q|N|N|100|N|N
MYNZ|Mainz Biomed N.V. - Ordinary Shares|S|N|N|100|N|N
MYPS|PLAYSTUDIOS, Inc.  - Class A Common Stock|G|N|N|100|N|N
MYPSW|PLAYSTUDIOS, Inc.  - Warrant|G|N|N|100|N|N
MYRG|MYR Group, Inc. - Common Stock|Q|N|N|100|N|N
MYSZ|My Size, Inc. - Common Stock|S|N|N|100|N|N
NA|Nano Labs Ltd - American Depositary Shares|G|N|N|100|N|N
NAAS|NaaS Technology Inc. - American Depositary Shares|S|N|N|100|N|N
NAII|Natural Alternatives International, Inc. - Common Stock|G|N|N|100|N|N
NAMS|NewAmsterdam Pharma Company N.V. - Ordinary Shares|G|N|N|100|N|N
NAMSW|NewAmsterdam Pharma Company N.V. - Warrant|G|N|N|100|N|N
NAOV|NanoVibronix, Inc. - Common Stock|S|N|D|100|N|N
NARI|Inari Medical, Inc. - Common Stock|Q|N|N|100|N|N
NATH|Nathan's Famous, Inc. - Common Stock|Q|N|N|100|N|N
NATR|Nature's Sunshine Products, Inc. - Common Stock|S|N|N|100|N|N
NAUT|Nautilus Biotechnology, Inc. - Common Stock|Q|N|N|100|N|N
NAVI|Navient Corporation - Common Stock|Q|N|N|100|N|N
NB|NioCorp Developments Ltd. - Common Stock|G|N|N|100|N|N
NBIX|Neurocrine Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
NBN|Northeast Bank - Common Stock|G|N|N|100|N|N
NBSE|NeuBase Therapeutics, Inc.  - Common Stock|S|N|N|100|N|N
NBST|Newbury Street Acquisition Corporation - Common Stock|S|N|N|100|N|N
NBSTU|Newbury Street Acquisition Corporation - Units|S|N|N|100|N|N
NBSTW|Newbury Street Acquisition Corporation - Warrants|S|N|N|100|N|N
NBTB|NBT Bancorp Inc. - Common Stock|Q|N|N|100|N|N
NBTX|Nanobiotix S.A. - ADSs|Q|N|N|100|N|N
NCAC|Newcourt Acquisition Corp - Class A Ordinary Share|G|N|D|100|N|N
NCACU|Newcourt Acquisition Corp - Unit|G|N|D|100|N|N
NCACW|Newcourt Acquisition Corp - Warrant|G|N|D|100|N|N
NCMI|National CineMedia, Inc. - Common Stock|Q|N|N|100|N|N
NCNA|NuCana plc - American Depositary Shares|Q|N|D|100|N|N
NCNC|noco-noco Inc. - Ordinary Share|S|N|N|100|N|N
NCNCW|noco-noco Inc. - Warrant|S|N|N|100|N|N
NCNO|nCino, Inc. - Common Stock|Q|N|N|100|N|N
NCPL|Netcapital Inc. - Common Stock|S|N|D|100|N|N
NCPLW|Netcapital Inc. - warrants|S|N|N|100|N|N
NCRA|Nocera, Inc. - common stock|S|N|D|100|N|N
NCSM|NCS Multistage Holdings, Inc. - Common Stock|S|N|N|100|N|N
NCTY|The9 Limited - American Depository Shares|S|N|D|100|N|N
NDAQ|Nasdaq, Inc. - Common Stock|Q|N|N|100|N|N
NDLS|Noodles & Company - Common Stock|Q|N|N|100|N|N
NDRA|ENDRA Life Sciences Inc. - Common Stock|S|N|N|100|N|N
NDSN|Nordson Corporation - Common Stock|Q|N|N|100|N|N
NECB|NorthEast Community Bancorp, Inc. - Common Stock|S|N|N|100|N|N
NEGG|Newegg Commerce, Inc. - Common Shares|S|N|N|100|N|N
NEO|NeoGenomics, Inc. - Common Stock|S|N|N|100|N|N
NEOG|Neogen Corporation - Common Stock|Q|N|N|100|N|N
NEON|Neonode Inc. - Common Stock|S|N|N|100|N|N
NEOV|NeoVolta Inc. - Common Stock|S|N|N|100|N|N
NEOVW|NeoVolta Inc. - Warrant|S|N|N|100|N|N
NEPH|Nephros, Inc. - Common Stock|S|N|N|100|N|N
NEPT|Neptune Wellness Solutions Inc. - Ordinary Shares|S|N|D|100|N|N
NERV|Minerva Neurosciences, Inc - Common Stock|S|N|N|100|N|N
NETD|Nabors Energy Transition Corp. II - Class A Ordinary Shares|G|N|N|100|N|N
NETDU|Nabors Energy Transition Corp. II - Unit|G|N|N|100|N|N
NETDW|Nabors Energy Transition Corp. II - Warrant|G|N|N|100|N|N
NEWT|NewtekOne, Inc. - Common Stock|G|N|N|100|N|N
NEWTI|NewtekOne, Inc. - 8.00% Fixed Rate Senior Notes due 2028|G|N|N|100|N|N
NEWTL|NewtekOne, Inc. - 5.75% Notes due 2024|G|N|N|100|N|N
NEWTZ|NewtekOne, Inc. - 5.50% Notes Due 2026|G|N|N|100|N|N
NEXI|NexImmune, Inc. - Common Stock|S|N|D|100|N|N
NEXT|NextDecade Corporation - Common Stock|S|N|N|100|N|N
NFBK|Northfield Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
NFE|New Fortress Energy Inc. - Class A Common Stock|Q|N|N|100|N|N
NFLX|Netflix, Inc. - Common Stock|Q|N|N|100|N|N
NFTG|The NFT Gaming Company, Inc. - Common Stock|S|N|D|100|N|N
NFTY|First Trust India Nifty 50 Equal Weight ETF|G|N|N|100|Y|N
NGM|NGM Biopharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
NGMS|NeoGames S.A. - Ordinary Shares|G|N|N|100|N|N
NHTC|Natural Health Trends Corp. - Commn Stock|S|N|N|100|N|N
NICE|NICE Ltd - American Depositary Shares each representing one Ordinary Share|Q|N|N|100|N|N
NICK|Nicholas Financial, Inc. - Common Stock|Q|N|N|100|N|N
NIKL|Sprott Nickel Miners ETF|G|N|N|100|Y|N
NIOBW|NioCorp Developments Ltd. - Warrant|S|N|N|100|N|N
NIR|Near Intelligence, Inc. - Common Stock|G|N|D|100|N|N
NIRWW|Near Intelligence, Inc. - Warrant|S|N|N|100|N|N
NISN|NiSun Intl Enterprise Development Group Co, Ltd - Class A Common Shares|S|N|N|100|N|N
NIU|Niu Technologies - American Depositary Shares|G|N|N|100|N|N
NKGN||G|N|N|100|N|N
NKGNW|NKGen Biotech, Inc. - Warrants|S|N|N|100|N|N
NKLA|Nikola Corporation - Common Stock|Q|N|N|100|N|N
NKSH|National Bankshares, Inc. - Common Stock|S|N|N|100|N|N
NKTR|Nektar Therapeutics - Common Stock|Q|N|D|100|N|N
NKTX|Nkarta, Inc. - Common Stock|Q|N|N|100|N|N
NLSP|NLS Pharmaceutics Ltd. - Common Shares|S|N|N|100|N|N
NLSPW|NLS Pharmaceutics Ltd. - Warrant|S|N|N|100|N|N
NLTX|Neoleukin Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
NMFC|New Mountain Finance Corporation - Common Stock|Q|N|N|100|N|N
NMIH|NMI Holdings Inc - Common Stock|G|N|N|100|N|N
NMRA|Neumora Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
NMRD|Nemaura Medical Inc. - Common Stock|S|N|D|100|N|N
NMRK|Newmark Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
NMTC|NeuroOne Medical Technologies Corporation - Common Stock|S|N|N|100|N|N
NN|NextNav Inc. - Common stock|S|N|N|100|N|N
NNAG|99 Acquisition Group Inc. - Class A Common Stock|G|N|N|100|N|N
NNAGR|99 Acquisition Group Inc. - Right|G|N|N|100|N|N
NNAGU|99 Acquisition Group Inc. - Unit|G|N|N|100|N|N
NNAGW|99 Acquisition Group Inc. - Warrant|G|N|N|100|N|N
NNAVW|NextNav Inc. - Warrant|S|N|N|100|N|N
NNBR|NN, Inc. - Common Stock|Q|N|N|100|N|N
NNDM|Nano Dimension Ltd. - American Depositary Shares|S|N|N|100|N|N
NNOX|NANO-X IMAGING LTD - Ordinary Shares|G|N|N|100|N|N
NODK|NI Holdings, Inc. - Common Stock|S|N|N|100|N|N
NOGN|Nogin, Inc. - Common Stock|G|N|D|100|N|N
NOGNW|Nogin, Inc. - Warrant|S|N|N|100|N|N
NOTV|Inotiv, Inc. - Common Stock|S|N|N|100|N|N
NOVT|Novanta Inc. - Common Shares|Q|N|N|100|N|N
NOVV|Nova Vision Acquisition Corp. - Ordinary share|S|N|D|100|N|N
NOVVR|Nova Vision Acquisition Corp. - Rights|S|N|N|100|N|N
NOVVU|Nova Vision Acquisition Corp. - Unit|S|N|N|100|N|N
NOVVW|Nova Vision Acquisition Corp. - Warrant|S|N|N|100|N|N
NPAB|New Providence Acquisition Corp. II - Class A Common Stock|G|N|N|100|N|N
NPABU|New Providence Acquisition Corp. II - Unit|G|N|N|100|N|N
NPABW|New Providence Acquisition Corp. II - Warrant|G|N|N|100|N|N
NPCE|Neuropace, Inc. - Common Stock|G|N|N|100|N|N
NRAC|Northern Revival Acquisition Corporation - Class A Ordinary share|S|N|N|100|N|N
NRACU|Northern Revival Acquisition Corporation - Unit|S|N|N|100|N|N
NRACW|Northern Revival Acquisition Corporation - Warrant|S|N|N|100|N|N
NRBO|NeuroBo Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
NRC|National Research Corporation - Common Stock|Q|N|N|100|N|N
NRDS|NerdWallet, Inc. - Class A Common Stock|G|N|N|100|N|N
NRIM|Northrim BanCorp Inc - Common Stock|Q|N|N|100|N|N
NRIX|Nurix Therapeutics, Inc. - Common stock|G|N|N|100|N|N
NRSN|NeuroSense Therapeutics Ltd. - Ordinary Shares|S|N|D|100|N|N
NRSNW|NeuroSense Therapeutics Ltd. - Warrant|S|N|N|100|N|N
NRXP|NRX Pharmaceuticals, Inc. - Common Stock|G|N|D|100|N|N
NRXPW|NRX Pharmaceuticals, Inc. - Warrant|G|N|D|100|N|N
NSIT|Insight Enterprises, Inc. - Common Stock|Q|N|N|100|N|N
NSPR|InspireMD Inc. - Common Stock|S|N|N|100|N|N
NSSC|NAPCO Security Technologies, Inc. - Common Stock|Q|N|N|100|N|N
NSTG|NanoString Technologies, Inc. - Common Stock|G|N|N|100|N|N
NSTS|NSTS Bancorp, Inc. - Common Stock|S|N|N|100|N|N
NSYS|Nortech Systems Incorporated - Common Stock|S|N|N|100|N|N
NTAP|NetApp, Inc. - Common Stock|Q|N|N|100|N|N
NTBL|Notable Labs, Inc. - Ordinary Shares|S|N|D|100|N|N
NTCT|NetScout Systems, Inc. - Common Stock|Q|N|N|100|N|N
NTES|NetEase, Inc. - American Depositary Shares, each representing 5 ordinary shares|Q|N|N|100|N|N
NTGR|NETGEAR, Inc. - Common Stock|Q|N|N|100|N|N
NTIC|Northern Technologies International Corporation - Common Stock|G|N|N|100|N|N
NTLA|Intellia Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
NTNX|Nutanix, Inc. - Class A Common Stock|Q|N|N|100|N|N
NTRA|Natera, Inc. - Common Stock|Q|N|N|100|N|N
NTRB|Nutriband Inc. - Common Stock|S|N|N|100|N|N
NTRBW|Nutriband Inc. - Warrant|S|N|N|100|N|N
NTRS|Northern Trust Corporation - Common Stock|Q|N|N|100|N|N
NTRSO|Northern Trust Corporation - Depositary Shares Each Representing a 1/1,000th Interest in a Share of Series E Non-Cumulative Perpetual Preferred Stock|Q|N|N|100|N|N
NTWK|NETSOL Technologies Inc. - Common Stock|S|N|N|100|N|N
NTZG|Nuveen Global Net Zero Transition ETF|G|N|N|100|Y|N
NUBI|Nubia Brand International Corp. - Class A Common Stock|G|N|D|100|N|N
NUBIU|Nubia Brand International Corp. - Unit|G|N|D|100|N|N
NUBIW|Nubia Brand International Corp. - Warrant|G|N|D|100|N|N
NURO|NeuroMetrix, Inc. - Common Stock|S|N|D|100|N|N
NUTX|Nutex Health Inc. - Common Stock|S|N|D|100|N|N
NUVL|Nuvalent, Inc. - Class A Common Stock|Q|N|N|100|N|N
NUWE|Nuwellis, Inc. - Common Stock|S|N|N|100|N|N
NUZE|NuZee, Inc. - Common Stock|S|N|N|100|N|N
NVAC|NorthView Acquisition Corporation - Common Stock|G|N|N|100|N|N
NVACR|NorthView Acquisition Corporation - Rights|G|N|N|100|N|N
NVACW|NorthView Acquisition Corporation - Warrant|G|N|N|100|N|N
NVAX|Novavax, Inc. - Common Stock|Q|N|N|100|N|N
NVCR|NovoCure Limited - Ordinary Shares|Q|N|N|100|N|N
NVCT|Nuvectis Pharma, Inc. - Common Stock|S|N|N|100|N|N
NVD|GraniteShares 1.5x Short NVDA Daily ETF|G|N|N|100|Y|N
NVDA|NVIDIA Corporation - Common Stock|Q|N|N|100|N|N
NVDD|Direxion Daily NVDA Bear 1X Shares|G|N|N|100|Y|N
NVDL|GraniteShares 1.5x Long NVDA Daily ETF|G|N|N|100|Y|N
NVDS|AXS 1.25X NVDA Bear Daily ETF|G|N|N|100|Y|N
NVDU|Direxion Daily NVDA Bull 1.5X Shares|G|N|N|100|Y|N
NVEC|NVE Corporation - Common Stock|S|N|N|100|N|N
NVEE|NV5 Global, Inc. - Common Stock|Q|N|N|100|N|N
NVEI|Nuvei Corporation - Subordinate Voting Shares|Q|N|N|100|N|N
NVFY|Nova Lifestyle, Inc - Common Stock|S|N|N|100|N|N
NVIV|InVivo Therapeutics Holdings Corp. - Common Stock|S|N|N|100|N|N
NVMI|Nova Ltd. - Ordinary Shares|Q|N|N|100|N|N
NVNI|Nvni Group Limited - Ordinary Shares|S|N|N|100|N|N
NVNIW|Nvni Group Limited - Warrants|S|N|N|100|N|N
NVNO|enVVeno Medical Corporation - Common Stock|S|N|N|100|N|N
NVOS|Novo Integrated Sciences, Inc. - Common Stock|S|N|D|100|N|N
NVTS|Navitas Semiconductor Corporation - Common Stock|G|N|N|100|N|N
NVVE|Nuvve Holding Corp. - Common Stock|S|N|D|100|N|N
NVVEW|Nuvve Holding Corp. - Warrant|S|N|N|100|N|N
NVX|NOVONIX Limited - American Depository Shares|G|N|N|100|N|N
NWBI|Northwest Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
NWE|NorthWestern Energy Group, Inc.  - Common Stock|Q|N|N|100|N|N
NWFL|Norwood Financial Corp. - Common Stock|G|N|N|100|N|N
NWGL|Nature Wood Group Limited - American Depositary Shares|S|N|N|100|N|N
NWL|Newell Brands Inc. - Common Stock|Q|N|N|100|N|N
NWLI|National Western Life Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
NWPX|Northwest Pipe Company - Common Stock|Q|N|N|100|N|N
NWS|News Corporation - Class B Common Stock|Q|N|N|100|N|N
NWSA|News Corporation - Class A Common Stock|Q|N|N|100|N|N
NWTN|NWTN Inc. - Class B Ordinary Shares|S|N|N|100|N|N
NWTNW|NWTN Inc. - Warrant|S|N|N|100|N|N
NXGL|NexGel, Inc - Common Stock|S|N|N|100|N|N
NXGLW|NexGel, Inc - Warrant|S|N|N|100|N|N
NXGN|NextGen Healthcare, Inc. - Common Stock|Q|N|N|100|N|N
NXL|Nexalin Technology, Inc. - Common Stock|S|N|D|100|N|N
NXLIW|Nexalin Technology, Inc. - Warrant|S|N|N|100|N|N
NXPI|NXP Semiconductors N.V. - Common Stock|Q|N|N|100|N|N
NXPL|NextPlat Corp - Common Stock|S|N|N|100|N|N
NXPLW|NextPlat Corp - Warrants|S|N|N|100|N|N
NXST|Nexstar Media Group, Inc. - Common Stock|Q|N|N|100|N|N
NXT|Nextracker Inc. - Class A Common Stock|Q|N|N|100|N|N
NXTC|NextCure, Inc. - Common Stock|Q|N|N|100|N|N
NXTG|First Trust Indxx NextG ETF|G|N|N|100|Y|N
NXTP|NextPlay Technologies, Inc. - Common Stock|S|N|E|100|N|N
NXU|Nxu, Inc.  - Class A Common Stock|S|N|D|100|N|N
NYAX|Nayax Ltd. - Ordinary Shares|Q|N|N|100|N|N
NYMT|New York Mortgage Trust, Inc. - Common Stock|Q|N|N|100|N|N
NYMTL|New York Mortgage Trust, Inc. - 6.875% Series F Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock, $0.01 par value per share|Q|N|N|100|N|N
NYMTM|New York Mortgage Trust, Inc. - 7.875% Series E Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
NYMTN|New York Mortgage Trust, Inc. - 8.00% Series D Fixed-to-Floating Rate Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
NYMTZ|New York Mortgage Trust, Inc. - 7.000% Series G Cumulative Redeemable Preferred Stock, $0.01 par value per share|Q|N|N|100|N|N
NYXH|Nyxoah SA - Ordinary Shares|G|N|N|100|N|N
NZAC|SPDR MSCI ACWI Climate Paris Aligned ETF|G|N|N|100|Y|N
NZUS|SPDR MSCI USA Climate Paris Aligned ETF|G|N|N|100|Y|N
OABI|OmniAb, Inc. - Common Stock|G|N|N|100|N|N
OABIW|OmniAb, Inc. - Warrant|S|N|N|100|N|N
OAKU|Oak Woods Acquisition Corporation - Class A Ordinary Shares|S|N|N|100|N|N
OAKUR|Oak Woods Acquisition Corporation - Right|S|N|N|100|N|N
OAKUU|Oak Woods Acquisition Corporation - Unit|S|N|N|100|N|N
OAKUW|Oak Woods Acquisition Corporation - Warrant|S|N|N|100|N|N
OB|Outbrain Inc. - Common Stock|Q|N|N|100|N|N
OBIL|US Treasury 12 Month Bill ETF|G|N|N|100|Y|N
OBIO|Orchestra BioMed Holdings, Inc. - Ordinary Shares|G|N|N|100|N|N
OBLG|Oblong Inc. - Common Stock|S|N|D|100|N|N
OBT|Orange County Bancorp, Inc. - Common Stock|S|N|N|100|N|N
OCAX|OCA Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
OCAXU|OCA Acquisition Corp. - Unit|S|N|N|100|N|N
OCAXW|OCA Acquisition Corp. - Warrant|S|N|N|100|N|N
OCC|Optical Cable Corporation - Common Stock|G|N|N|100|N|N
OCCI|OFS Credit Company, Inc. - Closed End Fund|S|N|N|100|N|N
OCCIN|OFS Credit Company, Inc. - 5.25% Series E Term Preferred Stock Due 2026|S|N|N|100|N|N
OCCIO|OFS Credit Company, Inc. - 6.125% Series C Term Preferred Stock|S|N|N|100|N|N
OCEA|Ocean Biomedical, Inc. - Common Stock|S|N|N|100|N|N
OCEAW|Ocean Biomedical, Inc. - Warrants|S|N|N|100|N|N
OCFC|OceanFirst Financial Corp. - Common Stock|Q|N|N|100|N|N
OCFCP|OceanFirst Financial Corp. - Depositary Shares|Q|N|N|100|N|N
OCG|Oriental Culture Holding LTD - Ordinary Shares|S|N|D|100|N|N
OCGN|Ocugen, Inc. - Common Stock|S|N|D|100|N|N
OCS|Oculis Holding AG - Ordinary shares|G|N|N|100|N|N
OCSAW|Oculis Holding AG - Warrants|G|N|N|100|N|N
OCSL|Oaktree Specialty Lending Corporation - Closed End Fund|Q|N|N|100|N|N
OCTO|Eightco Holdings Inc. - Common Stock|S|N|D|100|N|N
OCUL|Ocular Therapeutix, Inc. - Common Stock|G|N|N|100|N|N
OCUP|Ocuphire Pharma, Inc. - Common Stock|S|N|N|100|N|N
OCX|Oncocyte Corporation - Common Stock|S|N|N|100|N|N
ODD|ODDITY Tech Ltd. - Class A Ordinary Shares|G|N|N|100|N|N
ODDS|Pacer BlueStar Digital Entertainment ETF|G|N|N|100|Y|N
ODFL|Old Dominion Freight Line, Inc. - Common Stock|Q|N|N|100|N|N
ODP|The ODP Corporation - Common Stock|Q|N|N|100|N|N
ODVWW|Osisko Development Corp. - Warrant|S|N|N|100|N|N
OESX|Orion Energy Systems, Inc. - Common Stock|S|N|N|100|N|N
OFIX|Orthofix Medical Inc.  - Common Stock|Q|N|N|100|N|N
OFLX|Omega Flex, Inc. - Common Stock|G|N|N|100|N|N
OFS|OFS Capital Corporation - Closed End Fund|Q|N|N|100|N|N
OFSSH|OFS Capital Corporation - 4.95% Notes due 2028|Q|N|N|100|N|N
OGI|Organigram Holdings Inc. - Common Shares|Q|N|N|100|N|N
OHAA|OPY Acquisition Corp. I - Class A Common Stock|G|N|D|100|N|N
OHAAU|OPY Acquisition Corp. I - Units|G|N|N|100|N|N
OHAAW|OPY Acquisition Corp. I - Warrant|G|N|N|100|N|N
OKTA|Okta, Inc. - Class A Common Stock|Q|N|N|100|N|N
OKYO|OKYO Pharma Limited - Ordinary Shares|S|N|N|100|N|N
OLB|The OLB Group, Inc. - Common Stock|S|N|D|100|N|N
OLED|Universal Display Corporation - Common Stock|Q|N|N|100|N|N
OLIT|OmniLit Acquisition Corp. - Class A Common Stock|G|N|D|100|N|N
OLITU|OmniLit Acquisition Corp. - Units|G|N|D|100|N|N
OLITW|OmniLit Acquisition Corp. - Warrants.|G|N|D|100|N|N
OLK|Olink Holding AB (publ) - American Depositary Shares|G|N|N|100|N|N
OLLI|Ollie's Bargain Outlet Holdings, Inc. - Common Stock|G|N|N|100|N|N
OLMA|Olema Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
OLPX|Olaplex Holdings, Inc. - Common Stock|Q|N|N|100|N|N
OM|Outset Medical, Inc. - Common Stock|Q|N|N|100|N|N
OMAB|Grupo Aeroportuario del Centro Norte S.A.B. de C.V. - American Depositary Shares each representing 8 Series B shares|Q|N|N|100|N|N
OMCL|Omnicell, Inc. - Common Stock|Q|N|N|100|N|N
OMER|Omeros Corporation - Common Stock|G|N|N|100|N|N
OMEX|Odyssey Marine Exploration, Inc. - Common Stock|S|N|N|100|N|N
OMGA|Omega Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
OMH|Ohmyhome Limited - Ordinary Shares|S|N|N|100|N|N
OMIC|Singular Genomics Systems, Inc. - Common Stock|Q|N|D|100|N|N
OMQS|OMNIQ Corp. - Common Stock|S|N|D|100|N|N
ON|ON Semiconductor Corporation - Common Stock|Q|N|N|100|N|N
ONB|Old National Bancorp - Common Stock|Q|N|N|100|N|N
ONBPO|Old National Bancorp - Depositary Shares, Each Representing a 1/40th Interest in a Share of Series C Preferred Stock|Q|N|N|100|N|N
ONBPP|Old National Bancorp - Depositary Shares, Each Representing a 1/40th Interest in a Share of Series A Preferred Stock|Q|N|N|100|N|N
ONCT|Oncternal Therapeutics, Inc.  - Common Stock|S|N|D|100|N|N
ONCY|Oncolytics Biotech Inc. - Common Shares|S|N|N|100|N|N
ONDS|Ondas Holdings Inc. - Common Stock|S|N|D|100|N|N
ONEQ|Fidelity Nasdaq Composite Index ETF|G|N|N|100|Y|N
ONEW|OneWater Marine Inc. - Class A Common Stock|G|N|N|100|N|N
ONFO|Onfolio Holdings Inc. - Common Stock|S|N|N|100|N|N
ONFOW|Onfolio Holdings Inc. - Warrant|S|N|N|100|N|N
ONTX|Onconova Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
ONVO|Organovo Holdings, Inc. - Common Stock|S|N|N|100|N|N
ONYX|Onyx Acquisition Co. I - Class A Ordinary Shares|G|N|N|100|N|N
ONYXU|Onyx Acquisition Co. I - Unit|G|N|N|100|N|N
ONYXW|Onyx Acquisition Co. I - Warrant|G|N|N|100|N|N
OP|OceanPal Inc. - Common Stock|S|N|N|100|N|N
OPAL|OPAL Fuels Inc. - Class A Common Stock|S|N|N|100|N|N
OPBK|OP Bancorp - Common Stock|G|N|N|100|N|N
OPCH|Option Care Health, Inc. - Common Stock|Q|N|N|100|N|N
OPEN|Opendoor Technologies Inc  - Common Stock|Q|N|N|100|N|N
OPGN|OpGen, Inc. - Common Stock|S|N|D|100|N|N
OPHC|OptimumBank Holdings, Inc. - Common Stock|S|N|N|100|N|N
OPI|Office Properties Income Trust - Common Shares of Beneficial Interest|Q|N|N|100|N|N
OPINL|Office Properties Income Trust - 6.375% Senior Notes due 2050|G|N|N|100|N|N
OPK|Opko Health, Inc. - Common Stock|Q|N|N|100|N|N
OPOF|Old Point Financial Corporation - Common Stock|S|N|N|100|N|N
OPRA|Opera Limited - American Depositary Shares|Q|N|N|100|N|N
OPRT|Oportun Financial Corporation - common stock|Q|N|N|100|N|N
OPRX|OptimizeRx Corporation - Common Stock|S|N|N|100|N|N
OPT|Opthea Limited - American Depositary Shares|Q|N|N|100|N|N
OPTN|OptiNose, Inc. - Common Stock|Q|N|N|100|N|N
OPXS|Optex Systems Holdings, Inc. - Common Stock|S|N|N|100|N|N
ORGN|Origin Materials, Inc. - Class A Common Stock|S|N|N|100|N|N
ORGNW|Origin Materials, Inc. - Warrant|S|N|N|100|N|N
ORGO|Organogenesis Holdings Inc.  - Class A |S|N|N|100|N|N
ORGS|Orgenesis Inc. - Common Stock|S|N|D|100|N|N
ORIC|Oric Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
ORLY|O'Reilly Automotive, Inc. - Common Stock|Q|N|N|100|N|N
ORMP|Oramed Pharmaceuticals Inc. - Common Stock|S|N|N|100|N|N
ORRF|Orrstown Financial Services Inc - Common Stock|S|N|N|100|N|N
ORTX|Orchard Therapeutics plc - American Depositary Shares|S|N|N|100|N|N
OSA|ProSomnus, Inc. - Common Stock|G|N|D|100|N|N
OSAAW|ProSomnus, Inc. - Warrant|S|N|N|100|N|N
OSBC|Old Second Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
OSIS|OSI Systems, Inc. - Common Stock|Q|N|N|100|N|N
OSPN|OneSpan Inc. - Common Stock|S|N|N|100|N|N
OSS|One Stop Systems, Inc. - Common Stock|S|N|N|100|N|N
OST|Ostin Technology Group Co., Ltd. - Ordinary Shares|S|N|N|100|N|N
OSTK|Overstock.com, Inc. - Common Stock|G|N|N|100|N|N
OSUR|OraSure Technologies, Inc. - Common Stock|Q|N|N|100|N|N
OSW|OneSpaWorld Holdings Limited - Common Shares|S|N|N|100|N|N
OTEC|OceanTech Acquisitions I Corp. - Class A Common Stock|S|N|N|100|N|N
OTECU|OceanTech Acquisitions I Corp. - Units|S|N|N|100|N|N
OTECW|OceanTech Acquisitions I Corp. - Warrant|S|N|N|100|N|N
OTEX|Open Text Corporation - Common Shares|Q|N|N|100|N|N
OTLK|Outlook Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
OTLY|Oatly Group AB - American Depositary Shares|Q|N|N|100|N|N
OTMO|Otonomo Technologies Ltd. - Ordinary shares|S|N|N|100|N|N
OTRK|Ontrak, Inc. - Common Stock|S|N|D|100|N|N
OTRKP|Ontrak, Inc. - 9.50% Series A Cumulative Perpetual Preferred Stock|S|N|D|100|N|N
OTTR|Otter Tail Corporation - Common Stock|Q|N|N|100|N|N
OVBC|Ohio Valley Banc Corp. - Common Stock|G|N|N|100|N|N
OVID|Ovid Therapeutics Inc. - Common Stock|Q|N|N|100|N|N
OVLY|Oak Valley Bancorp (CA) - Common Stock|S|N|N|100|N|N
OXBR|Oxbridge Re Holdings Limited - Ordinary Shares|S|N|N|100|N|N
OXBRW|Oxbridge Re Holdings Limited - Warrant|S|N|N|100|N|N
OXLC|Oxford Lane Capital Corp. - Closed End Fund|Q|N|N|100|N|N
OXLCL|Oxford Lane Capital Corp. - 6.75% Notes due 2031|Q|N|N|100|N|N
OXLCM|Oxford Lane Capital Corp. - 6.75% Series 2024 Term Preferred Stock|Q|N|N|100|N|N
OXLCN|Oxford Lane Capital Corp. - 7.125% Series 2029 Term Preferred Stock|Q|N|N|100|N|N
OXLCO|Oxford Lane Capital Corp. - Preferred Stock Shares, 6.00% Series 2029|Q|N|N|100|N|N
OXLCP|Oxford Lane Capital Corp. - 6.25% Series 2027 Term Preferred Shares|Q|N|N|100|N|N
OXLCZ|Oxford Lane Capital Corp. - 5.00% Notes due 2027|Q|N|N|100|N|N
OXSQ|Oxford Square Capital Corp. - Closed End Fund|Q|N|N|100|N|N
OXSQG|Oxford Square Capital Corp. - 5.50% Notes due 2028|Q|N|N|100|N|N
OXSQL|Oxford Square Capital Corp. - 6.50% Notes due 2024|Q|N|N|100|N|N
OXSQZ|Oxford Square Capital Corp. - 6.25% Notes due 2026|Q|N|N|100|N|N
OXUS|Oxus Acquisition Corp. - Class A Ordinary Shares|S|N|D|100|N|N
OXUSU|Oxus Acquisition Corp. - Unit|S|N|N|100|N|N
OXUSW|Oxus Acquisition Corp. - Warrant|S|N|N|100|N|N
OZK|Bank OZK - Common Stock|Q|N|N|100|N|N
OZKAP|Bank OZK - 4.625% Series A Non-Cumulative Perpetual Preferred Stock|Q|N|N|100|N|N
PAA|Plains All American Pipeline, L.P. - Common Units representing Limited Partner Interests|Q|N|N|100|N|N
PABU|iShares Paris-Aligned Climate MSCI USA ETF|G|N|N|100|Y|N
PACB|Pacific Biosciences of California, Inc. - Common Stock|Q|N|N|100|N|N
PACW|PacWest Bancorp - Common Stock|Q|N|N|100|N|N
PACWP|PacWest Bancorp - Depositary Shares Each Representing a 1/40th Interest in a Share of 7.75% Fixed Rate Non-Cumulative Perpetual Preferred Stock, Series A|Q|N|N|100|N|N
PAGP|Plains GP Holdings, L.P. - Class A Shares representing limited partner interests|Q|N|N|100|N|N
PAHC|Phibro Animal Health Corporation - Class A Common Stock|G|N|N|100|N|N
PALI|Palisade Bio, Inc. - Common Stock|S|N|N|100|N|N
PALT|Paltalk, Inc. - Common Stock|S|N|N|100|N|N
PANL|Pangaea Logistics Solutions Ltd. - Common Stock|S|N|N|100|N|N
PANW|Palo Alto Networks, Inc. - Common Stock|Q|N|N|100|N|N
PARA|Paramount Global - Class B Common Stock|Q|N|N|100|N|N
PARAA|Paramount Global - Class A Common Stock|Q|N|N|100|N|N
PARAP|Paramount Global - 5.75% Series A Mandatory Convertible Preferred Stock|Q|N|N|100|N|N
PASG|Passage Bio, Inc. - Common Stock|Q|N|D|100|N|N
PATI|Patriot Transportation Holding, Inc. - Common Stock|Q|N|N|100|N|N
PATK|Patrick Industries, Inc. - Common Stock|Q|N|N|100|N|N
PAVM|PAVmed Inc. - Common Stock|S|N|D|100|N|N
PAVMZ|PAVmed Inc. - Series Z Warrant|S|N|N|100|N|N
PAVS|Paranovus Entertainment Technology Ltd. - Class A Ordinary Shares|S|N|N|100|N|N
PAX|Patria Investments Limited - Class A Common Shares|Q|N|N|100|N|N
PAYO|Payoneer Global Inc. - Common Stock|G|N|N|100|N|N
PAYOW|Payoneer Global Inc. - Warrant|G|N|N|100|N|N
PAYS|Paysign, Inc. - Common Stock|S|N|N|100|N|N
PAYX|Paychex, Inc. - Common Stock|Q|N|N|100|N|N
PBAX|Phoenix Biotech Acquisition Corp. - Class A Common Stock|G|N|D|100|N|N
PBAXU|Phoenix Biotech Acquisition Corp. - Unit|G|N|D|100|N|N
PBAXW|Phoenix Biotech Acquisition Corp. - Warrants|G|N|D|100|N|N
PBBK|PB Bankshares, Inc. - Common Stock|S|N|N|100|N|N
PBFS|Pioneer Bancorp, Inc. - Common Stock|S|N|N|100|N|N
PBHC|Pathfinder Bancorp, Inc. - Common Stock|S|N|N|100|N|N
PBLA|Panbela Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
PBPB|Potbelly Corporation - Common Stock|Q|N|N|100|N|N
PBTS|Powerbridge Technologies Co., Ltd. - Ordinary Shares|S|N|N|100|N|N
PBYI|Puma Biotechnology Inc - Common Stock|Q|N|N|100|N|N
PCAR|PACCAR Inc. - Common Stock|Q|N|N|100|N|N
PCB|PCB Bancorp - Common Stock|Q|N|N|100|N|N
PCCT|Perception Capital Corp. II - Class A Ordinary Shares|G|N|D|100|N|N
PCCTU|Perception Capital Corp. II - Units|G|N|D|100|N|N
PCCTW|Perception Capital Corp. II - Warrants|G|N|D|100|N|N
PCH|PotlatchDeltic Corporation - Common Stock|Q|N|N|100|N|N
PCRX|Pacira BioSciences, Inc. - Common Stock|Q|N|N|100|N|N
PCSA|Processa Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
PCT|PureCycle Technologies, Inc. - Common stock|S|N|N|100|N|N
PCTI|PCTEL, Inc. - Common Stock|Q|N|N|100|N|N
PCTTU|PureCycle Technologies, Inc. - Unit|S|N|N|100|N|N
PCTTW|PureCycle Technologies, Inc. - Warrant|S|N|N|100|N|N
PCTY|Paylocity Holding Corporation - Common Stock|Q|N|N|100|N|N
PCVX|Vaxcyte, Inc. - Common Stock|Q|N|N|100|N|N
PCYG|Park City Group, Inc. - Common Stock|S|N|N|100|N|N
PCYO|Pure Cycle Corporation - Common Stock|S|N|N|100|N|N
PDBA|Invesco Agriculture Commodity Strategy No K-1 ETF|G|N|N|100|Y|N
PDBC|Invesco Optimum Yield Diversified Commodity Strategy No K-1 ETF|G|N|N|100|Y|N
PDCO|Patterson Companies, Inc. - Common Stock|Q|N|N|100|N|N
PDD|PDD Holdings Inc. - American Depositary Shares|Q|N|N|100|N|N
PDEX|Pro-Dex, Inc. - Common Stock|S|N|N|100|N|N
PDFS|PDF Solutions, Inc. - Common Stock|Q|N|N|100|N|N
PDLB|Ponce Financial Group, Inc. - Common Stock|G|N|N|100|N|N
PDP|Invesco Dorsey Wright Momentum ETF|G|N|N|100|Y|N
PDSB|PDS Biotechnology Corporation - Common Stock|S|N|N|100|N|N
PEBK|Peoples Bancorp of North Carolina, Inc. - Common Stock|G|N|N|100|N|N
PEBO|Peoples Bancorp Inc. - Common Stock|Q|N|N|100|N|N
PECO|Phillips Edison & Company, Inc. - Common Stock|Q|N|N|100|N|N
PEGA|Pegasystems Inc. - Common Stock|Q|N|N|100|N|N
PEGR|Project Energy Reimagined Acquisition Corp. - Class A Ordinary Share|G|N|H|100|N|N
PEGRU|Project Energy Reimagined Acquisition Corp. - Unit|G|N|E|100|N|N
PEGRW|Project Energy Reimagined Acquisition Corp. - Warrant|G|N|E|100|N|N
PEGY|Pineapple Energy Inc. - Common Stock|S|N|N|100|N|N
PENN|PENN Entertainment, Inc. - Common Stock|Q|N|N|100|N|N
PEP|PepsiCo, Inc. - Common Stock|Q|N|N|100|N|N
PEPG|PepGen Inc. - Common Stock|Q|N|N|100|N|N
PEPL|PepperLime Health Acquisition Corporation - Class A Ordinary Share|G|N|D|100|N|N
PEPLU|PepperLime Health Acquisition Corporation - Unit|G|N|D|100|N|N
PEPLW|PepperLime Health Acquisition Corporation - Warrrant|G|N|D|100|N|N
PERI|Perion Network Ltd - Ordinary Shares|Q|N|N|100|N|N
PESI|Perma-Fix Environmental Services, Inc. - Common Stock|S|N|N|100|N|N
PET|Wag! Group Co. - Common Stock|G|N|N|100|N|N
PETQ|PetIQ, Inc. - Class A Common Stock|Q|N|N|100|N|N
PETS|PetMed Express, Inc. - Common Stock|Q|N|N|100|N|N
PETV|PetVivo Holdings, Inc. - Common Stock|S|N|N|100|N|N
PETVW|PetVivo Holdings, Inc. - Warrant|S|N|N|100|N|N
PETWW|Wag! Group Co. - Warrant|G|N|N|100|N|N
PETZ|TDH Holdings, Inc. - Common Shares|S|N|N|100|N|N
PEV|Phoenix Motor Inc. - Common Stock|S|N|D|100|N|N
PEY|Invesco High Yield Equity Dividend Achievers ETF|G|N|N|100|Y|N
PEZ|Invesco Dorsey Wright Consumer Cyclicals Momentum ETF|G|N|N|100|Y|N
PFBC|Preferred Bank - Common Stock|Q|N|N|100|N|N
PFC|Premier Financial Corp.  - Common Stock|Q|N|N|100|N|N
PFF|iShares Preferred and Income Securities ETF|G|N|N|100|Y|N
PFG|Principal Financial Group Inc - Common Stock|Q|N|N|100|N|N
PFI|Invesco Dorsey Wright Financial Momentum ETF|G|N|N|100|Y|N
PFIE|Profire Energy, Inc. - Common Stock|S|N|N|100|N|N
PFIN|P & F Industries, Inc. - Class A Common Stock|G|N|N|100|N|N
PFIS|Peoples Financial Services Corp.  - Common Stock|Q|N|N|100|N|N
PFM|Invesco Dividend Achievers ETF|G|N|N|100|Y|N
PFMT|Performant Financial Corporation - Common Stock|Q|N|N|100|N|N
PFSW|PFSweb, Inc. - Common Stock|S|N|N|100|N|N
PFTA|Perception Capital Corp. III - Class A Ordinary Share|S|N|N|100|N|N
PFTAU|Perception Capital Corp. III - Unit|S|N|N|100|N|N
PFTAW|Perception Capital Corp. III - Warrant|S|N|N|100|N|N
PFX|PhenixFIN Corporation  - Common Stock|G|N|N|100|N|N
PFXNZ|PhenixFIN Corporation  - 5.25% Notes due 2028|G|N|N|100|N|N
PGC|Peapack-Gladstone Financial Corporation - Common Stock|Q|N|N|100|N|N
PGEN|Precigen, Inc. - Common Stock|Q|N|N|100|N|N
PGJ|Invesco Golden Dragon China ETF|G|N|N|100|Y|N
PGNY|Progyny, Inc. - Common Stock|Q|N|N|100|N|N
PGY|Pagaya Technologies Ltd. - Class A Ordinary Shares|S|N|N|100|N|N
PGYWW|Pagaya Technologies Ltd. - Warrants|S|N|N|100|N|N
PHAR|Pharming Group N.V. - ADS, each representing 10 ordinary shares|G|N|N|100|N|N
PHAT|Phathom Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
PHIO|Phio Pharmaceuticals Corp. - Common Stock|S|N|N|100|N|N
PHO|Invesco Water Resources ETF|G|N|N|100|Y|N
PHUN|Phunware, Inc. - Common Stock|S|N|D|100|N|N
PHUNW|Phunware, Inc. - Warrants|S|N|N|100|N|N
PHVS|Pharvaris N.V. - Ordinary Shares|Q|N|N|100|N|N
PHXM|PHAXIAM Therapeutics S.A. - American Depositary Shares|S|N|N|100|N|N
PI|Impinj, Inc. - Common Stock|Q|N|N|100|N|N
PID|Invesco International Dividend Achievers ETF|G|N|N|100|Y|N
PIE|Invesco Dorsey Wright Emerging Markets Momentum ETF|G|N|N|100|Y|N
PIII|P3 Health Partners Inc. - Class A Common Stock|S|N|N|100|N|N
PIIIW|P3 Health Partners Inc. - Warrant|S|N|N|100|N|N
PIK|Kidpik Corp. - Common Stock|S|N|D|100|N|N
PINC|Premier, Inc. - Class A Common Stock|Q|N|N|100|N|N
PIO|Invesco Global Water ETF|G|N|N|100|Y|N
PIRS|Pieris Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
PIXY|ShiftPixy, Inc. - Common Stock|S|N|D|100|N|N
PIZ|Invesco Dorsey Wright Developed Markets Momentum ETF|G|N|N|100|Y|N
PKBK|Parke Bancorp, Inc. - Common Stock|S|N|N|100|N|N
PKOH|Park-Ohio Holdings Corp. - Common Stock|Q|N|N|100|N|N
PKW|Invesco BuyBack Achievers ETF|G|N|N|100|Y|N
PLAB|Photronics, Inc. - Common Stock|Q|N|N|100|N|N
PLAO|Patria Latin American Opportunity Acquisition Corp. - Class A Ordinary Shares|G|N|N|100|N|N
PLAOU|Patria Latin American Opportunity Acquisition Corp. - Unit|G|N|N|100|N|N
PLAOW|Patria Latin American Opportunity Acquisition Corp. - Warrant|G|N|D|100|N|N
PLAY|Dave & Buster's Entertainment, Inc. - Common Stock|Q|N|N|100|N|N
PLBC|Plumas Bancorp - Common Stock|S|N|N|100|N|N
PLBY|PLBY Group, Inc.  - Common Stock|G|N|N|100|N|N
PLCE|Children's Place, Inc. (The) - Common Stock|Q|N|N|100|N|N
PLL|Piedmont Lithium Inc.   - Common Stock|S|N|N|100|N|N
PLMI|Plum Acquisition Corp. I - Class A Ordinary Share|S|N|N|100|N|N
PLMIU|Plum Acquisition Corp. I - Units|S|N|N|100|N|N
PLMIW|Plum Acquisition Corp. I - Warrant|S|N|N|100|N|N
PLMR|Palomar Holdings, Inc. - Common stock|Q|N|N|100|N|N
PLPC|Preformed Line Products Company - Common Stock|Q|N|N|100|N|N
PLRX|Pliant Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
PLSE|Pulse Biosciences, Inc - Common Stock|S|N|N|100|N|N
PLTK|Playtika Holding Corp. - Common Stock|Q|N|N|100|N|N
PLTN|Plutonian Acquisition Corp. - Common Stock|S|N|N|100|N|N
PLTNR|Plutonian Acquisition Corp. - Rights|S|N|N|100|N|N
PLTNU|Plutonian Acquisition Corp. - Unit|S|N|N|100|N|N
PLTNW|Plutonian Acquisition Corp. - Warrant|S|N|N|100|N|N
PLUG|Plug Power, Inc. - Common Stock|S|N|N|100|N|N
PLUR|Pluri Inc. - Common Stock|G|N|D|100|N|N
PLUS|ePlus inc. - Common Stock|Q|N|N|100|N|N
PLXS|Plexus Corp. - Common Stock|Q|N|N|100|N|N
PLYA|Playa Hotels & Resorts N.V. - Ordinary Shares|Q|N|N|100|N|N
PMCB|PharmaCyte  Biotech, Inc. - Common Stock|S|N|N|100|N|N
PMD|Psychemedics Corporation - Common Stock|S|N|N|100|N|N
PMEC|Primech Holdings Ltd. - Ordinary Shares|S|N|N|100|N|N
PMGM|Priveterra Acquisition Corp. II - Class A Common Stock|S|N|N|100|N|N
PMGMU|Priveterra Acquisition Corp. II - Unit|S|N|N|100|N|N
PMGMW|Priveterra Acquisition Corp. II - Warrant to purchase Class A common stock|S|N|N|100|N|N
PMN|ProMIS Neurosciences Inc. - Common Shares|S|N|N|100|N|N
PMTS|CPI Card Group Inc. - Common Stock|G|N|N|100|N|N
PMVP|PMV Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
PNBK|Patriot National Bancorp Inc. - Common Stock|G|N|N|100|N|N
PNFP|Pinnacle Financial Partners, Inc. - Common Stock|Q|N|N|100|N|N
PNFPP|Pinnacle Financial Partners, Inc. - Depositary shares of Pinnacle Financial Partners, Inc., each representing a 1/40th Interest in a share of its 6.75% Fixed-Rate Non-Cumulative Perpetual Preferred Stock, Series B|Q|N|N|100|N|N
PNQI|Invesco Nasdaq Internet ETF|G|N|N|100|Y|N
PNRG|PrimeEnergy Resources Corporation - Common Stock|S|N|N|100|N|N
PNT|POINT Biopharma Global Inc.  - Common Stock|S|N|N|100|N|N
PNTG|The Pennant Group, Inc. - Common Stock|Q|N|N|100|N|N
POAI|Predictive Oncology Inc. - Common Stock|S|N|N|100|N|N
POCI|Precision Optics Corporation, Inc. - Common stock|S|N|N|100|N|N
PODC|PodcastOne, Inc. - Common Stock|S|N|N|100|N|N
PODD|Insulet Corporation - Common Stock|Q|N|N|100|N|N
POET|POET Technologies Inc. - Common Shares|S|N|N|100|N|N
POLA|Polar Power, Inc. - Common Stock|S|N|N|100|N|N
POOL|Pool Corporation - Common Stock|Q|N|N|100|N|N
POTX|Global X Cannabis ETF|G|N|N|100|Y|N
POWI|Power Integrations, Inc. - Common Stock|Q|N|N|100|N|N
POWL|Powell Industries, Inc. - Common Stock|Q|N|N|100|N|N
POWW|AMMO, Inc. - Common Stock|S|N|N|100|N|N
POWWP|AMMO, Inc. - 8.75% Series A Cumulative Redeemable Perpetual Preferred Stock|S|N|N|100|N|N
PPBI|Pacific Premier Bancorp Inc - Common Stock|Q|N|N|100|N|N
PPBT|Purple Biotech Ltd. - American Depositary Shares|S|N|N|100|N|N
PPC|Pilgrim's Pride Corporation - Common Stock|Q|N|N|100|N|N
PPH|VanEck Pharmaceutical ETF|G|N|N|100|Y|N
PPHP|PHP Ventures Acquisition Corp. - Class A Common Stock|S|N|D|100|N|N
PPHPR|PHP Ventures Acquisition Corp. - Rights|S|N|D|100|N|N
PPHPU|PHP Ventures Acquisition Corp. - Units|S|N|D|100|N|N
PPHPW|PHP Ventures Acquisition Corp. - Warrants|S|N|D|100|N|N
PPIH|Perma-Pipe International Holdings, Inc. - Common Stock|G|N|N|100|N|N
PPSI|Pioneer Power Solutions, Inc. - Common Stock|S|N|N|100|N|N
PPTA|Perpetua Resources Corp. - Common Shares|S|N|N|100|N|N
PPYA|Papaya Growth Opportunity Corp. I - Class A Common Stock|G|N|N|100|N|N
PPYAU|Papaya Growth Opportunity Corp. I - Unit|G|N|N|100|N|N
PPYAW|Papaya Growth Opportunity Corp. I - Warrant|G|N|N|100|N|N
PRAA|PRA Group, Inc. - Common Stock|Q|N|N|100|N|N
PRAX|Praxis Precision Medicines, Inc. - Common Stock|Q|N|N|100|N|N
PRCH|Porch Group, Inc. - Common Stock|S|N|D|100|N|N
PRCT|PROCEPT BioRobotics Corporation - Common Stock|G|N|N|100|N|N
PRDO|Perdoceo Education Corporation - Common Stock|Q|N|N|100|N|N
PRE|Prenetics Global Limited - Class A Ordinary Share|G|N|D|100|N|N
PRENW|Prenetics Global Limited - Warrant|S|N|N|100|N|N
PRFT|Perficient, Inc. - Common Stock|Q|N|N|100|N|N
PRFX|PainReform Ltd. - Ordinary Shares|S|N|N|100|N|N
PRFZ|Invesco FTSE RAFI US 1500 Small-Mid ETF|G|N|N|100|Y|N
PRGS|Progress Software Corporation - Common Stock|Q|N|N|100|N|N
PRLD|Prelude Therapeutics Incorporated - Common Stock|Q|N|N|100|N|N
PRLH|Pearl Holdings Acquisition Corp - Class A Ordinary Shares|G|N|N|100|N|N
PRLHU|Pearl Holdings Acquisition Corp - Unit|G|N|N|100|N|N
PRLHW|Pearl Holdings Acquisition Corp - Warrant|G|N|D|100|N|N
PRME|Prime Medicine, Inc. - Common Stock|G|N|N|100|N|N
PRN|Invesco Dorsey Wright Industrials Momentum ETF|G|N|N|100|Y|N
PROC|Procaps Group, S.A. - Ordinary Shares|G|N|N|100|N|N
PROCW|Procaps Group, S.A. - Warrants|G|N|N|100|N|N
PROF|Profound Medical Corp. - common stock|S|N|N|100|N|N
PROK|ProKidney Corp. - Class A Ordinary Shares|S|N|N|100|N|N
PROV|Provident Financial Holdings, Inc. - Common Stock|Q|N|N|100|N|N
PRPH|ProPhase Labs, Inc. - Common Stock|S|N|N|100|N|N
PRPL|Purple Innovation, Inc. - Common Stock|Q|N|N|100|N|N
PRPO|Precipio, Inc. - Common Stock|S|N|N|100|N|N
PRQR|ProQR Therapeutics N.V. - Ordinary Shares|S|N|N|100|N|N
PRSO|Peraso Inc. - Common Stock|S|N|D|100|N|N
PRSR|Prospector Capital Corp. - Class A Ordinary Shares|S|N|D|100|N|N
PRSRU|Prospector Capital Corp. - Unit|S|N|D|100|N|N
PRSRW|Prospector Capital Corp. - Warrants|S|N|D|100|N|N
PRST|Presto Automation, Inc. - Common Stock|G|N|N|100|N|N
PRSTW|Presto Automation, Inc. - Warrant|G|N|N|100|N|N
PRTA|Prothena Corporation plc - Ordinary Shares|Q|N|N|100|N|N
PRTC|PureTech Health plc - American Depositary Shares|G|N|N|100|N|N
PRTG|Portage Biotech Inc. - Common Stock|S|N|N|100|N|N
PRTH|Priority Technology Holdings, Inc. - Common Stock|S|N|N|100|N|N
PRTS|CarParts.com, Inc. - Common Stock|Q|N|N|100|N|N
PRVA|Privia Health Group, Inc. - Common Stock|Q|N|N|100|N|N
PRVT|Private Real Estate Strategy via Liquid REITs ETF|G|N|N|100|Y|N
PRZO|ParaZero Technologies Ltd. - Ordinary Shares|S|N|N|100|N|N
PSC|Principal U.S. Small-Cap ETF|G|N|N|100|Y|N
PSCC|Invesco S&P SmallCap Consumer Staples ETF|G|N|N|100|Y|N
PSCD|Invesco S&P SmallCap Consumer Discretionary ETF|G|N|N|100|Y|N
PSCE|Invesco S&P SmallCap Energy ETF|G|N|N|100|Y|N
PSCF|Invesco S&P SmallCap Financials ETF|G|N|N|100|Y|N
PSCH|Invesco S&P SmallCap Health Care ETF|G|N|N|100|Y|N
PSCI|Invesco S&P SmallCap Industrials ETF|G|N|N|100|Y|N
PSCM|Invesco S&P SmallCap Materials ETF|G|N|N|100|Y|N
PSCT|Invesco S&P SmallCap Information Technology ETF|G|N|N|100|Y|N
PSCU|Invesco S&P SmallCap Utilities & Communication Services ETF|G|N|N|100|Y|N
PSEC|Prospect Capital Corporation - Closed End Fund|Q|N|N|100|N|N
PSET|Principal Quality ETF|G|N|N|100|Y|N
PSHG|Performance Shipping Inc. - Common Shares|S|N|N|100|N|N
PSL|Invesco Dorsey Wright Consumer Staples Momentum ETF|G|N|N|100|Y|N
PSMT|PriceSmart, Inc. - Common Stock|Q|N|N|100|N|N
PSNL|Personalis, Inc. - Common Stock|G|N|N|100|N|N
PSNY|Polestar Automotive Holding UK Limited - Class A ADS|G|N|N|100|N|N
PSNYW|Polestar Automotive Holding UK Limited - Class C-1 ADS (ADW)|G|N|N|100|N|N
PSTV|PLUS THERAPEUTICS, Inc. - Common Stock|S|N|N|100|N|N
PSTX|Poseida Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
PSWD|Xtrackers Cybersecurity Select Equity ETF|G|N|N|100|Y|N
PT|Pintec Technology Holdings Limited - American Depositary Shares|G|N|N|100|N|N
PTC|PTC Inc. - Common Stock|Q|N|N|100|N|N
PTCT|PTC Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
PTEC|Global X PropTech ETF|G|N|N|100|Y|N
PTEN|Patterson-UTI Energy, Inc. - Common Stock|Q|N|N|100|N|N
PTF|Invesco Dorsey Wright Technology Momentum ETF|G|N|N|100|Y|N
PTGX|Protagonist Therapeutics, Inc. - Common Stock|G|N|D|100|N|N
PTH|Invesco Dorsey Wright Healthcare Momentum ETF|G|N|N|100|Y|N
PTHR|Pono Capital Three, Inc. - Class A Ordinary Shares|G|N|N|100|N|N
PTHRU|Pono Capital Three, Inc. - Unit|G|N|N|100|N|N
PTHRW|Pono Capital Three, Inc. - Warrant|G|N|N|100|N|N
PTIX|Protagenic Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
PTIXW|Protagenic Therapeutics, Inc. - Warrant|S|N|N|100|N|N
PTLO|Portillo's Inc. - Class A Common Stock|Q|N|N|100|N|N
PTMN|Portman Ridge Finance Corporation - Closed End Fund|Q|N|N|100|N|N
PTNQ|Pacer Trendpilot 100 ETF|G|N|N|100|Y|N
PTON|Peloton Interactive, Inc. - Common Stock|Q|N|N|100|N|N
PTPI|Petros Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
PTRS|Partners Bancorp - Common Stock|S|N|N|100|N|N
PTSI|P.A.M. Transportation Services, Inc. - Common Stock|G|N|N|100|N|N
PTVE|Pactiv Evergreen Inc. - Common stock|Q|N|N|100|N|N
PTWO|Pono Capital Two, Inc. - Class A Common Stock|G|N|N|100|N|N
PTWOU|Pono Capital Two, Inc. - Unit|G|N|N|100|N|N
PTWOW|Pono Capital Two, Inc. - Warrants|G|N|N|100|N|N
PUBM|PubMatic, Inc. - Class A Common Stock|G|N|N|100|N|N
PUCK|Goal Acquisitions Corp. - Common Stock|S|N|N|100|N|N
PUCKU|Goal Acquisitions Corp. - Unit|S|N|N|100|N|N
PUCKW|Goal Acquisitions Corp. - Warrant|S|N|N|100|N|N
PUI|Invesco Dorsey Wright Utilities Momentum ETF|G|N|N|100|Y|N
PULM|Pulmatrix, Inc. - Common Stock|S|N|N|100|N|N
PUYI|Puyi Inc. - American Depository Shares|G|N|N|100|N|N
PVBC|Provident Bancorp, Inc. - Common Stock|S|N|N|100|N|N
PWFL|PowerFleet, Inc. - Common Stock|G|N|N|100|N|N
PWM|Prestige Wealth Inc. - Ordinary Shares|S|N|N|100|N|N
PWOD|Penns Woods Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
PWP|Perella Weinberg Partners - Class A Common Stock|Q|N|N|100|N|N
PWUP|PowerUp Acquisition Corp. - Class A Ordinary Shares|G|N|N|100|N|N
PWUPU|PowerUp Acquisition Corp. - Unit|G|N|N|100|N|N
PWUPW|PowerUp Acquisition Corp. - Warrant|G|N|N|100|N|N
PXDT|Pixie Dust Technologies, Inc. - ADS, each representing one common share|S|N|E|100|N|N
PXI|Invesco Dorsey Wright Energy Momentum ETF|G|N|N|100|Y|N
PXLW|Pixelworks, Inc. - Common Stock|G|N|N|100|N|N
PXMD|PaxMedica, Inc. - Common stock|S|N|D|100|N|N
PXS|Pyxis Tankers Inc. - Common Stock|S|N|N|100|N|N
PXSAP|Pyxis Tankers Inc. - 7.75% Series A Cumulative Convertible Preferred Shares|S|N|N|100|N|N
PXSAW|Pyxis Tankers Inc. - Warrant|S|N|N|100|N|N
PY|Principal Value ETF|G|N|N|100|Y|N
PYCR|Paycor HCM, Inc. - Common Stock|Q|N|N|100|N|N
PYPD|PolyPid Ltd. - Ordinary Shares|S|N|N|100|N|N
PYPL|PayPal Holdings, Inc. - Common Stock|Q|N|N|100|N|N
PYR|PyroGenesis Canada Inc. - Common Shares|S|N|D|100|N|N
PYXS|Pyxis Oncology, Inc. - Common Stock|Q|N|N|100|N|N
PYZ|Invesco Dorsey Wright Basic Materials Momentum ETF|G|N|N|100|Y|N
PZZA|Papa John's International, Inc. - Common Stock|Q|N|N|100|N|N
QABA|First Trust NASDAQ ABA Community Bank Index Fund|G|N|N|100|Y|N
QAT|iShares MSCI Qatar ETF|G|N|N|100|Y|N
QCLN|First Trust NASDAQ Clean Edge Green Energy Index Fund|G|N|N|100|Y|N
QCLR|Global X NASDAQ 100 Collar 95-110 ETF|G|N|N|100|Y|N
QCOM|QUALCOMM Incorporated - Common Stock|Q|N|N|100|N|N
QCRH|QCR Holdings, Inc. - Common Stock|G|N|N|100|N|N
QDEL|QuidelOrtho Corporation - Common Stock|Q|N|N|100|N|N
QDRO|Quadro Acquisition One Corp. - Class A Ordinary Shares|S|N|N|100|N|N
QDROU|Quadro Acquisition One Corp. - Unit|S|N|N|100|N|N
QDROW|Quadro Acquisition One Corp. - Warrant|S|N|N|100|N|N
QETAU|Quetta Acquisition Corporation - Unit|G|N|N|100|N|N
QFIN|Qifu Technology, Inc - American Depositary Shares|Q|N|N|100|N|N
QH|Quhuo Limited - American Depository Shares|G|N|N|100|N|N
QIPT|Quipt Home Medical Corp. - Common Shares|S|N|N|100|N|N
QIWI|QIWI plc - American Depositary Shares|Q|N|D|100|N|N
QLGN|Qualigen Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
QLI|Qilian International Holding Group Ltd. - Ordinary Shares|G|N|D|100|N|N
QLYS|Qualys, Inc. - Common Stock|Q|N|N|100|N|N
QMCO|Quantum Corporation - Common Stock|G|N|D|100|N|N
QNCX|Quince Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
QNRX|Quoin Pharmaceuticals, Ltd. - American Depositary Shares|S|N|N|100|N|N
QNST|QuinStreet, Inc. - Common Stock|Q|N|N|100|N|N
QOMO|Qomolangma Acquisition Corp. - Common Stock|S|N|N|100|N|N
QOMOR|Qomolangma Acquisition Corp. - Right|S|N|N|100|N|N
QOMOU|Qomolangma Acquisition Corp. - Unit|S|N|N|100|N|N
QOMOW|Qomolangma Acquisition Corp. - Warrant|S|N|N|100|N|N
QQEW|First Trust NASDAQ-100 Equal Weighted Index Fund|G|N|N|100|Y|N
QQJG|Invesco ESG NASDAQ Next Gen 100 ETF|G|N|N|100|Y|N
QQMG|Invesco ESG NASDAQ 100 ETF|G|N|N|100|Y|N
QQQ|Invesco QQQ Trust, Series 1|G|N|N|100|Y|N
QQQA|ProShares Nasdaq-100 Dorsey Wright Momentum ETF|G|N|N|100|Y|N
QQQE|Direxion NASDAQ-100 Equal Weighted Index Shares|G|N|N|100|Y|N
QQQJ|Invesco NASDAQ Next Gen 100 ETF|G|N|N|100|Y|N
QQQM|Invesco NASDAQ 100 ETF|G|N|N|100|Y|N
QQQN|VictoryShares Nasdaq Next 50 ETF|G|N|N|100|Y|N
QQQS|Invesco NASDAQ Future Gen 200 ETF|G|N|N|100|Y|N
QQQX|Nuveen NASDAQ 100 Dynamic Overwrite Fund - Closed End Fund|Q|N|N|100|N|N
QQQY|Defiance Nasdaq 100 Enhanced Options Income ETF|G|N|N|100|Y|N
QQXT|First Trust NASDAQ-100 Ex-Technology Sector Index Fund|G|N|N|100|Y|N
QRHC|Quest Resource Holding Corporation - Common Stock|S|N|N|100|N|N
QRMI|Global X NASDAQ 100 Risk Managed Income ETF|G|N|N|100|Y|N
QRTEA|Qurate Retail, Inc. - Series A Common Stock|Q|N|D|100|N|N
QRTEB|Qurate Retail, Inc. - Series B Common Stock|Q|N|N|100|N|N
QRTEP|Qurate Retail, Inc. - 8.0% Fixed Rate Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
QRVO|Qorvo, Inc. - Common Stock|Q|N|N|100|N|N
QSG|QuantaSing Group Limited - American Depositary Shares|G|N|N|100|N|N
QSI|Quantum-Si Incorporated - Class A Common Stock|G|N|N|100|N|N
QSIAW|Quantum-Si Incorporated - Warrant|G|N|N|100|N|N
QTEC|First Trust NASDAQ-100-Technology Sector Index Fund|G|N|N|100|Y|N
QTR|Global X NASDAQ 100 Tail Risk ETF|G|N|N|100|Y|N
QTRX|Quanterix Corporation - Common Stock|G|N|N|100|N|N
QUBT|Quantum Computing Inc. - Common Stock|S|N|N|100|N|N
QUIK|QuickLogic Corporation - Common Stock|S|N|N|100|N|N
QURE|uniQure N.V. - Ordinary Shares|Q|N|N|100|N|N
QYLD|Global X NASDAQ 100 Covered Call ETF|G|N|N|100|Y|N
QYLE|Global X Nasdaq 100 ESG Covered Call ETF|G|N|N|100|Y|N
QYLG|Global X Nasdaq 100 Covered Call & Growth ETF|G|N|N|100|Y|N
RACY|Relativity Acquisition Corp. - Class A Common Stock|S|N|N|100|N|N
RACYU|Relativity Acquisition Corp. - Unit|S|N|N|100|N|N
RACYW|Relativity Acquisition Corp. - Warrant|S|N|N|100|N|N
RAIL|Freightcar America, Inc. - Common Stock|Q|N|N|100|N|N
RAIN|Rain Oncology Inc. - Common Stock|Q|N|N|100|N|N
RAND|Rand Capital Corporation - Closed End Fund|S|N|N|100|N|N
RANI|Rani Therapeutics Holdings, Inc. - Class A Common Stock|G|N|N|100|N|N
RAPT|RAPT Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
RARE|Ultragenyx Pharmaceutical Inc. - Common Stock|Q|N|N|100|N|N
RAVE|Rave Restaurant Group, Inc. - Common Stock|S|N|N|100|N|N
RAYA|Erayak Power Solution Group Inc. - Class A Ordinary Shares|S|N|N|100|N|N
RAYS|Global X Solar ETF|G|N|N|100|Y|N
RBB|RBB Bancorp - Common Stock|Q|N|N|100|N|N
RBBN|Ribbon Communications Inc.  - Common Stock|Q|N|N|100|N|N
RBCAA|Republic Bancorp, Inc. - Class A Common Stock|Q|N|N|100|N|N
RBKB|Rhinebeck Bancorp, Inc. - Common Stock|S|N|N|100|N|N
RCAC|Revelstone Capital Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
RCACU|Revelstone Capital Acquisition Corp. - Unit|G|N|N|100|N|N
RCACW|Revelstone Capital Acquisition Corp. - Warrant|G|N|D|100|N|N
RCAT|Red Cat Holdings, Inc. - Common Stock|S|N|N|100|N|N
RCEL|Avita Medical, Inc. - Common Stock|S|N|N|100|N|N
RCKT|Rocket Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
RCKTW|Rocket Pharmaceuticals, Inc. - Warrant|S|N|N|100|N|N
RCKY|Rocky Brands, Inc. - Common Stock|Q|N|N|100|N|N
RCM|R1 RCM Inc. - Common Stock|Q|N|N|100|N|N
RCMT|RCM Technologies, Inc. - Common Stock|G|N|N|100|N|N
RCON|Recon Technology, Ltd. - Class A Ordinary Shares|S|N|D|100|N|N
RCRT|Recruiter.com Group, Inc. - Common Stock|S|N|D|100|N|N
RCRTW|Recruiter.com Group, Inc. - Warrant|S|N|D|100|N|N
RDCM|Radcom Ltd. - Ordinary Shares|S|N|N|100|N|N
RDFN|Redfin Corporation - Common Stock|Q|N|N|100|N|N
RDHL|Redhill Biopharma Ltd. - American Depositary Shares|G|N|D|100|N|N
RDI|Reading International Inc - Class A Non-voting Common Stock|S|N|N|100|N|N
RDIB|Reading International Inc - Class B Voting Common Stock|S|N|N|100|N|N
RDNT|RadNet, Inc. - Common Stock|G|N|N|100|N|N
RDUS|Schnitzer Steel Industries, Inc. - Class A Common Stock|Q|N|N|100|N|N
RDVT|Red Violet, Inc. - Common Stock |S|N|N|100|N|N
RDVY|First Trust Rising Dividend Achievers ETF|G|N|N|100|Y|N
RDWR|Radware Ltd. - Ordinary Shares|Q|N|N|100|N|N
RDZN|Roadzen, Inc. - Ordinary Shares|G|N|N|100|N|N
RDZNW|Roadzen, Inc. - Warrants|S|N|N|100|N|N
REAL|The RealReal, Inc. - Common Stock|Q|N|N|100|N|N
REAX|The Real Brokerage, Inc. - Common Shares|S|N|N|100|N|N
REBN|Reborn Coffee, Inc. - Common Stock|S|N|D|100|N|N
REE|REE Automotive Ltd. - Class A Ordinary Shares|S|N|D|100|N|N
REFI|Chicago Atlantic Real Estate Finance, Inc. - Common Stock|G|N|N|100|N|N
REFR|Research Frontiers Incorporated - Common Stock|S|N|N|100|N|N
REG|Regency Centers Corporation - Common Stock|Q|N|N|100|N|N
REGCO|Regency Centers Corporation - 5.875% Series B Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
REGCP|Regency Centers Corporation - 6.25% Series A Cumulative Redeemable Preferred Stock|Q|N|N|100|N|N
REGN|Regeneron Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
REIT|ALPS Active REIT ETF|G|N|N|100|Y|N
REKR|Rekor Systems, Inc. - Common Stock|S|N|N|100|N|N
RELI|Reliance Global Group, Inc. - Common Stock|S|N|N|100|N|N
RELIW|Reliance Global Group, Inc. - Series A Warrants|S|N|N|100|N|N
RELL|Richardson Electronics, Ltd. - Common Stock|Q|N|N|100|N|N
RELY|Remitly Global, Inc. - Common stock|Q|N|N|100|N|N
RENB|Renovaro Biosciences Inc. - Common Stock|S|N|N|100|N|N
RENE|Cartesian Growth Corporation II - Class A Ordinary Shares|G|N|N|100|N|N
RENEU|Cartesian Growth Corporation II - Unit|G|N|N|100|N|N
RENEW|Cartesian Growth Corporation II - Warrant|G|N|N|100|N|N
RENT|Rent the Runway, Inc. - Class A Common Stock|S|N|N|100|N|N
REPL|Replimune Group, Inc. - Common Stock|Q|N|N|100|N|N
RETO|ReTo Eco-Solutions, Inc. - Common Shares|S|N|N|100|N|N
REVB|Revelation Biosciences, Inc. - Common Stock|S|N|D|100|N|N
REVBW|Revelation Biosciences, Inc. - Warrant|S|N|N|100|N|N
REYN|Reynolds Consumer Products Inc. - Common Stock|Q|N|N|100|N|N
RFAC|RF Acquisition Corp. - Class A Common Stock|G|N|N|100|N|N
RFACR|RF Acquisition Corp. - Rights|G|N|N|100|N|N
RFACU|RF Acquisition Corp. - Unit|G|N|N|100|N|N
RFACW|RF Acquisition Corp. - Warrants|G|N|N|100|N|N
RFDI|First Trust RiverFront Dynamic Developed International ETF|G|N|N|100|Y|N
RFEM|First Trust RiverFront Dynamic Emerging Markets ETF|G|N|N|100|Y|N
RFEU|First Trust RiverFront Dynamic Europe ETF|G|N|N|100|Y|N
RFIL|RF Industries, Ltd. - Common Stock|G|N|N|100|N|N
RGC|Regencell Bioscience Holdings Limited - Ordinary Shares|S|N|N|100|N|N
RGCO|RGC Resources Inc. - Common Stock|G|N|N|100|N|N
RGEN|Repligen Corporation - Common Stock|Q|N|N|100|N|N
RGF|The Real Good Food Company, Inc. - Class A Common Stock|G|N|N|100|N|N
RGLD|Royal Gold, Inc. - Common Stock|Q|N|N|100|N|N
RGLS|Regulus Therapeutics Inc. - Common Stock|S|N|N|100|N|N
RGNX|REGENXBIO Inc. - Common Stock|Q|N|N|100|N|N
RGP|Resources Connection, Inc. - Common Stock|Q|N|N|100|N|N
RGTI|Rigetti Computing, Inc.  - Common stock|S|N|N|100|N|N
RGTIW|Rigetti Computing, Inc.  - Redeemable warrants, each whole warrant exercisable for one Class A ordinary share at an exercise price of $11.50|S|N|N|100|N|N
RIBT|RiceBran Technologies - Common Stock|S|N|D|100|N|N
RICK|RCI Hospitality Holdings, Inc. - Common Stock|G|N|N|100|N|N
RIGL|Rigel Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
RILY|B. Riley Financial, Inc. - Common Stock|G|N|N|100|N|N
RILYG|B. Riley Financial, Inc. - 5.00% Senior Notes due 2026|G|N|N|100|N|N
RILYK|B. Riley Financial, Inc. - 5.50% Senior Notes Due 2026|G|N|N|100|N|N
RILYL|B. Riley Financial, Inc. - Depositary Shares, each representing a 1/1000th fractional interest in a share of Series B Cumulative Perpetual Preferred Stock|G|N|N|100|N|N
RILYM|B. Riley Financial, Inc. - 6.375% Senior Notes due 2025|G|N|N|100|N|N
RILYN|B. Riley Financial, Inc. - 6.50% Senior Notes Due 2026|G|N|N|100|N|N
RILYO|B. Riley Financial, Inc. - 6.75% Senior Notes due 2024|G|N|N|100|N|N
RILYP|B. Riley Financial, Inc. - Depositary Shares, each representing a 1/1000th fractional interest in a share of Series A Cumulative Perpetual Preferred Stock|G|N|N|100|N|N
RILYT|B. Riley Financial, Inc. - 6.00% Senior Notes Due 2028|G|N|N|100|N|N
RILYZ|B. Riley Financial, Inc. - 5.25% Senior Notes due 2028|G|N|N|100|N|N
RING|iShares MSCI Global Gold Miners ETF|G|N|N|100|Y|N
RIOT|Riot Platforms, Inc. - Common Stock|S|N|N|100|N|N
RIVN|Rivian Automotive, Inc. - Class A Common Stock|Q|N|N|100|N|N
RKDA|Arcadia Biosciences, Inc. - Common Stock|S|N|N|100|N|N
RKLB|Rocket Lab USA, Inc. - Common Stock|S|N|N|100|N|N
RLAY|Relay Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
RLMD|Relmada Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
RLYB|Rallybio Corporation - Common Stock|Q|N|N|100|N|N
RMBI|Richmond Mutual Bancorporation, Inc. - Common Stock|S|N|N|100|N|N
RMBL|RumbleOn, Inc. - Class B Common Stock|S|N|N|100|N|N
RMBS|Rambus, Inc. - Common Stock|Q|N|N|100|N|N
RMCF|Rocky Mountain Chocolate Factory, Inc. - Common Stock|G|N|N|100|N|N
RMGC|RMG Acquisition Corp. III - Class A Ordinary Shares|S|N|D|100|N|N
RMGCU|RMG Acquisition Corp. III - Unit|S|N|D|100|N|N
RMGCW|RMG Acquisition Corp. III - Warrant|S|N|D|100|N|N
RMNI|Rimini Street, Inc. - Common Stock|G|N|N|100|N|N
RMR|The RMR Group Inc. - Class A Common Stock|S|N|N|100|N|N
RMTI|Rockwell Medical, Inc. - Common Stock|S|N|N|100|N|N
RNA|Avidity Biosciences, Inc. - Common Stock|G|N|N|100|N|N
RNAZ|TransCode Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
RNEM|Emerging Markets Equity Select ETF|G|N|N|100|Y|N
RNEW|VanEck Green Infrastructure ETF|G|N|N|100|Y|N
RNLC|Large Cap US Equity Select ETF|G|N|N|100|Y|N
RNLX|Renalytix plc - American Depositary Shares|G|N|N|100|N|N
RNMC|Mid Cap US Equity Select ETF|G|N|N|100|Y|N
RNRG|Global X Renewable Energy Producers ETF|G|N|N|100|Y|N
RNSC|Small Cap US Equity Select ETF|G|N|N|100|Y|N
RNW|ReNew Energy Global plc - Class A Shares|Q|N|N|100|N|N
RNWWW|ReNew Energy Global plc - Warrant|Q|N|N|100|N|N
RNXT|RenovoRx, Inc. - Common Stock|S|N|D|100|N|N
ROAD|Construction Partners, Inc. - Common Stock|Q|N|N|100|N|N
ROBT|First Trust Nasdaq Artificial Intelligence and Robotics ETF|G|N|N|100|Y|N
ROCK|Gibraltar Industries, Inc. - Common Stock|Q|N|N|100|N|N
ROCL|Roth CH Acquisition V Co. - Common Stock|G|N|D|100|N|N
ROCLU|Roth CH Acquisition V Co. - Unit|G|N|N|100|N|N
ROCLW|Roth CH Acquisition V Co. - Warrant|G|N|N|100|N|N
ROE|Astoria US Quality Kings ETF|G|N|N|100|Y|N
ROIC|Retail Opportunity Investments Corp. - Common Stock|Q|N|N|100|N|N
ROIV|Roivant Sciences Ltd. - Common Shares|G|N|N|100|N|N
ROKU|Roku, Inc. - Class A Common Stock|Q|N|N|100|N|N
ROOT|Root, Inc. - Common Stock|Q|N|N|100|N|N
ROP|Roper Technologies, Inc. - Common Stock|Q|N|N|100|N|N
ROSE|Rose Hill Acquisition Corporation - Class A Ordinary Shares|S|N|D|100|N|N
ROSEU|Rose Hill Acquisition Corporation - Unit|S|N|N|100|N|N
ROSEW|Rose Hill Acquisition Corporation - Warrant|S|N|N|100|N|N
ROST|Ross Stores, Inc. - Common Stock|Q|N|N|100|N|N
ROVR|Rover Group, Inc. - Class A Common Stock|G|N|N|100|N|N
RPAY|Repay Holdings Corporation - Class A Common Stock|S|N|N|100|N|N
RPD|Rapid7, Inc. - Common Stock|G|N|N|100|N|N
RPHM|Reneo Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
RPID|Rapid Micro Biosystems, Inc. - Class A Common Stock|Q|N|N|100|N|N
RPRX|Royalty Pharma plc - Class A Ordinary Shares|Q|N|N|100|N|N
RPTX|Repare Therapeutics Inc. - Common Shares|Q|N|N|100|N|N
RRBI|Red River Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
RRGB|Red Robin Gourmet Burgers, Inc. - Common Stock|Q|N|N|100|N|N
RRR|Red Rock Resorts, Inc. - Class A Common Stock|Q|N|N|100|N|N
RSLS|ReShape Lifesciences, Inc. - Common Stock|S|N|N|100|N|N
RSSS|Research Solutions, Inc - Common Stock|S|N|N|100|N|N
RSVR|Reservoir Media, Inc.. - Common Stock|G|N|N|100|N|N
RSVRW|Reservoir Media, Inc.. - Warrant|G|N|N|100|N|N
RTC|Baijiayun Group Ltd - Class Ordinary Shares|G|N|N|100|N|N
RTH|VanEck Retail ETF|G|N|N|100|Y|N
RUM|Rumble Inc. - Class A Common Stock|G|N|N|100|N|N
RUMBW|Rumble Inc. - Warrant|G|N|N|100|N|N
RUN|Sunrun Inc. - Common Stock|Q|N|N|100|N|N
RUNN|Running Oak Efficient Growth ETF|G|N|N|100|Y|N
RUSHA|Rush Enterprises, Inc. - Class A Common Stock|Q|N|N|100|N|N
RUSHB|Rush Enterprises, Inc. - Class B Common Stock|Q|N|N|100|N|N
RVLP|RVL Pharmaceuticals plc - Ordinary Shares|Q|N|D|100|N|N
RVMD|Revolution Medicines, Inc. - Common Stock|Q|N|N|100|N|N
RVNC|Revance Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
RVPH|Reviva Pharmaceuticals Holdings, Inc. - Common Stock|S|N|N|100|N|N
RVPHW|Reviva Pharmaceuticals Holdings, Inc. - Warrants|S|N|N|100|N|N
RVSB|Riverview Bancorp Inc - Common Stock|Q|N|N|100|N|N
RVSN|Rail Vision Ltd. - Ordinary Shares|S|N|D|100|N|N
RVSNW|Rail Vision Ltd. - Warrant|S|N|N|100|N|N
RVYL|Ryvyl Inc. - Common Stock|S|N|N|100|N|N
RWAY|Runway Growth Finance Corp. - Common Stock|Q|N|N|100|N|N
RWAYL|Runway Growth Finance Corp. - 7.50% Notes due 2027|Q|N|N|100|N|N
RWAYZ|Runway Growth Finance Corp. - 8.00% Notes due 2027|Q|N|N|100|N|N
RWLK|ReWalk Robotics Ltd. - Ordinary Shares|S|N|D|100|N|N
RWOD|Redwoods Acquisition Corp. - Common Stock|G|N|N|100|N|N
RWODR|Redwoods Acquisition Corp. - Rights|G|N|N|100|N|N
RWODU|Redwoods Acquisition Corp. - Unit|G|N|N|100|N|N
RWODW|Redwoods Acquisition Corp. - Warrants|G|N|N|100|N|N
RXRX|Recursion Pharmaceuticals, Inc. - Class A Common Stock|Q|N|N|100|N|N
RXST|RxSight, Inc. - Common Stock|G|N|N|100|N|N
RXT|Rackspace Technology, Inc. - Common Stock|Q|N|N|100|N|N
RYAAY|Ryanair Holdings plc - American Depositary Shares, each representing five Ordinary Shares|Q|N|N|100|N|N
RYTM|Rhythm Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
RYZB|RayzeBio, Inc. - Common Stock|G|N|N|100|N|N
RZLT|Rezolute, Inc. - Common Stock (NV)|S|N|N|100|N|N
SABR|Sabre Corporation - Common Stock|Q|N|N|100|N|N
SABS|SAB Biotherapeutics, Inc. - Common Stock|S|N|D|100|N|N
SABSW|SAB Biotherapeutics, Inc. - Warrant|S|N|N|100|N|N
SAFT|Safety Insurance Group, Inc. - Common Stock|Q|N|N|100|N|N
SAGA|Sagaliam Acquisition Corp. - Class A Common Stock|G|N|H|100|N|N
SAGAR|Sagaliam Acquisition Corp. - Rights|G|N|H|100|N|N
SAGAU|Sagaliam Acquisition Corp. - Units|G|N|H|100|N|N
SAGE|Sage Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
SAI|SAI.TECH Global Corporation  - Class A Ordinary Shares|S|N|N|100|N|N
SAIA|Saia, Inc. - Common Stock|Q|N|N|100|N|N
SAITW|SAI.TECH Global Corporation  - Warrant|S|N|N|100|N|N
SALM|Salem Media Group, Inc. - Class A Common Stock|G|N|D|100|N|N
SAMG|Silvercrest Asset Management Group Inc. - Common Stock|G|N|N|100|N|N
SANA|Sana Biotechnology, Inc. - Common Stock|Q|N|N|100|N|N
SANG|Sangoma Technologies Corporation - Common Shares|Q|N|N|100|N|N
SANM|Sanmina Corporation - Common Stock|Q|N|N|100|N|N
SANW|S&W Seed Company - Common Stock|S|N|D|100|N|N
SARK|AXS Short Innovation Daily ETF|G|N|N|100|Y|N
SASI|Sigma Additive Solutions, Inc. - Common Stock|S|N|D|100|N|N
SASR|Sandy Spring Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
SATL|Satellogic Inc. - Class A Ordinary Shares|S|N|N|100|N|N
SATLW|Satellogic Inc. - Warrant|S|N|N|100|N|N
SATS|EchoStar Corporation - Common stock|Q|N|N|100|N|N
SAVA|Cassava Sciences, Inc. - Common Stock|S|N|N|100|N|N
SBAC|SBA Communications Corporation - Class A Common Stock|Q|N|N|100|N|N
SBCF|Seacoast Banking Corporation of Florida - Common Stock|Q|N|N|100|N|N
SBET|SharpLink Gaming Ltd. - Ordinary Shares|S|N|D|100|N|N
SBFG|SB Financial Group, Inc. - Common Stock|S|N|N|100|N|N
SBFM|Sunshine Biopharma Inc. - Common stock|S|N|D|100|N|N
SBFMW|Sunshine Biopharma Inc. - Warrant|S|N|N|100|N|N
SBGI|Sinclair, Inc. - Class A Common Stock|Q|N|N|100|N|N
SBLK|Star Bulk Carriers Corp. - Common Shares|Q|N|N|100|N|N
SBRA|Sabra Health Care REIT, Inc. - Common Stock|Q|N|N|100|N|N
SBSI|Southside Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
SBT|Sterling Bancorp, Inc. - Common Stock|S|N|N|100|N|N
SBUX|Starbucks Corporation - Common Stock|Q|N|N|100|N|N
SCHL|Scholastic Corporation - Common Stock|Q|N|N|100|N|N
SCKT|Socket Mobile, Inc. - Common Stock|S|N|N|100|N|N
SCLX|Scilex Holding Company - Common Stock|S|N|N|100|N|N
SCLXW|Scilex Holding Company - Warrant|S|N|N|100|N|N
SCNI|Scinai Immunotherapeutics Ltd. - American Depositary Shares|S|N|D|100|N|N
SCOR|comScore, Inc. - Common Stock|Q|N|D|100|N|N
SCPH|scPharmaceuticals Inc. - Common Stock|Q|N|N|100|N|N
SCPL|SciPlay Corporation - Class A Common Stock|Q|N|N|100|N|N
SCRM|Screaming Eagle Acquisition Corp. - Class A Ordinary Shares|G|N|N|100|N|N
SCRMU|Screaming Eagle Acquisition Corp. - Unit|G|N|N|100|N|N
SCRMW|Screaming Eagle Acquisition Corp. - Warrant|G|N|N|100|N|N
SCSC|ScanSource, Inc. - Common Stock|Q|N|N|100|N|N
SCTL|Societal CDMO, Inc. - Common Stock|S|N|D|100|N|N
SCVL|Shoe Carnival, Inc. - Common Stock|Q|N|N|100|N|N
SCWO|374Water Inc. - common stock|S|N|N|100|N|N
SCWX|SecureWorks Corp. - Class A Common Stock|Q|N|D|100|N|N
SCYX|SCYNEXIS, Inc. - Common Stock|G|N|N|100|N|N
SCZ|iShares MSCI EAFE Small-Cap ETF|G|N|N|100|Y|N
SDA|SunCar Technology Group Inc. - Ordinary Shares|S|N|N|100|N|N
SDAWW|SunCar Technology Group Inc. - Warrant|S|N|N|100|N|N
SDG|iShares MSCI Global Sustainable Development Goals ETF|G|N|N|100|Y|N
SDGR|Schrodinger, Inc. - Common Stock|Q|N|N|100|N|N
SDIG|Stronghold Digital Mining, Inc. - Class A Common Stock|G|N|N|100|N|N
SDOT|Sadot Group Inc. - Common Stock|S|N|N|100|N|N
SDSI|American Century Short Duration Strategic Income ETF|G|N|N|100|Y|N
SDVY|First Trust SMID Cap Rising Dividend Achievers ETF|G|N|N|100|Y|N
SEAT|Vivid Seats Inc. - Class A common stock|Q|N|N|100|N|N
SEATW|Vivid Seats Inc. - Warrant|Q|N|N|100|N|N
SECO|Secoo Holding Limited - American Depositary Shares|S|N|H|100|N|N
SEDG|SolarEdge Technologies, Inc. - Common Stock|Q|N|N|100|N|N
SEED|Origin Agritech Limited - Ordinary Shares|S|N|D|100|N|N
SEEL|Seelos Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
SEER|Seer, Inc. - Class A Common Stock|Q|N|N|100|N|N
SEIC|SEI Investments Company - Common Stock|Q|N|N|100|N|N
SELB|Selecta Biosciences, Inc. - Common Stock|G|N|N|100|N|N
SELF|Global Self Storage, Inc. - Common Stock|S|N|N|100|N|N
SENEA|Seneca Foods Corp. - Class A Common Stock|Q|N|N|100|N|N
SENEB|Seneca Foods Corp. - Class B Common Stock|Q|N|N|100|N|N
SEPA|SEP Acquisition Corp - Class A Common Stock|S|N|D|100|N|N
SEPAU|SEP Acquisition Corp - Unit|S|N|D|100|N|N
SEPAW|SEP Acquisition Corp - Warrants|S|N|D|100|N|N
SERA|Sera Prognostics, Inc. - Class A Common Stock|G|N|N|100|N|N
SETM|Sprott Energy Transition Materials ETF|G|N|N|100|Y|N
SEVN|Seven Hills Realty Trust  - Common Stock|S|N|N|100|N|N
SEZL|Sezzle Inc. - Common Stock|S|N|N|100|N|N
SFBC|Sound Financial Bancorp, Inc. - Common Stock|S|N|N|100|N|N
SFE|Safeguard Scientifics, Inc. - Common stock|S|N|N|100|N|N
SFIX|Stitch Fix, Inc. - Class A Common Stock|Q|N|N|100|N|N
SFM|Sprouts Farmers Market, Inc. - Common Stock|Q|N|N|100|N|N
SFNC|Simmons First National Corporation - Common Stock|Q|N|N|100|N|N
SFR|Appreciate Holdings, Inc. - Class A Common Stock|G|N|H|100|N|N
SFRWW|Appreciate Holdings, Inc. - Warrant|S|N|E|100|N|N
SFST|Southern First Bancshares, Inc. - Common Stock|G|N|N|100|N|N
SFT|Shift Technologies, Inc. - Class A Common Stock|S|N|D|100|N|N
SFWL|Shengfeng Development Limited - Class A Ordinary Shares|S|N|N|100|N|N
SGA|Saga Communications, Inc. - Class A Common Stock|G|N|N|100|N|N
SGBX|Safe & Green Holdings Corp. - Common Stock|S|N|N|100|N|N
SGC|Superior Group of Companies, Inc. - Common Stock|G|N|N|100|N|N
SGD|Safe and Green Development Corporation - Common Stock|S|N|N|100|N|N
SGEN|Seagen Inc.  - Common Stock|Q|N|N|100|N|N
SGH|SMART Global Holdings, Inc. - Ordinary Shares|Q|N|N|100|N|N
SGHT|Sight Sciences, Inc. - Common Stock|Q|N|N|100|N|N
SGII|Seaport Global Acquisition II Corp. - Class A Common Stock|G|N|D|100|N|N
SGIIU|Seaport Global Acquisition II Corp. - Unit|G|N|N|100|N|N
SGIIW|Seaport Global Acquisition II Corp. - Warrants|G|N|N|100|N|N
SGLY|Singularity Future Technology Ltd. - Common Stock|S|N|D|100|N|N
SGMA|SigmaTron International, Inc. - Common Stock|S|N|N|100|N|N
SGML|Sigma Lithium Corporation - common shares|S|N|N|100|N|N
SGMO|Sangamo Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
SGMT|Sagimet Biosciences Inc. - Series A Common Stock|G|N|N|100|N|N
SGRP|SPAR Group, Inc. - Common Stock|S|N|N|100|N|N
SGRY|Surgery Partners, Inc. - Common Stock|Q|N|N|100|N|N
SHBI|Shore Bancshares Inc - Common Stock|Q|N|N|100|N|N
SHC|Sotera Health Company - Common Stock|Q|N|N|100|N|N
SHCR|Sharecare, Inc. - Class A Common Stock|Q|N|N|100|N|N
SHCRW|Sharecare, Inc. - Warrant|Q|N|N|100|N|N
SHEN|Shenandoah Telecommunications Co - Common Stock|Q|N|N|100|N|N
SHFS|SHF Holdings, Inc. - Class A Common Stock|S|N|D|100|N|N
SHFSW|SHF Holdings, Inc. - Warrants|S|N|N|100|N|N
SHIP|Seanergy Maritime Holdings Corp. - Common Stock|S|N|N|100|N|N
SHLS|Shoals Technologies Group, Inc. - Class A Common Stock|G|N|N|100|N|N
SHLT|SHL Telemedicine Ltd - American Depositary Shares|S|N|N|100|N|N
SHOO|Steven Madden, Ltd. - Common Stock|Q|N|N|100|N|N
SHOT|Safety Shot, Inc. - Common Stock|S|N|N|100|N|N
SHOTW|Safety Shot, Inc. - Warrant|S|N|N|100|N|N
SHPH|Shuttle Pharmaceuticals Holdings, Inc. - common stock|S|N|D|100|N|N
SHPW|Shapeways Holdings, Inc. - Common Stock|G|N|N|100|N|N
SHPWW|Shapeways Holdings, Inc. - Warrants|G|N|N|100|N|N
SHUA|SHUAA Partners Acquisition Corp I - Class A Ordinary Share|S|N|N|100|N|N
SHUAU|SHUAA Partners Acquisition Corp I - Unit|S|N|N|100|N|N
SHUAW|SHUAA Partners Acquisition Corp I - Warrant|S|N|N|100|N|N
SHV|iShares Short Treasury Bond ETF|G|N|N|100|Y|N
SHY|iShares 1-3 Year Treasury Bond ETF|G|N|N|100|Y|N
SHYF|The Shyft Group, Inc. - Common Stock|Q|N|N|100|N|N
SIBN|SI-BONE, Inc. - Common Stock|G|N|N|100|N|N
SIDU|Sidus Space, Inc. - Class A Common Stock|S|N|D|100|N|N
SIEB|Siebert Financial Corp. - Common Stock|S|N|N|100|N|N
SIEN|Sientra, Inc. - Common Stock|Q|N|N|100|N|N
SIFY|Sify Technologies Limited - American Depository Shares, each represented by one Equity Share|S|N|N|100|N|N
SIGA|SIGA Technologies Inc. - Common Stock|G|N|N|100|N|N
SIGI|Selective Insurance Group, Inc. - Common Stock|Q|N|N|100|N|N
SIGIP|Selective Insurance Group, Inc. - Depositary Shares, each representing a 1/1,000th interest in a share of 4.60% Non-Cumulative Preferred Stock, Series B|Q|N|N|100|N|N
SILC|Silicom Ltd - Ordinary Shares|Q|N|N|100|N|N
SILK|Silk Road Medical, Inc. - Common Stock|Q|N|N|100|N|N
SILO|Silo Pharma, Inc. - common stock, effectuated 1:50 R/S on 9/15|S|N|N|100|N|N
SIMO|Silicon Motion Technology Corporation - American Depositary Shares, each representing four ordinary shares|Q|N|N|100|N|N
SINT|SiNtx Technologies, Inc. - Common Stock|S|N|N|100|N|N
SIRI|Sirius XM Holdings Inc. - Common Stock|Q|N|N|100|N|N
SISI|Shineco, Inc. - Common Stock|S|N|D|100|N|N
SITM|SiTime Corporation - Common Stock|G|N|N|100|N|N
SJ|Scienjoy Holding Corporation - Class A Ordinary Shares|S|N|N|100|N|N
SKGR|SK Growth Opportunities Corporation - Class A Common Stock|G|N|N|100|N|N
SKGRU|SK Growth Opportunities Corporation - Unit|G|N|N|100|N|N
SKGRW|SK Growth Opportunities Corporation - Warrant|G|N|N|100|N|N
SKIN|The Beauty Health Company - Class A Common Stock|S|N|N|100|N|N
SKOR|FlexShares Credit-Scored US Corporate Bond Index Fund|G|N|N|100|Y|N
SKWD|Skyward Specialty Insurance Group, Inc. - Common Stock|Q|N|N|100|N|N
SKYT|SkyWater Technology, Inc. - Common Stock|S|N|N|100|N|N
SKYU|ProShares Ultra Cloud Computing|G|N|N|100|Y|N
SKYW|SkyWest, Inc. - Common Stock|Q|N|N|100|N|N
SKYX|SKYX Platforms Corp. - Common Stock|S|N|N|100|N|N
SKYY|First Trust Cloud Computing ETF|G|N|N|100|Y|N
SLAB|Silicon Laboratories, Inc. - Common Stock|Q|N|N|100|N|N
SLAC|Social Leverage Acquisition Corp I - Common stock|G|N|D|100|N|N
SLACU|Social Leverage Acquisition Corp I - Unit|G|N|D|100|N|N
SLACW|Social Leverage Acquisition Corp I - Warrant|G|N|D|100|N|N
SLAM|Slam Corp. - Class A Ordinary Share|S|N|N|100|N|N
SLAMU|Slam Corp. - Unit|S|N|N|100|N|N
SLAMW|Slam Corp. - warrant|S|N|N|100|N|N
SLDB|Solid Biosciences Inc. - Common Stock|Q|N|N|100|N|N
SLDP|Solid Power, Inc. - Class A Common Stock|Q|N|N|100|N|N
SLDPW|Solid Power, Inc. - Warrant|Q|N|N|100|N|N
SLE|Super League Enterprise, Inc. - Common Stock|S|N|N|100|N|N
SLGC|SomaLogic, Inc. - Class A Common Stock|G|N|N|100|N|N
SLGCW|SomaLogic, Inc. - Warrant|G|N|N|100|N|N
SLGL|Sol-Gel Technologies Ltd. - Common Stock|G|N|N|100|N|N
SLM|SLM Corporation - Common Stock|Q|N|N|100|N|N
SLMBP|SLM Corporation - Floating Rate Non-Cumulative Preferred Stock, Series B|Q|N|N|100|N|N
SLN|Silence Therapeutics Plc - American Depository Share|G|N|N|100|N|N
SLNA|Selina Hospitality PLC - Ordinary Shares|G|N|D|100|N|N
SLNAW|Selina Hospitality PLC - Warrant|S|N|N|100|N|N
SLNG|Stabilis Solutions, Inc. - Common Stock|S|N|N|100|N|N
SLNH|Soluna Holdings, Inc. - Common Stock|S|N|D|100|N|N
SLNHP|Soluna Holdings, Inc. - 9.0% Series A Cumulative Perpetual Preferred Stock|S|N|N|100|N|N
SLNO|Soleno Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
SLP|Simulations Plus, Inc. - Common Stock|Q|N|N|100|N|N
SLQD|iShares 0-5 Year Investment Grade Corporate Bond ETF|G|N|N|100|Y|N
SLRC|SLR Investment Corp. - Closed End Fund|Q|N|N|100|N|N
SLRN|ACELYRIN, INC. - Common Stock|Q|N|N|100|N|N
SLRX|Salarius Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
SLS|SELLAS Life Sciences Group, Inc.  - Common Stock|S|N|N|100|N|N
SLVO|Credit Suisse X-Links Silver Shares Covered Call ETNs due April 21, 2033|G|N|N|100|N|N
SMAP|SportsMap Tech Acquisition Corp. - Common Stock|G|N|N|100|N|N
SMAPU|SportsMap Tech Acquisition Corp. - Units|G|N|N|100|N|N
SMAPW|SportsMap Tech Acquisition Corp. - Warrants|G|N|N|100|N|N
SMBC|Southern Missouri Bancorp, Inc. - Common Stock|G|N|N|100|N|N
SMBK|SmartFinancial, Inc. - Common Stock|S|N|N|100|N|N
SMCI|Super Micro Computer, Inc. - Common Stock|Q|N|N|100|N|N
SMCP|AlphaMark Actively Managed Small Cap ETF|G|N|N|100|Y|N
SMFL|Smart for Life, Inc. - Common Stock|S|N|N|100|N|N
SMH|VanEck Semiconductor ETF|G|N|N|100|Y|N
SMID|Smith-Midland Corporation - Common Stock|S|N|N|100|N|N
SMLR|Semler Scientific, Inc. - Common Stock|S|N|N|100|N|N
SMMF|Summit Financial Group, Inc. - Common Stock|Q|N|N|100|N|N
SMMT|Summit Therapeutics Inc.  - Common Stock|G|N|N|100|N|N
SMPL|The Simply Good Foods Company - Common Stock|S|N|N|100|N|N
SMRI|Bushido Capital US Equity ETF|G|N|N|100|Y|N
SMSI|Smith Micro Software, Inc. - Common Stock|S|N|N|100|N|N
SMTC|Semtech Corporation - Common Stock|Q|N|N|100|N|N
SMTI|Sanara MedTech Inc. - Common Stock|S|N|N|100|N|N
SMX|SMX (Security Matters) Public Limited Company - Class A Ordinary Shares|G|N|D|100|N|N
SMXWW|SMX (Security Matters) Public Limited Company - Warrant|S|N|N|100|N|N
SNAL|Snail, Inc. - Class A Common Stock|S|N|N|100|N|N
SNAX|Stryve Foods, Inc. - Class A Common Stock|S|N|N|100|N|N
SNAXW|Stryve Foods, Inc. - Warrant|S|N|N|100|N|N
SNBR|Sleep Number Corporation - Common Stock|Q|N|N|100|N|N
SNCE|Science 37 Holdings, Inc. - Common Stock|S|N|D|100|N|N
SNCR|Synchronoss Technologies, Inc. - Common Stock|S|N|D|100|N|N
SNCRL|Synchronoss Technologies, Inc. - 8.375% Senior Notes due 2026|G|N|N|100|N|N
SNCY|Sun Country Airlines Holdings, Inc. - Common Stock|Q|N|N|100|N|N
SND|Smart Sand, Inc. - Common Stock|Q|N|N|100|N|N
SNDL|SNDL Inc. - Common Shares|S|N|N|100|N|N
SNDX|Syndax Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
SNES|SenesTech, Inc. - Common Stock|S|N|D|100|N|N
SNEX|StoneX Group Inc. - Common Stock|Q|N|N|100|N|N
SNFCA|Security National Financial Corporation - Class A Common Stock|G|N|N|100|N|N
SNGX|Soligenix, Inc. - Common Stock|S|N|D|100|N|N
SNOA|Sonoma Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
SNPO|Snap One Holdings Corp. - Common Stock|Q|N|N|100|N|N
SNPS|Synopsys, Inc. - Common Stock|Q|N|N|100|N|N
SNPX|Synaptogenix, Inc. - Common Stock|S|N|D|100|N|N
SNSE|Sensei Biotherapeutics, Inc. - Common Stock|G|N|N|100|N|N
SNSR|Global X Internet of Things ETF|G|N|N|100|Y|N
SNT|Senstar Technologies Ltd. - Ordinary Shares|G|N|N|100|N|N
SNTG|Sentage Holdings Inc. - Ordinary shares|S|N|N|100|N|N
SNTI|Senti Biosciences, Inc.  - Common Stock|G|N|D|100|N|N
SNY|Sanofi - American Depositary Shares|Q|N|N|100|N|N
SOBR|SOBR Safe, Inc. - Common Stock|S|N|N|100|N|N
SOCL|Global X Social Media ETF|G|N|N|100|Y|N
SOFI|SoFi Technologies, Inc.  - Common Stock|Q|N|N|100|N|N
SOFO|Sonic Foundry, Inc. - Common Stock|S|N|D|100|N|N
SOHO|Sotherly Hotels Inc. - Common Stock|G|N|N|100|N|N
SOHOB|Sotherly Hotels Inc. - 8.0% Series B Cumulative Redeemable Perpetual Preferred Stock|G|N|N|100|N|N
SOHON|Sotherly Hotels Inc. - 8.25% Series D Cumulative Redeemable Perpetual Preferred Stock|G|N|N|100|N|N
SOHOO|Sotherly Hotels Inc. - 7.875% Series C Cumulative Redeemable Perpetual Preferred Stock|G|N|N|100|N|N
SOHU|Sohu.com Limited  - American Depositary Shares|Q|N|N|100|N|N
SOLO|Electrameccanica Vehicles Corp. Ltd. - Common Stock|S|N|D|100|N|N
SOND|Sonder Holdings Inc. - Class A Common Stock|Q|N|N|100|N|N
SONDW|Sonder Holdings Inc. - Warrants|Q|N|N|100|N|N
SONM|Sonim Technologies, Inc. - Common Stock|S|N|D|100|N|N
SONN|Sonnet BioTherapeutics Holdings, Inc. - Common Stock|S|N|N|100|N|N
SONO|Sonos, Inc. - Common Stock|Q|N|N|100|N|N
SOPA|Society Pass Incorporated - Common Stock|S|N|D|100|N|N
SOPH|SOPHiA GENETICS SA - Ordinary Shares|Q|N|N|100|N|N
SOTK|Sono-Tek Corporation - Common Stock|S|N|N|100|N|N
SOUN|SoundHound AI, Inc. - Class A Common Stock|G|N|N|100|N|N
SOUNW|SoundHound AI, Inc. - Warrant|G|N|N|100|N|N
SOVO|Sovos Brands, Inc. - Common Stock|Q|N|N|100|N|N
SOXQ|Invesco PHLX Semiconductor ETF|G|N|N|100|Y|N
SOXX|iShares Semiconductor ETF|G|N|N|100|Y|N
SP|SP Plus Corporation - Common Stock|Q|N|N|100|N|N
SPAQ|Horizon Kinetics SPAC Active ETF|G|N|N|100|Y|N
SPBC|Simplify U.S. Equity PLUS GBTC ETF|G|N|N|100|Y|N
SPC|CrossingBridge Pre-Merger SPAC ETF|G|N|N|100|Y|N
SPCB|SuperCom, Ltd. - Ordinary Shares|S|N|D|100|N|N
SPCX|AXS SPAC and New Issue ETF|G|N|N|100|Y|N
SPFI|South Plains Financial, Inc. - Common Stock|Q|N|N|100|N|N
SPGC|Sacks Parente Golf, Inc. - Common Stock|S|N|N|100|N|N
SPI|SPI Energy Co., Ltd. - Ordinary Shares|Q|N|N|100|N|N
SPKLU|Spark I Acquisition Corp. - Unit|G|N|N|100|N|N
SPLK|Splunk Inc. - Common Stock|Q|N|N|100|N|N
SPNS|Sapiens International Corporation N.V. - Common Shares|Q|N|N|100|N|N
SPOK|Spok Holdings, Inc. - Common Stock|Q|N|N|100|N|N
SPPL|SIMPPLE LTD. - Ordinary Shares|S|N|N|100|N|N
SPRB|Spruce Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
SPRC|SciSparc Ltd. - Ordinary Shares|S|N|N|100|N|N
SPRO|Spero Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
SPRX|Spear Alpha ETF|G|N|N|100|Y|N
SPRY|ARS Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
SPSC|SPS Commerce, Inc. - Common Stock|Q|N|N|100|N|N
SPT|Sprout Social, Inc - Class A Common Stock|S|N|N|100|N|N
SPTN|SpartanNash Company - Common Stock|Q|N|N|100|N|N
SPWH|Sportsman's Warehouse Holdings, Inc. - Common Stock|Q|N|N|100|N|N
SPWR|SunPower Corporation - Common Stock|Q|N|N|100|N|N
SQFT|Presidio Property Trust, Inc. - Class A Common Stock|S|N|D|100|N|N
SQFTP|Presidio Property Trust, Inc. - 9.375% Series D Cumulative Redeemable Perpetual Preferred Stock, $0.01 par value per share|S|N|N|100|N|N
SQFTW|Presidio Property Trust, Inc. - Series A Common Stock Purchase Warrants|S|N|N|100|N|N
SQL|SeqLL Inc. - Common stock|S|N|D|100|N|N
SQLLW|SeqLL Inc. - Warrant|S|N|N|100|N|N
SQLV|Royce Quant Small-Cap Quality Value ETF|G|N|N|100|Y|N
SQQQ|ProShares UltraPro Short QQQ|G|N|N|100|Y|N
SRAD|Sportradar Group AG - Class A Ordinary Shares|Q|N|N|100|N|N
SRBK|SR Bancorp, Inc. - Common stock|S|N|N|100|N|N
SRCE|1st Source Corporation - Common Stock|Q|N|N|100|N|N
SRCL|Stericycle, Inc. - Common Stock|Q|N|N|100|N|N
SRDX|Surmodics, Inc. - Common Stock|Q|N|N|100|N|N
SRET|Global X SuperDividend REIT ETF|G|N|N|100|Y|N
SRM|SRM Entertainment, Inc. - Common Stock|S|N|N|100|N|N
SRPT|Sarepta Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
SRRK|Scholar Rock Holding Corporation - Common Stock|Q|N|N|100|N|N
SRTS|Sensus Healthcare, Inc. - Common Stock|S|N|N|100|N|N
SRZN|Surrozen, Inc. - Common Stock|S|N|D|100|N|N
SRZNW|Surrozen, Inc. - Warrant|S|N|N|100|N|N
SSB|SouthState Corporation - Common Stock|Q|N|N|100|N|N
SSBI|Summit State Bank - Common Stock|G|N|N|100|N|N
SSBK|Southern States Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
SSIC|Silver Spike Investment Corp. - Common Stock|G|N|N|100|N|N
SSKN|Strata Skin Sciences, Inc. - Common Stock|S|N|D|100|N|N
SSNC|SS&C Technologies Holdings, Inc. - Common Stock|Q|N|N|100|N|N
SSNT|SilverSun Technologies, Inc. - Common Stock|S|N|N|100|N|N
SSP|E.W. Scripps Company (The) - Class A Common Stock|Q|N|N|100|N|N
SSRM|SSR Mining Inc. - Common Stock|Q|N|N|100|N|N
SSSS|SuRo Capital Corp. - Closed End Fund|Q|N|N|100|N|N
SSSSL|SuRo Capital Corp. - 6.00% Notes due 2026|G|N|N|100|N|N
SSTI|SoundThinking, Inc. - Common Stock|S|N|N|100|N|N
SSYS|Stratasys, Ltd. - Common Stock|Q|N|N|100|N|N
STAA|STAAR Surgical Company - Common Stock|G|N|N|100|N|N
STAF|Staffing 360 Solutions, Inc. - Common Stock|S|N|H|100|N|N
STBA|S&T Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
STBX|Starbox Group Holdings Ltd. - Ordinary Shares|S|N|N|100|N|N
STCN|Steel Connect, Inc. - Common Stock|S|N|N|100|N|N
STEP|StepStone Group Inc. - Class A Common Stock|Q|N|N|100|N|N
STER|Sterling Check Corp. - Common Stock|Q|N|N|100|N|N
STGW|Stagwell Inc. - Class A Common Stock|Q|N|N|100|N|N
STHO|Star Holdings - Shares of Beneficial Interest|G|N|N|100|N|N
STIM|Neuronetics, Inc. - Common Stock|G|N|N|100|N|N
STIX|Semantix, Inc. - Ordinary Shares|G|N|N|100|N|N
STIXW|Semantix, Inc. - Warrant|G|N|N|100|N|N
STKH|Steakholder Foods Ltd. - American Depositary Shares|S|N|N|100|N|N
STKL|SunOpta, Inc. - Common Stock|Q|N|N|100|N|N
STKS|The ONE Group Hospitality, Inc. - Common Stock|S|N|N|100|N|N
STLD|Steel Dynamics, Inc. - Common Stock|Q|N|N|100|N|N
STNE|StoneCo Ltd. - Class A Common Share|Q|N|N|100|N|N
STOK|Stoke Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
STRA|Strategic Education, Inc. - Common Stock|Q|N|N|100|N|N
STRC|Sarcos Technology and Robotics Corporation - Common stock|G|N|N|100|N|N
STRCW|Sarcos Technology and Robotics Corporation - Warrant|G|N|N|100|N|N
STRL|Sterling Infrastructure, Inc. - Common Stock|Q|N|N|100|N|N
STRM|Streamline Health Solutions, Inc. - Common Stock|S|N|N|100|N|N
STRO|Sutro Biopharma, Inc. - Common Stock|G|N|N|100|N|N
STRR|Star Equity Holdings, Inc. - Common Stock|G|N|N|100|N|N
STRRP|Star Equity Holdings, Inc. - Series A Cumulative Perpetual Preferred Stock|G|N|N|100|N|N
STRS|Stratus Properties Inc. - Common Stock|Q|N|N|100|N|N
STRT|STRATTEC SECURITY CORPORATION - Common Stock|G|N|N|100|N|N
STSS|Sharps Technology Inc. - Common Stock|S|N|D|100|N|N
STSSW|Sharps Technology Inc. - Warrant|S|N|N|100|N|N
STTK|Shattuck Labs, Inc. - Common Stock|Q|N|N|100|N|N
STX|Seagate Technology Holdings PLC - Ordinary Shares (Ireland)|Q|N|N|100|N|N
STXD|Strive 1000 Dividend Growth ETF|G|N|N|100|Y|N
STXG|Strive 1000 Growth ETF|G|N|N|100|Y|N
STXK|Strive Small-Cap ETF|G|N|N|100|Y|N
STXV|Strive 1000 Value ETF|G|N|N|100|Y|N
SUNW|Sunworks, Inc. - Common Stock|S|N|D|100|N|N
SUPN|Supernus Pharmaceuticals, Inc. - Common Stock|G|N|N|100|N|N
SURG|SurgePays, Inc. - Common Stock|S|N|N|100|N|N
SURGW|SurgePays, Inc. - Warrant|S|N|N|100|N|N
SUSB|iShares ESG Aware 1-5 Year USD Corporate Bond ETF|G|N|N|100|Y|N
SUSC|iShares ESG Aware USD Corporate Bond ETF|G|N|N|100|Y|N
SUSL|iShares ESG MSCI USA Leaders ETF|G|N|N|100|Y|N
SVA|Sinovac Biotech, Ltd. - Ordinary Shares (Antigua/Barbudo)|Q|N|N|100|N|N
SVC|Service Properties Trust - Shares of Beneficial Interest|Q|N|N|100|N|N
SVFD|Save Foods, Inc. - Common Stock|S|N|D|100|N|N
SVII|Spring Valley Acquisition Corp. II - Class A Ordinary Shares|G|N|N|100|N|N
SVIIR|Spring Valley Acquisition Corp. II - Rights|G|N|N|100|N|N
SVIIU|Spring Valley Acquisition Corp. II - Units|G|N|N|100|N|N
SVIIW|Spring Valley Acquisition Corp. II - Warrant|G|N|N|100|N|N
SVRA|Savara, Inc. - Common Stock|Q|N|N|100|N|N
SVRE|SaverOne 2014 Ltd. - American Depositary Shares|S|N|N|100|N|N
SVREW|SaverOne 2014 Ltd. - Warrant|S|N|N|100|N|N
SVVC|Firsthand Technology Value Fund, Inc. - Closed End Fund|Q|N|D|100|N|N
SWAG|Stran & Company, Inc. - Common Stock|S|N|N|100|N|N
SWAGW|Stran & Company, Inc. - Warrant|S|N|N|100|N|N
SWAV|ShockWave Medical, Inc. - Common Stock|Q|N|N|100|N|N
SWBI|Smith & Wesson Brands, Inc. - Common Stock|Q|N|N|100|N|N
SWIM|Latham Group, Inc. - Common Stock|Q|N|N|100|N|N
SWIN|Solowin Holdings - Ordinary Share|S|N|N|100|N|N
SWKH|SWK Holdings Corporation - Common Stock|G|N|N|100|N|N
SWKHL|SWK Holdings Corporation - 9.00% Senior Notes due 2027|G|N|N|100|N|N
SWKS|Skyworks Solutions, Inc. - Common Stock|Q|N|N|100|N|N
SWSS|Clean Energy Special Situations Corp.  - Common stock|S|N|E|100|N|N
SWSSU|Clean Energy Special Situations Corp.  - Unit|S|N|E|100|N|N
SWSSW|Clean Energy Special Situations Corp.  - Warrant|S|N|E|100|N|N
SWTX|SpringWorks Therapeutics, Inc. - common stock|Q|N|N|100|N|N
SWVL|Swvl Holdings Corp - Class A Common Shares|S|N|E|100|N|N
SWVLW|Swvl Holdings Corp - Warrant|S|N|E|100|N|N
SXTC|China SXT Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
SXTP|60 Degrees Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
SXTPW|60 Degrees Pharmaceuticals, Inc. - Warrant|S|N|N|100|N|N
SY|So-Young International Inc. - American Depository Shares|G|N|N|100|N|N
SYBT|Stock Yards Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
SYBX|Synlogic, Inc. - Common Stock|S|N|N|100|N|N
SYM|Symbotic Inc. - Class A Common Stock|G|N|N|100|N|N
SYNA|Synaptics Incorporated - Common Stock|Q|N|N|100|N|N
SYPR|Sypris Solutions, Inc. - Common Stock|G|N|N|100|N|N
SYRA|Syra Health Corp. - Class A Common Stock|S|N|N|100|N|N
SYRS|Syros Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
SYT|SYLA Technologies Co., Ltd. - American Depositary Shares|S|N|N|100|N|N
SYTA|Siyata Mobile, Inc. - Common Shares|S|N|N|100|N|N
SYTAW|Siyata Mobile, Inc. - Warrant|S|N|N|100|N|N
SZZL|Sizzle Acquisition Corp. - Common stock|G|N|N|100|N|N
SZZLU|Sizzle Acquisition Corp. - Unit|G|N|N|100|N|N
SZZLW|Sizzle Acquisition Corp. - Warrant|G|N|N|100|N|N
TACT|TransAct Technologies Incorporated - Common Stock|G|N|N|100|N|N
TAIT|Taitron Components Incorporated - Class A Common Stock|S|N|N|100|N|N
TALK|Talkspace, Inc. - Common Stock|S|N|N|100|N|N
TALKW|Talkspace, Inc. - Warrant|S|N|N|100|N|N
TALS|Talaris Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
TANH|Tantech Holdings Ltd. - Common Shares|S|N|N|100|N|N
TAOP|Taoping Inc. - Ordinary Shares|S|N|N|100|N|N
TARA|Protara Therapeutics, Inc.  - Common Stock|G|N|N|100|N|N
TARK|AXS 2X Innovation ETF|G|N|N|100|Y|N
TARS|Tarsus Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
TASK|TaskUs, Inc. - Class A Common Stock|Q|N|N|100|N|N
TAST|Carrols Restaurant Group, Inc. - Common Stock|Q|N|N|100|N|N
TATT|TAT Technologies Ltd. - Ordinary Shares|G|N|N|100|N|N
TAYD|Taylor Devices, Inc. - Common Stock|S|N|N|100|N|N
TBBK|The Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
TBCP|Thunder Bridge Capital Partners III Inc. - Class A Common Stock|S|N|D|100|N|N
TBCPU|Thunder Bridge Capital Partners III Inc. - Units|S|N|D|100|N|N
TBCPW|Thunder Bridge Capital Partners III Inc. - Warrant|S|N|D|100|N|N
TBIL|US Treasury 3 Month Bill ETF|G|N|N|100|Y|N
TBIO|Telesis Bio, Inc. - Common Stock|Q|N|N|100|N|N
TBLA|Taboola.com Ltd. - Ordinary Shares|Q|N|N|100|N|N
TBLAW|Taboola.com Ltd. - Warrant|Q|N|N|100|N|N
TBLD|Thornburg Income Builder Opportunities Trust - Closed End Fund|Q|N|N|100|N|N
TBLT|ToughBuilt Industries, Inc. - Common Stock|S|N|D|100|N|N
TBLTW|ToughBuilt Industries, Inc. - Warrant|S|N|N|100|N|N
TBMC|Trailblazer Merger Corporation I - Class A Common Stock|G|N|N|100|N|N
TBMCR|Trailblazer Merger Corporation I - Rights|G|N|N|100|N|N
TBNK|Territorial Bancorp Inc. - Common Stock|Q|N|N|100|N|N
TBPH|Theravance Biopharma, Inc. - Ordinary Shares|G|N|N|100|N|N
TC|TuanChe Limited - American Depositary Shares|S|N|D|100|N|N
TCBC|TC Bancshares, Inc. - Common Stock|S|N|N|100|N|N
TCBI|Texas Capital Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
TCBIO|Texas Capital Bancshares, Inc. - Depositary Shares 5.75% Fixed Rate Non-Cumulative Perpetual Preferred Stock Series B|Q|N|N|100|N|N
TCBK|TriCo Bancshares - Common Stock|Q|N|N|100|N|N
TCBP|TC BioPharm (Holdings) plc - American Depositary Shares|S|N|D|100|N|N
TCBPW|TC BioPharm (Holdings) plc - Warrants|S|N|N|100|N|N
TCBS|Texas Community Bancshares, Inc. - Common Stock|S|N|N|100|N|N
TCBX|Third Coast Bancshares, Inc. - Common Stock|Q|N|N|100|N|N
TCHI|iShares MSCI China Multisector Tech ETF|G|N|N|100|Y|N
TCJH|Top KingWin Ltd - Class A Ordinary Shares|S|N|N|100|N|N
TCMD|Tactile Systems Technology, Inc. - Common Stock|G|N|N|100|N|N
TCOM|Trip.com Group Limited - American Depositary Shares|Q|N|N|100|N|N
TCON|TRACON Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
TCPC|BlackRock TCP Capital Corp. - Closed End Fund|Q|N|N|100|N|N
TCRT|Alaunos Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
TCRX|TScan Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
TCX|Tucows Inc. - Common Stock|S|N|N|100|N|N
TDIV|First Trust NASDAQ Technology Dividend Index Fund|G|N|N|100|Y|N
TDSA|Cabana Target Drawdown 5 ETF|G|N|N|100|Y|N
TDSB|Cabana Target Drawdown 7 ETF|G|N|N|100|Y|N
TDSC|Cabana Target Drawdown 10 ETF|G|N|N|100|Y|N
TDSD|Cabana Target Drawdown 13 ETF|G|N|N|100|Y|N
TDSE|Cabana Target Drawdown 16 ETF|G|N|N|100|Y|N
TDUP|ThredUp Inc. - Class A Common Stock|Q|N|N|100|N|N
TEAM|Atlassian Corporation  - Class A Common Stock|Q|N|N|100|N|N
TECH|Bio-Techne Corp - Common Stock|Q|N|N|100|N|N
TECTP|Tectonic Financial, Inc. - 9.00% Fixed-to-Floating Rate Series B Non-Cumulative Perpetual Preferred Stock|S|N|N|100|N|N
TEDU|Tarena International, Inc. - American Depositary Shares|Q|N|D|100|N|N
TELA|TELA Bio, Inc. - Common stock|G|N|N|100|N|N
TENB|Tenable Holdings, Inc. - Common Stock|Q|N|N|100|N|N
TENK|TenX Keane Acquisition - Ordinary Share|G|N|N|100|N|N
TENKR|TenX Keane Acquisition - Right|G|N|N|100|N|N
TENKU|TenX Keane Acquisition - Unit|G|N|N|100|N|N
TENX|Tenax Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
TER|Teradyne, Inc. - Common Stock|Q|N|N|100|N|N
TERN|Terns Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
TETE|Technology & Telecommunication Acquisition Corporation - Class A Ordinary Shares|G|N|D|100|N|N
TETEU|Technology & Telecommunication Acquisition Corporation - Unit|G|N|D|100|N|N
TETEW|Technology & Telecommunication Acquisition Corporation - Warrant|G|N|D|100|N|N
TFFP|TFF Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
TFIN|Triumph Financial, Inc. - Common Stock|Q|N|N|100|N|N
TFINP|Triumph Financial, Inc. - Depositary Shares, Each Representing a 1/40th Interest in a Share of Series C Fixed-Rate Non-Cumulative Perpetual Preferred Stock|Q|N|N|100|N|N
TFSL|TFS Financial Corporation - Common Stock|Q|N|N|100|N|N
TGAA|Target Global Acquisition I Corp. - Class A Ordinary Share|G|N|N|100|N|N
TGAAU|Target Global Acquisition I Corp. - Unit|G|N|N|100|N|N
TGAAW|Target Global Acquisition I Corp. - Warrant|G|N|D|100|N|N
TGAN|Transphorm, Inc. - Common Stock|S|N|N|100|N|N
TGL|Treasure Global Inc. - Common Stock|S|N|D|100|N|N
TGTX|TG Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
TGVC|TG Venture Acquisition Corp. - Class A Common Stock|G|N|D|100|N|N
TGVCU|TG Venture Acquisition Corp. - Units|G|N|D|100|N|N
TGVCW|TG Venture Acquisition Corp. - Warrants|G|N|D|100|N|N
TH|Target Hospitality Corp. - Common Stock|S|N|N|100|N|N
THAR|Tharimmune, Inc. - Common Stock|S|N|D|100|N|N
THCH|TH International Limited - Ordinary shares|S|N|N|100|N|N
THCP|Thunder Bridge Capital Partners IV, Inc. - Class A Common Stock|G|N|N|100|N|N
THCPU|Thunder Bridge Capital Partners IV, Inc. - Unit|G|N|N|100|N|N
THCPW|Thunder Bridge Capital Partners IV, Inc. - Warrant|G|N|N|100|N|N
THFF|First Financial Corporation Indiana - Common Stock|Q|N|N|100|N|N
THMO|ThermoGenesis Holdings, Inc. - Common Stock|S|N|N|100|N|N
THRD|Third Harmonic Bio, Inc. - Common Stock|G|N|N|100|N|N
THRM|Gentherm Inc - Common Stock|Q|N|N|100|N|N
THRX|Theseus Pharmaceuticals, Inc. - Common Stock|Q|N|N|100|N|N
THRY|Thryv Holdings, Inc. - Common Stock|S|N|N|100|N|N
THTX|Theratechnologies Inc. - Common Shares|S|N|N|100|N|N
THWWW|Target Hospitality Corp. - Warrant expiring 3/15/2024|S|N|N|100|N|N
TIGO|Millicom International Cellular S.A. - Common Stock|Q|N|N|100|N|N
TIGR|UP Fintech Holding Limited - American Depositary Shares representing fifteen Class A Ordinary Shares|Q|N|N|100|N|N
TIL|Instil Bio, Inc. - Common Stock|S|N|D|100|N|N
TILE|Interface, Inc. - Common Stock|Q|N|N|100|N|N
TIO|Tingo Group, Inc. - Common Stock|S|N|N|100|N|N
TIPT|Tiptree Inc. - Common Stock|S|N|N|100|N|N
TIRX|TIAN RUIXIANG Holdings Ltd - Class A Ordinary Shares|S|N|N|100|N|N
TITN|Titan Machinery Inc. - Common Stock|Q|N|N|100|N|N
TIVC|Tivic Health Systems, Inc. - Common stock|S|N|N|100|N|N
TKLF|Yoshitsu Co., Ltd - American Depositary Shares|S|N|N|100|N|N
TKNO|Alpha Teknova, Inc. - Common Stock|G|N|N|100|N|N
TLF|Tandy Leather Factory, Inc. - common stock|S|N|N|100|N|N
TLGY|TLGY Acquisition Corporation - Class A Ordinary Share|G|N|D|100|N|N
TLGYU|TLGY Acquisition Corporation - Unit|G|N|N|100|N|N
TLGYW|TLGY Acquisition Corporation - Warrant|G|N|N|100|N|N
TLIS|Talis Biomedical Corporation - common stock|S|N|N|100|N|N
TLRY|Tilray Brands, Inc. - Common Stock|Q|N|N|100|N|N
TLS|Telos Corporation - Common Stock|G|N|N|100|N|N
TLSA|Tiziana Life Sciences Ltd - Common Shares|S|N|D|100|N|N
TLSI|TriSalus Life Sciences, Inc. - Common Stock|G|N|N|100|N|N
TLSIW|TriSalus Life Sciences, Inc. - Warrant|G|N|N|100|N|N
TLT|iShares 20+ Year Treasury Bond ETF|G|N|N|100|Y|N
TMC|TMC the metals company Inc. - Common Stock|Q|N|N|100|N|N
TMCI|Treace Medical Concepts, Inc. - Common Stock|Q|N|N|100|N|N
TMCWW|TMC the metals company Inc. - Warrant|Q|N|N|100|N|N
TMDX|TransMedics Group, Inc. - Common Stock|G|N|N|100|N|N
TMET|iShares Transition-Enabling Metals ETF|G|N|N|100|Y|N
TMPO|Tempo Automation Holdings, Inc. - Common Stock|G|N|H|100|N|N
TMPOW|Tempo Automation Holdings, Inc. - Warrant|G|N|H|100|N|N
TMTC|TMT Acquisition Corp - Ordinary Shares|G|N|N|100|N|N
TMTCR|TMT Acquisition Corp - Rights|G|N|N|100|N|N
TMTCU|TMT Acquisition Corp - Unit|G|N|N|100|N|N
TMUS|T-Mobile US, Inc. - Common Stock|Q|N|N|100|N|N
TNDM|Tandem Diabetes Care, Inc. - Common Stock|G|N|N|100|N|N
TNGX|Tango Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
TNON|Tenon Medical, Inc. - Common Stock|S|N|D|100|N|N
TNONW|Tenon Medical, Inc. - Warrant|S|N|N|100|N|N
TNXP|Tonix Pharmaceuticals Holding Corp. - Common Stock|S|N|N|100|N|N
TNYA|Tenaya Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
TOI|The Oncology Institute, Inc. - Common Stock|S|N|N|100|N|N
TOIIW|The Oncology Institute, Inc. - Warrant|S|N|N|100|N|N
TOMZ|TOMI Environmental Solutions, Inc. - Common Stock|S|N|N|100|N|N
TOP|TOP Financial Group Limited - Ordinary Shares|S|N|N|100|N|N
TOPS|TOP Ships Inc. - Common Stock|S|N|N|100|N|N
TORO|Toro Corp. - Common stock|S|N|N|100|N|N
TOUR|Tuniu Corporation - American Depositary Shares|G|N|N|100|N|N
TOWN|Towne Bank - Common Stock|Q|N|N|100|N|N
TPCS|TechPrecision Corporation - Common stock|S|N|N|100|N|N
TPG|TPG Inc. - Class A Common Stock|Q|N|N|100|N|N
TPIC|TPI Composites, Inc. - Common Stock|G|N|N|100|N|N
TPST|Tempest Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
TQQQ|ProShares UltraPro QQQ|G|N|N|100|Y|N
TRDA|Entrada Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
TREE|LendingTree, Inc. - Common Stock|Q|N|N|100|N|N
TRHC|Tabula Rasa HealthCare, Inc. - Common Stock|G|N|N|100|N|N
TRIB|Trinity Biotech plc - American Depositary Shares each representing 4 A Ordinary Shares|Q|N|D|100|N|N
TRIN|Trinity Capital Inc. - Common Stock|Q|N|N|100|N|N
TRINL|Trinity Capital Inc. - 7.00% Notes Due 2025|G|N|N|100|N|N
TRIP|TripAdvisor, Inc. - Common Stock|Q|N|N|100|N|N
TRKA|Troika Media Group, Inc. - Common Stock|S|N|E|100|N|N
TRKAW|Troika Media Group, Inc. - Warrant|S|N|E|100|N|N
TRMB|Trimble Inc. - Common Stock|Q|N|N|100|N|N
TRMD|TORM plc - Class A Common Stock|Q|N|N|100|N|N
TRMK|Trustmark Corporation - Common Stock|Q|N|N|100|N|N
TRMR|Tremor International Ltd. - American Depository Shares|G|N|N|100|N|N
TRNR|Interactive Strength Inc. - Common Stock|G|N|D|100|N|N
TRNS|Transcat, Inc. - Common Stock|G|N|N|100|N|N
TRON|Corner Growth Acquisition Corp. 2 - Class A Ordinary Share|S|N|N|100|N|N
TRONU|Corner Growth Acquisition Corp. 2 - Units|S|N|N|100|N|N
TRONW|Corner Growth Acquisition Corp. 2 - Warrants|S|N|N|100|N|N
TROO|TROOPS, Inc.  - Ordinary Shares|S|N|N|100|N|N
TROW|T. Rowe Price Group, Inc. - Common Stock|Q|N|N|100|N|N
TRS|TriMas Corporation - Common Stock|Q|N|N|100|N|N
TRST|TrustCo Bank Corp NY - Common Stock|Q|N|N|100|N|N
TRUE|TrueCar, Inc. - Common Stock|Q|N|N|100|N|N
TRUP|Trupanion, Inc. - Common Stock|G|N|N|100|N|N
TRVG|trivago N.V. - American Depositary Shares|Q|N|N|100|N|N
TRVI|Trevi Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
TRVN|Trevena, Inc. - Common Stock|S|N|D|100|N|N
TSAT|Telesat Corporation - Class A Common Shares and Class B Variable Voting Shares|Q|N|N|100|N|N
TSBK|Timberland Bancorp, Inc. - Common Stock|G|N|N|100|N|N
TSBX|Turnstone Biologics Corp. - Common Stock|G|N|N|100|N|N
TSCO|Tractor Supply Company - Common Stock|Q|N|N|100|N|N
TSDD|GraniteShares 1.5x Short TSLA Daily ETF|G|N|N|100|Y|N
TSEM|Tower Semiconductor Ltd. - Ordinary Shares|Q|N|N|100|N|N
TSHA|Taysha Gene Therapies, Inc. - Common Stock|Q|N|N|100|N|N
TSL|GraniteShares 1.25x Long TSLA Daily ETF|G|N|N|100|Y|N
TSLA|Tesla, Inc.  - Common Stock|Q|N|N|100|N|N
TSLL|Direxion Daily TSLA Bull 1.5X Shares|G|N|N|100|Y|N
TSLQ|AXS TSLA Bear Daily ETF|G|N|N|100|Y|N
TSLR|GraniteShares 1.75x Long TSLA Daily ETF|G|N|N|100|Y|N
TSLS|Direxion Daily TSLA Bear 1X Shares|G|N|N|100|Y|N
TSP|TuSimple Holdings Inc. - Class A Common Stock|Q|N|N|100|N|N
TSRI|TSR, Inc. - Common Stock|S|N|N|100|N|N
TSVT|2seventy bio, Inc. - Common Stock|Q|N|N|100|N|N
TTD|The Trade Desk, Inc. - Class A Common Stock|G|N|N|100|N|N
TTEC|TTEC Holdings, Inc. - Common Stock|Q|N|N|100|N|N
TTEK|Tetra Tech, Inc. - Common Stock|Q|N|N|100|N|N
TTGT|TechTarget, Inc. - Common Stock|G|N|N|100|N|N
TTMI|TTM Technologies, Inc. - Common Stock|Q|N|N|100|N|N
TTNP|Titan Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
TTOO|T2 Biosystems, Inc. - Common Stock|S|N|D|100|N|N
TTSH|Tile Shop Holdings, Inc. - Common Stock|S|N|N|100|N|N
TTWO|Take-Two Interactive Software, Inc. - Common Stock|Q|N|N|100|N|N
TUG|STF Tactical Growth ETF|G|N|N|100|Y|N
TUGN|STF Tactical Growth & Income ETF|G|N|N|100|Y|N
TUR|iShares MSCI Turkey ETF|G|N|N|100|Y|N
TURB|Turbo Energy, S.A. - American Depositary Shares|S|N|N|100|N|N
TURN|180 Degree Capital Corp. - Closed End Fund|G|N|N|100|N|N
TUSK|Mammoth Energy Services, Inc. - Common Stock|Q|N|N|100|N|N
TVTX|Travere Therapeutics, Inc. - Common Stock|G|N|N|100|N|N
TW|Tradeweb Markets Inc. - Class A Common Stock|Q|N|N|100|N|N
TWEB|SoFi Web 3 ETF|G|N|N|100|Y|N
TWIN|Twin Disc, Incorporated - Common Stock|Q|N|N|100|N|N
TWKS|Thoughtworks Holding, Inc. - Common Stock|Q|N|N|100|N|N
TWLV|Twelve Seas Investment Company II - Class A Common Stock|S|N|N|100|N|N
TWLVU|Twelve Seas Investment Company II - Unit|S|N|N|100|N|N
TWLVW|Twelve Seas Investment Company II - Warrant|S|N|N|100|N|N
TWNK|Hostess Brands, Inc. - Class A Common Stock|S|N|N|100|N|N
TWOU|2U, Inc. - Common Stock|Q|N|N|100|N|N
TWST|Twist Bioscience Corporation - Common Stock|Q|N|N|100|N|N
TXG|10x Genomics, Inc. - Common Stock|Q|N|N|100|N|N
TXMD|TherapeuticsMD, Inc. - Common Stock|Q|N|N|100|N|N
TXN|Texas Instruments Incorporated - Common Stock|Q|N|N|100|N|N
TXRH|Texas Roadhouse, Inc. - Common Stock|Q|N|N|100|N|N
TYGO|Tigo Energy, Inc. - Common Stock|S|N|N|100|N|N
TYRA|Tyra Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
TZOO|Travelzoo - Common Stock|Q|N|N|100|N|N
UAE|iShares MSCI UAE ETF|G|N|N|100|Y|N
UAL|United Airlines Holdings, Inc. - Common Stock|Q|N|N|100|N|N
UBCP|United Bancorp, Inc. - Common Stock|S|N|N|100|N|N
UBFO|United Security Bancshares - Common Stock|Q|N|N|100|N|N
UBND|VictoryShares Core Plus Intermediate Bond ETF|G|N|N|100|Y|N
UBSI|United Bankshares, Inc. - Common Stock|Q|N|N|100|N|N
UBX|Unity Biotechnology, Inc. - Common Stock|Q|N|N|100|N|N
UCAR|U Power Limited - Ordinary Shares|S|N|N|100|N|N
UCBI|United Community Banks, Inc. - Common Stock|Q|N|N|100|N|N
UCBIO|United Community Banks, Inc. - Depositary Shares each representing 1/1,000th interest in a share of Series I Non-Cumulative Preferred Stock|Q|N|N|100|N|N
UCL|uCloudlink Group Inc. - American Depositary Shares|G|N|N|100|N|N
UCRD|VictoryShares Corporate Bond ETF|G|N|N|100|Y|N
UCTT|Ultra Clean Holdings, Inc. - Common Stock|Q|N|N|100|N|N
UCYB|ProShares Ultra Nasdaq Cybersecurity|G|N|N|100|Y|N
UDMY|Udemy, Inc. - Common Stock|Q|N|N|100|N|N
UEIC|Universal Electronics Inc. - Common Stock|Q|N|N|100|N|N
UEVM|VictoryShares Emerging Markets Value Momentum ETF|G|N|N|100|Y|N
UFCS|United Fire Group, Inc - Common Stock|Q|N|N|100|N|N
UFIV|US Treasury 5 Year Note ETF|G|N|N|100|Y|N
UFO|Procure Space ETF|G|N|N|100|Y|N
UFPI|UFP Industries, Inc. - Common Stock|Q|N|N|100|N|N
UFPT|UFP Technologies, Inc. - Common Stock|S|N|N|100|N|N
UG|United-Guardian, Inc. - Common Stock|G|N|N|100|N|N
UGRO|urban-gro, Inc. - Common Stock|S|N|N|100|N|N
UHG|United Homes Group, Inc - Class A Common Stock|G|N|N|100|N|N
UHGWW|United Homes Group, Inc - Warrant|S|N|N|100|N|N
UITB|VictoryShares Core Intermediate Bond ETF|G|N|N|100|Y|N
UIVM|VictoryShares International Value Momentum ETF|G|N|N|100|Y|N
UK|Ucommune International Ltd  - Ordinary Shares|S|N|D|100|N|N
UKOMW|Ucommune International Ltd  - Warrant expiring 11/17/2025|S|N|N|100|N|N
ULBI|Ultralife Corporation - Common Stock|G|N|N|100|N|N
ULCC|Frontier Group Holdings, Inc. - Common Stock|Q|N|N|100|N|N
ULH|Universal Logistics Holdings, Inc. - Common Stock|Q|N|N|100|N|N
ULTA|Ulta Beauty, Inc. - Common Stock|Q|N|N|100|N|N
ULVM|VictoryShares US Value Momentum ETF|G|N|N|100|Y|N
UMBF|UMB Financial Corporation - Common Stock|Q|N|N|100|N|N
UMMA|Wahed Dow Jones Islamic World ETF|G|N|N|100|Y|N
UNB|Union Bankshares, Inc. - Common Stock|G|N|N|100|N|N
UNCY|Unicycive Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
UNIT|Uniti Group Inc. - Common Stock|Q|N|N|100|N|N
UNIY|WisdomTree Voya Yield Enhanced USD Universal Bond Fund|G|N|N|100|Y|N
UNTY|Unity Bancorp, Inc. - Common Stock|G|N|N|100|N|N
UONE|Urban One, Inc.  - Class A Common Stock|S|N|E|100|N|N
UONEK|Urban One, Inc.  - Class D Common Stock|S|N|E|100|N|N
UPBD|Upbound Group, Inc. - Common Stock|Q|N|N|100|N|N
UPC|Universe Pharmaceuticals Inc - Ordinary Shares|G|N|D|100|N|N
UPGR|Xtrackers US Green Infrastructure Select Equity ETF|G|N|N|100|Y|N
UPLD|Upland Software, Inc. - Common Stock|G|N|N|100|N|N
UPST|Upstart Holdings, Inc. - Common stock|Q|N|N|100|N|N
UPWD|JPMorgan Social Advancement ETF|G|N|N|100|Y|N
UPWK|Upwork Inc. - Common Stock|Q|N|N|100|N|N
UPXI|Upexi, Inc. - Common Stock|S|N|N|100|N|N
URBN|Urban Outfitters, Inc. - Common Stock|Q|N|N|100|N|N
URGN|UroGen Pharma Ltd. - Ordinary Shares|G|N|N|100|N|N
URNJ|Sprott Junior Uranium Miners ETF|G|N|N|100|Y|N
UROY|Uranium Royalty Corp. - Common Stock|S|N|N|100|N|N
USAP|Universal Stainless & Alloy Products, Inc. - Common Stock|Q|N|N|100|N|N
USAU|U.S. Gold Corp. - Common Stock|S|N|N|100|N|N
USBF|iShares USD Bond Factor ETF|G|N|N|100|Y|N
USCB|USCB Financial Holdings, Inc.  - Class A Common Stock|G|N|N|100|N|N
USCL|iShares Climate Conscious & Transition MSCI USA ETF|G|N|N|100|Y|N
USCT|Roth CH Acquisition Co. - Class A Ordinary Shares|G|N|N|100|N|N
USCTU|Roth CH Acquisition Co. - Unit|G|N|N|100|N|N
USCTW|Roth CH Acquisition Co. - Warrant|G|N|N|100|N|N
USEA|United Maritime Corporation - Common Stock|S|N|N|100|N|N
USEG|U.S. Energy Corp. - Common Stock|S|N|N|100|N|N
USFI|BrandywineGLOBAL - U.S. Fixed Income ETF|G|N|N|100|Y|N
USGO|U.S. GoldMining Inc. - Common stock|S|N|N|100|N|N
USGOW|U.S. GoldMining Inc. - Warrant|S|N|N|100|N|N
USIG|iShares Broad USD Investment Grade Corporate Bond ETF|G|N|N|100|Y|N
USIO|Usio, Inc. - Common Stock|G|N|N|100|N|N
USLM|United States Lime & Minerals, Inc. - Common Stock|Q|N|N|100|N|N
USMC|Principal U.S. Mega-Cap ETF|G|N|N|100|Y|N
USOI|Credit Suisse X-Links Crude Oil Shares Covered Call ETN|G|N|N|100|N|N
USTB|VictoryShares Short-Term Bond ETF|G|N|N|100|Y|N
USVM|VictoryShares US Small Mid Cap Value Momentum ETF|G|N|N|100|Y|N
USVN|US Treasury 7 Year Note ETF|G|N|N|100|Y|N
USXF|iShares ESG Advanced MSCI USA ETF|G|N|N|100|Y|N
UTEN|US Treasury 10 Year Note ETF|G|N|N|100|Y|N
UTHR|United Therapeutics Corporation - Common Stock|Q|N|N|100|N|N
UTHY|US Treasury 30 Year Bond ETF|G|N|N|100|Y|N
UTMD|Utah Medical Products, Inc. - Common Stock|Q|N|N|100|N|N
UTRE|US Treasury 3 Year Note ETF|G|N|N|100|Y|N
UTRS|Minerva Surgical, Inc. - Common Stock|S|N|N|100|N|N
UTSI|UTStarcom Holdings Corp - Ordinary Shares|Q|N|N|100|N|N
UTWO|US Treasury 2 Year Note ETF|G|N|N|100|Y|N
UTWY|US Treasury 20 Year Bond ETF|G|N|N|100|Y|N
UVSP|Univest Financial Corporation - Common Stock|Q|N|N|100|N|N
UXIN|Uxin Limited - American Depositary Shares|Q|N|N|100|N|N
VABK|Virginia National Bankshares Corporation - Common Stock|S|N|N|100|N|N
VACC|Vaccitech plc - American Depositary Shares|G|N|N|100|N|N
VALN|Valneva SE - American Depositary Shares|Q|N|N|100|N|N
VALU|Value Line, Inc. - Common Stock|S|N|N|100|N|N
VANI|Vivani Medical, Inc.  - Common Stock|S|N|N|100|N|N
VAQC|Vector Acquisition Corporation II - Class A Ordinary Shares|S|N|N|100|N|N
VAXX|Vaxxinity, Inc. - Class A Common Stock|G|N|N|100|N|N
VBFC|Village Bank and Trust Financial Corp. - Common Stock|S|N|N|100|N|N
VBIV|VBI Vaccines, Inc. - Ordinary Shares|S|N|N|100|N|N
VBNK|VersaBank - Common Shares|Q|N|N|100|N|N
VBTX|Veritex Holdings, Inc. - Common Stock|G|N|N|100|N|N
VC|Visteon Corporation - Common Stock|Q|N|N|100|N|N
VCEL|Vericel Corporation - Common Stock|G|N|N|100|N|N
VCIG|VCI Global Limited - Ordinary Share|S|N|N|100|N|N
VCIT|Vanguard Intermediate-Term Corporate Bond ETF|G|N|N|100|Y|N
VCLT|Vanguard Long-Term Corporate Bond ETF|G|N|N|100|Y|N
VCNX|Vaccinex, Inc. - Common Stock|S|N|D|100|N|N
VCSA|Vacasa, Inc. - Class A Common Stock|Q|N|D|100|N|N
VCSH|Vanguard Short-Term Corporate Bond ETF|G|N|N|100|Y|N
VCTR|Victory Capital Holdings, Inc. - Common Stock|Q|N|N|100|N|N
VCXA|10X Capital Venture Acquisition Corp. II - Class A Ordinary Share|S|N|N|100|N|N
VCXAU|10X Capital Venture Acquisition Corp. II - Unit|S|N|N|100|N|N
VCXAW|10X Capital Venture Acquisition Corp. II - Warrant|S|N|N|100|N|N
VCYT|Veracyte, Inc. - Common Stock|G|N|N|100|N|N
VECO|Veeco Instruments Inc. - Common Stock|Q|N|N|100|N|N
VEEE|Twin Vee PowerCats Co. - Common Stock|S|N|N|100|N|N
VEON|VEON Ltd. - American Depositary Shares|S|N|N|100|N|N
VERA|Vera Therapeutics, Inc. - Class A Common Stock|G|N|N|100|N|N
VERB|Verb Technology Company, Inc. - Common Stock|S|N|D|100|N|N
VERBW|Verb Technology Company, Inc. - Warrant|S|N|D|100|N|N
VERI|Veritone, Inc. - Common Stock|G|N|N|100|N|N
VERO|Venus Concept Inc.  - Common Stock|S|N|D|100|N|N
VERU|Veru Inc. - Common Stock|S|N|N|100|N|N
VERV|Verve Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
VERX|Vertex, Inc. - Class A Common Stock|G|N|N|100|N|N
VERY|Vericity, Inc. - Common Stock|S|N|N|100|N|N
VEV|Vicinity Motor Corp. - Common Stock|S|N|N|100|N|N
VFF|Village Farms International, Inc. - Common Shares|S|N|D|100|N|N
VFLO|VictoryShares Free Cash Flow ETF|G|N|N|100|Y|N
VFS|VinFast Auto Ltd. - Ordinary Shares|Q|N|N|100|N|N
VFSWW|VinFast Auto Ltd. - Warrant|S|N|N|100|N|N
VGAS|Verde Clean Fuels, Inc. - Class A Common Stock|S|N|N|100|N|N
VGASW|Verde Clean Fuels, Inc. - Warrant|S|N|N|100|N|N
VGIT|Vanguard Intermediate-Term Treasury ETF|G|N|N|100|Y|N
VGLT|Vanguard Long-Term Treasury ETF|G|N|N|100|Y|N
VGSH|Vanguard Short-Term Treasury ETF|G|N|N|100|Y|N
VIA|Via Renewables, Inc. - Class A Common Stock|Q|N|N|100|N|N
VIASP|Via Renewables, Inc. - 8.75% Series A Fixed-to-Floating Rate Cumulative Redeemable Perpetual Preferred Stock|Q|N|N|100|N|N
VIAV|Viavi Solutions Inc. - Common Stock|Q|N|N|100|N|N
VICR|Vicor Corporation - Common Stock|Q|N|N|100|N|N
VIEW|View, Inc. - Class A Common Stock|G|N|N|100|N|N
VIEWW|View, Inc. - Warrant|G|N|N|100|N|N
VIGI|Vanguard International Dividend Appreciation ETF|G|N|N|100|Y|N
VIGL|Vigil Neuroscience, Inc. - Common Stock|Q|N|N|100|N|N
VII|7GC & Co. Holdings Inc. - Class A common stock|S|N|N|100|N|N
VIIAU|7GC & Co. Holdings Inc. - Unit|S|N|N|100|N|N
VIIAW|7GC & Co. Holdings Inc. - Warrant|S|N|N|100|N|N
VINC|Vincerx Pharma, Inc. - Common Stock|S|N|D|100|N|N
VINO|Gaucho Group Holdings, Inc. - Common Stock|S|N|D|100|N|N
VINP|Vinci Partners Investments Ltd. - Class A Common Shares|Q|N|N|100|N|N
VIOT|Viomi Technology Co., Ltd - American Depositary Shares|Q|N|N|100|N|N
VIR|Vir Biotechnology, Inc. - Common Stock|Q|N|N|100|N|N
VIRC|Virco Manufacturing Corporation - Common Stock|G|N|N|100|N|N
VIRI|Virios Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
VIRT|Virtu Financial, Inc. - Class A Common Stock|Q|N|N|100|N|N
VIRX|Viracta Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
VISL|Vislink Technologies, Inc. - Common Stock|S|N|N|100|N|N
VITL|Vital Farms, Inc. - Common Stock|G|N|N|100|N|N
VIVK|Vivakor, Inc. - Common Stock|S|N|N|100|N|N
VJET|voxeljet AG - American Depositary Shares|S|N|N|100|N|N
VKTX|Viking Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
VLCN|Volcon, Inc. - Common stock|S|N|D|100|N|N
VLGEA|Village Super Market, Inc. - Class A Common Stock|Q|N|N|100|N|N
VLY|Valley National Bancorp - Common Stock|Q|N|N|100|N|N
VLYPO|Valley National Bancorp - 5.5% Fixed to Floating Rate Series B Non-Cumulative Perpetual Preferred Stock|Q|N|N|100|N|N
VLYPP|Valley National Bancorp - 6.25% Fixed-to-Floating Rate Series A Non-Cumulative Perpetual Preferred Stock|Q|N|N|100|N|N
VMAR|Vision Marine Technologies Inc. - Common Shares|S|N|N|100|N|N
VMBS|Vanguard Mortgage-Backed Securities ETF|G|N|N|100|Y|N
VMCA|Valuence Merger Corp. I - Class A Ordinary Shares|G|N|N|100|N|N
VMCAU|Valuence Merger Corp. I - Unit|G|N|N|100|N|N
VMCAW|Valuence Merger Corp. I - Warrant|G|N|D|100|N|N
VMD|Viemed Healthcare, Inc. - Common Shares|S|N|N|100|N|N
VMEO|Vimeo, Inc. - Common Stock|Q|N|N|100|N|N
VNDA|Vanda Pharmaceuticals Inc. - Common Stock|G|N|N|100|N|N
VNET|VNET Group, Inc. - American Depositary Shares|Q|N|N|100|N|N
VNOM|Viper Energy Partners LP - Common Unit|Q|N|N|100|N|N
VNQI|Vanguard Global ex-U.S. Real Estate ETF|G|N|N|100|Y|N
VOD|Vodafone Group Plc - American Depositary Shares each representing ten Ordinary Shares|Q|N|N|100|N|N
VONE|Vanguard Russell 1000 ETF|G|N|N|100|Y|N
VONG|Vanguard Russell 1000 Growth ETF|G|N|N|100|Y|N
VONV|Vanguard Russell 1000 Value ETF|G|N|N|100|Y|N
VOR|Vor Biopharma Inc. - Common Stock|Q|N|N|100|N|N
VOXR|Vox Royalty Corp. - common stock|S|N|N|100|N|N
VOXX|VOXX International Corporation - Class A Common Stock|Q|N|N|100|N|N
VPN|Global X Data Center REITs & Digital Infrastructure ETF|G|N|N|100|Y|N
VR|Global X Metaverse ETF|G|N|N|100|Y|N
VRA|Vera Bradley, Inc. - Common Stock|Q|N|N|100|N|N
VRAR|The Glimpse Group, Inc. - Common Stock|S|N|N|100|N|N
VRAX|Virax Biolabs Group Limited - Ordinary Shares|S|N|D|100|N|N
VRCA|Verrica Pharmaceuticals Inc. - Common Stock|G|N|N|100|N|N
VRDN|Viridian Therapeutics, Inc.  - Common Stock|S|N|N|100|N|N
VREX|Varex Imaging Corporation - Common Stock|Q|N|N|100|N|N
VRIG|Invesco Variable Rate Investment Grade ETF|G|N|N|100|Y|N
VRM|Vroom, Inc. - Common Stock|Q|N|N|100|N|N
VRME|VerifyMe, Inc. - Common Stock|S|N|N|100|N|N
VRMEW|VerifyMe, Inc. - Warrant|S|N|N|100|N|N
VRNA|Verona Pharma plc - American Depositary Shares|G|N|N|100|N|N
VRNS|Varonis Systems, Inc. - Common Stock|Q|N|N|100|N|N
VRNT|Verint Systems Inc. - Common Stock|Q|N|N|100|N|N
VRPX|Virpax Pharmaceuticals, Inc. - Common Stock|S|N|D|100|N|N
VRRM|Verra Mobility Corporation - Class A Common Stock|S|N|N|100|N|N
VRSK|Verisk Analytics, Inc. - Common Stock|Q|N|N|100|N|N
VRSN|VeriSign, Inc. - Common Stock|Q|N|N|100|N|N
VRTS|Virtus Investment Partners, Inc. - Common Stock|Q|N|N|100|N|N
VRTX|Vertex Pharmaceuticals Incorporated - Common Stock|Q|N|N|100|N|N
VS|Versus Systems Inc. - Common Shares|S|N|D|100|N|N
VSAC|Vision Sensing Acquisition Corp. - Class A Common Stock|G|N|D|100|N|N
VSACU|Vision Sensing Acquisition Corp. - Unit|G|N|D|100|N|N
VSACW|Vision Sensing Acquisition Corp. - Warrants|G|N|D|100|N|N
VSAT|ViaSat, Inc. - Common Stock|Q|N|N|100|N|N
VSDA|VictoryShares Dividend Accelerator ETF|G|N|N|100|Y|N
VSEC|VSE Corporation - Common Stock|Q|N|N|100|N|N
VSME|VS Media Holdings Limited - Class A Ordinary Shares|S|N|N|100|N|N
VSMV|VictoryShares US Multi-Factor Minimum Volatility ETF|G|N|N|100|Y|N
VSSYW|Versus Systems Inc. - Class A Warrants|S|N|N|100|N|N
VSTA|Vasta Platform Limited - Class A Ordinary Shares|Q|N|N|100|N|N
VSTM|Verastem, Inc. - Common Stock|S|N|N|100|N|N
VTC|Vanguard Total Corporate Bond ETF|G|N|N|100|Y|N
VTGN|VistaGen Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
VTHR|Vanguard Russell 3000 ETF|G|N|N|100|Y|N
VTIP|Vanguard Short-Term Inflation-Protected Securities Index Fund ETF Shares|G|N|N|100|Y|N
VTNR|Vertex Energy, Inc - Common Stock|S|N|N|100|N|N
VTRS|Viatris Inc. - Common Stock|Q|N|N|100|N|N
VTRU|Vitru Limited - Common Shares|Q|N|N|100|N|N
VTSI|VirTra, Inc. - Common Stock|S|N|N|100|N|N
VTVT|vTv Therapeutics Inc. - Class A Common Stock|S|N|D|100|N|N
VTWG|Vanguard Russell 2000 Growth ETF|G|N|N|100|Y|N
VTWO|Vanguard Russell 2000 ETF|G|N|N|100|Y|N
VTWV|Vanguard Russell 2000 Value ETF|G|N|N|100|Y|N
VTYX|Ventyx Biosciences, Inc. - Common Stock|Q|N|N|100|N|N
VUZI|Vuzix Corporation  - Common Stock|S|N|N|100|N|N
VVOS|Vivos Therapeutics, Inc. - Common Stock|S|N|D|100|N|N
VVPR|VivoPower International PLC - Ordinary Shares|S|N|D|100|N|N
VWE|Vintage Wine Estates, Inc. - Common Stock|G|N|D|100|N|N
VWEWW|Vintage Wine Estates, Inc. - Warrants|S|N|N|100|N|N
VWOB|Vanguard Emerging Markets Government Bond ETF|G|N|N|100|Y|N
VXRT|Vaxart, Inc. - Common Stock|S|N|D|100|N|N
VXUS|Vanguard Total International Stock ETF|G|N|N|100|Y|N
VYGR|Voyager Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
VYMI|Vanguard International High Dividend Yield ETF|G|N|N|100|Y|N
VYNE|VYNE Therapeutics Inc. - Common Stock|S|N|N|100|N|N
WABC|Westamerica Bancorporation - Common Stock|Q|N|N|100|N|N
WABF|Western Asset Bond ETF|G|N|N|100|Y|N
WAFD|WaFd, Inc. - Common Stock|Q|N|N|100|N|N
WAFDP|WaFd, Inc. - Depositary Shares|Q|N|N|100|N|N
WAFU|Wah Fu Education Group Limited - Ordinary Shares|S|N|N|100|N|N
WALD|Waldencast plc - Class A Ordinary Share|S|N|E|100|N|N
WALDW|Waldencast plc - Warrant|S|N|E|100|N|N
WASH|Washington Trust Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
WATT|Energous Corporation - Common Stock|S|N|N|100|N|N
WAVD|WaveDancer, Inc.  - Common Stock|S|N|D|100|N|N
WAVE|Eco Wave Power Global AB (publ) - American Depositary Shares|S|N|N|100|N|N
WAVS|Western Acquisition Ventures Corp. - Common Stock|S|N|N|100|N|N
WAVSU|Western Acquisition Ventures Corp. - Unit|S|N|N|100|N|N
WAVSW|Western Acquisition Ventures Corp. - Warrant|S|N|N|100|N|N
WB|Weibo Corporation - American Depositary Shares|Q|N|N|100|N|N
WBA|Walgreens Boots Alliance, Inc. - Common Stock|Q|N|N|100|N|N
WBD|Warner Bros. Discovery, Inc. - Series A Common Stock|Q|N|N|100|N|N
WBND|Western Asset Total Return ETF|G|N|N|100|Y|N
WCBR|WisdomTree Cybersecurity Fund|G|N|N|100|Y|N
WCLD|WisdomTree Cloud Computing Fund|G|N|N|100|Y|N
WDAY|Workday, Inc. - Class A Common Stock|Q|N|N|100|N|N
WDC|Western Digital Corporation - Common Stock|Q|N|N|100|N|N
WDFC|WD-40 Company - Common Stock|Q|N|N|100|N|N
WEN|Wendy's Company (The) - Common Stock|Q|N|N|100|N|N
WERN|Werner Enterprises, Inc. - Common Stock|Q|N|N|100|N|N
WEST|Westrock Coffee Company - Common Stock|G|N|N|100|N|N
WESTW|Westrock Coffee Company - Warrants|G|N|N|100|N|N
WETG|WeTrade Group Inc. - Ordinary Shares|S|N|N|100|N|N
WEYS|Weyco Group, Inc. - Common Stock|Q|N|N|100|N|N
WFCF|Where Food Comes From, Inc. - Common Stock|S|N|N|100|N|N
WFRD|Weatherford International plc - Ordinary shares|Q|N|N|100|N|N
WGMI|Valkyrie Bitcoin Miners ETF|G|N|N|100|Y|N
WGRO|WisdomTree U.S. Growth & Momentum Fund|G|N|N|100|Y|N
WGS|GeneDx Holdings Corp. - Class A Common Stock|Q|N|N|100|N|N
WGSWW|GeneDx Holdings Corp. - Warrant|Q|N|N|100|N|N
WHF|WhiteHorse Finance, Inc. - Closed End Fund|Q|N|N|100|N|N
WHFCL|WhiteHorse Finance, Inc. - 7.875% Notes due 2028|Q|N|N|100|N|N
WHLM|Wilhelmina International, Inc. - Common Stock|S|N|N|100|N|N
WHLR|Wheeler Real Estate Investment Trust, Inc. - Common Stock|S|N|N|100|N|N
WHLRD|Wheeler Real Estate Investment Trust, Inc. - Series D Cumulative Preferred Stock|S|N|N|100|N|N
WHLRL|Wheeler Real Estate Investment Trust, Inc. - 7.00% Senior Subordinated Convertible Notes Due 2031|S|N|N|100|N|N
WHLRP|Wheeler Real Estate Investment Trust, Inc. - Series B Preferred Stock|S|N|N|100|N|N
WILC|G. Willi-Food International,  Ltd. - Ordinary Shares|S|N|N|100|N|N
WIMI|WiMi Hologram Cloud Inc. - American Depositary Share|G|N|D|100|N|N
WINA|Winmark Corporation - Common Stock|G|N|N|100|N|N
WINC|Western Asset Short Duration Income ETF|G|N|N|100|Y|N
WING|Wingstop Inc. - Common Stock|Q|N|N|100|N|N
WINT|Windtree Therapeutics, Inc. - Common Stock|S|N|N|100|N|N
WINV|WinVest Acquisition Corp. - Common Stock|S|N|N|100|N|N
WINVR|WinVest Acquisition Corp. - Right|S|N|N|100|N|N
WINVU|WinVest Acquisition Corp. - Unit|S|N|N|100|N|N
WINVW|WinVest Acquisition Corp. - Warrant|S|N|N|100|N|N
WIRE|Encore Wire Corporation - Common Stock|Q|N|N|100|N|N
WISA|WiSA Technologies, Inc. - Common Stock|S|N|D|100|N|N
WISH|ContextLogic Inc. - Class A Common Stock|Q|N|N|100|N|N
WIX|Wix.com Ltd. - Ordinary Shares|Q|N|N|100|N|N
WIZ|Merlyn.AI Bull-Rider Bear-Fighter ETF|G|N|N|100|Y|N
WKEY|WISeKey International Holding Ltd - American Depositary Shares|G|N|N|100|N|N
WKHS|Workhorse Group, Inc. - Common Stock|S|N|D|100|N|N
WKME|WalkMe Ltd. - Ordinary Shares|Q|N|N|100|N|N
WKSP|Worksport, Ltd. - Common Stock|S|N|N|100|N|N
WKSPW|Worksport, Ltd. - Warrant|S|N|N|100|N|N
WLDN|Willdan Group, Inc. - Common Stock|G|N|N|100|N|N
WLDS|Wearable Devices Ltd. - Ordinary Share|S|N|N|100|N|N
WLDSW|Wearable Devices Ltd. - Warrant|S|N|N|100|N|N
WLFC|Willis Lease Finance Corporation - Common Stock|G|N|N|100|N|N
WLGS|Wang & Lee Group, Inc. - Ordinary Shares|S|N|N|100|N|N
WMG|Warner Music Group Corp. - Class A Common Stock|Q|N|N|100|N|N
WMPN|William Penn Bancorporation - Common Stock|S|N|N|100|N|N
WNDY|Global X Wind Energy ETF|G|N|N|100|Y|N
WNEB|Western New England Bancorp, Inc. - Common Stock|Q|N|N|100|N|N
WNW|Meiwu Technology Company Limited - Ordinary Shares|S|N|D|100|N|N
WOOD|iShares Global Timber & Forestry ETF|G|N|N|100|Y|N
WOOF|Petco Health and Wellness Company, Inc. - Class A Common Stock|Q|N|N|100|N|N
WORX|SCWorx Corp. - Common Stock|S|N|D|100|N|N
WPRT|Westport Fuel Systems Inc - Common Shares|Q|N|N|100|N|N
WRAP|Wrap Technologies, Inc. - Common Stock|S|N|N|100|N|N
WRLD|World Acceptance Corporation - Common Stock|Q|N|N|100|N|N
WRND|IQ Global Equity R&D Leaders ETF|G|N|N|100|Y|N
WRNT|Warrantee Inc. - American Depositary Shares|S|N|E|100|N|N
WSBC|WesBanco, Inc. - Common Stock|Q|N|N|100|N|N
WSBCP|WesBanco, Inc. - Depositary Shares, Each Representing a 1/40th Interest in a Share of 6.75% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock, Series A|Q|N|N|100|N|N
WSBF|Waterstone Financial, Inc. - Common Stock|Q|N|N|100|N|N
WSC|WillScot Mobile Mini Holdings Corp. - Class A Common Stock|S|N|N|100|N|N
WSFS|WSFS Financial Corporation - Common Stock|Q|N|N|100|N|N
WTBA|West Bancorporation - Common Stock|Q|N|N|100|N|N
WTER|The Alkaline Water Company Inc. - Common Stock|S|N|D|100|N|N
WTFC|Wintrust Financial Corporation - Common Stock|Q|N|N|100|N|N
WTFCM|Wintrust Financial Corporation - Fixed-to-Floating Rate Non-Cumulative Perpetual Preferred Stock, Series D|Q|N|N|100|N|N
WTFCP|Wintrust Financial Corporation - Depositary Shares, Each Representing a 1/1,000th Interest in a Share of 6.875% Fixed-Rate Reset Non-Cumulative Perpetual Preferred Stock, Series E|Q|N|N|100|N|N
WTMA|Welsbach Technology Metals Acquisition Corp. - Common Stock|G|N|D|100|N|N
WTMAR|Welsbach Technology Metals Acquisition Corp. - one right to receive 1/10th of a share of common stock|G|N|N|100|N|N
WTMAU|Welsbach Technology Metals Acquisition Corp. - Unit|G|N|N|100|N|N
WTO|UTime Limited - Ordinary Shares|S|N|D|100|N|N
WTW|Willis Towers Watson Public Limited Company - Ordinary Shares|Q|N|N|100|N|N
WULF|TeraWulf Inc. - Common Stock|S|N|N|100|N|N
WVE|Wave Life Sciences Ltd. - Ordinary Shares|G|N|N|100|N|N
WVVI|Willamette Valley Vineyards, Inc. - Common Stock|S|N|N|100|N|N
WVVIP|Willamette Valley Vineyards, Inc. - Series A Redeemable Preferred Stock|S|N|N|100|N|N
WW|WW International, Inc.  - Common Stock|Q|N|N|100|N|N
WWAC|Worldwide Webb Acquisition Corp. - Class A Ordinary Share|S|N|D|100|N|N
WWACU|Worldwide Webb Acquisition Corp. - Unit|S|N|N|100|N|N
WWACW|Worldwide Webb Acquisition Corp. - Warrant|S|N|N|100|N|N
WWD|Woodward, Inc. - Common Stock|Q|N|N|100|N|N
WYNN|Wynn Resorts, Limited - Common Stock|Q|N|N|100|N|N
XAIR|Beyond Air, Inc. - Common Stock|S|N|N|100|N|N
XBIL|US Treasury 6 Month Bill ETF|G|N|N|100|Y|N
XBIO|Xenetic Biosciences, Inc. - Common Stock|S|N|N|100|N|N
XBIOW|Xenetic Biosciences, Inc. - Warrants|S|N|N|100|N|N
XBIT|XBiotech Inc. - Common Stock|Q|N|N|100|N|N
XCUR|Exicure, Inc. - Common Stock|S|N|D|100|N|N
XDNA|Kelly CRISPR & Gene Editing Technology ETF|G|N|N|100|Y|N
XEL|Xcel Energy Inc. - Common Stock|Q|N|N|100|N|N
XELA|Exela Technologies, Inc. - Common Stock|S|N|E|100|N|N
XELAP|Exela Technologies, Inc. - 6.00% Series B Cumulative Convertible Perpetual Preferred Stock|S|N|E|100|N|N
XELB|Xcel Brands, Inc - Common Stock|S|N|N|100|N|N
XENE|Xenon Pharmaceuticals Inc. - Common Shares|G|N|N|100|N|N
XERS|Xeris Biopharma Holdings, Inc. - Common Stock|Q|N|N|100|N|N
XFIN|ExcelFin Acquisition Corp - Class A Common Stock|G|N|N|100|N|N
XFINU|ExcelFin Acquisition Corp - Unit|G|N|N|100|N|N
XFINW|ExcelFin Acquisition Corp - Warrant|G|N|N|100|N|N
XFIX|F/m Opportunistic Income ETF|G|N|N|100|Y|N
XFOR|X4 Pharmaceuticals, Inc. - Common Stock|S|N|N|100|N|N
XGN|Exagen Inc. - Common Stock|G|N|N|100|N|N
XLO|Xilio Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
XMTR|Xometry, Inc. - Class A Common Stock|Q|N|N|100|N|N
XNCR|Xencor, Inc. - Common Stock|G|N|N|100|N|N
XNET|Xunlei Limited - American Depositary Shares|Q|N|N|100|N|N
XOMA|XOMA Corporation - Common Stock|G|N|N|100|N|N
XOMAO|XOMA Corporation - Depositary Shares Rep Series B 8.375% Cumulative Preferred Stock|G|N|N|100|N|N
XOMAP|XOMA Corporation - 8.625% Series A Cumulative Perpetual Preferred Stock|G|N|N|100|N|N
XOS|Xos, Inc. - Common Stock|S|N|D|100|N|N
XOSWW|Xos, Inc. - Warrants|S|N|N|100|N|N
XP|XP Inc. - Class A Common Stock|Q|N|N|100|N|N
XPDB|Power & Digital Infrastructure Acquisition II Corp. - Class A common stock|G|N|N|100|N|N
XPDBU|Power & Digital Infrastructure Acquisition II Corp. - Unit|G|N|N|100|N|N
XPDBW|Power & Digital Infrastructure Acquisition II Corp. - Warrant|G|N|N|100|N|N
XPEL|XPEL, Inc. - Common Stock|S|N|N|100|N|N
XPON|Expion360 Inc. - Common Stock|S|N|N|100|N|N
XRAY|DENTSPLY SIRONA Inc. - Common Stock|Q|N|N|100|N|N
XRTX|XORTX Therapeutics Inc. - Common Stock|S|N|D|100|N|N
XRX|Xerox Holdings Corporation - Common Stock|Q|N|N|100|N|N
XT|iShares Exponential Technologies ETF|G|N|N|100|Y|N
XTLB|XTL Biopharmaceuticals Ltd. - American Depositary Shares|S|N|N|100|N|N
XWEL|XWELL, Inc. - Common Stock|S|N|N|100|N|N
XXII|22nd Century Group, Inc - Common Stock|S|N|N|100|N|N
YGF|YanGuFang International Group Co., Ltd. - Ordinary Shares|S|N|N|100|N|N
YGMZ|MingZhu Logistics Holdings Limited - Ordinary Shares|S|N|D|100|N|N
YHGJ|Yunhong Green CTI Ltd. - Common Stock|S|N|N|100|N|N
YI|111, Inc. - American Depositary Shares|G|N|N|100|N|N
YJ|Yunji Inc. - American Depository Shares|G|N|D|100|N|N
YLDE|ClearBridge Dividend Strategy ESG ETF|G|N|N|100|Y|N
YMAB|Y-mAbs Therapeutics, Inc. - Common Stock|Q|N|N|100|N|N
YNDX|Yandex N.V. - Class A Ordinary Shares|Q|N|D|100|N|N
YORW|The York Water Company - Common Stock|Q|N|N|100|N|N
YOSH|Yoshiharu Global Co. - Class A Common Stock|S|N|D|100|N|N
YOTA|Yotta Acquisition Corporation - Common Stock|G|N|N|100|N|N
YOTAR|Yotta Acquisition Corporation - Right|G|N|N|100|N|N
YOTAU|Yotta Acquisition Corporation - Unit|G|N|N|100|N|N
YOTAW|Yotta Acquisition Corporation - Warrant|G|N|N|100|N|N
YQ|17 Education & Technology Group Inc. - American Depositary Shares|Q|N|D|100|N|N
YS|YS Biopharma Co., Ltd. - Ordinary Shares|S|N|N|100|N|N
YSBPW|YS Biopharma Co., Ltd. - Warrants|S|N|N|100|N|N
YTEN|Yield10 Bioscience, Inc.  - Common Stock|S|N|D|100|N|N
YTRA|Yatra Online, Inc. - Ordinary Shares|S|N|N|100|N|N
YY|JOYY Inc. - American Depositary Shares|Q|N|N|100|N|N
Z|Zillow Group, Inc. - Class C Capital Stock|Q|N|N|100|N|N
ZAPP|Zapp Electric Vehicles Group Limited - Ordinary shares|G|N|N|100|N|N
ZAPPW|Zapp Electric Vehicles Group Limited - Warrant|S|N|N|100|N|N
ZAZZT|Tick Pilot Test Stock Class A Common Stock|G|Y|N|100||N
ZBRA|Zebra Technologies Corporation - Class A Common Stock|Q|N|N|100|N|N
ZBZZT|Test Pilot Test Stock Class B Common Stock|G|Y|N|100||N
ZCMD|Zhongchao Inc. - Class A Ordinary Shares|S|N|N|100|N|N
ZCZZT|Tick Pilot Test Stock Class C |G|Y|N|100||N
ZD|Ziff Davis, Inc. - Common Stock|Q|N|N|100|N|N
ZENV|Zenvia Inc. - Class A Common Stock|S|N|N|100|N|N
ZEUS|Olympic Steel, Inc. - Common Stock|Q|N|N|100|N|N
ZFOX|ZeroFox Holdings, Inc. - Common Stock|G|N|N|100|N|N
ZFOXW|ZeroFox Holdings, Inc. - Warrant|S|N|N|100|N|N
ZG|Zillow Group, Inc. - Class A Common Stock|Q|N|N|100|N|N
ZI|ZoomInfo Technologies Inc. - Common Stock|Q|N|N|100|N|N
ZIMV|ZimVie Inc. - Common Stock|Q|N|N|100|N|N
ZION|Zions Bancorporation N.A. - Common Stock|Q|N|N|100|N|N
ZIONL|Zions Bancorporation N.A. - 6.95% Fixed-to-Floating Rate Subordinated Notes due September 15, 2028|G|N|N|100|N|N
ZIONO|Zions Bancorporation N.A. - Depositary Shares each representing a 1/40th ownership interest in a share of Series G Fixed/Floating-Rate Non-Cumulative Perpetual Preferred Stock|G|N|N|100|N|N
ZIONP|Zions Bancorporation N.A. - Depositary Shares each representing a 1/40th ownership interest in a share of Series A Floating-Rate Non-Cumulative Perpetual Preferred Stock|G|N|N|100|N|N
ZIVO|Zivo Bioscience, Inc. - Common Stock|S|N|D|100|N|N
ZIVOW|Zivo Bioscience, Inc. - Warrants|S|N|D|100|N|N
ZJYL|JIN MEDICAL INTERNATIONAL LTD. - Ordinary Shares|S|N|D|100|N|N
ZJZZT|NASDAQ TEST STOCK|Q|Y|N|100||N
ZKIN|ZK International Group Co., Ltd - Ordinary Share|S|N|D|100|N|N
ZLAB|Zai Lab Limited - American Depositary Shares|G|N|N|100|N|N
ZLS|Zalatoris II Acquisition Corp - Class A Ordinary Shares|S|N|D|100|N|N
ZLSWU|Zalatoris II Acquisition Corp - Unit|S|N|N|100|N|N
ZLSWW|Zalatoris II Acquisition Corp - Warrant|S|N|N|100|N|N
ZM|Zoom Video Communications, Inc. - Class A Common Stock|Q|N|N|100|N|N
ZNTL|Zentalis Pharmaceuticals, Inc. - common stock|G|N|N|100|N|N
ZS|Zscaler, Inc. - Common Stock|Q|N|N|100|N|N
ZTEK|Zentek Ltd. - common stock|S|N|D|100|N|N
ZUMZ|Zumiez Inc. - Common Stock|Q|N|N|100|N|N
ZURA|Zura Bio Limited - Class A Ordinary shares|S|N|N|100|N|N
ZURAW|Zura Bio Limited - Warrant|S|N|N|100|N|N
ZVRA|Zevra Therapeutics, Inc.  - Common Stock|Q|N|N|100|N|N
ZVSA|ZyVersa Therapeutics, Inc. - Common Stock|G|N|D|100|N|N
ZVZZC|NASDAQ TEST STOCK Nextshares Test Security|G|Y|N|100||Y
ZVZZT|NASDAQ TEST STOCK|G|Y|N|100||N
ZWZZT|NASDAQ TEST STOCK|S|Y|N|100||N
ZXYZ.A|Nasdaq Symbology Test Common Stock|Q|Y|N|100||N
ZXZZT|NASDAQ TEST STOCK|G|Y|N|100||N
ZYME|Zymeworks Inc. - Common Stock|Q|N|N|100|N|N
ZYXI|Zynex, Inc. - Common Stock|Q|N|N|100|N|N
"""
# Split the text into lines and create a list
lines = security_text.strip().split('\n')

# Extract "Symbol" and "Security Name" data from each line with spaces between data types
security_data = [f"{line.split('|')[0].strip()} | {line.split('|')[1].strip()}" for line in lines[1:]]

# --- Main st.form ---
with st.form("Stock Ticker Symbol Selector"):
    selectedCompany = st.selectbox(
        'Select or type a company', 
        security_data,
        placeholder="Select...",
        )
    submitted = st.form_submit_button("Get Data!") 
if submitted: 
    if not selectedCompany:
        st.info("Trouble on our side...") 
        st.stop()

# --- NEWS API KEY --- 
api_key = "1928fba2a2b644fca3c9e87990ea34ca"

#--- ST.FORM DEF OUTCOME  --- 
with st.spinner("Collecting your data..."): 
    if submitted:
        stockTicker = [line.split(' | ')[0] for line in selectedCompany]
        data = yf.Ticker(stockTicker).info
        analysis = yf.Ticker(stockTicker).financials
        # headlines = yf.Ticker(stockTicker).news
        news_url = f"https://newsapi.org/v2/everything?q={stockTicker}&pageSize=10&apiKey={api_key}"
        response = requests.get(news_url)

        tab1, tab2, tab3 = st.tabs(["News", "Summary", "Financials"]) 
        #--- DATA TAB DEF --- 
        with tab2:
            st.subheader("Finance Data Relevant to Selected Stock:")
            st.write(data) 
        #--- NEWS TAB DEF --- 
        with tab1:
            st.subheader("News Lines Relevant to Selected Stock:") 
            if response.status_code == 200:
                news_data = response.json() 
                articles = news_data["articles"]
            
            for article in articles:
                st.image(f"{article['urlToImage']}")  
                st.subheader(f"{article['title']}")
                st.write(f"{article['description']}")
                st.caption(f"**Source:** {article['source']['name']}")
                st.caption(f"**Published At:** {article['publishedAt']}")
                st.write(f"**URL:** [{article['url']}]({article['url']})")
                st.write("---")
                
        with tab3:
            st.subheader("Financials Table:") 
            st.table(analysis)
        #st.error("Error fetching news data. Please try again later.")
            