
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Amazon.DynamoDBv2.Model;

namespace DynamoDB_intro
{
    public static partial class Ddb_Intro
    {
        private static TableDescription tableDescription;
        public static ScanResponse ScanResults;
        public static QueryResponse QueryResults;
        public static string Message;

        /*--------------------------------------------------------------------------
        *                       CreatingTable_async
        *--------------------------------------------------------------------------*/
        public static async Task CreatingTable_async(string new_table_name,
                                   List<AttributeDefinition> table_attributes,
                                   List<KeySchemaElement> table_key_schema,
                                   ProvisionedThroughput provisionedThroughput,
                                   List<LocalSecondaryIndex> table_loc_sec_indexes)
        {
            Message = "";
            Message = String.Format("  -- Creating a new table named {0}...", new_table_name);
            Console.WriteLine(Message);

            if (await checkingTableExistence_async(new_table_name))
            {
                Message += String.Format("     -- No need to create a new table...");
                Console.WriteLine(Message);
                return;
            }
            if (operationFailed)
                return;

            operationSucceeded = false;
            Task<bool> newTbl = CreateNewTable_async(new_table_name,
                                                      table_attributes,
                                                      table_key_schema,
                                                      provisionedThroughput, 
                                                      table_loc_sec_indexes);
            await newTbl;
        }


        /*--------------------------------------------------------------------------
         *                      checkingTableExistence_async
         *--------------------------------------------------------------------------*/
        public static async Task<bool> checkingTableExistence_async(string table_name)
        {
            Message = "";
            DescribeTableResponse descResponse;

            operationSucceeded = false;
            operationFailed = false;
            ListTablesResponse tblResponse = await Ddb_Intro.client.ListTablesAsync();
            if (tblResponse.TableNames.Contains(table_name))
            {
                Message = String.Format("A table named {0} already exists in DynamoDB!", table_name);
                Console.WriteLine(Message);
                // If the table exists, get its description
                try
                {
                    descResponse = await Ddb_Intro.client.DescribeTableAsync(table_name);
                    operationSucceeded = true;
                }
                catch (Exception ex)
                {
                    Message += String.Format("However, its description is not available ({0})", ex.Message);
                    Console.WriteLine(Message);

                    Ddb_Intro.tableDescription = null;
                    operationFailed = true;
                    return (true);
                }
                Ddb_Intro.tableDescription = descResponse.Table;
                return (true);
            }
            else
            {
                Message = 
                    String.Format("A table named {0} does not exists in DynamoDB!", table_name);
                return (false);
            }
        }

        public static async Task<bool> ScanTable_async(string table_name)
        {
            Message = "";

            ScanRequest request;
            ScanResponse response;

            // Build the 'DeleteTableRequest' structure for the new table
            request = new ScanRequest
            {
                TableName = table_name
            };

            operationSucceeded = false;
            operationFailed = false;
            try
            {
                Task<ScanResponse> _table = Ddb_Intro.client.ScanAsync(request);
                response = await _table;
                ScanResults = response;
                Message = String.Format("-- Scanned the \"{0}\" table successfully!", table_name);
                Console.WriteLine(Message);
                operationSucceeded = true;
            }
            catch (Exception ex)
            {
                Message = String.Format("-- FAILED to scan the table \"{1}\", because: {0}.", ex.Message, table_name);
                Console.WriteLine(Message);
                operationFailed = true;
                return (false);
            }
            return (true);
        }

        public static async Task<bool> DeleteTable_async(string table_name)
        {
            Message = "";

            DeleteTableRequest request;
            DeleteTableResponse response;

            // Build the 'DeleteTableRequest' structure for the new table
            request = new DeleteTableRequest
            {
                TableName = table_name
            };

            operationSucceeded = false;
            operationFailed = false;
            try
            {
                Task<DeleteTableResponse> _table = Ddb_Intro.client.DeleteTableAsync(request);
                response = await _table;
                Message = String.Format("-- Deleted the \"{0}\" table successfully!", table_name);
                Console.WriteLine(Message);
                operationSucceeded = true;
            }
            catch (Exception ex)
            {
                Message = String.Format("-- FAILED to delete the table \"{1}\", because: {0}.", ex.Message, table_name);
                Console.WriteLine(Message);
                operationFailed = true;
                return (false);
            }
            return (true);
        }

        public static async Task<bool> DescribeTable_async(string table_name)
        {
            Message = "";

            DescribeTableRequest request;
            DescribeTableResponse response;

            // Build the 'DeleteTableRequest' structure for the new table
            request = new DescribeTableRequest
            {
                TableName = table_name
            };

            operationSucceeded = false;
            operationFailed = false;
            try
            {
                Task<DescribeTableResponse> _table = Ddb_Intro.client.DescribeTableAsync(request);
                response = await _table;
                TableDescription tableDescription = response.Table;

                Message += String.Format("Table name: {0}\n", tableDescription.TableName);
                Message += String.Format("Creation time: {0}\n", tableDescription.CreationDateTime);
                Message += String.Format("Item count: {0}\n", tableDescription.ItemCount);
                Message += String.Format("Table size (bytes): {0}\n", tableDescription.TableSizeBytes);
                Message += String.Format("Table status: {0}\n", tableDescription.TableStatus);

                // List table key schema
                List<KeySchemaElement> tableSchema = tableDescription.KeySchema;
                for (int i = 0; i < tableSchema.Count; i++)
                {
                    KeySchemaElement element = tableSchema[i];
                    Message += String.Format("Key: Name = {0}, KeyType = {1}\n",
                        element.AttributeName, element.KeyType);
                }

                // List attribute definitions
                List<AttributeDefinition> attributeDefinitions = tableDescription.AttributeDefinitions;
                for (int i = 0; i < attributeDefinitions.Count; i++)
                {
                    AttributeDefinition definition = attributeDefinitions[i];
                    Message += String.Format("Attribute: Name = {0}, Type = {1}\n",
                        definition.AttributeName, definition.AttributeType);
                }
                Message += String.Format("Throughput: Reads = {0}, Writes = {1}\n",
                    tableDescription.ProvisionedThroughput.ReadCapacityUnits,
                    tableDescription.ProvisionedThroughput.WriteCapacityUnits);


                Console.WriteLine(Message);
                operationSucceeded = true;
            }
            catch (Exception ex)
            {
                Message = String.Format("-- FAILED to obtain description the table \"{1}\", because: {0}.", ex.Message, table_name);
                Console.WriteLine(Message);
                operationFailed = true;
                return (false);
            }
            return (true);
        }


        /*--------------------------------------------------------------------------
        *                CreateNewTable_async
        *--------------------------------------------------------------------------*/
        public static async Task<bool> CreateNewTable_async(string table_name,
                                                             List<AttributeDefinition> table_attributes,
                                                             List<KeySchemaElement> table_key_schema,
                                                             ProvisionedThroughput provisioned_throughput, 
                                                             List<LocalSecondaryIndex> table_loc_sec_indexes)
        {
            CreateTableRequest request;
            CreateTableResponse response;

            // Build the 'CreateTableRequest' structure for the new table
            request = new CreateTableRequest
            {
                TableName = table_name,
                AttributeDefinitions = table_attributes,
                KeySchema = table_key_schema,
                // Provisioned-throughput settings are always required,
                // although the local test version of DynamoDB ignores them.
                ProvisionedThroughput = provisioned_throughput,
                LocalSecondaryIndexes = table_loc_sec_indexes
            };

            operationSucceeded = false;
            operationFailed = false;
            try
            {
                Task<CreateTableResponse> makeTbl = Ddb_Intro.client.CreateTableAsync(request);
                response = await makeTbl;
                Message += String.Format("     -- Created the \"{0}\" table successfully!", table_name);
                Console.WriteLine(Message);
                operationSucceeded = true;
            }
            catch (Exception ex)
            {
                Message = String.Format("     FAILED to create the new table, because: {0}.", ex.Message);
                Console.WriteLine(Message);
                operationFailed = true;
                return (false);
            }

            // Report the status of the new table...
            Message += String.Format("     Status of the new table: '{0}'.", response.TableDescription.TableStatus);
            Console.WriteLine(Message);
            Ddb_Intro.tableDescription = response.TableDescription;
            return (true);
        }

        public static async Task<bool> QueryTable_async(QueryRequest qRequest)
        {
            Message = "";

            operationSucceeded = false;
            operationFailed = false;

            QueryResponse response;

            try
            {
                Task<QueryResponse> clientQueryTask = client.QueryAsync(qRequest);
                response = await clientQueryTask;
                QueryResults = response;
                operationSucceeded = true;
                Message = String.Format("-- Queried table \"{0}\" successfully!", qRequest.TableName);
                
            }
            catch (Exception ex)
            {
                Message = String.Format("The low-level query FAILED, because:  {0}.", ex.Message);
                operationFailed = true;
                return (false);
            }

            return (true);
        }

    }
}
