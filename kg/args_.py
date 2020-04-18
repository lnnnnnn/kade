# TRIPLE_ARG={
#     'u':[1,0],
#     'v':[1,0],
#     'w':[0,0],
#     'tp':[0,1]
# }

TRIPLE_ARG={
    'u':{'node':1,'sort':0},
    'v':{'node':1,'sort':0},
    'w':{'node':0,'sort':0},
    'tp':{'node':0,'sort':1}
}

TRIPLE_COL = ['u', 'v', 'w', 'tp']
TRIPLE_S = 0
TRIPLE_O = 1
#TRIPLE_COL = {
#	's': 'u',
#	'p': 'tp',
#	'o': 'v'
#}

def PRINT_PREDICATE(edge):
	return '%s(%.3f)' % (edge['tp'], float(edge['w']))

MENT2ENT_ARG = None

ENTITIES_USE_OBJECTID = True

ENTITY_ARG={
    'entity_name':'node'
}

# DB_ARG={
# 'db_name':'graph',
# 'db_host' : '10.141.208.26',
# 'db_port' : 27017,
# 'db_username' : 'gdmdbuser',
# 'db_password' : '6QEUI8dhnq'
# }

TABLENAME_ARG={
'usertablename' : 'user',
'edgestablename' : 'graph_edges',
'nodestablename' : 'graph_nodes',
'schematablename' : 'schema'
}

USER_ARG={
'user_username' : 'username',
'user_password' :'password'
}
SCHEMA_COL=['u', 'v', 'w', 'tp']
