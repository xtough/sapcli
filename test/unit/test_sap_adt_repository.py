#!/usr/bin/env python3

import unittest

import sap.adt

from mock import Connection

from fixtures_adt_repository import PACKAGE_ROOT_NODESTRUCTURE_OK_RESPONSE


class TestRepository(unittest.TestCase):

    def test_read_node(self):
        connection = Connection([PACKAGE_ROOT_NODESTRUCTURE_OK_RESPONSE])

        mypkg = sap.adt.Package(connection, '$VICTORY')
        repository = sap.adt.Repository(connection)

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


if __name__ == '__main__':
    unittest.main()
