import csv
import boto3
import argparse 
import time
from decimal import *

def main():
   try:
      parser = argparse.ArgumentParser()  
      parser.add_argument("--csv_file", "--f", type=str, required=True)
      parser.add_argument("--table_name", "--t", type=str, required=True)
      parser.add_argument("--endpoint_url", "--u", type=str, required=True)

      args = parser.parse_args()

      _csv_file = args.csv_file
      _table_name = args.table_name
      _endpoint_url = args.endpoint_url

      start = time.time()
      json_data = convert_csv_to_json_list(_csv_file)
      batch_write(json_data, _table_name, _endpoint_url)
      end = time.time()
      print("\n+++ Elapsed time: {}\n".format(end - start)) 

   except Exception as ex:
      print ("Error : ", ex.args)   
   finally:
      input("Press Enter to continue...")


def ignore_exception(IgnoreException=Exception,DefaultVal=None):
   """ 
   From: 
      https://stackoverflow.com/questions/2262333/is-there-a-built-in-or-more-pythonic-way-to-try-to-parse-a-string-to-an-integer
      Decorator for ignoring exception from a function
      e.g.   @ignore_exception(DivideByZero)
      e.g.2. ignore_exception(DivideByZero)(Divide)(2/0)
      ex:
      sint = ignore_exception(ValueError)(int)
      print sint("Hello World") # prints none
      print sint("1340") # prints 1340
   """
   def dec(function):
      def _dec(*args, **kwargs):
         try:
            return function(*args, **kwargs)
         except IgnoreException:
            return DefaultVal
      return _dec
   return dec

def convert_csv_to_json_list(file):
   items = []
   with open(file) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:

         data = {}
         
         # int or float parser funcs
         sint = ignore_exception(ValueError)(int)
         sfloat = ignore_exception(ValueError)(float)

         for colName in row.keys():
            if colName == 'fips':
               data[colName] = int(row[colName])
            elif colName == 'area_name' or colName == 'state_abbreviation':
               data[colName] = " " if not row[colName] else row[colName]
            else:
               if sint(row[colName]) is not None:
                  data[colName] = int(row[colName])
               elif sfloat(row[colName]) is not None:
                  data[colName] = Decimal(row[colName])
               else:
                  data[colName] = row[colName]

         items.append(data)
   return items

def batch_write(items, _table_name, _endpoint_url):
   db_res = boto3.resource('dynamodb', endpoint_url=_endpoint_url, region_name='us-west-2')
   table = db_res.Table(_table_name)
   db_client = boto3.client('dynamodb', endpoint_url=_endpoint_url, region_name='us-west-2')

   scan = table.scan()

   # Clean out the table
   if scan['Count'] > 0:
      with table.batch_writer() as batch:
            for each in scan['Items']:
               batch.delete_item(
                  Key={
                     'fips': int(each['fips']),
                     'area_name' : each['area_name']
                     })

   # write to table         
   with table.batch_writer() as batch:
      for item in items:
         batch.put_item(Item=item)

   print('Data import finished')

if __name__ == '__main__':
   main()
