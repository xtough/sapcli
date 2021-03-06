#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
import unittest
from unittest.mock import Mock, PropertyMock, patch, mock_open, call
from types import SimpleNamespace

import sap.cli.checkout

from mock import Connection


def parse_args(argv):
    parser = ArgumentParser()
    sap.cli.checkout.CommandGroup().install_parser(parser)
    return parser.parse_args(argv)


def assert_wrote_file(unit_test, fake_open, file_name, contents, fileno=1):
    start = (fileno - 1) * 4
    unit_test.assertEqual(fake_open.mock_calls[start + 0], call(file_name, 'w'))
    unit_test.assertEqual(fake_open.mock_calls[start + 1], call().__enter__())
    unit_test.assertEqual(fake_open.mock_calls[start + 2], call().write(contents))
    unit_test.assertEqual(fake_open.mock_calls[start + 3], call().__exit__(None, None, None))


class TestCheckoutCommandGroup(unittest.TestCase):

    def test_constructor(self):
        sap.cli.checkout.CommandGroup()


class TestCheckout(unittest.TestCase):

    @patch('sap.adt.Class.test_classes', new_callable=PropertyMock)
    @patch('sap.adt.Class.implementations', new_callable=PropertyMock)
    @patch('sap.adt.Class.definitions', new_callable=PropertyMock)
    @patch('sap.adt.Class.text', new_callable=PropertyMock)
    def test_checkout_class(self, fake_text, fake_defs, fake_impls, fake_tests):
        fake_text.return_value = 'class zcl_hello_world'

        fake_defs.return_value = Mock()
        fake_defs.return_value.text = '* definitions'

        fake_impls.return_value = Mock()
        fake_impls.return_value.text = '* implementations'

        fake_tests.return_value = Mock()
        fake_tests.return_value.text = '* tests'

        args = parse_args(['class', 'ZCL_HELLO_WORLD'])
        with patch('sap.cli.checkout.open', mock_open()) as fake_open:
            args.execute(Connection(), args)

        assert_wrote_file(self, fake_open, 'zcl_hello_world.clas.abap', 'class zcl_hello_world', fileno=1)
        assert_wrote_file(self, fake_open, 'zcl_hello_world.clas.locals_def.abap', '* definitions', fileno=2)
        assert_wrote_file(self, fake_open, 'zcl_hello_world.clas.locals_imp.abap', '* implementations', fileno=3)
        assert_wrote_file(self, fake_open, 'zcl_hello_world.clas.testclasses.abap', '* tests', fileno=4)

    @patch('sap.adt.Interface.text', new_callable=PropertyMock)
    def test_checkout_interface(self, fake_text):
        fake_text.return_value = 'interface zif_hello_world'

        args = parse_args(['interface', 'ZIF_HELLO_WORLD'])
        with patch('sap.cli.checkout.open', mock_open()) as fake_open:
            args.execute(Connection(), args)

        assert_wrote_file(self, fake_open, 'zif_hello_world.intf.abap', 'interface zif_hello_world')

    @patch('sap.adt.Program.text', new_callable=PropertyMock)
    def test_checkout_program(self, fake_text):
        fake_text.return_value = 'REPORT z_hello_world'

        args = parse_args(['program', 'Z_HELLO_WORLD'])
        with patch('sap.cli.checkout.open', mock_open()) as fake_open:
            args.execute(Connection(), args)

        assert_wrote_file(self, fake_open, 'z_hello_world.prog.abap', 'REPORT z_hello_world')


class TestCheckoutPackage(unittest.TestCase):

    @patch('sap.cli.checkout.checkout_class')
    @patch('sap.cli.checkout.checkout_interface')
    @patch('sap.cli.checkout.checkout_program')
    @patch('sap.adt.package.walk')
    def test_checkout_package_simple(self, fake_walk, fake_prog, fake_intf, fake_clas):
        conn = Connection([])

        fake_walk.return_value = iter(
            (([],
              ['$VICTORY_TESTS'],
              [SimpleNamespace(typ='INTF/OI', name='ZIF_HELLO_WORLD'),
               SimpleNamespace(typ='CLAS/OC', name='ZCL_HELLO_WORLD'),
               SimpleNamespace(typ='PROG/P', name='Z_HELLO_WORLD'),
               SimpleNamespace(typ='7777/3', name='Magic Unicorn')]),
             (['$VICTORY_TESTS'],
              [],
              [SimpleNamespace(typ='CLAS/OC', name='ZCL_TESTS')]))
        )

        args = parse_args(['package', '$VICTORY'])
        with patch('sap.cli.checkout.print') as fake_print:
            args.execute(conn, args)

        fake_prog.assert_called_once_with(conn, 'Z_HELLO_WORLD')
        fake_intf.assert_called_once_with(conn, 'ZIF_HELLO_WORLD')
        fake_clas.assert_called_once_with(conn, 'ZCL_HELLO_WORLD')

        self.assertEqual(fake_print.mock_calls, [call('Ignoring sub-package: $VICTORY_TESTS', file=sys.stderr),
                                                 call('Unsupported object: 7777/3 Magic Unicorn', file=sys.stderr)])


if __name__ == '__main__':
    unittest.main()
