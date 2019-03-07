"""ADT Object export"""

import sap.adt
import sap.cli.core


class CommandGroup(sap.cli.core.CommandGroup):
    """Commands for exporting ADT objects"""

    def __init__(self):
        super(CommandGroup, self).__init__('checkout')


def download_abap_source(object_name, source_object, typsfx):
    """Reads the text and saves it in the corresponding file"""

    filename = f'{object_name}{typsfx}.abap'
    with open(filename, 'w') as dest:
        dest.write(source_object.text)


def download_class(clas):
    """Download entire class"""

    download_abap_source(clas.name, clas, '.clas')
    download_abap_source(clas.name, clas.definitions, '.clas.locals_def')
    download_abap_source(clas.name, clas.implementations, '.clas.locals_imp')
    download_abap_source(clas.name, clas.test_classes, '.clas.testclasses')


@CommandGroup.command('class')
@CommandGroup.argument('name')
def abapclass(connection, args):
    """Download all class sources"""

    download_class(sap.adt.Class(connection, args.name))


@CommandGroup.command()
@CommandGroup.argument('name')
def program(connection, args):
    """Download program sources"""

    download_abap_source(args.name, sap.adt.Program(connection, args.name), '.prog')


@CommandGroup.command()
@CommandGroup.argument('name')
def interface(connection, args):
    """Download interface sources"""

    download_abap_source(args.name, sap.adt.Interface(connection, args.name), '.intf')
