"""ADT Repository wrappers"""


def nodekeys_list_table(nodekeys):
    """Converts List of nodekeys to XML ABAP internal table"""

    body = '\n'.join(map(lambda key: f'<TV_NODEKEY>{key}</TV_NODEKEY>', nodekeys))
    return f'<DATA>\n{body}\n</DATA>'


class Repository:
    """Repository proxy"""

    def __init__(self, connection):
        self._connection = connection

    def read_node(self, adt_object, withdescr=False):
        """Returns node structure iterator"""

        keys = nodekeys_list_table(('000000',))
        self._connection.execute(
            'POST',
            'repository/nodestructure',
            params={
                'parent_name': adt_object.name,
                'parent_tech_name': adt_object.name,
                'parent_type': adt_object.objtype.code,
                'withShortDescriptions': str(withdescr).lower()},
            headers={
                'Accept': 'application/vnd.sap.as+xml;charset=UTF-8;dataname=com.sap.adt.RepositoryObjectTreeContent',
                'Content-Type': 'application/vnd.sap.as+xml; charset=UTF-8; dataname=null'},
            body=f'''<?xml version="1.0" encoding="UTF-8"?>
<asx:abap xmlns:asx="http://www.sap.com/abapxml" version="1.0">
<asx:values>
{keys}
</asx:values>
</asx:abap>''')
