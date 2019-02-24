"""ADT proxy for ABAP Unit"""

import sys

import sap.adt
import sap.adt.aunit
import sap.cli.core
from sap.errors import SAPCliError


class CommandGroup(sap.cli.core.CommandGroup):
    """Adapter converting command line parameters to sap.adt.Class methods
       calls.
    """

    def __init__(self):
        super(CommandGroup, self).__init__('aunit')


def print_results_to_stream(run_results, stream):
    """Print results to stream"""

    for alert in run_results.alerts:
        print(f'{alert.severity} {alert.kind} {alert.title}', file=stream)

    for program in run_results.programs:
        print(f'{program.name}', file=stream)

        for test_class in program.test_classes:
            print(f'  {test_class.name}', file=stream)

            for test_method in test_class.test_methods:
                print(f'    {test_method.name}', file=stream)

                for alert in test_method.alerts:
                    print(f'      {alert.severity} {alert.kind} {alert.title}', file=stream)


@CommandGroup.command()
@CommandGroup.argument('name')
@CommandGroup.argument('type', choices=['program', 'class', 'package'])
def run(connection, args):
    """Prints it out based on command line configuration.

       Exceptions:
         - SAPCliError:
           - when the given type does not belong to the type white list
    """

    types = {'program': sap.adt.Program, 'class': sap.adt.Class, 'package': sap.adt.Package}
    try:
        typ = types[args.type]
    except KeyError:
        raise SAPCliError(f'Unknown type: {args.type}')

    aunit = sap.adt.AUnit(connection)
    obj = typ(connection, args.name)
    response = aunit.execute(obj)
    run_results = sap.adt.aunit.parse_run_results(response.text)
    print_results_to_stream(run_results, sys.stdout)
