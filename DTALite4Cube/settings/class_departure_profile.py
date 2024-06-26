class DepartureProfile:
    def __init__(self, departure_profile_defaults):
        # self.departure_profile_defaults = departure_profile_defaults
        for default_attribute, default_value in departure_profile_defaults.items():
            setattr(self, default_attribute, default_value)

    def update_profile(self, **kwargs):
        updated_attributes = set()
        for attribute, value in kwargs.items():
            if hasattr(self, attribute):
                setattr(self, attribute, value)
                updated_attributes.add(attribute)
            else:
                print(f"Ignoring unknown attribute: {attribute}")

        not_updated_attributes = set(vars(self).keys()) - updated_attributes
        for attribute in not_updated_attributes:
            # add if attribue is None exit
            print(f"Warning: {attribute} has not been updated and is set to: {getattr(self, attribute)}")


# Define the default profiles as dictionaries
departure_profile_defaults = {
    "departure_time_profile_no": 1,
    "T0000": 0.000571,
    "T0005": 0.000571,
    "T0010": 0.000571,
    "T0015": 0.000571,
    "T0020": 0.000571,
    "T0025": 0.000571,
    "T0030": 0.000506,
    "T0035": 0.000506,
    "T0040": 0.000506,
    "T0045": 0.000445,
    "T0050": 0.000445,
    "T0055": 0.000445,
    "T0060": 0.000391,
    "T0065": 0.000391,
    "T0070": 0.000391,
    "T0075": 0.000357,
    "T0080": 0.000357,
    "T0085": 0.000357,
    "T0090": 0.000328,
    "T0095": 0.000328,
    "T0100": 0.000328,
    "T0105": 0.000319,
    "T0110": 0.000319,
    "T0115": 0.000319,
    "T0120": 0.000302,
    "T0125": 0.000302,
    "T0130": 0.000302,
    "T0135": 0.000292,
    "T0140": 0.000292,
    "T0145": 0.000292,
    "T0150": 0.000296,
    "T0155": 0.000296,
    "T0160": 0.000296,
    "T0165": 0.00031,
    "T0170": 0.00031,
    "T0175": 0.00031,
    "T0180": 0.00031,
    "T0185": 0.00031,
    "T0190": 0.00031,
    "T0195": 0.000319,
    "T0200": 0.000319,
    "T0205": 0.000319,
    "T0210": 0.000383,
    "T0215": 0.000383,
    "T0220": 0.000383,
    "T0225": 0.000496,
    "T0230": 0.000496,
    "T0235": 0.000496,
    "T0240": 0.000568,
    "T0245": 0.000568,
    "T0250": 0.000568,
    "T0255": 0.000656,
    "T0260": 0.000656,
    "T0265": 0.000656,
    "T0270": 0.00095,
    "T0275": 0.00095,
    "T0280": 0.00095,
    "T0285": 0.001368,
    "T0290": 0.001368,
    "T0295": 0.001368,
    "T0300": 0.001587,
    "T0305": 0.001587,
    "T0310": 0.001587,
    "T0315": 0.00175,
    "T0320": 0.00175,
    "T0325": 0.00175,
    "T0330": 0.002288,
    "T0335": 0.002288,
    "T0340": 0.002288,
    "T0345": 0.002921,
    "T0350": 0.002921,
    "T0355": 0.002921,
    "T0360": 0.003242,
    "T0365": 0.003242,
    "T0370": 0.003242,
    "T0375": 0.003218,
    "T0380": 0.003218,
    "T0385": 0.003218,
    "T0390": 0.003803,
    "T0395": 0.003803,
    "T0400": 0.003803,
    "T0405": 0.004459,
    "T0410": 0.004459,
    "T0415": 0.004459,
    "T0420": 0.005002,
    "T0425": 0.005002,
    "T0430": 0.005002,
    "T0435": 0.005207,
    "T0440": 0.005207,
    "T0445": 0.005207,
    "T0450": 0.005677,
    "T0455": 0.005677,
    "T0460": 0.005677,
    "T0465": 0.005994,
    "T0470": 0.005994,
    "T0475": 0.005994,
    "T0480": 0.006018,
    "T0485": 0.006018,
    "T0490": 0.006018,
    "T0495": 0.005508,
    "T0500": 0.005508,
    "T0505": 0.005508,
    "T0510": 0.00529,
    "T0515": 0.00529,
    "T0520": 0.00529,
    "T0525": 0.005058,
    "T0530": 0.005058,
    "T0535": 0.005058,
    "T0540": 0.004833,
    "T0545": 0.004833,
    "T0550": 0.004833,
    "T0555": 0.004421,
    "T0560": 0.004421,
    "T0565": 0.004421,
    "T0570": 0.004327,
    "T0575": 0.004327,
    "T0580": 0.004327,
    "T0585": 0.004364,
    "T0590": 0.004364,
    "T0595": 0.004364,
    "T0600": 0.004343,
    "T0605": 0.004343,
    "T0610": 0.004343,
    "T0615": 0.004139,
    "T0620": 0.004139,
    "T0625": 0.004139,
    "T0630": 0.004201,
    "T0635": 0.004201,
    "T0640": 0.004201,
    "T0645": 0.004291,
    "T0650": 0.004291,
    "T0655": 0.004291,
    "T0660": 0.00435,
    "T0665": 0.00435,
    "T0670": 0.00435,
    "T0675": 0.004409,
    "T0680": 0.004409,
    "T0685": 0.004409,
    "T0690": 0.004566,
    "T0695": 0.004566,
    "T0700": 0.004566,
    "T0705": 0.004674,
    "T0710": 0.004674,
    "T0715": 0.004674,
    "T0720": 0.004761,
    "T0725": 0.004761,
    "T0730": 0.004761,
    "T0735": 0.004827,
    "T0740": 0.004827,
    "T0745": 0.004827,
    "T0750": 0.004882,
    "T0755": 0.004882,
    "T0760": 0.004882,
    "T0765": 0.0049,
    "T0770": 0.0049,
    "T0775": 0.0049,
    "T0780": 0.004887,
    "T0785": 0.004887,
    "T0790": 0.004887,
    "T0795": 0.004835,
    "T0800": 0.004835,
    "T0805": 0.004835,
    "T0810": 0.004899,
    "T0815": 0.004899,
    "T0820": 0.004899,
    "T0825": 0.005023,
    "T0830": 0.005023,
    "T0835": 0.005023,
    "T0840": 0.005065,
    "T0845": 0.005065,
    "T0850": 0.005065,
    "T0855": 0.005162,
    "T0860": 0.005162,
    "T0865": 0.005162,
    "T0870": 0.005436,
    "T0875": 0.005436,
    "T0880": 0.005436,
    "T0885": 0.005772,
    "T0890": 0.005772,
    "T0895": 0.005772,
    "T0900": 0.005907,
    "T0905": 0.005907,
    "T0910": 0.005907,
    "T0915": 0.005877,
    "T0920": 0.005877,
    "T0925": 0.005877,
    "T0930": 0.00605,
    "T0935": 0.00605,
    "T0940": 0.00605,
    "T0945": 0.006196,
    "T0950": 0.006196,
    "T0955": 0.006196,
    "T0960": 0.006248,
    "T0965": 0.006248,
    "T0970": 0.006248,
    "T0975": 0.006308,
    "T0980": 0.006308,
    "T0985": 0.006308,
    "T0990": 0.006404,
    "T0995": 0.006404,
    "T1000": 0.006404,
    "T1005": 0.006391,
    "T1010": 0.006391,
    "T1015": 0.006391,
    "T1020": 0.006401,
    "T1025": 0.006401,
    "T1030": 0.006401,
    "T1035": 0.006526,
    "T1040": 0.006526,
    "T1045": 0.006526,
    "T1050": 0.006574,
    "T1055": 0.006574,
    "T1060": 0.006574,
    "T1065": 0.006271,
    "T1070": 0.006271,
    "T1075": 0.006271,
    "T1080": 0.005937,
    "T1085": 0.005937,
    "T1090": 0.005937,
    "T1095": 0.005578,
    "T1100": 0.005578,
    "T1105": 0.005578,
    "T1110": 0.005293,
    "T1115": 0.005293,
    "T1120": 0.005293,
    "T1125": 0.004834,
    "T1130": 0.004834,
    "T1135": 0.004834,
    "T1140": 0.004387,
    "T1145": 0.004387,
    "T1150": 0.004387,
    "T1155": 0.00403,
    "T1160": 0.00403,
    "T1165": 0.00403,
    "T1170": 0.003748,
    "T1175": 0.003748,
    "T1180": 0.003748,
    "T1185": 0.003382,
    "T1190": 0.003382,
    "T1195": 0.003382,
    "T1200": 0.003121,
    "T1205": 0.003121,
    "T1210": 0.003121,
    "T1215": 0.002963,
    "T1220": 0.002963,
    "T1225": 0.002963,
    "T1230": 0.00289,
    "T1235": 0.00289,
    "T1240": 0.00289,
    "T1245": 0.002671,
    "T1250": 0.002671,
    "T1255": 0.002671,
    "T1260": 0.002468,
    "T1265": 0.002468,
    "T1270": 0.002468,
    "T1275": 0.002365,
    "T1280": 0.002365,
    "T1285": 0.002365,
    "T1290": 0.002249,
    "T1295": 0.002249,
    "T1300": 0.002249,
    "T1305": 0.002015,
    "T1310": 0.002015,
    "T1315": 0.002015,
    "T1320": 0.001784,
    "T1325": 0.001784,
    "T1330": 0.001784,
    "T1335": 0.00164,
    "T1340": 0.00164,
    "T1345": 0.00164,
    "T1350": 0.001474,
    "T1355": 0.001474,
    "T1360": 0.001474,
    "T1365": 0.001312,
    "T1370": 0.001312,
    "T1375": 0.001312,
    "T1380": 0.001132,
    "T1385": 0.001132,
    "T1390": 0.001132,
    "T1395": 0.001005,
    "T1400": 0.001005,
    "T1405": 0.001005,
    "T1410": 0.000889,
    "T1415": 0.000889,
    "T1420": 0.000889,
    "T1425": 0.000778,
    "T1430": 0.000778,
    "T1435": 0.000778
}
