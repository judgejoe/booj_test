import unittest
import etl
import lxml 
import pandas as pd

class TestTransform(unittest.TestCase):
 
    def setUp(self):
        self.empty_filename = 'test_data/empty.xml'
        self.filename = 'test_data/test_listings.xml'
        self.context = '/Listings/Listing'
        self.columns = [{'name' : 'MlsId',                 'xpath' : 'string(ListingDetails/MlsId/text())',               'vtype' : 'scalar'},
                        {'name' : 'MlsName',               'xpath' : 'string(ListingDetails/MlsName/text())',             'vtype' : 'scalar'},
                        {'name' : 'DateListed',            'xpath' : 'string(ListingDetails/DateListed/text())',          'vtype' : 'scalar'},
                        {'name' : 'StreetAddress',         'xpath' : 'string(Location/StreetAddress/text())',             'vtype' : 'scalar'},
                        {'name' : 'City',                  'xpath' : 'string(Location/City/text())',                      'vtype' : 'scalar'},
                        {'name' : 'State',                 'xpath' : 'string(Location/State/text())',                     'vtype' : 'scalar'},
                        {'name' : 'Zip',                   'xpath' : 'string(Location/Zip/text())',                       'vtype' : 'scalar'},
                        {'name' : 'Price',                 'xpath' : 'string(ListingDetails/Price/text())',               'vtype' : 'scalar'},
                        {'name' : 'Bedrooms',              'xpath' : 'number(BasicDetails/Bedrooms/text())',              'vtype' : 'scalar'},
                        {'name' : 'Bathrooms_raw',         'xpath' : 'number(BasicDetails/Bathrooms/text())',             'vtype' : 'scalar'},
                        {'name' : 'FullBathrooms',         'xpath' : 'number(BasicDetails/FullBathrooms/text())',         'vtype' : 'scalar'},
                        {'name' : 'HalfBathrooms',         'xpath' : 'number(BasicDetails/HalfBathrooms/text())',         'vtype' : 'scalar'},
                        {'name' : 'ThreeQuarterBathrooms', 'xpath' : 'string(BasicDetails/ThreeQuarterBathrooms/text())', 'vtype' : 'scalar'},
                        {'name' : 'Full_Description',      'xpath' : 'string(BasicDetails/Description/text())',           'vtype' : 'scalar'},
                        {'name' : 'Appliances',            'xpath' : 'RichDetails/Appliances/*/text()',                   'vtype' : 'list'},
                        {'name' : 'Rooms',                 'xpath' : 'RichDetails/Rooms/*/text()',                        'vtype' : 'list'}]


    def test_bathrooms_field(self):
        df = etl.extract_xml(self.filename, self.columns, self.context)
        df = etl.transform_zillow(df)
        self.assertEqual(df.iloc[0]['Bathrooms'], 3.5)

    def test_bathrooms_calc_field(self):
        df = etl.extract_xml(self.filename, self.columns, self.context)
        df = etl.transform_zillow(df)
        self.assertEqual(df.iloc[1]['Bathrooms'], 3)

    def test_bathrooms_field_na(self):
        df = etl.extract_xml(self.filename, self.columns, self.context)
        df = etl.transform_zillow(df)
        self.assertTrue(pd.isnull(df.iloc[2]['Bathrooms']))

    def test_description_trunc(self):
        df = etl.extract_xml(self.filename, self.columns, self.context)
        df = etl.transform_zillow(df)
        self.assertEqual(len(df.iloc[0]['Description']),200)
''' 
    def test_empty_files(self):
        columns  = [{'name':'grandchildnode1','xpath':'string(grandchildnode1/text())','ctype':'scalar'},
                    {'name':'grandchildnode2','xpath':'string(grandchildnode2/text())','ctype':'scalar'},
                    {'name':'grandchildnode3','xpath':'grandchildnode3/*/text()','ctype':'list'}]
        try:
            self.assertRaises(lxml.etree.XMLSyntaxError, etl.extract_xml(self.empty_filename, columns, self.context))
        except lxml.etree.XMLSyntaxError:
            pass
 
    def test_list_extraction(self):
        columns  = [{'name':'grandchildnode1','xpath':'string(grandchildnode1/text())','ctype':'scalar'},
                    {'name':'grandchildnode2','xpath':'string(grandchildnode2/text())','ctype':'scalar'},
                    {'name':'grandchildnode3','xpath':'grandchildnode3/*/text()','ctype':'list'}]
        df = etl.extract_xml(self.filename, columns, self.context)
        self.assertEqual(df.iloc[0]['grandchildnode3'], "3,4")
        self.assertEqual(df.iloc[1]['grandchildnode3'], "3")

    def test_scalar_extraction(self):
        columns  = [{'name':'grandchildnode1','xpath':'string(grandchildnode1/text())','ctype':'scalar'},
                    {'name':'grandchildnode2','xpath':'string(grandchildnode2/text())','ctype':'scalar'},
                    {'name':'grandchildnode3','xpath':'grandchildnode3/*/text()','ctype':'list'}]
        df = etl.extract_xml(self.filename, columns, self.context)
        self.assertEqual(df.iloc[0]['grandchildnode1'], "1")

    def test_list_type_error(self):
        columns  = [{'name':'grandchildnode1','xpath':'string(grandchildnode1/text())','ctype':'scalar'},
                    {'name':'grandchildnode2','xpath':'string(grandchildnode2/text())','ctype':'scalar'},
                    {'name':'grandchildnode3','xpath':'grandchildnode3/*/text()','ctype':'scalar'}]
        try:
            self.assertRaises(TypeError, etl.extract_xml(self.filename, columns, self.context))
        except TypeError:
            pass

    def test_scalar_type_error(self):
        columns  = [{'name':'grandchildnode1','xpath':'string(grandchildnode1/text())','ctype':'scalar'},
                    {'name':'grandchildnode2','xpath':'string(grandchildnode2/text())','ctype':'list'},
                    {'name':'grandchildnode3','xpath':'grandchildnode3/*/text()','ctype':'list'}]
        try:
            self.assertRaises(TypeError, etl.extract_xml(self.filename, columns, self.context))
        except TypeError:
            pass
'''
if __name__ == '__main__':
    unittest.main()
