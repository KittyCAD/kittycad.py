from enum import Enum


class Currency(str, Enum):
    """Currency is the list of supported currencies.

    This comes from the Stripe API docs: For more details see <https://support.stripe.com/questions/which-currencies-does-stripe-support>."""  # noqa: E501

    """# United Arab Emirates Dirham """  # noqa: E501
    AED = "aed"
    """# Afghan Afghani """  # noqa: E501
    AFN = "afn"
    """# Albanian Lek """  # noqa: E501
    ALL = "all"
    """# Armenian Dram """  # noqa: E501
    AMD = "amd"
    """# Netherlands Antillean Gulden """  # noqa: E501
    ANG = "ang"
    """# Angolan Kwanza """  # noqa: E501
    AOA = "aoa"
    """# Argentine Peso """  # noqa: E501
    ARS = "ars"
    """# Australian Dollar """  # noqa: E501
    AUD = "aud"
    """# Aruban Florin """  # noqa: E501
    AWG = "awg"
    """# Azerbaijani Manat """  # noqa: E501
    AZN = "azn"
    """# Bosnia & Herzegovina Convertible Mark """  # noqa: E501
    BAM = "bam"
    """# Barbadian Dollar """  # noqa: E501
    BBD = "bbd"
    """# Bangladeshi Taka """  # noqa: E501
    BDT = "bdt"
    """# Bulgarian Lev """  # noqa: E501
    BGN = "bgn"
    """# Burundian Franc """  # noqa: E501
    BIF = "bif"
    """# Bermudian Dollar """  # noqa: E501
    BMD = "bmd"
    """# Brunei Dollar """  # noqa: E501
    BND = "bnd"
    """# Bolivian Boliviano """  # noqa: E501
    BOB = "bob"
    """# Brazilian Real """  # noqa: E501
    BRL = "brl"
    """# Bahamian Dollar """  # noqa: E501
    BSD = "bsd"
    """# Botswana Pula """  # noqa: E501
    BWP = "bwp"
    """# Belize Dollar """  # noqa: E501
    BZD = "bzd"
    """# Canadian Dollar """  # noqa: E501
    CAD = "cad"
    """# Congolese Franc """  # noqa: E501
    CDF = "cdf"
    """# Swiss Franc """  # noqa: E501
    CHF = "chf"
    """# Chilean Peso """  # noqa: E501
    CLP = "clp"
    """# Chinese Renminbi Yuan """  # noqa: E501
    CNY = "cny"
    """# Colombian Peso """  # noqa: E501
    COP = "cop"
    """# Costa Rican Colón """  # noqa: E501
    CRC = "crc"
    """# Cape Verdean Escudo """  # noqa: E501
    CVE = "cve"
    """# Czech Koruna """  # noqa: E501
    CZK = "czk"
    """# Djiboutian Franc """  # noqa: E501
    DJF = "djf"
    """# Danish Krone """  # noqa: E501
    DKK = "dkk"
    """# Dominican Peso """  # noqa: E501
    DOP = "dop"
    """# Algerian Dinar """  # noqa: E501
    DZD = "dzd"
    """# Estonian Kroon """  # noqa: E501
    EEK = "eek"
    """# Egyptian Pound """  # noqa: E501
    EGP = "egp"
    """# Ethiopian Birr """  # noqa: E501
    ETB = "etb"
    """# Euro """  # noqa: E501
    EUR = "eur"
    """# Fijian Dollar """  # noqa: E501
    FJD = "fjd"
    """# Falkland Islands Pound """  # noqa: E501
    FKP = "fkp"
    """# British Pound """  # noqa: E501
    GBP = "gbp"
    """# Georgian Lari """  # noqa: E501
    GEL = "gel"
    """# Gibraltar Pound """  # noqa: E501
    GIP = "gip"
    """# Gambian Dalasi """  # noqa: E501
    GMD = "gmd"
    """# Guinean Franc """  # noqa: E501
    GNF = "gnf"
    """# Guatemalan Quetzal """  # noqa: E501
    GTQ = "gtq"
    """# Guyanese Dollar """  # noqa: E501
    GYD = "gyd"
    """# Hong Kong Dollar """  # noqa: E501
    HKD = "hkd"
    """# Honduran Lempira """  # noqa: E501
    HNL = "hnl"
    """# Croatian Kuna """  # noqa: E501
    HRK = "hrk"
    """# Haitian Gourde """  # noqa: E501
    HTG = "htg"
    """# Hungarian Forint """  # noqa: E501
    HUF = "huf"
    """# Indonesian Rupiah """  # noqa: E501
    IDR = "idr"
    """# Israeli New Sheqel """  # noqa: E501
    ILS = "ils"
    """# Indian Rupee """  # noqa: E501
    INR = "inr"
    """# Icelandic Króna """  # noqa: E501
    ISK = "isk"
    """# Jamaican Dollar """  # noqa: E501
    JMD = "jmd"
    """# Japanese Yen """  # noqa: E501
    JPY = "jpy"
    """# Kenyan Shilling """  # noqa: E501
    KES = "kes"
    """# Kyrgyzstani Som """  # noqa: E501
    KGS = "kgs"
    """# Cambodian Riel """  # noqa: E501
    KHR = "khr"
    """# Comorian Franc """  # noqa: E501
    KMF = "kmf"
    """# South Korean Won """  # noqa: E501
    KRW = "krw"
    """# Cayman Islands Dollar """  # noqa: E501
    KYD = "kyd"
    """# Kazakhstani Tenge """  # noqa: E501
    KZT = "kzt"
    """# Lao Kip """  # noqa: E501
    LAK = "lak"
    """# Lebanese Pound """  # noqa: E501
    LBP = "lbp"
    """# Sri Lankan Rupee """  # noqa: E501
    LKR = "lkr"
    """# Liberian Dollar """  # noqa: E501
    LRD = "lrd"
    """# Lesotho Loti """  # noqa: E501
    LSL = "lsl"
    """# Lithuanian Litas """  # noqa: E501
    LTL = "ltl"
    """# Latvian Lats """  # noqa: E501
    LVL = "lvl"
    """# Moroccan Dirham """  # noqa: E501
    MAD = "mad"
    """# Moldovan Leu """  # noqa: E501
    MDL = "mdl"
    """# Malagasy Ariary """  # noqa: E501
    MGA = "mga"
    """# Macedonian Denar """  # noqa: E501
    MKD = "mkd"
    """# Mongolian Tögrög """  # noqa: E501
    MNT = "mnt"
    """# Macanese Pataca """  # noqa: E501
    MOP = "mop"
    """# Mauritanian Ouguiya """  # noqa: E501
    MRO = "mro"
    """# Mauritian Rupee """  # noqa: E501
    MUR = "mur"
    """# Maldivian Rufiyaa """  # noqa: E501
    MVR = "mvr"
    """# Malawian Kwacha """  # noqa: E501
    MWK = "mwk"
    """# Mexican Peso """  # noqa: E501
    MXN = "mxn"
    """# Malaysian Ringgit """  # noqa: E501
    MYR = "myr"
    """# Mozambican Metical """  # noqa: E501
    MZN = "mzn"
    """# Namibian Dollar """  # noqa: E501
    NAD = "nad"
    """# Nigerian Naira """  # noqa: E501
    NGN = "ngn"
    """# Nicaraguan Córdoba """  # noqa: E501
    NIO = "nio"
    """# Norwegian Krone """  # noqa: E501
    NOK = "nok"
    """# Nepalese Rupee """  # noqa: E501
    NPR = "npr"
    """# New Zealand Dollar """  # noqa: E501
    NZD = "nzd"
    """# Panamanian Balboa """  # noqa: E501
    PAB = "pab"
    """# Peruvian Nuevo Sol """  # noqa: E501
    PEN = "pen"
    """# Papua New Guinean Kina """  # noqa: E501
    PGK = "pgk"
    """# Philippine Peso """  # noqa: E501
    PHP = "php"
    """# Pakistani Rupee """  # noqa: E501
    PKR = "pkr"
    """# Polish Złoty """  # noqa: E501
    PLN = "pln"
    """# Paraguayan Guaraní """  # noqa: E501
    PYG = "pyg"
    """# Qatari Riyal """  # noqa: E501
    QAR = "qar"
    """# Romanian Leu """  # noqa: E501
    RON = "ron"
    """# Serbian Dinar """  # noqa: E501
    RSD = "rsd"
    """# Russian Ruble """  # noqa: E501
    RUB = "rub"
    """# Rwandan Franc """  # noqa: E501
    RWF = "rwf"
    """# Saudi Riyal """  # noqa: E501
    SAR = "sar"
    """# Solomon Islands Dollar """  # noqa: E501
    SBD = "sbd"
    """# Seychellois Rupee """  # noqa: E501
    SCR = "scr"
    """# Swedish Krona """  # noqa: E501
    SEK = "sek"
    """# Singapore Dollar """  # noqa: E501
    SGD = "sgd"
    """# Saint Helenian Pound """  # noqa: E501
    SHP = "shp"
    """# Sierra Leonean Leone """  # noqa: E501
    SLL = "sll"
    """# Somali Shilling """  # noqa: E501
    SOS = "sos"
    """# Surinamese Dollar """  # noqa: E501
    SRD = "srd"
    """# São Tomé and Príncipe Dobra """  # noqa: E501
    STD = "std"
    """# Salvadoran Colón """  # noqa: E501
    SVC = "svc"
    """# Swazi Lilangeni """  # noqa: E501
    SZL = "szl"
    """# Thai Baht """  # noqa: E501
    THB = "thb"
    """# Tajikistani Somoni """  # noqa: E501
    TJS = "tjs"
    """# Tongan Paʻanga """  # noqa: E501
    TOP = "top"
    """# Turkish Lira """  # noqa: E501
    TRY = "try"
    """# Trinidad and Tobago Dollar """  # noqa: E501
    TTD = "ttd"
    """# New Taiwan Dollar """  # noqa: E501
    TWD = "twd"
    """# Tanzanian Shilling """  # noqa: E501
    TZS = "tzs"
    """# Ukrainian Hryvnia """  # noqa: E501
    UAH = "uah"
    """# Ugandan Shilling """  # noqa: E501
    UGX = "ugx"
    """# United States Dollar """  # noqa: E501
    USD = "usd"
    """# Uruguayan Peso """  # noqa: E501
    UYU = "uyu"
    """# Uzbekistani Som """  # noqa: E501
    UZS = "uzs"
    """# Venezuelan Bolívar """  # noqa: E501
    VEF = "vef"
    """# Vietnamese Đồng """  # noqa: E501
    VND = "vnd"
    """# Vanuatu Vatu """  # noqa: E501
    VUV = "vuv"
    """# Samoan Tala """  # noqa: E501
    WST = "wst"
    """# Central African Cfa Franc """  # noqa: E501
    XAF = "xaf"
    """# East Caribbean Dollar """  # noqa: E501
    XCD = "xcd"
    """# West African Cfa Franc """  # noqa: E501
    XOF = "xof"
    """# Cfp Franc """  # noqa: E501
    XPF = "xpf"
    """# Yemeni Rial """  # noqa: E501
    YER = "yer"
    """# South African Rand """  # noqa: E501
    ZAR = "zar"
    """# Zambian Kwacha """  # noqa: E501
    ZMW = "zmw"

    def __str__(self) -> str:
        return str(self.value)
