using System;
using Abp.Threading;
using System.Windows.Forms;
using DynamoDB_intro;
using Amazon.DynamoDBv2.Model;
using System.Collections.Generic;
using Amazon.DynamoDBv2;
using System.IO;
using System.Linq;
using Newtonsoft.Json;
using System.Data;
using Newtonsoft.Json.Linq;

namespace _2T
{
    public partial class main : Form
    {
        private static List<string> area_names = new List<string>();
        private static List<string> state_abbrev;

        public main()
        {
            InitializeComponent();
        }

        private void checkIfTableExistsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var table_name = txtBoxTableName.Text;
            if (table_name == null)
            {
                throw new ArgumentNullException("table_name cannot be empty");
            }

            Ddb_Intro.createClient(true);
            AsyncHelper.RunSync<bool>(() => Ddb_Intro.checkingTableExistence_async(table_name));
            stsLabel.Text = Ddb_Intro.Message;
        }

        private void testLocalDBConnectionToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Ddb_Intro.createClient(true);
            stsLabel.Text = Ddb_Intro.Message;
        }

        private void deleteTableToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var table_name = txtBoxTableName.Text;
            if (table_name == null)
            {
                throw new ArgumentNullException("table_name cannot be empty");
            }

            Ddb_Intro.createClient(true);
            AsyncHelper.RunSync<bool>(() => Ddb_Intro.DeleteTable_async(table_name));
            stsLabel.Text = Ddb_Intro.Message;
        }

        private void describeTableToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var table_name = txtBoxTableName.Text;
            if (table_name == null)
            {
                throw new ArgumentNullException("table_name cannot be empty");
            }

            Ddb_Intro.createClient(true);
            AsyncHelper.RunSync<bool>(() => Ddb_Intro.DescribeTable_async(table_name));
            MessageBox.Show(Ddb_Intro.Message);
        }

        private void createTableToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var table_name = txtBoxTableName.Text;
            if (table_name == null)
            {
                throw new ArgumentNullException("table_name cannot be empty");
            }

            Ddb_Intro.createClient(true);

            var AttributeDefinitions = new List<AttributeDefinition>()
            {
                new AttributeDefinition { AttributeName = "fips",  AttributeType = "N" },
                new AttributeDefinition { AttributeName = "area_name",  AttributeType = "S" }
            };

            var KeySchema = new List<KeySchemaElement>()
            {
                new KeySchemaElement    { AttributeName = "fips",   KeyType = "HASH" }
                ,new KeySchemaElement    { AttributeName = "area_name",   KeyType = "RANGE" }
            };

            var ProvisionedThroughput = new ProvisionedThroughput
            {
                ReadCapacityUnits = 1,
                WriteCapacityUnits = 1
            };

            var LocalSecondaryIndexes = new List<LocalSecondaryIndex>();
            //                  {
            //                      new LocalSecondaryIndex()
            //                      {
            //                          IndexName = "byStateCounty_index",

            //                          KeySchema = new List<KeySchemaElement>() {
            //                              new KeySchemaElement() {
            //                                  AttributeName = "Id", KeyType = "HASH"
            //                              },
            //                              new KeySchemaElement() {
            //                                  AttributeName = "PostedBy", KeyType = "RANGE"
            //                              }
            //                          },
            //                          Projection = new Projection() {
            //                              ProjectionType = ProjectionType.KEYS_ONLY
            //                          }
            //                      }
            //                  };


            AsyncHelper.RunSync(() => Ddb_Intro.CreatingTable_async(
                                        table_name, 
                                        AttributeDefinitions, 
                                        KeySchema, 
                                        ProvisionedThroughput,
                                        LocalSecondaryIndexes));
            stsLabel.Text = Ddb_Intro.Message;
        }

        private void loadDataToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //--f data\county_facts_sm.csv --t counts
            string _path = getAppPath();
            string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\import_data"));
            Directory.SetCurrentDirectory(_newPath);
            var endpoint_url = 
                System.Configuration.ConfigurationManager.AppSettings.Get("endpoint_url");
            var csv_file =
                System.Configuration.ConfigurationManager.AppSettings.Get("csv_file");

            var strCmdText = $"--f {(_newPath + "\\" + csv_file)} --t {txtBoxTableName.Text} --u {endpoint_url}";
            run_python_cmd("import_data.py", strCmdText, true, false);

        }

        private void scanTableToolStripMenuItem_Click(object sender, EventArgs e)
        {

            var table_name = txtBoxTableName.Text;
            if (table_name == null)
            {
                throw new ArgumentNullException("table_name cannot be empty");
            }

            Ddb_Intro.createClient(true);
            AsyncHelper.RunSync<bool>(() => Ddb_Intro.ScanTable_async(table_name));
            //var t = Ddb_Intro.ScanTable_async(table_name).Result;
            stsLabel.Text =  Ddb_Intro.Message;

            // Distinct list of State Abbreviations
            //.Where(o => !string.IsNullOrWhiteSpace(o))
            state_abbrev = 
                Ddb_Intro.ScanResults.Items.Select(dict => dict["state_abbreviation"].S).Distinct().OrderBy(o => o).ToList();
            
            // Bind to Drop-downs
            BindingSource bndSource_state_abbrev = new BindingSource();
            bndSource_state_abbrev.DataSource = state_abbrev;
            cmbStates.DataSource = bndSource_state_abbrev.DataSource;

            //foreach (Dictionary<string, AttributeValue> item in Ddb_Intro.ScanResults.Items)
            //{
            //    // Process the result.
            //    PrintItem(item);
            //}
        }

        private void cmbStates_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void btnSelectArea_Click(object sender, EventArgs e)
        {
            area_names =
                Ddb_Intro.ScanResults.Items.Where(dict => dict["state_abbreviation"].S == cmbStates.SelectedValue.ToString()).Select(dict => dict["area_name"].S).Distinct().OrderBy(o => o).ToList();
            // Bind to Drop-downs
            BindingSource bndSource_areas = new BindingSource();
            bndSource_areas.DataSource = area_names;
            cmbAreas.DataSource = bndSource_areas.DataSource;
            //cmbAreas.DisplayMember = "Area";
            //cmbAreas.ValueMember = "Area";
        }

        private void btnDataByStateArea_Click(object sender, EventArgs e)
        {
            var selection =
                Ddb_Intro.ScanResults.Items.Where(dict => dict["state_abbreviation"].S == 
                                    cmbStates.SelectedValue.ToString() &&
                                    dict["area_name"].S == cmbAreas.SelectedValue.ToString());

            string json = JsonConvert.SerializeObject(selection);
            string jsonFormatted = JValue.Parse(json).ToString(Formatting.Indented);

            //foreach (Dictionary<string, AttributeValue> item in selection)
            //{
            //    // Process the result.
            //    PrintItem(item);
            //}
            txtOutput.Text = jsonFormatted;

            stsLabel.Text = $"Found {selection.ToList().Count} records";
        }

        private void btnSelectByState_Click(object sender, EventArgs e)
        {
            var selection =
                Ddb_Intro.ScanResults.Items.Where(dict => dict["state_abbreviation"].S == 
                cmbStates.SelectedValue.ToString());

            string json = JsonConvert.SerializeObject(selection);
            string jsonFormatted = JValue.Parse(json).ToString(Formatting.Indented);

            //foreach (Dictionary<string, AttributeValue> item in selection)
            //{
            //    // Process the result.
            //    PrintItem(item);
            //}
            txtOutput.Text = jsonFormatted;

            stsLabel.Text = $"Found {selection.ToList().Count} records";
        }

        private void btnSelectByStateQry_Click(object sender, EventArgs e)
        {
            var table_name = txtBoxTableName.Text;
            if (table_name == null)
            {
                throw new ArgumentNullException("table_name cannot be empty");
            }

            Ddb_Intro.createClient(true);
            QueryRequest qRequest = new QueryRequest
            {
                TableName = table_name,
                //ExpressionAttributeNames = new Dictionary<string, string>
                //    {
                //      { "#st", "area_name" },
                //      { "#fp", "fips" }
                //    },
                ExpressionAttributeValues = new Dictionary<string, AttributeValue>
                    {
                      // { "area_name",   new AttributeValue { S = cmbAreas.SelectedValue.ToString() } },
                      { ":fips",   new AttributeValue { N = "1001" } }
                    },
                KeyConditionExpression = "fips = :fips",
                ProjectionExpression = "fips"
            };
                
            if (AsyncHelper.RunSync<bool>(() => Ddb_Intro.QueryTable_async(qRequest)))
            {
                string json = JsonConvert.SerializeObject(Ddb_Intro.QueryResults.Items);
                string jsonFormatted = JValue.Parse(json).ToString(Formatting.Indented);
                txtOutput.Text = jsonFormatted;
            }

            //foreach (Dictionary<string, AttributeValue> item in selection)
            //{
            //    // Process the result.

            //    PrintItem(item);
            //}

            stsLabel.Text = Ddb_Intro.Message;

        }

        private void crossTab()
        {
            List<int[]> perc = new List<int[]>();
            perc.Add(new int[] { 0, 10 });
            perc.Add(new int[] { 11, 20 });
            perc.Add(new int[] { 21, 30 });
            perc.Add(new int[] { 31, 40 });
            perc.Add(new int[] { 41, 50 });
            perc.Add(new int[] { 51, 60 });
            perc.Add(new int[] { 61, 70 });
            perc.Add(new int[] { 71, 80 });
            perc.Add(new int[] { 81, 90 });
            perc.Add(new int[] { 91, 100 });
            
            var selection =
                Ddb_Intro.ScanResults.Items.Where(dict => Convert.ToDouble(dict["EDU685213"].N) <= 0 && Convert.ToDouble(dict["EDU685213"].N) >= 10).Count();
        }
    }
}
