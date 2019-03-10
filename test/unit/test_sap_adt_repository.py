#!/usr/bin/env python3

import unittest
from types import SimpleNamespace

import sap.adt

from mock import Connection

from fixtures_adt_repository import PACKAGE_ROOT_NODESTRUCTURE_OK_RESPONSE


class TestRepository(unittest.TestCase):

    def test_read_node(self):
        connection = Connection([PACKAGE_ROOT_NODESTRUCTURE_OK_RESPONSE])

        mypkg = sap.adt.Package(connection, '$VICTORY')
        repository = sap.adt.Repository(connection)

        #sap.get_logger().setLevel(0)
        node = repository.read_node(mypkg)

        self.assertEqual(connection.mock_methods(), [('POST', '/sap/bc/adt/repository/nodestructure')])

        self.assertEqual(connection.execs[0].headers,
            {'Accept': 'application/vnd.sap.as+xml;charset=UTF-8;dataname=com.sap.adt.RepositoryObjectTreeContent',
             'Content-Type': 'application/vnd.sap.as+xml; charset=UTF-8; dataname=null'})

        self.assertEqual(connection.execs[0].params,
            {'parent_name': '$VICTORY',
             'parent_tech_name': '$VICTORY',
             'parent_type': 'DEVC/K',
             'withShortDescriptions': 'false'})

        self.assertEqual(connection.execs[0].body, '''<?xml version="1.0" encoding="UTF-8"?>
<asx:abap xmlns:asx="http://www.sap.com/abapxml" version="1.0">
<asx:values>
<DATA>
<TV_NODEKEY>000000</TV_NODEKEY>
</DATA>
</asx:values>
</asx:abap>''')

        self.assertEqual([vars(obj) for obj in node.objects],
                         [vars(SimpleNamespace(
                              DESCRIPTION='Package with Tests',
                              DESCRIPTION_TYPE='',
                              EXPANDABLE='X',
                              IS_ABSTRACT='',
                              IS_CONSTANT='',
                              IS_CONSTRUCTOR='',
                              IS_EVENT_HANDLER='',
                              IS_FINAL='',
                              IS_FOR_TESTING='',
                              IS_READ_ONLY='',
                              IS_REDEFINITION='',
                              IS_STATIC='',
                              NODE_ID='',
                              OBJECT_NAME='$VICTORY_TESTS',
                              OBJECT_TYPE='DEVC/K',
                              OBJECT_URI='/sap/bc/adt/packages/%24victory_tests',
                              OBJECT_VIT_URI='/sap/bc/adt/vit/wb/object_type/devck/object_name/%24VICTORY_TESTS',
                              PARENT_NAME='',
                              TECH_NAME='$VICTORY_TESTS',
                              VISIBILITY='0'
                              ))])

        self.assertEqual(node.categories,
                         [SimpleNamespace(CATEGORY='packages', CATEGORY_LABEL='Package'),
                          SimpleNamespace(CATEGORY='source_library', CATEGORY_LABEL='Source Code Library')])

        self.assertEqual(node.types,
                         [SimpleNamespace(OBJECT_TYPE='CLAS/OC', CATEGORY_TAG='source_library', OBJECT_TYPE_LABEL='Classes', NODE_ID='000005'),
                          SimpleNamespace(OBJECT_TYPE='DEVC/K', CATEGORY_TAG='packages', OBJECT_TYPE_LABEL='Subpackages', NODE_ID='000007'),
                          SimpleNamespace(OBJECT_TYPE='INTF/OI', CATEGORY_TAG='source_library', OBJECT_TYPE_LABEL='Interfaces', NODE_ID='000011'),
                          SimpleNamespace(OBJECT_TYPE='PROG/P', CATEGORY_TAG='source_library', OBJECT_TYPE_LABEL='Programs', NODE_ID='000002')])


if __name__ == '__main__':
    unittest.main()
