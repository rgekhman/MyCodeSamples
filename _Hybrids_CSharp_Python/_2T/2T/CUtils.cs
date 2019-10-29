using Amazon.DynamoDBv2.Model;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;
using System.Windows.Forms;

namespace _2T
{
    public partial class main
    {
        public static StringBuilder sbOutput = new StringBuilder("");

        private string getAppPath()
        {
            string _path = Path.GetDirectoryName(
                    System.Reflection.Assembly.GetExecutingAssembly().CodeBase);
            _path = _path.Replace("file:\\", "");
            int index = _path.IndexOf("\\bin");
            if (index > 0)
                _path = _path.Substring(0, index);

            return _path;
        }

        private void run_python_cmd(string cmd, string args = "", bool _UseShellExecute = false, bool _RedirectStandardOutput = true)
        {
            try
            {
                var hostName = System.Environment.MachineName;

                string pyExe;
                ProcessStartInfo start = new ProcessStartInfo();
                if (hostName == "RGEK-LAPTOP-01")
                {
                    pyExe = System.Configuration.ConfigurationManager.AppSettings.Get("PythonExe_01");
                    start.FileName = pyExe;
                }
                else if (hostName == "RGEK-LAPTOP-02")
                {
                    pyExe = System.Configuration.ConfigurationManager.AppSettings.Get("PythonExe_02");
                    start.FileName = pyExe;
                }
                else
                    return;

                start.Arguments = string.Format("{0} {1}", cmd, args);
                start.UseShellExecute = _UseShellExecute;
                start.RedirectStandardOutput = _RedirectStandardOutput;
                using (Process process = Process.Start(start))
                {
                    if (_RedirectStandardOutput)
                    {
                        using (StreamReader reader = process.StandardOutput)
                        {
                            string result = reader.ReadToEnd();
                            MessageBox.Show(result, "Information ...");
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private static void PrintItem(
                    Dictionary<string, AttributeValue> attributeList)
        {
            sbOutput.Clear();

            foreach (KeyValuePair<string, AttributeValue> kvp in attributeList)
            {
                string attributeName = kvp.Key;
                AttributeValue value = kvp.Value;

                sbOutput.Append
                    (
                    attributeName + " " +
                    (value.S == null ? "" : value.S) +
                    (value.N == null ? "" : value.N) + "\n"
                    //(value.SS == null ? "" : "SS=[" + string.Join(",", value.SS.ToArray()) + "]") +
                    //(value.NS == null ? "" : "NS=[" + string.Join(",", value.NS.ToArray()) + "]")
                    );
            }
            sbOutput.Append("************************************************");
        }

    }
}
