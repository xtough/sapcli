"""Repository ADT fixtures"""

from mock import Response

PACKAGE_ROOT_NODESTRUCTURE_XML = '''<?xml version="1.0" encoding="UTF-8"?><asx:abap xmlns:asx="http://www.sap.com/abapxml" version="1.0">
  <asx:values>
    <DATA>
      <TREE_CONTENT>
        <SEU_ADT_REPOSITORY_OBJ_NODE>
          <OBJECT_TYPE>DEVC/K</OBJECT_TYPE>
          <OBJECT_NAME>$VICTORY_TESTS</OBJECT_NAME>
          <TECH_NAME>$VICTORY_TESTS</TECH_NAME>
          <OBJECT_URI>/sap/bc/adt/packages/%24victory_tests</OBJECT_URI>
          <OBJECT_VIT_URI>/sap/bc/adt/vit/wb/object_type/devck/object_name/%24VICTORY_TESTS</OBJECT_VIT_URI>
          <EXPANDABLE>X</EXPANDABLE>
          <IS_FINAL/>
          <IS_ABSTRACT/>
          <IS_FOR_TESTING/>
          <IS_EVENT_HANDLER/>
          <IS_CONSTRUCTOR/>
          <IS_REDEFINITION/>
          <IS_STATIC/>
          <IS_READ_ONLY/>
          <IS_CONSTANT/>
          <VISIBILITY>0</VISIBILITY>
          <NODE_ID/>
          <PARENT_NAME/>
          <DESCRIPTION>Package with Tests</DESCRIPTION>
          <DESCRIPTION_TYPE/>
        </SEU_ADT_REPOSITORY_OBJ_NODE>
      </TREE_CONTENT>
      <CATEGORIES>
        <SEU_ADT_OBJECT_CATEGORY_INFO>
          <CATEGORY>packages</CATEGORY>
          <CATEGORY_LABEL>Package</CATEGORY_LABEL>
        </SEU_ADT_OBJECT_CATEGORY_INFO>
        <SEU_ADT_OBJECT_CATEGORY_INFO>
          <CATEGORY>source_library</CATEGORY>
          <CATEGORY_LABEL>Source Code Library</CATEGORY_LABEL>
        </SEU_ADT_OBJECT_CATEGORY_INFO>
      </CATEGORIES>
      <OBJECT_TYPES>
        <SEU_ADT_OBJECT_TYPE_INFO>
          <OBJECT_TYPE>CLAS/OC</OBJECT_TYPE>
          <CATEGORY_TAG>source_library</CATEGORY_TAG>
          <OBJECT_TYPE_LABEL>Classes</OBJECT_TYPE_LABEL>
          <NODE_ID>000005</NODE_ID>
        </SEU_ADT_OBJECT_TYPE_INFO>
        <SEU_ADT_OBJECT_TYPE_INFO>
          <OBJECT_TYPE>DEVC/K</OBJECT_TYPE>
          <CATEGORY_TAG>packages</CATEGORY_TAG>
          <OBJECT_TYPE_LABEL>Subpackages</OBJECT_TYPE_LABEL>
          <NODE_ID>000007</NODE_ID>
        </SEU_ADT_OBJECT_TYPE_INFO>
        <SEU_ADT_OBJECT_TYPE_INFO>
          <OBJECT_TYPE>INTF/OI</OBJECT_TYPE>
          <CATEGORY_TAG>source_library</CATEGORY_TAG>
          <OBJECT_TYPE_LABEL>Interfaces</OBJECT_TYPE_LABEL>
          <NODE_ID>000011</NODE_ID>
        </SEU_ADT_OBJECT_TYPE_INFO>
        <SEU_ADT_OBJECT_TYPE_INFO>
          <OBJECT_TYPE>PROG/P</OBJECT_TYPE>
          <CATEGORY_TAG>source_library</CATEGORY_TAG>
          <OBJECT_TYPE_LABEL>Programs</OBJECT_TYPE_LABEL>
          <NODE_ID>000002</NODE_ID>
        </SEU_ADT_OBJECT_TYPE_INFO>
      </OBJECT_TYPES>
    </DATA>
  </asx:values>
</asx:abap>
'''

PACKAGE_ROOT_NODESTRUCTURE_OK_RESPONSE = Response(status_code=200, text=PACKAGE_ROOT_NODESTRUCTURE_XML, headers={
    'Content-Type': 'application/vnd.sap.as+xml; charset=utf-8; dataname=com.sap.adt.RepositoryObjectTreeContent'})
