napp = {
    # Mappings are dictionaries that map variable names to
    # functions that rewrite the value for a variable (for e.g. unit conversion)
    'mappings': {
        # format AGE to 3 positions
        'AGE': lambda x: x.zfill(3)
    },
    # Nocode is a list of variables whose values should not be coded (i.e. they should become literals)
    'nocode': ['AGE', 'BPLPARSE', 'CFU', 'CFUSIZE', 'CITYPOP', 'CNTYAREA', 'COUNTYUS',
               'ELDCH', 'ENUMDIST', 'FAMUNIT', 'HEADLOC', 'HHNBRNO', 'HHWT',
               'LINENUM', 'MOMLOC', 'NAMEFRST', 'NAMELAST', 'NCOUPLES', 'NFAMS', 'NHGISJOIN',
               'NMOTHERS', 'NUMPERHH', 'OCCSTRNG', 'OCSCORUS', 'PAGENUM', 'PARISHGB', 'PARSE', 'PERNUM',
               'PERWT', 'POPLOC', 'PRMFAMSZ', 'QOCCGB', 'REALPROP', 'RECTYPE',
               'REEL', 'RELATS', 'RESLSNO', 'SDSTCA', 'SEAUS', 'SEIUS', 'SERIAL', 'SERVANTS',
               'SPLOC', 'YEAR', 'YNGCH', 'YRSUSA1']
}