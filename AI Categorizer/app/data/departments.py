"""
Department Knowledge Base

This file contains the complete list of supported departments
and the types of complaints they handle.

This acts as the single source of truth for the AI system.
"""

DEPARTMENTS = [
 {
    "id": "POLICE",

    "department": "Police Department",

    "description": (
        "Responsible for maintaining law and order, public safety, "
        "crime prevention, criminal investigations, traffic "
        "enforcement and emergency police response."
    ),

    "handles": [
        "Theft",
        "Robbery",
        "Fraud",
        "Cybercrime",
        "Domestic Violence",
        "Assault",
        "Missing Persons",
        "Traffic Violations",
        "Public Disturbances",
        "Harassment",
        "Kidnapping",
        "Illegal Activities",
        "Public Nuisance",
        "Illegal Gambling",
        "Drug Related Crimes",
        "Extortion",
    ],

    "keywords": [
        "theft",
        "stolen",
        "robbery",
        "crime",
        "criminal",
        "fraud",
        "cybercrime",
        "cyber attack",
        "hack",
        "hacked",
        "online scam",
        "cheating",
        "kidnap",
        "kidnapping",
        "fight",
        "violence",
        "assault",
        "harassment",
        "molestation",
        "threat",
        "murder",
        "traffic",
        "accident",
        "rash driving",
        "drunk driving",
        "police",
        "illegal activity",
        "drug",
        "missing",
        "lost person",
    ],

    "priority_rules": {
        "high": [
            "murder",
            "kidnapping",
            "terrorism",
            "armed robbery",
            "sexual assault",
            "life threat",
            "bomb threat",
        ],
        "medium": [
            "fraud",
            "cybercrime",
            "robbery",
            "assault",
            "missing person",
            "harassment",
        ],
        "low": [
            "traffic complaint",
            "noise complaint",
            "public disturbance",
        ],
    },

    "sample_complaints": [

        # English
        "Someone stole my bike.",
        "My mobile phone has been stolen.",
        "A person hacked my bank account.",
        "Someone hacked my social media account.",
        "There is a fight happening nearby.",
        "Someone is threatening me.",
        "My wallet was stolen yesterday.",
        "My child is missing.",
        "There is illegal gambling in my area.",
        "A drunk person is creating trouble.",

        # Tamil
        "என் பைக் திருடப்பட்டது.",
        "என் மொபைல் திருடப்பட்டது.",
        "என்னை ஒருவர் மிரட்டுகிறார்.",
        "ஒருவர் என் கணக்கை ஹேக் செய்துவிட்டார்.",
        "ஒரு குழந்தை காணாமல் போயுள்ளது.",

        # Tanglish
        "Bike thiruditaanga.",
        "Phone poiduchu.",
        "Yaravo threaten panraanga.",
        "Account hack pannitaanga.",
        "Paiyan missing.",

        # Hindi
        "मेरी बाइक चोरी हो गई।",
        "मेरा मोबाइल चोरी हो गया।",
        "कोई मुझे धमकी दे रहा है।",
        "मेरा अकाउंट हैक हो गया।",
        "एक बच्चा गायब हो गया है।",

        # Hinglish
        "Bike chori ho gaya.",
        "Phone chori ho gaya.",
        "Someone hacked my account.",
        "Mujhe threat mil raha hai.",
        "Ek ladka missing hai.",

        # Telugu
        "నా బైక్ దొంగిలించారు.",
        "నా ఫోన్ దొంగిలించారు.",
        "నా అకౌంట్ హ్యాక్ చేశారు.",
        "ఒక పిల్లవాడు కనిపించడం లేదు.",

        # Kannada
        "ನನ್ನ ಬೈಕ್ ಕಳ್ಳತನವಾಗಿದೆ.",
        "ನನ್ನ ಮೊಬೈಲ್ ಕಳುವಾಗಿದೆ.",
        "ನನ್ನ ಖಾತೆ ಹ್ಯಾಕ್ ಆಗಿದೆ.",
        "ಒಬ್ಬ ಮಗು ಕಾಣೆಯಾಗಿದೆ.",

        # Malayalam
        "എന്റെ ബൈക്ക് മോഷണം പോയി.",
        "എന്റെ ഫോൺ മോഷണം പോയി.",
        "എന്റെ അക്കൗണ്ട് ഹാക്ക് ചെയ്തു.",
        "ഒരു കുട്ടിയെ കാണാനില്ല.",
    ],
    },

 {
    "id": "FIRE",

    "department": "Fire & Rescue Department",

    "description": (
        "Responsible for fire emergencies, gas leaks, rescue "
        "operations, building collapses, flood rescue, chemical "
        "accidents and emergency disaster response."
    ),

    "handles": [
        "Fire",
        "Gas Leak",
        "Explosion",
        "Building Collapse",
        "Flood Rescue",
        "Road Accident Rescue",
        "Industrial Fire",
        "Chemical Leak",
        "Smoke",
        "Emergency Rescue",
        "Tree Rescue",
        "Lift Rescue",
        "Electrical Fire",
        "Forest Fire",
    ],

    "keywords": [
        "fire",
        "flames",
        "burning",
        "smoke",
        "gas leak",
        "lpg leak",
        "cylinder blast",
        "explosion",
        "blast",
        "collapse",
        "building collapse",
        "rescue",
        "chemical leak",
        "factory fire",
        "short circuit fire",
        "forest fire",
        "accident rescue",
    ],

    "priority_rules": {
        "high": [
            "fire",
            "gas leak",
            "explosion",
            "building collapse",
            "chemical leak",
            "forest fire",
        ],
        "medium": [
            "smoke",
            "minor fire",
            "vehicle fire",
            "lift rescue",
        ],
        "low": [
            "fire safety inspection",
        ],
    },

    "sample_complaints": [

        # English
        "There is a fire in my house.",
        "A gas leak has been detected.",
        "The building caught fire.",
        "Smoke is coming from the warehouse.",
        "A chemical leak happened in the factory.",
        "An LPG cylinder exploded.",
        "The building has collapsed.",
        "People are trapped inside the building.",

        # Tamil
        "வீட்டில் தீ விபத்து ஏற்பட்டுள்ளது.",
        "எரிவாயு கசிவு ஏற்பட்டுள்ளது.",
        "கட்டிடம் இடிந்து விழுந்துள்ளது.",
        "தொழிற்சாலையில் தீ விபத்து.",

        # Tanglish
        "Gas leak aaguthu.",
        "Building collapse aayiduchu.",
        "Factory la fire.",
        "Smoke varuthu.",

        # Hindi
        "घर में आग लग गई है।",
        "गैस लीक हो रही है।",
        "इमारत गिर गई है।",
        "फैक्ट्री में आग लग गई।",

        # Hinglish
        "Gas leak ho raha hai.",
        "Building collapse ho gaya.",
        "Factory me fire lag gaya.",
        "Smoke bahut aa raha hai.",

        # Telugu
        "ఇంట్లో మంటలు చెలరేగాయి.",
        "గ్యాస్ లీక్ అవుతోంది.",
        "భవనం కూలిపోయింది.",

        # Kannada
        "ಮನೆಯಲ್ಲಿ ಬೆಂಕಿ ಕಾಣಿಸಿಕೊಂಡಿದೆ.",
        "ಗ್ಯಾಸ್ ಸೋರಿಕೆ ಆಗುತ್ತಿದೆ.",
        "ಕಟ್ಟಡ ಕುಸಿದಿದೆ.",

        # Malayalam
        "വീട്ടിൽ തീപിടിച്ചു.",
        "ഗ്യാസ് ചോർച്ചയുണ്ട്.",
        "കെട്ടിടം തകർന്നു വീണു.",
    ],
 },

 {
    "id": "HEALTH",

    "department": "Health Department",

    "description": (
        "Responsible for public health services, government hospitals, "
        "primary health centres, disease prevention, vaccination, "
        "sanitation awareness and public health emergencies."
    ),

    "handles": [
        "Government Hospitals",
        "Primary Health Centres",
        "Disease Control",
        "Vaccination",
        "Mosquito Control",
        "Public Health Complaints",
        "Medical Camps",
        "Health Awareness",
        "Epidemics",
        "Food Poisoning",
        "Public Sanitation",
        "Medical Emergency Coordination",
    ],

    "keywords": [
        "hospital",
        "government hospital",
        "health centre",
        "health",
        "doctor",
        "nurse",
        "vaccination",
        "vaccine",
        "fever",
        "virus",
        "dengue",
        "malaria",
        "mosquito",
        "dog bite",
        "food poisoning",
        "infection",
        "epidemic",
        "covid",
        "public health",
        "medical",
        "sanitation",
    ],

    "priority_rules": {
        "high": [
            "disease outbreak",
            "epidemic",
            "pandemic",
            "food poisoning",
            "medical emergency",
            "dead animal causing disease",
        ],
        "medium": [
            "mosquito breeding",
            "hospital complaint",
            "vaccination issue",
            "doctor unavailable",
            "health centre closed",
        ],
        "low": [
            "medical camp request",
            "health awareness",
            "general enquiry",
        ],
    },

    "sample_complaints": [

        # English
        "Government hospital has no doctors.",
        "Mosquitoes are increasing in our area.",
        "There is a dengue outbreak.",
        "Vaccination is not available.",
        "People got food poisoning after eating.",
        "The health centre is closed.",
        "The hospital is unhygienic.",
        "A dead animal is causing a bad smell.",

        # Tamil
        "அரசு மருத்துவமனையில் மருத்துவர் இல்லை.",
        "எங்கள் பகுதியில் கொசுக்கள் அதிகமாக உள்ளன.",
        "டெங்கு பரவி வருகிறது.",
        "தடுப்பூசி கிடைக்கவில்லை.",
        "மருத்துவமனை மிகவும் அசுத்தமாக உள்ளது.",

        # Tanglish
        "Hospital la doctor illa.",
        "Mosquito romba iruku.",
        "Vaccine kedaikala.",
        "Hospital clean illa.",

        # Hindi
        "सरकारी अस्पताल में डॉक्टर नहीं हैं।",
        "हमारे इलाके में मच्छर बहुत हैं।",
        "डेंगू फैल रहा है।",
        "टीका उपलब्ध नहीं है।",

        # Hinglish
        "Hospital me doctor nahi hai.",
        "Mosquito bahut hai.",
        "Vaccine nahi mil raha.",
        "Hospital clean nahi hai.",

        # Telugu
        "ప్రభుత్వ ఆసుపత్రిలో డాక్టర్లు లేరు.",
        "మా ప్రాంతంలో దోమలు చాలా ఉన్నాయి.",
        "డెంగ్యూ వ్యాపిస్తోంది.",

        # Kannada
        "ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ವೈದ್ಯರಿಲ್ಲ.",
        "ನಮ್ಮ ಪ್ರದೇಶದಲ್ಲಿ ಸೊಳ್ಳೆಗಳು ತುಂಬಾ ಇವೆ.",
        "ಡೆಂಗ್ಯೂ ಹರಡುತ್ತಿದೆ.",

        # Malayalam
        "സർക്കാർ ആശുപത്രിയിൽ ഡോക്ടർമാരില്ല.",
        "ഞങ്ങളുടെ പ്രദേശത്ത് കൊതുകുകൾ വളരെ കൂടുതലാണ്.",
        "ഡെങ്കിപ്പനി പടരുന്നു.",
    ],
    },
 {
    "id": "ELECTRICITY",

    "department": "Electricity Department",

    "description": (
        "Responsible for electricity generation, transmission, "
        "distribution, power restoration, transformers, electric "
        "poles, meters, street lights and electrical safety."
    ),

    "handles": [
        "Power Outage",
        "Power Fluctuation",
        "Transformer Failure",
        "Street Light Issues",
        "Electric Pole Damage",
        "Meter Problems",
        "Live Wire Complaint",
        "Electric Shock Hazard",
        "Illegal Electricity Connection",
        "Fuse Problems",
        "Cable Damage",
        "Voltage Issues",
    ],

    "keywords": [
        "electricity",
        "current",
        "power",
        "power cut",
        "power outage",
        "no power",
        "street light",
        "streetlight",
        "transformer",
        "electric pole",
        "wire",
        "cable",
        "meter",
        "voltage",
        "fuse",
        "eb",
        "tneb",
        "live wire",
        "short circuit",
        "electric shock",
        "current illa",
        "light eriyala",
    ],

    "priority_rules": {
        "high": [
            "live wire",
            "electric shock",
            "transformer explosion",
            "high voltage",
            "pole fell",
            "electrocution",
        ],
        "medium": [
            "power outage",
            "transformer failure",
            "street light not working",
            "power fluctuation",
            "meter complaint",
        ],
        "low": [
            "new connection",
            "billing enquiry",
            "meter reading",
        ],
    },

    "sample_complaints": [

        # English
        "There is no electricity in my area.",
        "Power has been cut since morning.",
        "Street lights are not working.",
        "Transformer has exploded.",
        "Live electric wire is hanging.",
        "Electric pole has fallen.",
        "Voltage is very low.",
        "Meter is not working.",

        # Tamil
        "எங்கள் பகுதியில் மின்சாரம் இல்லை.",
        "மின்கம்பி கீழே விழுந்துள்ளது.",
        "தெரு விளக்கு எரியவில்லை.",
        "டிரான்ஸ்பார்மர் வெடித்துவிட்டது.",

        # Tanglish
        "Current illa.",
        "Light eriyala.",
        "Transformer blast aayiduchu.",
        "Wire keela vizhundhuruku.",

        # Hindi
        "बिजली नहीं आ रही है।",
        "ट्रांसफॉर्मर फट गया।",
        "सड़क की लाइट नहीं जल रही है।",
        "बिजली का तार नीचे गिर गया है।",

        # Hinglish
        "Current nahi aa raha.",
        "Street light nahi jal rahi.",
        "Transformer blast ho gaya.",
        "Wire neeche gir gaya.",

        # Telugu
        "కరెంట్ లేదు.",
        "ట్రాన్స్‌ఫార్మర్ పేలిపోయింది.",
        "స్ట్రీట్ లైట్ పనిచేయడం లేదు.",

        # Kannada
        "ಕರಂಟ್ ಇಲ್ಲ.",
        "ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ ಸ್ಫೋಟಗೊಂಡಿದೆ.",
        "ಬೀದಿ ದೀಪ ಬೆಳಗುತ್ತಿಲ್ಲ.",

        # Malayalam
        "കറന്റ് ഇല്ല.",
        "ട്രാൻസ്ഫോർമർ പൊട്ടിത്തെറിച്ചു.",
        "തെരുവ് ലൈറ്റ് പ്രവർത്തിക്കുന്നില്ല.",
    ],
    },
 {
    "id": "WATER",

    "department": "Water Supply Department",

    "description": (
        "Responsible for supplying safe drinking water, maintaining "
        "water pipelines, repairing leakages, restoring water supply "
        "and ensuring water quality."
    ),

    "handles": [
        "No Water Supply",
        "Water Leakage",
        "Pipeline Damage",
        "Burst Water Pipe",
        "Low Water Pressure",
        "Contaminated Water",
        "Drinking Water Issues",
        "Water Tank Problems",
        "Water Distribution",
        "Water Valve Issues",
        "Water Connection Complaints",
        "Water Quality Complaints",
    ],

    "keywords": [
        "water",
        "drinking water",
        "water supply",
        "no water",
        "water leakage",
        "leak",
        "pipeline",
        "pipe",
        "burst pipe",
        "tap",
        "water tank",
        "contaminated water",
        "dirty water",
        "muddy water",
        "water pressure",
        "valve",
        "thanni",
        "water connection",
        "pipe broken",
        "pipeline damage",
    ],

    "priority_rules": {
        "high": [
            "major pipeline burst",
            "contaminated drinking water",
            "no water for entire area",
            "water pipe burst",
        ],
        "medium": [
            "water leakage",
            "low water pressure",
            "water tank overflow",
            "pipeline damage",
        ],
        "low": [
            "new water connection",
            "billing enquiry",
            "general complaint",
        ],
    },

    "sample_complaints": [

        # English
        "There is no water supply in our area.",
        "The water pipeline has burst.",
        "Water is leaking continuously.",
        "Dirty water is coming from the tap.",
        "There is very low water pressure.",
        "The water tank is overflowing.",
        "The pipeline near my house is damaged.",
        "Drinking water smells bad.",

        # Tamil
        "எங்கள் பகுதியில் தண்ணீர் வரவில்லை.",
        "தண்ணீர் குழாய் உடைந்துள்ளது.",
        "குழாயில் இருந்து தண்ணீர் கசிகிறது.",
        "அழுக்கு தண்ணீர் வருகிறது.",

        # Tanglish
        "Thanni varala.",
        "Pipe odanjiduchu.",
        "Water leakage iruku.",
        "Dirty water varuthu.",

        # Hindi
        "पानी नहीं आ रहा है।",
        "पाइपलाइन टूट गई है।",
        "पानी लगातार लीक हो रहा है।",
        "गंदा पानी आ रहा है।",

        # Hinglish
        "Pani nahi aa raha.",
        "Pipeline toot gaya.",
        "Water leak ho raha hai.",
        "Dirty water aa raha hai.",

        # Telugu
        "నీళ్లు రావడం లేదు.",
        "పైప్ పగిలిపోయింది.",
        "నీరు లీక్ అవుతోంది.",

        # Kannada
        "ನೀರು ಬರುತ್ತಿಲ್ಲ.",
        "ಪೈಪ್ ಒಡೆದಿದೆ.",
        "ನೀರು ಸೋರಿಕೆಯಾಗುತ್ತಿದೆ.",

        # Malayalam
        "വെള്ളം വരുന്നില്ല.",
        "പൈപ്പ് പൊട്ടിയിരിക്കുന്നു.",
        "വെള്ളം ചോർന്നുകൊണ്ടിരിക്കുന്നു.",
    ],
    },
 {
    "id": "SEWER",

    "department": "Sewerage & Drainage Department",

    "description": (
        "Responsible for maintenance of underground drainage systems, "
        "storm water drains, sewage pipelines, manholes and prevention "
        "of sewage overflow and waterlogging."
    ),

    "handles": [
        "Blocked Drain",
        "Sewage Overflow",
        "Drainage Maintenance",
        "Waterlogging",
        "Open Manhole",
        "Broken Manhole Cover",
        "Drain Cleaning",
        "Storm Water Drain",
        "Sewage Leakage",
        "Underground Drain Damage",
        "Drain Blockage",
        "Overflowing Drain",
    ],

    "keywords": [
        "drain",
        "drainage",
        "sewer",
        "sewage",
        "sewerage",
        "blocked drain",
        "overflow",
        "dirty water",
        "waste water",
        "manhole",
        "drain cleaning",
        "storm water",
        "waterlogging",
        "drain blockage",
        "drain full",
        "septic",
        "open manhole",
        "bad smell",
    ],

    "priority_rules": {
        "high": [
            "major sewage overflow",
            "open manhole",
            "flooded drain",
            "large drainage blockage",
        ],
        "medium": [
            "blocked drain",
            "waterlogging",
            "dirty water overflow",
            "broken manhole cover",
        ],
        "low": [
            "routine drain cleaning",
            "maintenance request",
        ],
    },

    "sample_complaints": [

        # English
        "Drain is completely blocked.",
        "Sewage is overflowing onto the road.",
        "Dirty water is overflowing.",
        "The manhole cover is broken.",
        "There is heavy waterlogging after rain.",
        "The drain has not been cleaned.",
        "Bad smell is coming from the drain.",
        "There is an open manhole on the road.",

        # Tamil
        "சாக்கடை அடைத்துவிட்டது.",
        "கழிவுநீர் சாலையில் வழிகிறது.",
        "மழைக்குப் பிறகு தண்ணீர் தேங்கியுள்ளது.",
        "மூடப்படாத மேன்ஹோல் உள்ளது.",

        # Tanglish
        "Drain full ah iruku.",
        "Sewage overflow aaguthu.",
        "Water logging iruku.",
        "Manhole open ah iruku.",

        # Hindi
        "नाली जाम हो गई है।",
        "सीवेज सड़क पर बह रहा है।",
        "बारिश के बाद पानी भर गया है।",
        "मैनहोल खुला हुआ है।",

        # Hinglish
        "Drain block ho gaya.",
        "Sewage overflow ho raha hai.",
        "Road pe water logging hai.",
        "Manhole open hai.",

        # Telugu
        "డ్రైన్ మూసుకుపోయింది.",
        "మురుగు నీరు రోడ్డుపైకి వస్తోంది.",
        "రోడ్డుపై నీరు నిలిచిపోయింది.",

        # Kannada
        "ಚರಂಡಿ ಮುಚ್ಚಿದೆ.",
        "ಕೊಳಚೆ ನೀರು ರಸ್ತೆಗೆ ಹರಿಯುತ್ತಿದೆ.",
        "ರಸ್ತೆಯಲ್ಲಿ ನೀರು ನಿಂತಿದೆ.",

        # Malayalam
        "ഓട അടഞ്ഞിരിക്കുന്നു.",
        "മലിനജലം റോഡിലേക്ക് ഒഴുകുന്നു.",
        "റോഡിൽ വെള്ളം കെട്ടിക്കിടക്കുന്നു.",
    ],
    },
 {
    "id": "MUNICIPAL",

    "department": "Municipal Corporation/Panchayat",

    "description": (
        "Responsible for civic administration including garbage "
        "collection, sanitation, public toilets, parks, street "
        "cleaning, encroachments and municipal public services."
    ),

    "handles": [
        "Garbage Collection",
        "Street Cleaning",
        "Public Toilets",
        "Park Maintenance",
        "Roadside Waste",
        "Encroachment",
        "Dead Animal Removal",
        "Public Dustbins",
        "Solid Waste Management",
        "Municipal Sanitation",
        "Birth Certificate",
        "Death Certificate",
    ],

    "keywords": [
        "garbage",
        "trash",
        "waste",
        "dustbin",
        "cleanliness",
        "street cleaning",
        "public toilet",
        "park",
        "garden",
        "encroachment",
        "dead animal",
        "birth certificate",
        "death certificate",
        "municipality",
        "corporation",
        "panchayat",
        "garbage collection",
        "waste collection",
        "sanitation",
    ],

    "priority_rules": {
        "high": [
            "garbage causing disease",
            "dead animal on road",
            "overflowing garbage",
            "public health risk",
        ],
        "medium": [
            "garbage not collected",
            "dirty public toilet",
            "park maintenance",
            "street cleaning",
            "encroachment",
        ],
        "low": [
            "birth certificate",
            "death certificate",
            "general civic enquiry",
        ],
    },

    "sample_complaints": [

        # English
        "Garbage has not been collected for three days.",
        "The public toilet is very dirty.",
        "There is a dead dog on the road.",
        "The park is not maintained.",
        "People have dumped garbage near my house.",
        "Street cleaning has not been done.",
        "Someone has encroached on the footpath.",
        "I need a birth certificate.",

        # Tamil
        "குப்பை எடுக்கவில்லை.",
        "பொது கழிப்பறை மிகவும் அசுத்தமாக உள்ளது.",
        "சாலையில் இறந்த நாய் கிடக்கிறது.",
        "பூங்கா பராமரிக்கப்படவில்லை.",

        # Tanglish
        "Garbage edukala.",
        "Toilet clean illa.",
        "Park maintain pannala.",
        "Road la kuppai iruku.",

        # Hindi
        "कचरा नहीं उठाया गया।",
        "सार्वजनिक शौचालय बहुत गंदा है।",
        "सड़क पर मरा हुआ कुत्ता पड़ा है।",
        "पार्क की सफाई नहीं हुई।",

        # Hinglish
        "Garbage collect nahi hua.",
        "Public toilet clean nahi hai.",
        "Road pe dead dog pada hai.",
        "Park maintain nahi hai.",

        # Telugu
        "చెత్త తీసుకెళ్లలేదు.",
        "పబ్లిక్ టాయిలెట్ చాలా మురికిగా ఉంది.",
        "రోడ్డుపై చనిపోయిన కుక్క ఉంది.",

        # Kannada
        "ಕಸ ತೆಗೆದುಕೊಂಡಿಲ್ಲ.",
        "ಸಾರ್ವಜನಿಕ ಶೌಚಾಲಯ ತುಂಬಾ ಅಶುಚಿಯಾಗಿದೆ.",
        "ರಸ್ತೆಯಲ್ಲಿ ಸತ್ತ ನಾಯಿ ಇದೆ.",

        # Malayalam
        "മാലിന്യം എടുത്തിട്ടില്ല.",
        "പൊതു ശൗചാലയം വളരെ അശുചിയാണ്.",
        "റോഡിൽ ചത്ത നായ കിടക്കുന്നു.",
    ],
    },
 {
    "id": "PWD",

    "department": "Public Works Department (PWD)",

    "description": (
        "Responsible for construction, maintenance and repair of "
        "government roads, bridges, culverts, footpaths, public "
        "buildings and other public infrastructure."
    ),

    "handles": [
        "Potholes",
        "Road Damage",
        "Broken Roads",
        "Road Cracks",
        "Bridge Damage",
        "Bridge Maintenance",
        "Government Buildings",
        "Footpath Damage",
        "Road Cave-in",
        "Road Repair",
        "Highway Maintenance",
        "Retaining Wall Damage",
        "Road Shoulder Damage",
        "Public Building Maintenance",
    ],

    "keywords": [
        "pothole",
        "road",
        "road damage",
        "broken road",
        "road crack",
        "road repair",
        "bridge",
        "bridge crack",
        "bridge damage",
        "footpath",
        "sidewalk",
        "government building",
        "culvert",
        "highway",
        "road collapse",
        "road cave in",
        "damaged road",
        "bad road",
        "road maintenance",
        "public works",
    ],

    "priority_rules": {
        "high": [
            "bridge collapse",
            "road collapse",
            "major pothole causing accidents",
            "collapsed culvert",
            "unsafe bridge",
        ],
        "medium": [
            "road damage",
            "large pothole",
            "broken footpath",
            "bridge crack",
            "road crack",
        ],
        "low": [
            "minor road repair",
            "footpath maintenance",
            "road improvement",
        ],
    },

    "sample_complaints": [

        # English
        "There is a huge pothole on the road.",
        "The road is badly damaged.",
        "The bridge has developed cracks.",
        "The footpath is broken.",
        "The highway is full of potholes.",
        "Government building wall has cracked.",
        "The road has caved in after rain.",
        "Bridge is unsafe for vehicles.",

        # Tamil
        "சாலையில் பெரிய பள்ளம் உள்ளது.",
        "சாலை மிகவும் சேதமடைந்துள்ளது.",
        "பாலத்தில் விரிசல் ஏற்பட்டுள்ளது.",
        "நடைபாதை உடைந்துள்ளது.",

        # Tanglish
        "Road romba mosama iruku.",
        "Road oda pochu.",
        "Bridge crack aayiduchu.",
        "Footpath odanjiduchu.",

        # Hindi
        "सड़क में बड़ा गड्ढा है।",
        "सड़क पूरी तरह टूट गई है।",
        "पुल में दरार आ गई है।",
        "फुटपाथ टूट गया है।",

        # Hinglish
        "Road pe bada gadda hai.",
        "Road damage ho gaya.",
        "Bridge crack ho gaya.",
        "Footpath toot gaya.",

        # Telugu
        "రోడ్డులో పెద్ద గుంత ఉంది.",
        "రోడ్డు పూర్తిగా దెబ్బతింది.",
        "వంతెనకు పగుళ్లు వచ్చాయి.",

        # Kannada
        "ರಸ್ತೆಯಲ್ಲಿ ದೊಡ್ಡ ಗುಂಡಿ ಇದೆ.",
        "ರಸ್ತೆ ಸಂಪೂರ್ಣ ಹಾಳಾಗಿದೆ.",
        "ಸೇತುವೆಗೆ ಬಿರುಕು ಬಿದ್ದಿದೆ.",

        # Malayalam
        "റോഡിൽ വലിയ കുഴിയുണ്ട്.",
        "റോഡ് തകർന്നിരിക്കുന്നു.",
        "പാലത്തിന് വിള്ളൽ ഉണ്ട്.",
    ],
    },
 {
    "id": "RTO",

    "department": "Transport Department (RTO)",

    "description": (
        "Responsible for driving licences, vehicle registration, "
        "vehicle permits, road tax, vehicle fitness certificates, "
        "public transport regulation and transport-related services."
    ),

    "handles": [
        "Driving Licence",
        "Learner Licence",
        "Vehicle Registration",
        "RC Book",
        "Road Tax",
        "Vehicle Permit",
        "Fitness Certificate",
        "Vehicle Ownership Transfer",
        "Duplicate RC",
        "Driving Test",
        "Commercial Vehicle Permit",
        "Transport Complaints",
    ],

    "keywords": [
        "driving licence",
        "driving license",
        "learner licence",
        "learner license",
        "vehicle registration",
        "registration certificate",
        "rc",
        "rc book",
        "road tax",
        "permit",
        "fitness certificate",
        "vehicle transfer",
        "ownership transfer",
        "transport",
        "rto",
        "driving test",
        "commercial vehicle",
        "license renewal",
        "vehicle documents",
    ],

    "priority_rules": {
        "high": [
            "illegal commercial transport",
            "unsafe public transport",
            "fake driving licence",
        ],
        "medium": [
            "vehicle registration delay",
            "licence issue",
            "fitness certificate issue",
            "permit issue",
        ],
        "low": [
            "duplicate rc",
            "road tax enquiry",
            "licence renewal",
        ],
    },

    "sample_complaints": [

        # English
        "My driving licence application is delayed.",
        "I have not received my RC book.",
        "Vehicle registration is pending.",
        "Road tax payment is not updating.",
        "Fitness certificate is delayed.",
        "Ownership transfer has not been completed.",
        "Driving test has not been scheduled.",
        "Commercial vehicle permit is pending.",

        # Tamil
        "என் ஓட்டுநர் உரிமம் இன்னும் வரவில்லை.",
        "RC புத்தகம் கிடைக்கவில்லை.",
        "வாகன பதிவு இன்னும் முடிக்கப்படவில்லை.",
        "சாலை வரி செலுத்தியதும் புதுப்பிக்கப்படவில்லை.",

        # Tanglish
        "License varala.",
        "RC book kedaikala.",
        "Vehicle registration pending.",
        "Road tax update aagala.",

        # Hindi
        "मेरा ड्राइविंग लाइसेंस अभी तक नहीं मिला।",
        "आरसी बुक नहीं मिली।",
        "वाहन पंजीकरण लंबित है।",
        "रोड टैक्स अपडेट नहीं हुआ।",

        # Hinglish
        "Driving licence nahi mila.",
        "RC book nahi mila.",
        "Registration pending hai.",
        "Road tax update nahi hua.",

        # Telugu
        "నా డ్రైవింగ్ లైసెన్స్ ఇంకా రాలేదు.",
        "ఆర్‌సీ బుక్ రాలేదు.",
        "వాహనం రిజిస్ట్రేషన్ పెండింగ్‌లో ఉంది.",

        # Kannada
        "ನನ್ನ ಚಾಲನಾ ಪರವಾನಗಿ ಇನ್ನೂ ಬಂದಿಲ್ಲ.",
        "ಆರ್‌ಸಿ ಪುಸ್ತಕ ಸಿಕ್ಕಿಲ್ಲ.",
        "ವಾಹನ ನೋಂದಣಿ ಬಾಕಿಯಿದೆ.",

        # Malayalam
        "എന്റെ ഡ്രൈവിംഗ് ലൈസൻസ് ഇതുവരെ ലഭിച്ചില്ല.",
        "ആർ.സി. ബുക്ക് ലഭിച്ചില്ല.",
        "വാഹന രജിസ്ട്രേഷൻ ഇപ്പോഴും പൂർത്തിയായിട്ടില്ല.",
    ],
    },
 {
    "id": "RTO",

    "department": "Transport Department (RTO)",

    "description": (
        "Responsible for driving licences, vehicle registration, "
        "vehicle permits, road tax, vehicle fitness certificates, "
        "public transport regulation and transport-related services."
    ),

    "handles": [
        "Driving Licence",
        "Learner Licence",
        "Vehicle Registration",
        "RC Book",
        "Road Tax",
        "Vehicle Permit",
        "Fitness Certificate",
        "Vehicle Ownership Transfer",
        "Duplicate RC",
        "Driving Test",
        "Commercial Vehicle Permit",
        "Transport Complaints",
    ],

    "keywords": [
        "driving licence",
        "driving license",
        "learner licence",
        "learner license",
        "vehicle registration",
        "registration certificate",
        "rc",
        "rc book",
        "road tax",
        "permit",
        "fitness certificate",
        "vehicle transfer",
        "ownership transfer",
        "transport",
        "rto",
        "driving test",
        "commercial vehicle",
        "license renewal",
        "vehicle documents",
    ],

    "priority_rules": {
        "high": [
            "illegal commercial transport",
            "unsafe public transport",
            "fake driving licence",
        ],
        "medium": [
            "vehicle registration delay",
            "licence issue",
            "fitness certificate issue",
            "permit issue",
        ],
        "low": [
            "duplicate rc",
            "road tax enquiry",
            "licence renewal",
        ],
    },

    "sample_complaints": [

        # English
        "My driving licence application is delayed.",
        "I have not received my RC book.",
        "Vehicle registration is pending.",
        "Road tax payment is not updating.",
        "Fitness certificate is delayed.",
        "Ownership transfer has not been completed.",
        "Driving test has not been scheduled.",
        "Commercial vehicle permit is pending.",

        # Tamil
        "என் ஓட்டுநர் உரிமம் இன்னும் வரவில்லை.",
        "RC புத்தகம் கிடைக்கவில்லை.",
        "வாகன பதிவு இன்னும் முடிக்கப்படவில்லை.",
        "சாலை வரி செலுத்தியதும் புதுப்பிக்கப்படவில்லை.",

        # Tanglish
        "License varala.",
        "RC book kedaikala.",
        "Vehicle registration pending.",
        "Road tax update aagala.",

        # Hindi
        "मेरा ड्राइविंग लाइसेंस अभी तक नहीं मिला।",
        "आरसी बुक नहीं मिली।",
        "वाहन पंजीकरण लंबित है।",
        "रोड टैक्स अपडेट नहीं हुआ।",

        # Hinglish
        "Driving licence nahi mila.",
        "RC book nahi mila.",
        "Registration pending hai.",
        "Road tax update nahi hua.",

        # Telugu
        "నా డ్రైవింగ్ లైసెన్స్ ఇంకా రాలేదు.",
        "ఆర్‌సీ బుక్ రాలేదు.",
        "వాహనం రిజిస్ట్రేషన్ పెండింగ్‌లో ఉంది.",

        # Kannada
        "ನನ್ನ ಚಾಲನಾ ಪರವಾನಗಿ ಇನ್ನೂ ಬಂದಿಲ್ಲ.",
        "ಆರ್‌ಸಿ ಪುಸ್ತಕ ಸಿಕ್ಕಿಲ್ಲ.",
        "ವಾಹನ ನೋಂದಣಿ ಬಾಕಿಯಿದೆ.",

        # Malayalam
        "എന്റെ ഡ്രൈവിംഗ് ലൈസൻസ് ഇതുവരെ ലഭിച്ചില്ല.",
        "ആർ.സി. ബുക്ക് ലഭിച്ചില്ല.",
        "വാഹന രജിസ്ട്രേഷൻ ഇപ്പോഴും പൂർത്തിയായിട്ടില്ല.",
    ],
    },
 {
    "id": "REGISTRATION",

    "department": "Registration Department",

    "description": (
        "Responsible for registration of immovable properties, "
        "marriages, legal documents, sale deeds, gift deeds, "
        "leases, mortgages and other officially registrable documents."
    ),

    "handles": [
        "Property Registration",
        "Sale Deed Registration",
        "Gift Deed Registration",
        "Settlement Deed",
        "Lease Registration",
        "Mortgage Registration",
        "Marriage Registration",
        "Document Registration",
        "EC (Encumbrance Certificate)",
        "Certified Copy",
        "Document Verification",
        "Registration Correction",
    ],

    "keywords": [
        "registration",
        "property registration",
        "sale deed",
        "gift deed",
        "settlement deed",
        "lease",
        "mortgage",
        "document registration",
        "marriage registration",
        "encumbrance certificate",
        "ec",
        "certified copy",
        "sub registrar",
        "sub-registrar",
        "registration office",
        "document verification",
        "property document",
    ],

    "priority_rules": {
        "high": [
            "property fraud",
            "fake registration",
            "forged document",
            "duplicate registration",
        ],
        "medium": [
            "registration delay",
            "marriage registration delay",
            "document verification",
            "encumbrance certificate delay",
        ],
        "low": [
            "certified copy request",
            "general enquiry",
            "document correction",
        ],
    },

    "sample_complaints": [

        # English
        "My property registration is delayed.",
        "Marriage registration has not been completed.",
        "Need an Encumbrance Certificate.",
        "Sale deed registration is pending.",
        "I need a certified copy of my document.",
        "Property document contains mistakes.",
        "Document verification is pending.",
        "Registration office is delaying my application.",

        # Tamil
        "சொத்து பதிவு தாமதமாகியுள்ளது.",
        "திருமண பதிவு இன்னும் முடிக்கப்படவில்லை.",
        "EC கிடைக்கவில்லை.",
        "பத்திர பதிவு நிலுவையில் உள்ளது.",

        # Tanglish
        "Property registration pending.",
        "Marriage registration mudiyala.",
        "EC kedaikala.",
        "Document verification pending.",

        # Hindi
        "संपत्ति पंजीकरण लंबित है।",
        "विवाह पंजीकरण पूरा नहीं हुआ।",
        "ईसी नहीं मिला।",
        "दस्तावेज़ सत्यापन लंबित है।",

        # Hinglish
        "Property registration pending hai.",
        "Marriage registration nahi hua.",
        "EC nahi mila.",
        "Document verification pending hai.",

        # Telugu
        "ఆస్తి రిజిస్ట్రేషన్ పెండింగ్‌లో ఉంది.",
        "వివాహ నమోదు పూర్తికాలేదు.",
        "ఈసీ రాలేదు.",

        # Kannada
        "ಆಸ್ತಿ ನೋಂದಣಿ ಬಾಕಿಯಿದೆ.",
        "ವಿವಾಹ ನೋಂದಣಿ ಪೂರ್ಣವಾಗಿಲ್ಲ.",
        "ಇಸಿ ಸಿಕ್ಕಿಲ್ಲ.",

        # Malayalam
        "സ്വത്ത് രജിസ്ട്രേഷൻ പൂർത്തിയായിട്ടില്ല.",
        "വിവാഹ രജിസ്ട്രേഷൻ പൂർത്തിയായിട്ടില്ല.",
        "ഇ.സി ലഭിച്ചില്ല.",
    ],
    },
 {
    "id": "FOREST",

    "department": "Forest Department",

    "description": (
        "Responsible for forest conservation, wildlife protection, "
        "illegal tree cutting, forest encroachment, biodiversity "
        "protection and management of reserved forest areas."
    ),

    "handles": [
        "Illegal Tree Cutting",
        "Forest Encroachment",
        "Wildlife Protection",
        "Human-Wildlife Conflict",
        "Forest Fire",
        "Poaching",
        "Illegal Sandalwood Cutting",
        "Timber Smuggling",
        "Wild Animal Rescue",
        "Protected Forest Issues",
        "Forest Plantation",
        "Tree Protection",
    ],

    "keywords": [
        "forest",
        "tree",
        "tree cutting",
        "illegal tree cutting",
        "wildlife",
        "elephant",
        "tiger",
        "deer",
        "monkey",
        "snake",
        "forest fire",
        "poaching",
        "encroachment",
        "timber",
        "wood smuggling",
        "animal rescue",
        "reserved forest",
        "forest land",
        "sandalwood",
        "wild animal",
    ],

    "priority_rules": {
        "high": [
            "forest fire",
            "elephant attack",
            "tiger sighting",
            "poaching",
            "illegal tree cutting",
            "wildlife emergency",
        ],
        "medium": [
            "forest encroachment",
            "tree cutting",
            "animal rescue",
            "timber smuggling",
        ],
        "low": [
            "tree plantation request",
            "forest awareness",
            "general enquiry",
        ],
    },

    "sample_complaints": [

        # English
        "Someone is cutting trees illegally.",
        "Wild elephants entered our village.",
        "A forest fire has started.",
        "There is illegal forest encroachment.",
        "A snake entered my house.",
        "Timber is being smuggled.",
        "Poachers are hunting animals.",
        "A deer is injured.",

        # Tamil
        "சட்டவிரோதமாக மரங்களை வெட்டுகின்றனர்.",
        "யானைகள் கிராமத்திற்குள் வந்துள்ளன.",
        "காட்டுத்தீ ஏற்பட்டுள்ளது.",
        "காட்டை ஆக்கிரமித்துள்ளனர்.",

        # Tanglish
        "Tree cut panraanga.",
        "Elephant oorukulla vandhuruku.",
        "Forest fire aaguthu.",
        "Forest encroachment pannirukaanga.",

        # Hindi
        "अवैध रूप से पेड़ काटे जा रहे हैं।",
        "हाथी गाँव में आ गए हैं।",
        "जंगल में आग लग गई है।",
        "जंगल की जमीन पर कब्जा किया गया है।",

        # Hinglish
        "Tree illegal cut kar rahe hain.",
        "Elephant village me aa gaya.",
        "Forest fire lag gaya.",
        "Forest land encroach kiya hai.",

        # Telugu
        "అక్రమంగా చెట్లు నరుకుతున్నారు.",
        "ఏనుగులు గ్రామంలోకి వచ్చాయి.",
        "అడవిలో మంటలు చెలరేగాయి.",

        # Kannada
        "ಅಕ್ರಮವಾಗಿ ಮರಗಳನ್ನು ಕಡಿಯುತ್ತಿದ್ದಾರೆ.",
        "ಆನೆಗಳು ಗ್ರಾಮಕ್ಕೆ ಬಂದಿವೆ.",
        "ಕಾಡಿನಲ್ಲಿ ಬೆಂಕಿ ಕಾಣಿಸಿಕೊಂಡಿದೆ.",

        # Malayalam
        "നിയമവിരുദ്ധമായി മരങ്ങൾ വെട്ടുന്നു.",
        "ആനകൾ ഗ്രാമത്തിലേക്ക് വന്നിരിക്കുന്നു.",
        "കാട്ടുതീ പടരുന്നു.",
    ],
    },
 {
    "id": "PCB",

    "department": "Pollution Control Board",

    "description": (
        "Responsible for monitoring, preventing and controlling "
        "air pollution, water pollution, noise pollution, industrial "
        "pollution and environmental protection."
    ),

    "handles": [
        "Air Pollution",
        "Water Pollution",
        "Noise Pollution",
        "Industrial Pollution",
        "Chemical Waste",
        "Hazardous Waste",
        "River Pollution",
        "Lake Pollution",
        "Groundwater Pollution",
        "Factory Emissions",
        "Dust Pollution",
        "Environmental Complaints",
    ],

    "keywords": [
        "pollution",
        "air pollution",
        "water pollution",
        "noise pollution",
        "industrial pollution",
        "factory smoke",
        "chemical waste",
        "hazardous waste",
        "river pollution",
        "lake pollution",
        "dust",
        "smoke",
        "burning waste",
        "garbage burning",
        "toxic gas",
        "contaminated river",
        "contaminated lake",
        "environment",
        "pcb",
        "factory emission",
    ],

    "priority_rules": {
        "high": [
            "chemical leak",
            "toxic gas",
            "industrial pollution",
            "hazardous waste",
            "river contamination",
        ],
        "medium": [
            "air pollution",
            "water pollution",
            "noise pollution",
            "factory smoke",
            "garbage burning",
        ],
        "low": [
            "dust pollution",
            "environment awareness",
            "general enquiry",
        ],
    },

    "sample_complaints": [

        # English
        "The factory is releasing thick smoke.",
        "There is heavy air pollution in our area.",
        "Chemical waste is being dumped into the river.",
        "The lake water is polluted.",
        "The factory is causing noise pollution.",
        "People are burning garbage.",
        "There is a strong chemical smell.",
        "Dust pollution is increasing due to construction.",

        # Tamil
        "தொழிற்சாலையில் இருந்து புகை வருகிறது.",
        "எங்கள் பகுதியில் காற்று மாசு அதிகமாக உள்ளது.",
        "ஆற்றில் இரசாயன கழிவு கொட்டப்படுகிறது.",
        "ஏரி மாசடைந்துள்ளது.",

        # Tanglish
        "Factory smoke romba varuthu.",
        "Air pollution adhigama iruku.",
        "Chemical waste river la podraanga.",
        "Garbage burn panraanga.",

        # Hindi
        "फैक्ट्री से बहुत धुआं निकल रहा है।",
        "हमारे इलाके में वायु प्रदूषण बहुत है।",
        "नदी में रासायनिक कचरा डाला जा रहा है।",
        "लोग कचरा जला रहे हैं।",

        # Hinglish
        "Factory se smoke aa raha hai.",
        "Air pollution bahut hai.",
        "River me chemical waste daal rahe hain.",
        "Garbage jala rahe hain.",

        # Telugu
        "ఫ్యాక్టరీ నుంచి ఎక్కువ పొగ వస్తోంది.",
        "మా ప్రాంతంలో గాలి కాలుష్యం ఎక్కువగా ఉంది.",
        "నదిలో రసాయన వ్యర్థాలు వేస్తున్నారు.",

        # Kannada
        "ಕಾರ್ಖಾನೆಯಿಂದ ಹೆಚ್ಚು ಹೊಗೆ ಬರುತ್ತಿದೆ.",
        "ನಮ್ಮ ಪ್ರದೇಶದಲ್ಲಿ ವಾಯು ಮಾಲಿನ್ಯ ಹೆಚ್ಚಾಗಿದೆ.",
        "ನದಿಗೆ ರಾಸಾಯನಿಕ ತ್ಯಾಜ್ಯ ಸುರಿಯುತ್ತಿದ್ದಾರೆ.",

        # Malayalam
        "ഫാക്ടറിയിൽ നിന്ന് കനത്ത പുക വരുന്നു.",
        "ഞങ്ങളുടെ പ്രദേശത്ത് വായു മലിനീകരണം കൂടുതലാണ്.",
        "നദിയിൽ രാസമാലിന്യം ഒഴുക്കുന്നു.",
    ],
    },
 {
    "id": "LABOUR",

    "department": "Labour Department",

    "description": (
        "Responsible for labour welfare, employee rights, minimum "
        "wages, workplace safety, labour law enforcement, industrial "
        "disputes and prevention of child labour."
    ),

    "handles": [
        "Labour Disputes",
        "Minimum Wage Complaints",
        "Workplace Safety",
        "Child Labour",
        "Bonded Labour",
        "Salary Issues",
        "Unpaid Wages",
        "Industrial Disputes",
        "Contract Labour",
        "Employee Welfare",
        "Factory Labour Complaints",
        "Labour Law Violations",
    ],

    "keywords": [
        "labour",
        "worker",
        "employee",
        "salary",
        "wages",
        "minimum wage",
        "unpaid salary",
        "factory",
        "construction worker",
        "child labour",
        "bonded labour",
        "workplace",
        "industrial dispute",
        "labour rights",
        "labour office",
        "contract labour",
        "overtime",
        "unsafe workplace",
        "employee complaint",
        "worker safety",
    ],

    "priority_rules": {
        "high": [
            "child labour",
            "bonded labour",
            "fatal workplace accident",
            "unsafe factory",
            "forced labour",
        ],
        "medium": [
            "salary not paid",
            "minimum wage violation",
            "industrial dispute",
            "unsafe workplace",
        ],
        "low": [
            "employment enquiry",
            "general labour complaint",
            "contract clarification",
        ],
    },

    "sample_complaints": [

        # English
        "My salary has not been paid.",
        "The factory is using child labour.",
        "Workers are not receiving minimum wages.",
        "The workplace is unsafe.",
        "The company is forcing overtime.",
        "Workers are not provided safety equipment.",
        "Labour laws are being violated.",
        "Construction workers are working without helmets.",

        # Tamil
        "எனக்கு சம்பளம் வழங்கப்படவில்லை.",
        "தொழிற்சாலையில் குழந்தை தொழிலாளர்கள் வேலை செய்கிறார்கள்.",
        "குறைந்தபட்ச ஊதியம் வழங்கப்படவில்லை.",
        "வேலை செய்யும் இடம் பாதுகாப்பாக இல்லை.",

        # Tanglish
        "Salary kudukala.",
        "Child labour use panraanga.",
        "Minimum wage kudukala.",
        "Safety illa.",

        # Hindi
        "मुझे वेतन नहीं मिला।",
        "फैक्ट्री में बाल मजदूरी हो रही है।",
        "न्यूनतम वेतन नहीं दिया जा रहा है।",
        "कार्यस्थल सुरक्षित नहीं है।",

        # Hinglish
        "Salary nahi mila.",
        "Child labour use kar rahe hain.",
        "Minimum wage nahi de rahe.",
        "Factory safe nahi hai.",

        # Telugu
        "నాకు జీతం ఇవ్వలేదు.",
        "ఫ్యాక్టరీలో బాల కార్మికులు పని చేస్తున్నారు.",
        "కనీస వేతనం ఇవ్వడం లేదు.",

        # Kannada
        "ನನಗೆ ಸಂಬಳ ನೀಡಿಲ್ಲ.",
        "ಕಾರ್ಖಾನೆಯಲ್ಲಿ ಬಾಲ ಕಾರ್ಮಿಕರನ್ನು ಕೆಲಸಕ್ಕೆ ಇಡಲಾಗಿದೆ.",
        "ಕನಿಷ್ಠ ವೇತನ ನೀಡುತ್ತಿಲ್ಲ.",

        # Malayalam
        "എനിക്ക് ശമ്പളം നൽകിയിട്ടില്ല.",
        "ഫാക്ടറിയിൽ ബാലവേല നടക്കുന്നു.",
        "കുറഞ്ഞ വേതനം പോലും നൽകുന്നില്ല.",
    ],
    },
 {
    "id": "CONSUMER",

    "department": "Consumer Affairs Department",

    "description": (
        "Responsible for protecting consumer rights, resolving "
        "consumer disputes, unfair trade practices, defective "
        "products and service-related complaints."
    ),

    "handles": [
        "Defective Products",
        "Poor Service",
        "Refund Issues",
        "Warranty Claims",
        "Online Shopping Complaints",
        "Overcharging",
        "False Advertisement",
        "Unfair Trade Practices",
        "Consumer Fraud",
        "Billing Issues",
        "Product Replacement",
        "Service Delay",
    ],

    "keywords": [
        "consumer",
        "refund",
        "replacement",
        "defective product",
        "damaged product",
        "wrong product",
        "online shopping",
        "shopping",
        "service complaint",
        "poor service",
        "warranty",
        "guarantee",
        "overcharging",
        "fake product",
        "billing issue",
        "invoice",
        "customer service",
        "consumer court",
        "fraud product",
        "unfair trade",
    ],

    "priority_rules": {
        "high": [
            "consumer fraud",
            "large financial loss",
            "fake product",
            "unsafe product",
        ],
        "medium": [
            "refund not received",
            "replacement delayed",
            "service complaint",
            "overcharging",
        ],
        "low": [
            "warranty enquiry",
            "general consumer enquiry",
            "billing clarification",
        ],
    },

    "sample_complaints": [

        # English
        "I received a defective product.",
        "The company is not giving my refund.",
        "Wrong item was delivered.",
        "Customer service is not responding.",
        "The shop charged more than the MRP.",
        "Warranty claim was rejected.",
        "The product stopped working in two days.",
        "I received a fake product.",

        # Tamil
        "குறைபாடுள்ள பொருள் கிடைத்தது.",
        "எனது பணத்தை திருப்பி தரவில்லை.",
        "தவறான பொருள் அனுப்பப்பட்டுள்ளது.",
        "MRP-ஐ விட அதிகமாக பணம் வாங்கினர்.",

        # Tanglish
        "Refund kudukala.",
        "Wrong product vandhuruku.",
        "Fake product anupirukaanga.",
        "Customer care respond pannala.",

        # Hindi
        "मुझे खराब उत्पाद मिला।",
        "मेरा रिफंड नहीं मिला।",
        "गलत सामान भेजा गया।",
        "एमआरपी से ज्यादा पैसे लिए गए।",

        # Hinglish
        "Refund nahi mila.",
        "Wrong product deliver hua.",
        "Customer care reply nahi kar raha.",
        "Fake product mila.",

        # Telugu
        "నాకు పాడైన వస్తువు వచ్చింది.",
        "రిఫండ్ ఇవ్వడం లేదు.",
        "తప్పు వస్తువు పంపించారు.",

        # Kannada
        "ನನಗೆ ದೋಷಪೂರಿತ ಉತ್ಪನ್ನ ಬಂದಿದೆ.",
        "ರಿಫಂಡ್ ನೀಡುತ್ತಿಲ್ಲ.",
        "ತಪ್ಪು ಉತ್ಪನ್ನ ಕಳುಹಿಸಿದ್ದಾರೆ.",

        # Malayalam
        "എനിക്ക് തകരാറുള്ള ഉൽപ്പന്നം ലഭിച്ചു.",
        "റീഫണ്ട് നൽകിയിട്ടില്ല.",
        "തെറ്റായ ഉൽപ്പന്നം അയച്ചു.",
    ],
    },
 {
    "id": "FOOD",

    "department": "Food Safety Department",

    "description": (
        "Responsible for ensuring food safety, food hygiene, "
        "preventing food adulteration, inspecting restaurants, "
        "bakeries, hotels and food businesses, and protecting "
        "public health from unsafe food."
    ),

    "handles": [
        "Food Poisoning",
        "Food Adulteration",
        "Expired Food",
        "Unhygienic Restaurant",
        "Unsafe Drinking Water",
        "Bakery Inspection",
        "Street Food Hygiene",
        "Spoiled Food",
        "Contaminated Food",
        "Food Business Inspection",
        "Improper Food Storage",
        "Food Quality Complaints",
    ],

    "keywords": [
        "food",
        "restaurant",
        "hotel",
        "canteen",
        "bakery",
        "expired food",
        "spoiled food",
        "food poisoning",
        "adulterated food",
        "unsafe food",
        "dirty food",
        "hygiene",
        "kitchen",
        "street food",
        "contaminated food",
        "food quality",
        "food inspection",
        "fssai",
        "drinking water",
        "unhygienic",
    ],

    "priority_rules": {
        "high": [
            "food poisoning",
            "expired food",
            "contaminated food",
            "adulterated food",
            "unsafe drinking water",
        ],
        "medium": [
            "dirty restaurant",
            "poor hygiene",
            "spoiled food",
            "unclean kitchen",
        ],
        "low": [
            "food licence enquiry",
            "inspection request",
            "general complaint",
        ],
    },

    "sample_complaints": [

        # English
        "The restaurant served spoiled food.",
        "I got food poisoning after eating here.",
        "Expired food is being sold.",
        "The hotel kitchen is very dirty.",
        "Street food is prepared unhygienically.",
        "The bakery is selling stale bread.",
        "The drinking water is contaminated.",
        "The restaurant is very unhygienic.",

        # Tamil
        "உணவு கெட்டுப்போயுள்ளது.",
        "இந்த ஹோட்டலில் சாப்பிட்ட பிறகு உணவு விஷம் ஏற்பட்டது.",
        "காலாவதியான உணவுப் பொருட்கள் விற்கப்படுகின்றன.",
        "ஹோட்டல் மிகவும் அசுத்தமாக உள்ளது.",

        # Tanglish
        "Food spoil aayiduchu.",
        "Hotel clean illa.",
        "Expired food sell panraanga.",
        "Food poison aayiduchu.",

        # Hindi
        "रेस्टोरेंट में खराब खाना दिया गया।",
        "खाना खाने के बाद फूड पॉइज़निंग हो गई।",
        "एक्सपायर्ड खाना बेचा जा रहा है।",
        "होटल बहुत गंदा है।",

        # Hinglish
        "Food spoil ho gaya.",
        "Hotel clean nahi hai.",
        "Expired food bech rahe hain.",
        "Food poisoning ho gaya.",

        # Telugu
        "హోటల్‌లో పాడైన ఆహారం ఇచ్చారు.",
        "ఆహారం తిన్న తర్వాత ఫుడ్ పాయిజనింగ్ వచ్చింది.",
        "గడువు ముగిసిన ఆహారం అమ్ముతున్నారు.",

        # Kannada
        "ಹೋಟೆಲ್‌ನಲ್ಲಿ ಹಾಳಾದ ಆಹಾರ ನೀಡಿದ್ದಾರೆ.",
        "ಆಹಾರ ತಿಂದ ನಂತರ ಫುಡ್ ಪಾಯಿಸನಿಂಗ್ ಆಯಿತು.",
        "ಅವಧಿ ಮುಗಿದ ಆಹಾರ ಮಾರುತ್ತಿದ್ದಾರೆ.",

        # Malayalam
        "ഹോട്ടലിൽ പാഴായ ഭക്ഷണം നൽകി.",
        "ഭക്ഷണം കഴിച്ചതിന് ശേഷം ഫുഡ് പോയിസണിംഗ് ഉണ്ടായി.",
        "കാലാവധി കഴിഞ്ഞ ഭക്ഷണം വിൽക്കുന്നു.",
    ],
    },
 {
    "id": "EDUCATION",

    "department": "Education Department",

    "description": (
        "Responsible for administration of government schools and "
        "colleges, teacher management, scholarships, admissions, "
        "school infrastructure, student welfare and educational "
        "services."
    ),

    "handles": [
        "Government School Complaints",
        "Government College Complaints",
        "Teacher Complaints",
        "Scholarship Issues",
        "School Admission",
        "College Admission",
        "School Infrastructure",
        "Mid-Day Meal Issues",
        "Student Welfare",
        "School Management",
        "Textbook Distribution",
        "Educational Certificates",
    ],

    "keywords": [
        "school",
        "college",
        "education",
        "teacher",
        "student",
        "principal",
        "headmaster",
        "scholarship",
        "admission",
        "classroom",
        "midday meal",
        "mid day meal",
        "textbook",
        "uniform",
        "government school",
        "government college",
        "education office",
        "certificate",
        "school building",
        "exam",
    ],

    "priority_rules": {
        "high": [
            "school building collapse",
            "student safety",
            "teacher assault",
            "unsafe school building",
        ],
        "medium": [
            "scholarship delay",
            "teacher absent",
            "admission issue",
            "midday meal complaint",
            "school infrastructure",
        ],
        "low": [
            "certificate request",
            "general enquiry",
            "textbook request",
        ],
    },

    "sample_complaints": [

        # English
        "Teachers are not coming regularly.",
        "Scholarship amount has not been credited.",
        "Government school building is damaged.",
        "Students are not getting textbooks.",
        "Mid-day meal quality is poor.",
        "Admission has been delayed.",
        "The classroom roof is leaking.",
        "There are no toilets in the school.",

        # Tamil
        "ஆசிரியர்கள் பள்ளிக்கு வரவில்லை.",
        "உதவித்தொகை கிடைக்கவில்லை.",
        "அரசுப் பள்ளி கட்டிடம் சேதமடைந்துள்ளது.",
        "பாடப்புத்தகங்கள் வழங்கப்படவில்லை.",

        # Tanglish
        "Teacher varala.",
        "Scholarship varala.",
        "School building damage.",
        "Book kudukala.",

        # Hindi
        "शिक्षक स्कूल नहीं आ रहे हैं।",
        "छात्रवृत्ति नहीं मिली।",
        "सरकारी स्कूल की इमारत खराब है।",
        "किताबें नहीं मिलीं।",

        # Hinglish
        "Teacher school nahi aa rahe.",
        "Scholarship nahi mila.",
        "School building damage hai.",
        "Books nahi mile.",

        # Telugu
        "ఉపాధ్యాయులు పాఠశాలకు రావడం లేదు.",
        "స్కాలర్‌షిప్ రాలేదు.",
        "ప్రభుత్వ పాఠశాల భవనం దెబ్బతింది.",

        # Kannada
        "ಶಿಕ್ಷಕರು ಶಾಲೆಗೆ ಬರುತ್ತಿಲ್ಲ.",
        "ವಿದ್ಯಾರ್ಥಿವೇತನ ಬಂದಿಲ್ಲ.",
        "ಸರ್ಕಾರಿ ಶಾಲೆಯ ಕಟ್ಟಡ ಹಾಳಾಗಿದೆ.",

        # Malayalam
        "അധ്യാപകർ സ്കൂളിൽ വരുന്നില്ല.",
        "സ്കോളർഷിപ്പ് ലഭിച്ചിട്ടില്ല.",
        "സർക്കാർ സ്കൂൾ കെട്ടിടം തകർന്നിരിക്കുന്നു.",
    ],
    },
 {
    "id": "SOCIAL",

    "department": "Social Welfare Department",

    "description": (
        "Responsible for implementing government welfare schemes, "
        "social security programmes, pensions and welfare services "
        "for senior citizens, widows, persons with disabilities and "
        "economically weaker sections."
    ),

    "handles": [
        "Old Age Pension",
        "Widow Pension",
        "Disability Pension",
        "Government Welfare Schemes",
        "Senior Citizen Welfare",
        "Women Welfare",
        "Child Welfare",
        "SC/ST Welfare",
        "Financial Assistance",
        "Government Benefits",
        "Social Security",
        "Welfare Scheme Complaints",
    ],

    "keywords": [
        "pension",
        "old age pension",
        "widow pension",
        "disability pension",
        "social welfare",
        "welfare scheme",
        "government scheme",
        "beneficiary",
        "financial assistance",
        "old age",
        "senior citizen",
        "disabled",
        "disability",
        "widow",
        "social security",
        "benefit",
        "scholarship",
        "scheme",
        "allowance",
        "welfare office",
    ],

    "priority_rules": {
        "high": [
            "disabled person not receiving benefits",
            "elderly person abandoned",
            "urgent financial assistance",
        ],
        "medium": [
            "pension delay",
            "scheme application pending",
            "beneficiary issue",
            "allowance not received",
        ],
        "low": [
            "scheme enquiry",
            "document clarification",
            "general welfare request",
        ],
    },

    "sample_complaints": [

        # English
        "My old age pension has not been credited.",
        "Widow pension is pending.",
        "Disability pension has stopped.",
        "Government welfare benefits have not been received.",
        "My scheme application is pending.",
        "Senior citizen pension has been delayed.",
        "Financial assistance has not been approved.",
        "My welfare application was rejected without reason.",

        # Tamil
        "முதியோர் ஓய்வூதியம் கிடைக்கவில்லை.",
        "விதவை ஓய்வூதியம் நிலுவையில் உள்ளது.",
        "மாற்றுத்திறனாளி உதவித்தொகை நிறுத்தப்பட்டுள்ளது.",
        "அரசு நலத்திட்ட உதவி கிடைக்கவில்லை.",

        # Tanglish
        "Pension varala.",
        "Scheme approve pannala.",
        "Allowance kedaikala.",
        "Benefit varala.",

        # Hindi
        "मुझे वृद्धावस्था पेंशन नहीं मिली।",
        "विधवा पेंशन लंबित है।",
        "दिव्यांग पेंशन बंद हो गई है।",
        "सरकारी योजना का लाभ नहीं मिला।",

        # Hinglish
        "Pension nahi mila.",
        "Scheme approve nahi hua.",
        "Benefit nahi mila.",
        "Allowance nahi aaya.",

        # Telugu
        "వృద్ధాప్య పెన్షన్ రాలేదు.",
        "వితంతు పెన్షన్ పెండింగ్‌లో ఉంది.",
        "ప్రభుత్వ పథకం ప్రయోజనం అందలేదు.",

        # Kannada
        "ವೃದ್ಧಾಪ್ಯ ಪಿಂಚಣಿ ಬಂದಿಲ್ಲ.",
        "ವಿಧವಾ ಪಿಂಚಣಿ ಬಾಕಿಯಿದೆ.",
        "ಸರ್ಕಾರದ ಯೋಜನೆಯ ಲಾಭ ಸಿಕ್ಕಿಲ್ಲ.",

        # Malayalam
        "വാർദ്ധക്യ പെൻഷൻ ലഭിച്ചില്ല.",
        "വിധവ പെൻഷൻ ലഭിച്ചിട്ടില്ല.",
        "സർക്കാർ ക്ഷേമ പദ്ധതിയുടെ ആനുകൂല്യം ലഭിച്ചില്ല.",
    ],
    },
 {
    "id": "WCD",

    "department": "Women & Child Development Department",

    "description": (
        "Responsible for the welfare, protection and development of "
        "women and children through government schemes, child "
        "protection services, nutrition programmes and women safety "
        "initiatives."
    ),

    "handles": [
        "Child Protection",
        "Women Welfare",
        "Domestic Violence Support",
        "Child Abuse",
        "Child Labour Rehabilitation",
        "Anganwadi Services",
        "ICDS Services",
        "Nutrition Programmes",
        "Pregnant Women Welfare",
        "Girl Child Welfare",
        "Women Empowerment",
        "Child Welfare Schemes",
    ],

    "keywords": [
        "woman",
        "women",
        "child",
        "children",
        "girl",
        "boy",
        "anganwadi",
        "icds",
        "nutrition",
        "pregnant",
        "pregnancy",
        "child abuse",
        "domestic violence",
        "child welfare",
        "women welfare",
        "girl child",
        "malnutrition",
        "mother",
        "baby",
        "child protection",
    ],

    "priority_rules": {
        "high": [
            "child abuse",
            "child trafficking",
            "domestic violence",
            "sexual abuse",
            "abandoned child",
            "child marriage",
        ],
        "medium": [
            "anganwadi complaint",
            "nutrition issue",
            "pregnant woman assistance",
            "women welfare issue",
        ],
        "low": [
            "scheme enquiry",
            "benefit application",
            "general complaint",
        ],
    },

    "sample_complaints": [

        # English
        "A child is being abused.",
        "Domestic violence support is needed.",
        "Anganwadi centre is closed.",
        "Children are not receiving nutritious food.",
        "Pregnant women are not receiving benefits.",
        "A child has been abandoned.",
        "Girl child scholarship is pending.",
        "ICDS services are not functioning.",

        # Tamil
        "ஒரு குழந்தை துன்புறுத்தப்படுகிறது.",
        "குடும்ப வன்முறைக்கு உதவி தேவை.",
        "அங்கன்வாடி மையம் மூடப்பட்டுள்ளது.",
        "கர்ப்பிணிப் பெண்களுக்கு உதவி கிடைக்கவில்லை.",

        # Tanglish
        "Child abuse nadakuthu.",
        "Domestic violence help venum.",
        "Anganwadi open illa.",
        "Nutrition food kudukala.",

        # Hindi
        "एक बच्चे के साथ दुर्व्यवहार हो रहा है।",
        "घरेलू हिंसा के लिए सहायता चाहिए।",
        "आंगनवाड़ी केंद्र बंद है।",
        "गर्भवती महिलाओं को लाभ नहीं मिल रहा।",

        # Hinglish
        "Child abuse ho raha hai.",
        "Domestic violence help chahiye.",
        "Anganwadi band hai.",
        "Nutrition food nahi mil raha.",

        # Telugu
        "ఒక చిన్నారిపై వేధింపులు జరుగుతున్నాయి.",
        "అంగన్‌వాడీ కేంద్రం మూసి ఉంది.",
        "గర్భిణీ మహిళలకు సహాయం అందడం లేదు.",

        # Kannada
        "ಮಗುವಿನ ಮೇಲೆ ದೌರ್ಜನ್ಯ ನಡೆಯುತ್ತಿದೆ.",
        "ಅಂಗನವಾಡಿ ಕೇಂದ್ರ ಮುಚ್ಚಲಾಗಿದೆ.",
        "ಗರ್ಭಿಣಿಯರಿಗೆ ಸೌಲಭ್ಯ ಸಿಗುತ್ತಿಲ್ಲ.",

        # Malayalam
        "ഒരു കുട്ടിയെ പീഡിപ്പിക്കുന്നു.",
        "അങ്കണവാടി കേന്ദ്രം അടഞ്ഞിരിക്കുന്നു.",
        "ഗർഭിണികൾക്ക് ആനുകൂല്യം ലഭിക്കുന്നില്ല.",
    ],
    },
 {
    "id": "AGRICULTURE",

    "department": "Agriculture Department",

    "description": (
        "Responsible for agricultural development, farmer welfare, "
        "crop protection, irrigation support, soil health, pest "
        "management and implementation of government agricultural "
        "schemes."
    ),

    "handles": [
        "Crop Damage",
        "Pest Infestation",
        "Farmer Welfare Schemes",
        "Crop Disease",
        "Seed Distribution",
        "Fertilizer Supply",
        "Irrigation Assistance",
        "Soil Testing",
        "Agricultural Equipment",
        "Organic Farming",
        "Crop Insurance",
        "Farmer Subsidies",
    ],

    "keywords": [
        "farmer",
        "crop",
        "agriculture",
        "field",
        "farm",
        "pest",
        "insect",
        "crop disease",
        "fertilizer",
        "seed",
        "irrigation",
        "soil",
        "tractor",
        "harvest",
        "cultivation",
        "crop insurance",
        "farmer scheme",
        "subsidy",
        "drought",
        "agriculture office",
    ],

    "priority_rules": {
        "high": [
            "crop disease outbreak",
            "massive crop damage",
            "locust attack",
            "severe drought",
            "major irrigation failure",
        ],
        "medium": [
            "pest infestation",
            "fertilizer shortage",
            "seed supply delay",
            "crop insurance issue",
        ],
        "low": [
            "scheme enquiry",
            "soil testing request",
            "general farming advice",
        ],
    },

    "sample_complaints": [

        # English
        "My crops are damaged by pests.",
        "There is no irrigation water.",
        "Fertilizers are not available.",
        "Seeds have not been supplied.",
        "My crop insurance claim is pending.",
        "The crop has been affected by disease.",
        "Government subsidy has not been received.",
        "My farmland has dried due to drought.",

        # Tamil
        "என் பயிர்களை பூச்சிகள் சேதப்படுத்துகின்றன.",
        "பாசனத்திற்கு தண்ணீர் இல்லை.",
        "உரம் கிடைக்கவில்லை.",
        "விதைகள் வழங்கப்படவில்லை.",

        # Tanglish
        "Crop damage aayiduchu.",
        "Thanni illa irrigation-ku.",
        "Fertilizer kedaikala.",
        "Seed kudukala.",

        # Hindi
        "मेरी फसल कीटों से खराब हो गई।",
        "सिंचाई के लिए पानी नहीं है।",
        "उर्वरक उपलब्ध नहीं हैं।",
        "बीज नहीं मिले।",

        # Hinglish
        "Crop damage ho gaya.",
        "Pani nahi hai irrigation ke liye.",
        "Fertilizer nahi mila.",
        "Seed nahi mila.",

        # Telugu
        "నా పంటకు పురుగులు పట్టాయి.",
        "సాగునీరు లేదు.",
        "ఎరువులు అందలేదు.",

        # Kannada
        "ನನ್ನ ಬೆಳೆಗೆ ಕೀಟ ಹಾನಿಯಾಗಿದೆ.",
        "ನೀರಾವರಿಗೆ ನೀರು ಇಲ್ಲ.",
        "ರಸಗೊಬ್ಬರ ಸಿಗುತ್ತಿಲ್ಲ.",

        # Malayalam
        "എന്റെ വിള നശിച്ചിരിക്കുന്നു.",
        "ജലസേചനത്തിന് വെള്ളമില്ല.",
        "വളം ലഭിക്കുന്നില്ല.",
    ],
    },
 {
    "id": "ANIMAL",

    "department": "Animal Husbandry Department",

    "description": (
        "Responsible for livestock health, veterinary services, "
        "animal disease control, dairy development, poultry welfare, "
        "animal vaccination and overall livestock management."
    ),

    "handles": [
        "Livestock Diseases",
        "Veterinary Services",
        "Animal Vaccination",
        "Dairy Development",
        "Poultry Farming",
        "Goat Farming",
        "Cattle Health",
        "Animal Birth Services",
        "Artificial Insemination",
        "Animal Welfare",
        "Livestock Insurance",
        "Veterinary Hospital Complaints",
    ],

    "keywords": [
        "cow",
        "buffalo",
        "goat",
        "sheep",
        "pig",
        "horse",
        "livestock",
        "cattle",
        "veterinary",
        "vet",
        "animal hospital",
        "animal disease",
        "vaccination",
        "dairy",
        "milk",
        "poultry",
        "chicken",
        "animal welfare",
        "livestock insurance",
        "animal husbandry",
    ],

    "priority_rules": {
        "high": [
            "livestock disease outbreak",
            "mass animal deaths",
            "suspected rabies",
            "foot and mouth disease",
            "bird flu",
        ],
        "medium": [
            "animal vaccination",
            "veterinary doctor unavailable",
            "livestock illness",
            "dairy complaint",
        ],
        "low": [
            "breeding assistance",
            "livestock insurance enquiry",
            "general veterinary advice",
        ],
    },

    "sample_complaints": [

        # English
        "My cow is seriously sick.",
        "Veterinary doctor is not available.",
        "Many cattle are dying in the village.",
        "Vaccination has not been done.",
        "There is a disease spreading among goats.",
        "The veterinary hospital is closed.",
        "My poultry birds are dying.",
        "Need artificial insemination service.",

        # Tamil
        "என் மாடு மிகவும் நோயாக உள்ளது.",
        "கால்நடை மருத்துவர் இல்லை.",
        "கிராமத்தில் பல மாடுகள் இறக்கின்றன.",
        "தடுப்பூசி போடவில்லை.",

        # Tanglish
        "Cow-ku romba sick.",
        "Vet doctor illa.",
        "Vaccination pannala.",
        "Goat-ku disease vandhuruku.",

        # Hindi
        "मेरी गाय बीमार है।",
        "पशु चिकित्सक उपलब्ध नहीं हैं।",
        "गांव में कई मवेशी मर रहे हैं।",
        "टीकाकरण नहीं हुआ।",

        # Hinglish
        "Cow bahut sick hai.",
        "Vet doctor nahi hai.",
        "Vaccination nahi hua.",
        "Goat ko disease ho gaya.",

        # Telugu
        "నా ఆవు అనారోగ్యంగా ఉంది.",
        "వెటర్నరీ డాక్టర్ లేరు.",
        "పశువులకు వ్యాధి వ్యాపిస్తోంది.",

        # Kannada
        "ನನ್ನ ಹಸು ಅನಾರೋಗ್ಯದಲ್ಲಿದೆ.",
        "ಪಶುವೈದ್ಯರು ಇಲ್ಲ.",
        "ಜಾನುವಾರುಗಳಿಗೆ ರೋಗ ಹರಡುತ್ತಿದೆ.",

        # Malayalam
        "എന്റെ പശു രോഗബാധിതമാണ്.",
        "മൃഗഡോക്ടർ ലഭ്യമല്ല.",
        "കന്നുകാലികളിൽ രോഗം പടരുന്നു.",
    ],
    },
 {
    "id": "FISHERIES",

    "department": "Fisheries Department",

    "description": (
        "Responsible for fisheries development, fish farmer welfare, "
        "aquaculture, inland and marine fisheries, fishing licences, "
        "fish health and government fisheries schemes."
    ),

    "handles": [
        "Fishing Licence",
        "Fish Farmer Welfare",
        "Aquaculture",
        "Fish Disease",
        "Fish Seed Distribution",
        "Fish Pond Management",
        "Marine Fisheries",
        "Inland Fisheries",
        "Fishing Boat Registration",
        "Fishing Subsidy",
        "Fish Market Hygiene",
        "Fisheries Scheme Complaints",
    ],

    "keywords": [
        "fish",
        "fisheries",
        "fishing",
        "fishing licence",
        "fishing license",
        "fish farmer",
        "boat",
        "aquaculture",
        "fish pond",
        "fish disease",
        "marine",
        "lake",
        "river",
        "fish seed",
        "fishing subsidy",
        "net",
        "harbour",
        "harbor",
        "fish market",
        "fisherman",
    ],

    "priority_rules": {
        "high": [
            "mass fish death",
            "fish disease outbreak",
            "boat accident",
            "marine emergency",
        ],
        "medium": [
            "licence delay",
            "fish pond disease",
            "subsidy issue",
            "fish market hygiene",
        ],
        "low": [
            "scheme enquiry",
            "registration request",
            "general fisheries complaint",
        ],
    },

    "sample_complaints": [

        # English
        "Many fish have died in my pond.",
        "Fishing licence has not been issued.",
        "Fish are affected by disease.",
        "Fishing subsidy has not been received.",
        "Fish market is unhygienic.",
        "My fishing boat registration is pending.",
        "Fish seed has not been supplied.",
        "Aquaculture scheme benefits are delayed.",

        # Tamil
        "என் குளத்தில் மீன்கள் இறந்துவிட்டன.",
        "மீன்பிடி உரிமம் கிடைக்கவில்லை.",
        "மீன்களுக்கு நோய் பரவியுள்ளது.",
        "மீனவர் மானியம் கிடைக்கவில்லை.",

        # Tanglish
        "Fish ellam sethupochu.",
        "Fishing licence varala.",
        "Fish-ku disease vandhuruku.",
        "Subsidy kedaikala.",

        # Hindi
        "तालाब में मछलियाँ मर गई हैं।",
        "मछली पकड़ने का लाइसेंस नहीं मिला।",
        "मछलियों में बीमारी फैल गई है।",
        "सब्सिडी नहीं मिली।",

        # Hinglish
        "Fish mar gayi.",
        "Fishing licence nahi mila.",
        "Fish ko disease ho gaya.",
        "Subsidy nahi mila.",

        # Telugu
        "చెరువులో చేపలు చనిపోయాయి.",
        "ఫిషింగ్ లైసెన్స్ రాలేదు.",
        "చేపలకు వ్యాధి వచ్చింది.",

        # Kannada
        "ಕೊಳದಲ್ಲಿನ ಮೀನುಗಳು ಸತ್ತಿವೆ.",
        "ಮೀನುಗಾರಿಕೆ ಪರವಾನಗಿ ಸಿಕ್ಕಿಲ್ಲ.",
        "ಮೀನುಗಳಿಗೆ ರೋಗ ಬಂದಿದೆ.",

        # Malayalam
        "കുളത്തിലെ മീനുകൾ ചത്തു.",
        "മത്സ്യബന്ധന ലൈസൻസ് ലഭിച്ചില്ല.",
        "മീനുകൾക്ക് രോഗം ബാധിച്ചു.",
    ],
    },
 {
    "id": "HOUSING",

    "department": "Housing Board / Urban Development",

    "description": (
        "Responsible for government housing schemes, affordable "
        "housing, urban planning, layout approvals, slum "
        "rehabilitation and urban infrastructure development."
    ),

    "handles": [
        "Government Housing Schemes",
        "Housing Allotment",
        "Urban Planning",
        "Building Layout Approval",
        "Slum Rehabilitation",
        "Housing Construction",
        "Affordable Housing",
        "Housing Loan Subsidy",
        "Housing Board Complaints",
        "Building Plan Approval",
        "Urban Infrastructure",
        "Residential Development",
    ],

    "keywords": [
        "housing",
        "house",
        "home",
        "government house",
        "housing board",
        "urban development",
        "layout",
        "layout approval",
        "building approval",
        "building plan",
        "house allotment",
        "housing scheme",
        "pmay",
        "slum",
        "rehabilitation",
        "residential",
        "construction",
        "town planning",
        "urban planning",
        "housing subsidy",
    ],

    "priority_rules": {
        "high": [
            "unsafe government housing",
            "building collapse risk",
            "major housing safety issue",
        ],
        "medium": [
            "housing allotment delay",
            "layout approval pending",
            "housing scheme delay",
            "building approval delay",
        ],
        "low": [
            "housing enquiry",
            "scheme information",
            "application status",
        ],
    },

    "sample_complaints": [

        # English
        "My government house allotment is delayed.",
        "Housing scheme application is pending.",
        "Building plan approval has not been issued.",
        "The government apartment has developed cracks.",
        "My PMAY application is pending.",
        "The housing board has not responded.",
        "Slum rehabilitation work has stopped.",
        "Urban development work is incomplete.",

        # Tamil
        "அரசு வீட்டு ஒதுக்கீடு தாமதமாகியுள்ளது.",
        "வீட்டு திட்ட விண்ணப்பம் நிலுவையில் உள்ளது.",
        "கட்டிட அனுமதி கிடைக்கவில்லை.",
        "அரசு குடியிருப்பில் விரிசல் ஏற்பட்டுள்ளது.",

        # Tanglish
        "House allotment pending.",
        "PMAY approve pannala.",
        "Building approval varala.",
        "Housing board respond pannala.",

        # Hindi
        "सरकारी घर का आवंटन लंबित है।",
        "आवास योजना आवेदन लंबित है।",
        "बिल्डिंग प्लान मंजूर नहीं हुआ।",
        "पीएमएवाई आवेदन लंबित है।",

        # Hinglish
        "House allotment pending hai.",
        "PMAY approve nahi hua.",
        "Building approval nahi mila.",
        "Housing board reply nahi de raha.",

        # Telugu
        "ప్రభుత్వ ఇల్లు కేటాయింపు పెండింగ్‌లో ఉంది.",
        "హౌసింగ్ స్కీమ్ దరఖాస్తు పెండింగ్‌లో ఉంది.",
        "బిల్డింగ్ అనుమతి రాలేదు.",

        # Kannada
        "ಸರ್ಕಾರಿ ಮನೆ ಹಂಚಿಕೆ ಬಾಕಿಯಿದೆ.",
        "ವಸತಿ ಯೋಜನೆ ಅರ್ಜಿ ಬಾಕಿಯಿದೆ.",
        "ಕಟ್ಟಡ ಅನುಮತಿ ಸಿಕ್ಕಿಲ್ಲ.",

        # Malayalam
        "സർക്കാർ വീട് അനുവദിച്ചിട്ടില്ല.",
        "ഭവന പദ്ധതിയുടെ അപേക്ഷ ഇപ്പോഴും ബാക്കി.",
        "കെട്ടിട അനുമതി ലഭിച്ചിട്ടില്ല.",
    ],
    },
 {
    "id": "DISASTER",

    "department": "Disaster Management Authority",

    "description": (
        "Responsible for disaster preparedness, emergency response, "
        "relief operations, rehabilitation, early warning systems "
        "and coordination during natural and man-made disasters."
    ),

    "handles": [
        "Flood",
        "Cyclone",
        "Earthquake",
        "Landslide",
        "Tsunami",
        "Disaster Relief",
        "Disaster Rehabilitation",
        "Emergency Shelter",
        "Storm Damage",
        "Lightning Incidents",
        "Disaster Rescue",
        "Emergency Coordination",
    ],

    "keywords": [
        "flood",
        "cyclone",
        "earthquake",
        "tsunami",
        "landslide",
        "storm",
        "heavy rain",
        "cloudburst",
        "lightning",
        "disaster",
        "relief",
        "rehabilitation",
        "evacuation",
        "rescue",
        "shelter",
        "natural disaster",
        "emergency",
        "calamity",
        "disaster management",
        "rain damage",
    ],

    "priority_rules": {
        "high": [
            "flood",
            "cyclone",
            "earthquake",
            "tsunami",
            "landslide",
            "major disaster",
            "people trapped",
            "emergency evacuation",
        ],
        "medium": [
            "storm damage",
            "heavy rainfall",
            "relief camp request",
            "rehabilitation request",
        ],
        "low": [
            "awareness programme",
            "preparedness enquiry",
            "general information",
        ],
    },

    "sample_complaints": [

        # English
        "Our village is flooded.",
        "People are trapped due to flooding.",
        "A cyclone has damaged our houses.",
        "A landslide has blocked the road.",
        "Relief materials have not reached us.",
        "Emergency shelter is needed.",
        "Heavy rain has damaged our homes.",
        "Earthquake has damaged buildings.",

        # Tamil
        "எங்கள் கிராமத்தில் வெள்ளம் ஏற்பட்டுள்ளது.",
        "மக்கள் வெள்ளத்தில் சிக்கியுள்ளனர்.",
        "புயலால் வீடுகள் சேதமடைந்துள்ளன.",
        "நிலச்சரிவு ஏற்பட்டுள்ளது.",

        # Tanglish
        "Flood aayiduchu.",
        "People trap aayirukaanga.",
        "Cyclone nala house damage.",
        "Relief kedaikala.",

        # Hindi
        "हमारे गांव में बाढ़ आ गई है।",
        "लोग बाढ़ में फंसे हुए हैं।",
        "चक्रवात से घर क्षतिग्रस्त हो गए।",
        "भूस्खलन हो गया है।",

        # Hinglish
        "Flood aa gaya.",
        "Log flood me phas gaye.",
        "Cyclone se ghar damage ho gaya.",
        "Relief nahi mila.",

        # Telugu
        "మా గ్రామంలో వరద వచ్చింది.",
        "ప్రజలు వరదలో చిక్కుకున్నారు.",
        "తుఫాను వల్ల ఇళ్లు దెబ్బతిన్నాయి.",

        # Kannada
        "ನಮ್ಮ ಗ್ರಾಮದಲ್ಲಿ ಪ್ರವಾಹ ಬಂದಿದೆ.",
        "ಜನರು ಪ್ರವಾಹದಲ್ಲಿ ಸಿಲುಕಿದ್ದಾರೆ.",
        "ಚಂಡಮಾರುತದಿಂದ ಮನೆಗಳು ಹಾನಿಗೊಂಡಿವೆ.",

        # Malayalam
        "ഞങ്ങളുടെ ഗ്രാമത്തിൽ വെള്ളപ്പൊക്കം ഉണ്ടായി.",
        "ആളുകൾ വെള്ളപ്പൊക്കത്തിൽ കുടുങ്ങിയിരിക്കുന്നു.",
        "ചുഴലിക്കാറ്റിൽ വീടുകൾ നശിച്ചു.",
    ],
    },
 {
    "id": "TELECOM",

    "department": "Telecom Service Provider",

    "description": (
        "Responsible for mobile network services, broadband and "
        "fiber internet, SIM activation, mobile connectivity, "
        "telephone services and telecom infrastructure."
    ),

    "handles": [
        "Mobile Network Issues",
        "No Signal",
        "Poor Network Coverage",
        "Call Drops",
        "Broadband Issues",
        "Fiber Internet",
        "SIM Activation",
        "SIM Replacement",
        "Internet Speed Issues",
        "Mobile Data Issues",
        "Tower Complaints",
        "Telecom Billing",
    ],

    "keywords": [
        "network",
        "mobile network",
        "signal",
        "no signal",
        "call drop",
        "internet",
        "wifi",
        "broadband",
        "fiber",
        "sim",
        "mobile data",
        "tower",
        "telecom",
        "airtel",
        "jio",
        "vi",
        "bsnl",
        "5g",
        "4g",
        "network issue",
    ],

    "priority_rules": {
        "high": [
            "emergency communication failure",
            "complete network outage",
            "tower collapse",
        ],
        "medium": [
            "internet not working",
            "poor network",
            "call drop",
            "broadband outage",
            "sim activation issue",
        ],
        "low": [
            "plan enquiry",
            "billing enquiry",
            "sim replacement",
        ],
    },

    "sample_complaints": [

        # English
        "There is no mobile network in my area.",
        "Internet is not working.",
        "Broadband has been down since morning.",
        "Calls keep getting disconnected.",
        "SIM card has not been activated.",
        "Mobile data is very slow.",
        "Network tower is damaged.",
        "WiFi connection is not working.",

        # Tamil
        "எங்கள் பகுதியில் மொபைல் சிக்னல் இல்லை.",
        "இணையம் வேலை செய்யவில்லை.",
        "பிராட்பேண்ட் வேலை செய்யவில்லை.",
        "அழைப்புகள் துண்டிக்கப்படுகின்றன.",

        # Tanglish
        "Signal illa.",
        "Internet work aagala.",
        "Broadband down.",
        "Call drop aaguthu.",

        # Hindi
        "नेटवर्क नहीं आ रहा है।",
        "इंटरनेट काम नहीं कर रहा।",
        "ब्रॉडबैंड बंद है।",
        "कॉल बार-बार कट रही है।",

        # Hinglish
        "Network nahi aa raha.",
        "Internet nahi chal raha.",
        "Broadband down hai.",
        "Call drop ho raha hai.",

        # Telugu
        "సిగ్నల్ లేదు.",
        "ఇంటర్నెట్ పనిచేయడం లేదు.",
        "బ్రాడ్‌బ్యాండ్ పనిచేయడం లేదు.",

        # Kannada
        "ಸಿಗ್ನಲ್ ಇಲ್ಲ.",
        "ಇಂಟರ್ನೆಟ್ ಕೆಲಸ ಮಾಡುತ್ತಿಲ್ಲ.",
        "ಬ್ರಾಡ್‌ಬ್ಯಾಂಡ್ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿಲ್ಲ.",

        # Malayalam
        "സിഗ്നൽ ലഭിക്കുന്നില്ല.",
        "ഇന്റർനെറ്റ് പ്രവർത്തിക്കുന്നില്ല.",
        "ബ്രോഡ്ബാൻഡ് പ്രവർത്തിക്കുന്നില്ല.",
    ],
    },

 {
    "id": "BANK",

    "department": "Bank",

    "description": (
        "Responsible for banking services including savings and current "
        "accounts, ATM services, debit and credit cards, loans, digital "
        "banking, UPI, NEFT/RTGS/IMPS transactions, fraud reporting and "
        "customer banking support."
    ),

    "handles": [
        "Account Issues",
        "ATM Cash Not Dispensed",
        "ATM Card Problems",
        "Debit Card Issues",
        "Credit Card Issues",
        "Online Banking",
        "UPI Problems",
        "NEFT/RTGS/IMPS",
        "Loan Complaints",
        "Unauthorized Transactions",
        "Bank Fraud",
        "Internet Banking",
        "Cheque Issues",
        "Passbook Issues",
        "KYC Problems",
        "Bank Account Freeze",
    ],

    "keywords": [
        "bank",
        "bank account",
        "atm",
        "atm card",
        "cash withdrawal",
        "debit card",
        "credit card",
        "upi",
        "gpay",
        "phonepe",
        "paytm",
        "internet banking",
        "mobile banking",
        "loan",
        "emi",
        "account",
        "transaction",
        "fraud",
        "unauthorized transaction",
        "kyc",
        "cheque",
        "net banking",
        "imps",
        "neft",
        "rtgs",
    ],

    "priority_rules": {
        "high": [
            "bank fraud",
            "unauthorized transaction",
            "account hacked",
            "money stolen",
            "phishing attack",
            "atm cash debited but not received",
        ],
        "medium": [
            "atm not working",
            "loan issue",
            "upi transaction failed",
            "internet banking issue",
            "debit card blocked",
            "credit card complaint",
        ],
        "low": [
            "kyc update",
            "passbook update",
            "general enquiry",
            "cheque book request",
        ],
    },

    "sample_complaints": [

        # English
        "Money was deducted but cash did not come from the ATM.",
        "My bank account has been hacked.",
        "UPI transaction failed but money was deducted.",
        "Internet banking is not working.",
        "My debit card has been blocked.",
        "Unauthorized transaction happened in my account.",
        "Loan application is still pending.",
        "I am unable to withdraw cash from the ATM.",

        # Tamil
        "ATM-ல் பணம் வரவில்லை ஆனால் கணக்கில் இருந்து பணம் கழிக்கப்பட்டது.",
        "என் வங்கி கணக்கு ஹேக் செய்யப்பட்டது.",
        "UPI பரிவர்த்தனை தோல்வியடைந்தது.",
        "இணைய வங்கி சேவை வேலை செய்யவில்லை.",

        # Tanglish
        "ATM la cash varala.",
        "Account hack pannitaanga.",
        "UPI fail aayiduchu.",
        "Money deduct aayiduchu.",

        # Hindi
        "एटीएम से पैसा नहीं निकला लेकिन खाते से कट गया।",
        "मेरा बैंक अकाउंट हैक हो गया।",
        "यूपीआई ट्रांजैक्शन फेल हो गया।",
        "इंटरनेट बैंकिंग काम नहीं कर रही।",

        # Hinglish
        "ATM se cash nahi nikla.",
        "Account hack ho gaya.",
        "UPI fail ho gaya.",
        "Money deduct ho gaya.",

        # Telugu
        "ఏటీఎం నుండి డబ్బు రాలేదు కానీ ఖాతా నుండి డబ్బు కట్ అయింది.",
        "నా బ్యాంక్ ఖాతా హ్యాక్ అయింది.",
        "యూపీఐ లావాదేవీ విఫలమైంది.",

        # Kannada
        "ಎಟಿಎಂನಿಂದ ಹಣ ಬಂದಿಲ್ಲ ಆದರೆ ಖಾತೆಯಿಂದ ಕಡಿತವಾಗಿದೆ.",
        "ನನ್ನ ಬ್ಯಾಂಕ್ ಖಾತೆ ಹ್ಯಾಕ್ ಆಗಿದೆ.",
        "ಯುಪಿಐ ವ್ಯವಹಾರ ವಿಫಲವಾಗಿದೆ.",

        # Malayalam
        "എടിഎമ്മിൽ നിന്ന് പണം ലഭിച്ചില്ല, പക്ഷേ അക്കൗണ്ടിൽ നിന്ന് കുറച്ചു.",
        "എന്റെ ബാങ്ക് അക്കൗണ്ട് ഹാക്ക് ചെയ്തു.",
        "യുപിഐ ഇടപാട് പരാജയപ്പെട്ടു.",
    ],
 },

    

    
]