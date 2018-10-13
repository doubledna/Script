#!/usr/bin/python
# coding=uft-8

# Used for LDAP unified validation
import os
import ldap
# LDAP configurationimport ldap
from django_auth_ldap.config import LDAPSearch
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# basedn = "OU=Users,DC=xxx,DC=com"
AUTH_LDAP_SERVER_URI = 'ldap://IP:PORT'
AUTH_LDAP_BIND_DN = "CN=readonly,DC=xxx,DC=com"
AUTH_LDAP_BIND_PASSWORD = "xxx"
AUTH_LDAP_USER_SEARCH = LDAPSearch('ou=Users,dc=xxx,dc=com', ldap.SCOPE_SUBTREE, "(mail=%(user)s)")
# AUTH_LDAP_USER_DN_TEMPLATE = "cn=%(user)s, ou=Users, dc=xxx, dc=com"

AUTH_LDAP_USER_ATTR_MAP = {
     "first_name": "givenName",
     "last_name": "sn",
     "email": "mail"
}

# Group authority management
# created at 2018.06.13
from django_auth_ldap.config import  GroupOfUniqueNamesType

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=xxx,dc=com",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfUniqueNames)",
)

# very importance ! ! !
AUTH_LDAP_GROUP_TYPE = GroupOfUniqueNamesType(name_attr='cn')
# AUTH_LDAP_REQUIRE_GROUP = 'cn=vpn,ou=groups,dc=xxx,dc=com'
# AUTH_LDAP_DENY_GROUP = 'cn=disabled,ou=groups,dc=xxx,dc=com'

AUTH_LDAP_FIND_GROUP_PERMS = True


# from django_auth_ldap.config import LDAPGroupQuery
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=super_admin,ou=groups,dc=xxx,dc=com",
    "is_staff": "cn=super_admin,ou=groups,dc=xxx,dc=com",
    "is_superuser": "cn=super_admin,ou=groups,dc=xxx,dc=com",
}

AUTH_LDAP_MIRROR_GROUPS = True
# AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_ALWAYS_UPDATE_USER = True

