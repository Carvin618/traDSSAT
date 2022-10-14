import re

from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar
from tradssat.format.exper_fmt import *

TRT_HEAD = re.compile(r'TREATMENTS(\W+[-]+FACTOR LEVELS[-]+)?')
GENERAL = 'GENERAL'

header_vars = [
    CharacterVar('EXPCODE', 10, info='Experiment identifier', fmt=EXPCODE),
    CharacterVar('ENAME', 60, info='Experiment name', fmt=ENAME, right_align=False)
]

main_vars = {
    # A special variable used to sign hidden variables.
    # CharacterVar('', 5, hidden=True),

    # General
    CharacterVar('PEOPLE', 75,  sect=GENERAL, info='Names of scientists', right_align=False),
    CharacterVar('ADDRESS', 75,  sect=GENERAL, info='Contact address of principal scientist', right_align=False),
    CharacterVar('SITE', 75,  sect=GENERAL, info='Name and location of experimental site(s)', right_align=False),

    FloatVar('PAREA', 6, 1, sect=GENERAL, spc=3, info='Gross plot area per rep, m-2'),
    IntegerVar('PRNO', 5, sect=GENERAL, info='Rows per plot'),
    FloatVar('PLEN', 5, 1, sect=GENERAL, info='Plot length, m'),
    IntegerVar('PLDR', 5, sect=GENERAL, info='Plots relative to drains, degrees'),
    IntegerVar('PLSP', 5, sect=GENERAL, info='Plot spacing, cm'),
    CharacterVar('PLAY', 5, sect=GENERAL, info='Plot layout'),
    FloatVar('HAREA', 5, 1, sect=GENERAL, info='Harvest area, m-2'),
    IntegerVar('HRNO', 5, sect=GENERAL, info='Harvest row number'),
    FloatVar('HLEN', 5, 1, sect=GENERAL, info='Harvest row length, m'),
    CharacterVar('HARM', 15,  sect=GENERAL, info='Harvest method'),

    # TODO: Need to support Multi-line.
    CharacterVar('NOTES', 500, sect=GENERAL, info='Notes', right_align=False),

    # Treatments
    IntegerVar('N', 2, spc=0, sect=TRT_HEAD, info='Treatment number'),
    IntegerVar('R', 1, sect=TRT_HEAD, info='Rotation component: number (default=1)', fmt=ROTNO),
    IntegerVar('O', 1, sect=TRT_HEAD, info='Rotation component: option (default=1)', fmt=ROTOPT),
    IntegerVar('C', 1, sect=TRT_HEAD, info='Crop component number (default = 0)', fmt=CRPNO),
    CharacterVar('TNAME', 25, info='Treatment name', fmt=TITLET, right_align=False),
    IntegerVar('CU', 2, info='Cultivar level', fmt=LNCU),
    IntegerVar('FL', 2, info='Field level', fmt=LNFLD),
    IntegerVar('SA', 2, info='Soil analysis level', fmt=LNSA),
    IntegerVar('IC', 2, info='Initial conditions level', fmt=LNIC),
    IntegerVar('MP', 2, info='Planting level', fmt=LNPLT),
    IntegerVar('MI', 2, info='Irrigation level', fmt=LNIR),
    IntegerVar('MF', 2, info='Fertilizer level', fmt=LNFER),
    IntegerVar('MR', 2, info='Residue level', fmt=LNRES),
    IntegerVar('MC', 2, info='Chemical applications level', fmt=LNCHE),
    IntegerVar('MT', 2, info='Tillage and rotations level', fmt=LNTIL),
    IntegerVar('ME', 2, info='Environmental modifications level', fmt=LNENV),
    IntegerVar('MH', 2, info='Harvest level', fmt=LNHAR),
    IntegerVar('SM', 2, info='Simulation control level', fmt=LNSIM),

    # Cultivars
    IntegerVar('C', 2, spc=0, sect='CULTIVARS', info='Cultivar level', fmt=LNCU),
    CharacterVar('CR', 2, info='Crop code', fmt=CG),
    CharacterVar('INGENO', 6,  info='Cultivar identifier (Institute code + Number)', fmt=VARNO),
    CharacterVar('CNAME', 16,  info='Cultivar name', fmt=CNAME, right_align=False),

    # Fields
    IntegerVar('L', 2, spc=0, sect='FIELDS', info='Field level', fmt=LNFLD),
    CharacterVar('ID_FIELD', 8, info='Field ID (Institute + Site + Field)', fmt=FLDNAM),
    CharacterVar('WSTA', 8,  info='Weather station code (Institute+Site)', fmt=WSTA, right_align=False),
    CharacterVar('FLSA', 5,  info='Slope and aspect, degrees from horizontal plus direction (W, NW, etc.)', fmt=SLOPE),
    FloatVar('FLOB', 5, 0, info='Obstruction to sun, degrees', fmt=FLOB),
    CharacterVar('FLDT', 5,  info='Drainage type, code', fmt=DFDRN),
    FloatVar('FLDD', 5, 0, info='Drain depth, cm', fmt=FLDD),
    FloatVar('FLDS', 5, 0, info='Drain spacing, m', fmt=SFDRN),
    CharacterVar('FLST', 5,  info='Surface stones(Abundance,%+Size,S,M,L)', fmt=FLST),
    CharacterVar('SLTX', 5,  info='Soil texture', fmt=SLTX, right_align=False),
    FloatVar('SLDP', 5, 0, info='Soil depth, cm', fmt=SLDP),
    CharacterVar('ID_SOIL', 10, info='Soil ID (Institute+Site+Year+Soil)', fmt=SLNO, right_align=False),
    CharacterVar('FLNAME', 25, info='Field level name', fmt=FLNAME, right_align=False),  # size is guess

    # Todo: define and verify
    FloatVar('XCRD', 15, 5, ),
    FloatVar('YCRD', 15, 5, ),
    FloatVar('ELEV', 9, 2, ),
    FloatVar('AREA', 17, 1, ),
    IntegerVar('SLEN', 5, ),
    FloatVar('FLWR', 5, 1, ),
    FloatVar('SLAS', 5, 1, ),
    CharacterVar('FLHST', 5),
    CharacterVar('FHDUR', 5),

    # Soil analysis
    IntegerVar('A', 2, spc=0, sect='SOIL ANALYSIS', info='Soil analysis level', fmt=LNSA),
    IntegerVar('SADAT', 5, info='Analysis date, year + days from Jan. 1', fmt=SADAT),
    CharacterVar('SMHB', 5,  info='pH in buffer determination method, code', fmt=SMHB),
    CharacterVar('SMPX', 5,  info='Phosphorus determination method, code', fmt=SMPX),
    CharacterVar('SMKE', 5, info='Potassium determination method, code', fmt=SMKE),
    FloatVar('SABL', 5, 0, info='Depth, base of layer, cm', fmt=SABL),
    FloatVar('SADM', 5, 1, info='Bulk density, moist, g cm-3', fmt=SADM),
    FloatVar('SAOC', 5, 2, info='Organic carbon, g kg-1 ', fmt=SAOC),
    FloatVar('SANI', 5, 2, info='Total nitrogen, g kg-1', fmt=SANI),
    FloatVar('SAPHW', 5, 1, info='pH in water', fmt=SAPHW),
    FloatVar('SAPHB', 5, 1, info='pH in buffer', fmt=SAPHB),
    FloatVar('SAPX', 5, 1, info='Phosphorus, extractable, mg kg-1 ', fmt=SAPX),
    FloatVar('SAKE', 5, 1, info='Potassium, exchangeable, cmol kg-1', fmt=SAKE),
    FloatVar('SASC', 5, 1, fmt=SASC),
    CharacterVar('SANAME', 25,  info='Soil analysis level name', fmt=SANAME),  # size is guess

    # Initial conditions
    IntegerVar('C', 2, spc=0, sect='INITIAL CONDITIONS', info='Initial conditions level', fmt=LNIC),
    CharacterVar('PCR', 5,  info='Previous crop code', fmt=PRCROP),
    IntegerVar('ICDAT', 5, info='Initial conditions measurement date, year + days', fmt=IDAYIC),
    FloatVar('ICRT', 5, 0, info='Root weight from previous crop, kg ha-1', fmt=WRESR),
    FloatVar('ICND', 5, 0, info='Nodule weight from previous crop, kg ha-1', fmt=WRESND),
    FloatVar('ICRN', 5, 2, info='Rhizobia number, 0 to 1 scale (default = 1)', fmt=EFINOC),
    FloatVar('ICRE', 5, 2, info='Rhizobia effectiveness, 0 to 1 scale (default = 1)', fmt=EFNFIX),

    # todo: define and verify
    FloatVar('ICWD', 5, 2, fmt=ICWD),
    FloatVar('ICRES', 5, 0, fmt=ICRES),
    FloatVar('ICREN', 5, 2, fmt=ICREN),
    FloatVar('ICREP', 5, 0, fmt=ICREP),
    FloatVar('ICRIP', 5, 0, fmt=ICRIP),
    FloatVar('ICRID', 5, 0, fmt=ICRID),
    CharacterVar('ICNAME', 25, info='Inicial condition level name', fmt=ICNAME, right_align=False),

    FloatVar('ICBL', 5, 0, info='Depth, base of layer, cm', fmt=DLAYRI),
    FloatVar('SH2O', 5, 3, info='Water, cm3 cm-3 x 100 volume percent', fmt=SWINIT),
    FloatVar('SNH4', 5, 1, info='Ammonium, KCl, g elemental N Mg-1 soil', fmt=INH4),
    FloatVar('SNO3', 5, 1, info='Nitrate, KCl, g elemental N Mg-1 soil', fmt=INO3),

    # Planting details
    IntegerVar('P', 2, spc=0, sect='PLANTING DETAILS', info='Planting level number', fmt=LNPLT),
    IntegerVar('PDATE', 5, info='Planting date, year + days from Jan. 1', fmt=YRPLT),
    IntegerVar('EDATE', 5, info='Emergence date, earliest treatment', fmt=IEMRG),
    FloatVar('PPOP', 5, 2, info='Plant population at seeding, plants m-2', fmt=PLANTS),
    FloatVar('PPOE', 5, 2, info='Plant population at emergence, plants m-2 ', fmt=PLTPOP),
    CharacterVar(
        'PLME', 1, spc=5, info='Planting method, transplant (T), seed (S), pregerminated seed (P) or nursery (N)',
        fmt=PLME
    ),
    CharacterVar('PLDS', 1, spc=5, info='Planting distribution, row (R), broadcast (B) or hill (H) ', fmt=PLDS),
    FloatVar('PLRS', 5, 1, info='Row spacing, cm', fmt=ROWSPC),
    FloatVar('PLRD', 5, 0, info='Row direction, degrees from N', fmt=AZIR),
    FloatVar('PLDP', 5, 1, info='Planting depth, cm', fmt=SDEPTH),
    FloatVar('PLWT', 5, 0, info='Planting material dry weight, kg ha-1', fmt=SDWTPL),
    FloatVar('PAGE', 5, 0, info='Transplant age, days ', fmt=SDAGE),
    FloatVar('PENV', 5, 1, info='Temp. of transplant environment, °C', fmt=ATEMP),
    FloatVar('PLPH', 5, 1, info='Plants per hill (if appropriate)', fmt=PLPH),
    FloatVar('SPRL', 5, 1, info='Initial sprout length', fmt=SPRLAP),

    # Todo: DSSAT model parse below four parameters but the input file doesn't provided. Need to check the document.
    IntegerVar('NFOR', 5, fmt=NFORC),
    FloatVar('PLTF', 5, 0, fmt=PLTFOR),
    IntegerVar('NDOF', 5, fmt=NDOF),
    IntegerVar('PMTY', 5, fmt=PMTYPE),

    CharacterVar('PLNAME', 25, info='Planting details level name', fmt=PLNAME, right_align=False),

    # IRRIGATION AND WATER MANAGEMENT
    IntegerVar('I', 2, spc=0, sect='IRRIGATION AND WATER MANAGEMENT', info='Irrigation level', fmt=LNIR),
    FloatVar('EFIR', 5, 2, info='Irrigation application efficiency, fraction', fmt=EFFIRX),
    FloatVar('IDEP', 5, 0, info='Management depth for automatic application, cm', fmt=DSOILX),
    FloatVar('ITHR', 5, 0, info='Threshold for automatic appl., % of max. available', fmt=THETCX),
    FloatVar('IEPT', 5, 0, info='End point for automatic appl., % of max. available', fmt=IEPTX),
    CharacterVar('IOFF', 5, info='End of applications, growth stage ', fmt=IOFFX),
    CharacterVar('IAME', 5, info='Method for automatic applications, code', fmt=IAMEX),
    FloatVar('IAMT', 5, 0, info='Amount per irrigation if fixed, mm', fmt=AIRAMX),

    # Todo: check size
    CharacterVar('IRNAME', 25, info='Irrigation level name', fmt=IRNAME, right_align=False),

    IntegerVar('IDATE', 5, info='Irrigation date, year + day or days from planting', fmt=IDLAPL),
    CharacterVar('IROP', 5, info='Irrigation operation, code', fmt=IRRCOD),
    FloatVar(
        'IRVAL', 5, 1,
        info='Irrigation amount, depth of water/water table, bund height, or percolation rate, mm or mm day -1',
        fmt=AMT
    ),
    IntegerVar('IIRV', 5, fmt=IIRV),

    # FERTILIZERS (INORGANIC)
    IntegerVar('F', 2, spc=0, sect='FERTILIZERS (INORGANIC)', info='Fertilizer application level', fmt=LNFERT),
    IntegerVar('FDATE', 5, info='Fertilization date, year + day or days from planting', fmt=FDAY),
    CharacterVar('FMCD', 5, info='Fertilizer material, code', fmt=IFTYPE),
    CharacterVar('FACD', 5, info='Fertilizer application/placement, code', fmt=FERCOD),
    FloatVar('FDEP', 5, 0, info='Fertilizer incorporation/application depth, cm', fmt=DFERT),
    FloatVar('FAMN', 5, 0, info='N in applied fertilizer, kg ha-1', fmt=ANFER),
    FloatVar('FAMP', 5, 0, info='P in applied fertilizer, kg ha-1', fmt=APFER),
    FloatVar('FAMK', 5, 0, info='K in applied fertilizer, kg ha-1', fmt=AKFER),
    FloatVar('FAMC', 5, 0, info='Ca in applied fertilizer, kg ha-1', fmt=ACFER),
    FloatVar('FAMO', 5, 0, info='Other elements in applied fertilizer, kg ha-1', fmt=AOFER),
    CharacterVar('FOCD', 5, info='Other element code, e.g., MG', fmt=FOCOD),

    # Todo: check size
    CharacterVar('FERNAME', 25, info='Fertilizer level name', fmt=FERNAME, right_align=False),

    # RESIDUES AND ORGANIC FERTILIZER
    IntegerVar('R', 2, spc=0, sect='RESIDUES AND ORGANIC FERTILIZER', info='Residue management level', fmt=LNRES),
    IntegerVar('RDATE', 5, info='Incorporation date, year + days', fmt=RESDAY),
    CharacterVar('RCOD', 5, info='Residue material, code', fmt=RESCOD),
    FloatVar('RAMT', 5, 0, info='Residue amount, kg ha-1', fmt=RESIDUE),
    FloatVar('RESN', 5, 2, info='Residue nitrogen concentration, %', fmt=RESN),
    FloatVar('RESP', 5, 2, info='Residue phosphorus concentration, %', fmt=RESP),
    FloatVar('RESK', 5, 2, info='Residue potassium concentration, %', fmt=RESK),
    FloatVar('RINP', 5, 0, info='Residue incorporation percentage, %', fmt=RINP),
    FloatVar('RDEP', 5, 0, info='Residue incorporation depth, cm', fmt=DEPRES),

    # Todo: check
    CharacterVar('RMET', 5, info='<same as FACD> Fertilizer application/placement, code', fmt=RMET),
    CharacterVar('RENAME', 25, info='Residue management level name', fmt=RENAME, right_align=False),

    # CHEMICAL APPLICATIONS
    IntegerVar('C', 2, spc=0, sect='CHEMICAL APPLICATIONS', info='Chemical applications level', fmt=LNCHE),
    IntegerVar('CDATE', 5, info='Application date, year + day or days from planting', fmt=CDATE),
    CharacterVar('CHCOD', 5, info='Chemical material, code', fmt=CHCOD),
    FloatVar('CHAMT', 5, 2, info='Chemical application amount, kg ha-1', fmt=CHAMT),
    CharacterVar('CHME', 5, info='Chemical application method, code', fmt=CHMET),
    FloatVar('CHDEP', 5, 0, info='Chemical application depth, cm', fmt=CHDEP),
    CharacterVar('CHT', 5, info='Chemical targets', fmt=CHT),
    CharacterVar('CHNAME', 25, info='Chemical application level name', fmt=CHNAME, right_align=False),  # todo: check size

    # TILLAGE
    IntegerVar('T', 2, spc=0, info='Tillage level', fmt=TL),
    IntegerVar('TDATE', 5, info='Tillage date, year + day', fmt=TDATE),
    CharacterVar('TIMPL', 5, info='Tillage implement, code', fmt=TIMPL),
    FloatVar('TDEP', 5, 0, info='Tillage implement, code', fmt=TDEP),
    CharacterVar('TINAME', 5, fmt=TINAME, right_align=False),

    # ENVIRONMENT MODIFICATIONS
    IntegerVar('E', 2, spc=0, info='Environment modifications level ', fmt=LNENV),
    IntegerVar('ODATE', 5, info='Modification date, year + day or days from planting', fmt=WMDATE),
    # The following are officially 2 variables each in DSSAT (code + value). However, as this is almost impossible
    # to implement sanely here (no space between variable names, and repeated names in the same section, we will treat
    # these as character values including both the code and value.
    CharacterVar('EDAY', size=5, info='Daylength adjustment, factor (A, S, M, R) + h', fmt=EDAY, right_align=False),
    CharacterVar('ERAD', size=5, info='Radiation adjustment, factor (A, S, M, R) + MJ m-2 d-1', fmt=ERAD,
                 right_align=False),
    CharacterVar('EMAX', size=5, info='Temperature (maximum) adjustment, factor (A, S, M, R) + °C', fmt=EMAX,
                 right_align=False),
    CharacterVar('EMIN', size=5, info='Temperature (minimum) adjustment, factor (A, S, M, R) + °C', fmt=EMIN,
                 right_align=False),
    CharacterVar('ERAIN', size=5, info='Precipitation adjustment, factor (A, S, M, R) + mm', fmt=ERAIN),
    CharacterVar('ECO2', size=5, info='CO2 adjustment, factor (A, S, M, R) + vpm', fmt=ECO2, right_align=False),
    CharacterVar('EDEW', size=5, info='Humidity (dew pt) adjustment, factor (A, S, M, R) + °C', fmt=EDEW,
                 right_align=False),
    CharacterVar('EWIND', size=5, info='Daylength adjustment, factor (A, S, M, R) + h', fmt=EWIND),
    # todo: check size
    CharacterVar('ENVNAME', size=25, info='Environmental modification level name', fmt=ENVNAME, right_align=False),

    # HARVEST DETAILS
    IntegerVar('H', 2, spc=0, info='Harvest level', fmt=LNHAR),
    IntegerVar('HDATE', 5, info='Harvest date, year + day or days from planting', fmt=HDATE),
    CharacterVar('HSTG', 5, info='Harvest stage', fmt=HSTG),
    CharacterVar('HCOM', 5, info='Harvest component, code', fmt=HCOM),
    CharacterVar('HSIZE', 5, info='Harvest size group, code', fmt=HSIZ),
    FloatVar('HPC', 5, 0, info='Harvest percentage, %', fmt=HPC),

    # Todo: check
    FloatVar('HBPC', 5, 0, info='', fmt=HBPC),
    CharacterVar('HNAME', 25, info='Harvest details level name', fmt=HNAME, right_align=False),

    # SIMULATION CONTROLS
    IntegerVar('N', 2, spc=0, sect='SIMULATION CONTROLS', info='Simulation control level number', fmt=LNSIM),
    CharacterVar('GENERAL', 11, info='Identifier', fmt=TITCOM, right_align=False),
    IntegerVar('NYERS', 2, spc=4, info='Years', fmt=NYRS),
    IntegerVar('NREPS', 2, spc=4, info='Replications', fmt=NREPSQ),
    CharacterVar(
        'START', 1, spc=5,
        info='Start of Simulation, code: '
             'E = On reported emergence date; '
             'I = When initial conditions measured; '
             'P = On reported planting date; '
             'S = On specified date',
        fmt=ISIMI,
    ),
    IntegerVar('SDATE', 5, info='Date, year + day (if needed)', fmt=YRSIM),
    IntegerVar('RSEED', 5, info='Random number seed', fmt=RSEED),
    CharacterVar('SNAME', 25, info='Title', fmt=TITSIM, right_align=False),
    CharacterVar('SMODEL', 8, info='', fmt=CRMODEL, right_align=False),  # todo: check

    CharacterVar('OPTIONS', 11, info='Identifier', fmt=TITOPT, right_align=False),
    CharacterVar('WATER', 1, spc=5, info='Water (Y = yes; N = no)', fmt=ISWWAT),
    CharacterVar('NITRO', 1, spc=5, info='Nitrogen (Y = yes; N = no)', fmt=ISWNIT),
    CharacterVar('SYMBI', 1, spc=5, info='Symbiosis (Y= yes, N= no, U= unlimited N)', fmt=ISWSYM),
    CharacterVar('PHOSP', 1, spc=5, info='Phosphorus (Y = yes; N = no)', fmt=ISWPHO),
    CharacterVar('POTAS', 1, spc=5, info='Potassium (Y = yes; N = no)', fmt=ISWPOT),
    CharacterVar('DISES', 1, spc=5, info='Diseases and other pests (Y = yes; N = no)', fmt=ISWDIS),
    CharacterVar('CHEM', 1, spc=5, info='Chemical applications (Y = yes; N = no)', fmt=ISWCHE),
    CharacterVar('TILL', 1, spc=5, info='Tillage (Y = yes; N = no)', fmt=ISWTIL),
    CharacterVar('CO2', 1, spc=5, miss='', info='CO2 effects (Y = yes; N = no)', fmt=ICO2),

    CharacterVar('METHODS', 11, info='Identifier', fmt=TITMET, right_align=False),
    CharacterVar(
        'WTHER', 1, spc=5,
        info='Weather: '
             'M = Measured data, as recorded; '
             'G = Simulated data, stored as *.WTG files; '
             'S = Simulated data (Internal weather generator using monthly inputs); '
             'W = Simulated data (Internal WGEN weather generator) ',
        fmt=MEWTH
    ),
    CharacterVar(
        'INCON', 1, spc=5,
        info='Initial Soil Conditions: '
             'M = As reported; '
             'S = Simulated outputs from previous model run',
        fmt=MESIC
    ),
    CharacterVar(
        'LIGHT', 1, spc=5,
        info='Light interception: '
             'E = Exponential with LAI; '
             "H = ‘Hedgerow’ calculations",
        fmt=MELI
    ),
    CharacterVar(
        'EVAPO', 1, spc=5,
        info='Evaporation: '
             'P = FAO - Penman; '
             'R = Ritchie modification of Priestley-Taylor',
        fmt=MEEVP
    ),
    CharacterVar(
        'INFIL', 1, spc=5,
        info='Infiltration: '
             'R = Ritchie method; '
             'S = Soil Conservation Service routines',
        fmt=MEINF
    ),
    CharacterVar(
        'PHOTO', 1, spc=5,
        info='Photosynthesis: '
             'C = Canopy photosynthesis response curve; '
             'R = Radiation use efficiency; '
             'L = Leaf photosynthesis response curve',
        fmt=MEPHO
    ),

    # Todo: check and document
    CharacterVar(
        'HYDRO', 1, spc=5,
        info='',
        fmt=MEHYD
    ),
    IntegerVar('NSWIT', 1, spc=5, info='', fmt=NSWITCH),
    CharacterVar(
        'MESOM', 1, spc=5, info='',
        fmt=MESOM
    ),
    CharacterVar(
        'MESEV', 1, spc=5, info='',
        fmt=MESEV
    ),
    CharacterVar('MESOL', 1, spc=5, fmt=MESOL),
    CharacterVar('METMP', 1, spc=5, fmt=METMP),
    CharacterVar('MEGHG', 1, spc=5, fmt=MEGHG),

    CharacterVar('MANAGEMENT', 11, info='Identifier', fmt=TITMAT, right_align=False),
    CharacterVar(
        'PLANT', 1, spc=5,
        info='Planting/Transplanting: '
             'A = Automatic when conditions satisfactory; '
             'R = On reported date',
        fmt=IPLTI
    ),
    CharacterVar(
        'IRRIG', 1, spc=5,
        info='Irrigation and Water Management: '
             'A = Automatic when required; '
             'N = Not irrigated; '
             'F = Automatic with fixed amounts at each irrigation date; '
             'R = On reported dates; '
             'D = As reported, in days after planting',
        fmt=IIRRI
    ),
    CharacterVar(
        'FERTI', 1, spc=5,
        info='Fertilization: '
             'A = Automatic when required; '
             'N = Not fertilized; '
             'F = Automatic with fixed amounts at each fertilization date; '
             'R = On reported dates; '
             'D = As reported, in days after planting',
        fmt=IFERI
    ),
    CharacterVar(
        'RESID', 1, spc=5,
        info='Residue applications: '
             'A = Automatic for multiple years/crop sequences; '
             'N = No applications; '
             'F = Automatic with fixed amounts at each residue application date; '
             'R = On reported dates; '
             'D = As reported, in days after planting',
        fmt=IRESI),
    CharacterVar(
        'HARVS', 1, spc=5,
        info='Harvest: '
             'A = Automatic when conditions satisfactory; '
             'G = At reported growth stage(s); '
             'M = At maturity; '
             'R = On reported date(s); '
             'D = On reported days after planting',
        fmt=IHARI),

    CharacterVar('OUTPUTS', 11, info='Identifier', fmt=TITOUT, right_align=False),
    CharacterVar('FNAME', 1, spc=5, info='Experiment (Y = yes, files named with the experiment code; N = no)', fmt=IOX),
    CharacterVar('OVVEW', 1, spc=5, info='Overview (Y = yes, new; A = append; N = no)', fmt=IDETO),
    CharacterVar('SUMRY', 1, spc=5, info='Summary (Y = yes, new; A = append; N = no)', fmt=IDETS),
    IntegerVar('FROPT', 2, spc=4, info='Frequency of output (days)', fmt=FROP),
    CharacterVar('GROUT', 1, spc=5, info='Growth (Y = yes; N = no)', fmt=IDETG),
    CharacterVar('CAOUT', 1, spc=5, info='Carbon (Y = yes; N = no)', fmt=IDETC),
    CharacterVar('WAOUT', 1, spc=5, info='Water (Y = yes; N = no)', fmt=IDETW),
    CharacterVar('NIOUT', 1, spc=5, info='Nitrogen (Y = yes; N = no)', fmt=IDETN),
    CharacterVar('MIOUT', 1, spc=5, info='Phosphorous (Y = yes; N = no)', fmt=IDETP),
    CharacterVar('DIOUT', 1, spc=5, info='Diseases and other pests (Y = yes; N = no)', fmt=IDETD),

    # todo: check and document
    CharacterVar('VBOSE', 1, spc=5, info='Wide (Y) or 80-column (N) daily outputs', fmt=IDETL),
    CharacterVar('CHOUT', 1, spc=5, fmt=IDETH),
    CharacterVar('OPOUT', 1, spc=5, fmt=IDETR),
    CharacterVar('FMOPT', 1, spc=5, fmt=FMOPT),

    # Automatic Management
    CharacterVar('AUTOMATIC MANAGEMENT', 0, fmt=SM_AUTO_MANAGEMENT_V),  # No idea why this variable even exists

    CharacterVar('PLANTING', 11, info='Identifier', fmt=TITPLA, right_align=False),
    IntegerVar('PFRST', 5, info='Earliest, year and day of year (YRDOY)', fmt=PWDINF),
    IntegerVar('PLAST', 5, info='Latest, year and day of year (YRDOY)', fmt=PWDINL),
    FloatVar('PH2OL', 5, 0, info='Lowermost soil water, % ', fmt=SWPLTL),
    FloatVar('PH2OU', 5, 0, info='Uppermost soil water, %', fmt=SWPLTH),
    FloatVar('PH2OD', 5, 0, info='Management depth for water, cm', fmt=SWPLTD),
    FloatVar('PSTMX', 5, 0, info='Max. soil temp. (10 cm av.), °C', fmt=PTX),
    FloatVar('PSTMN', 5, 0, info='Min. soil temp. (10 cm av.), °C', fmt=PTTN),

    CharacterVar('IRRIGATION', 11, info='Identifier', fmt=TITIRR, right_align=False),
    FloatVar('IMDEP', 5, 0, info='Management depth, cm', fmt=DSOIL),
    FloatVar('ITHRL', 5, 0, info='Threshold, % of maximum available', fmt=THETAC),
    FloatVar('ITHRU', 5, 0, info='End point, % of maximum available', fmt=IEPT),
    CharacterVar('IROFF', 5, info='End of applications, growth stage', fmt=IOFF),
    CharacterVar('IMETH', 5, info='Method, code', fmt=IAME),
    FloatVar('IRAMT', 5, 0, info='Amount per irrigation, if fixed, mm', fmt=AIRAMT),
    FloatVar('IREFF', 5, 2, info='Irrigation application efficiency, fraction', fmt=EFFIRR),

    CharacterVar('NITROGEN', 11, info='Identifier', fmt=TITNIT, right_align=False),
    FloatVar('NMDEP', 5, 0, info='Application depth, cm', fmt=DSOILN),
    FloatVar('NMTHR', 5, 0, info='Threshold, N stress factor, %', fmt=SOILNC),
    FloatVar('NAMNT', 5, 0, info='Amount per application, kg N ha-1', fmt=SOILNX),
    CharacterVar('NCODE', 5, info='Material, code', fmt=NCODE),
    CharacterVar('NAOFF', 5, info='End of applications, growth stage', fmt=NEND),

    CharacterVar('RESIDUES', 11, info='Identifier', fmt=TITRES, right_align=False),
    FloatVar('RIPCN', 5, 0, info='Incorporation percentage, % of remaining', fmt=RIP),
    IntegerVar('RTIME', 5, info='Incorporation time, days after harvest', fmt=NRESDL),
    FloatVar('RIDEP', 5, 0, info='Incorporation depth, cm', fmt=DRESMG),

    CharacterVar('HARVEST', 11, info='Identifier', fmt=TITHAR, right_align=False),
    IntegerVar('HFRST', 5, info='Earliest, days after maturity', fmt=HDLAY),
    IntegerVar('HLAST', 5, info='Latest, year and day of year (YRDOY)', fmt=HLATE),
    FloatVar('HPCNP', 5, 0, info='Percentage of product harvested, %', fmt=HPP),
    FloatVar('HPCNR', 5, 0, info='Percentage of residue harvested, %', fmt=HRP)

}
