#node:0��ʵ��/����ʵ��   1ȫΪʵ��  2 <a href="oe"> om</a>��ʽ
#s p o ģʽo��Ҫ��Ϊ1 ��ɾ��һ��ʵ��ʱ����ɾ����oΪ���ʵ��ıߣ����´�����ѯ���Ϊ�գ�����������
# TRIPLE_ARG={
#     's':[1,0],
#     'p':[0,1],
#     'o':[2,0]
# }

TRIPLE_ARG={
    's':{'node':1,'sort':0},
    'p':{'node':0,'sort':1},
    'o':{'node':0,'sort':0}
    # 'o':{'node':0,'sort':0}
}

MENT2ENT_ARG={
    'm':{'node':0,'sort':1},
    'e':{'node':1,'sort':0}
}
TRIPLE_COL = 'spo'
MENT2ENT_COL = 'me'
TRIPLE_S = 0
TRIPLE_P = 1
TRIPLE_O = 2

def PRINT_PREDICATE(edge):
	return edge['p']

ENTITIES_USE_OBJECTID = False
ENTITY_ARG={
    'entity_name':'_id'
}

# DB_ARG={
# 'db_name':'cndbpedia',
# 'db_host' : '10.141.208.26',
# 'db_port' : 27017,
# 'db_username' : 'gdmdbuser',
# 'db_password' : '6QEUI8dhnq'
# }

TABLENAME_ARG={
'usertablename' : 'user',
'edgestablename' : 'triples',
'nodestablename' : 'entities',
'ment2enttablename':'ment2ent',
'schematablename':'schema1'
}

USER_ARG={
'user_username' : 'username',
'user_password' : 'password'
}
SCHEMA_COL='spo'