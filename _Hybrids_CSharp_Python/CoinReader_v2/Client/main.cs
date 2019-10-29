using System;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading;
using System.Windows.Forms;
using AForge.Video;
using AForge.Video.DirectShow;
using Client.Classes;

namespace Client
{
    public partial class main : Form
    {
        FilterInfoCollection _videoDevices = 
            new FilterInfoCollection(FilterCategory.VideoInputDevice);
        VideoCaptureDevice _videoSource;

        bool isSaveModel = false;
        bool isSaveScene = false;
        private bool isStreamingVideo = false;
        string _currModelFile = "";
        string _currSceneFile = "";

        public main()
        {
            InitializeComponent();

            List<FilterInfo> _oDevList = _videoDevices.Cast<FilterInfo>().ToList();

            cmbImagingDevices.DisplayMember = "Name";
            cmbImagingDevices.ValueMember = "MonikerString";
            cmbImagingDevices.DataSource = _oDevList;

            tvMenu.ExpandAll();
            this.CenterToScreen();
        }

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

        private void video_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            #region "Save model" 
            if (isStreamingVideo)
            {
                if (isSaveModel)
                {
                    Bitmap current = (Bitmap)eventArgs.Frame.Clone();
                    string _path = getAppPath();
                    string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\"));
                    string fileName = System.IO.Path.Combine(_newPath + "main\\_img\\_models", DateTime.Now.ToString("yyyy-MM-dd_hh-mm-ss") + ".jpg");
                    current.Save(fileName);
                    current.Dispose();
                    isSaveModel = false;
                    _currModelFile = fileName;
                    //this.InvokeEx(f => f.isSaveImage = false);
                    MessageBox.Show("File \n" + fileName + "\n saved");
                }
            }
            #endregion

            #region " Save scene "
            if (isStreamingVideo)
            {
                if (isSaveScene)
                {
                    Bitmap current = (Bitmap)eventArgs.Frame.Clone();
                    string _path = getAppPath();
                    string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\"));
                    string fileName = System.IO.Path.Combine(_newPath + "main\\_img\\_scenes", DateTime.Now.ToString("yyyy-MM-dd_hh-mm-ss") + ".jpg");
                    current.Save(fileName);
                    current.Dispose();
                    isSaveScene = false;
                    _currSceneFile = fileName;
                    //this.InvokeEx(f => f.isSaveImage = false);
                    MessageBox.Show("File \n" + fileName + "\n saved");
                }
            }
            #endregion

            var _image = (Bitmap)eventArgs.Frame.Clone();
            // process the frame
            pctBoxCapture.Image = _image;
            this.InvokeEx(f => f.pctBoxCapture.Visible = true);
        }

        private void btnStartCapture_Click(object sender, EventArgs e)
        {
            isStreamingVideo = true;

            // set NewFrame event handler
            _videoSource.NewFrame += new NewFrameEventHandler(video_NewFrame);

            // start the video source
            _videoSource.Start();
        }

        private void cmbImagingDevices_SelectedIndexChanged(object sender, EventArgs e)
        {
            var _cb = (ComboBox)sender;
            // create video source
            _videoSource = new VideoCaptureDevice(_videoDevices[_cb.SelectedIndex].MonikerString);
        }

        private void btnEndCapture_Click(object sender, EventArgs e)
        {
            isStreamingVideo = false;
            pctBoxCapture.Visible = false;
            // signal to stop when you no longer need capturing
            _videoSource.SignalToStop();
            this.Refresh();
        }

        private void main_FormClosed(object sender, FormClosedEventArgs e)
        {
            //btnEndCapture_Click(null, null);
            //var retVal =  
            //    MessageBox.Show("Save changes?", "Coin Reader", MessageBoxButtons.YesNoCancel);
            //if (retVal == DialogResult.Yes || retVal == DialogResult.No)
            //{
            //    Application.Exit();
            //}
            //else if (retVal == DialogResult.Cancel)
            //{
            //    //e.Cancel = true;
            //}
        }

        private void btnSaveScene_Click(object sender, EventArgs e)
        {
            if (isStreamingVideo)
            {
                isSaveScene = true;
            }
        }

        private void btnSaveModel_Click(object sender, EventArgs e)
        {
            if (isStreamingVideo)
            {
                isSaveModel = true;
            }
        }

        private void btnViewModels_Click(object sender, EventArgs e)
        {
            // Displays an OpenFileDialog so the user can select a Cursor.  
            var _ofd = new OpenFileDialog();
            _ofd.Filter = "Images (*.BMP;*.JPG;*.GIF; *.PNG)|*.BMP;*.JPG;*.GIF;*.PNG|" +
                            "All files (*.*)|*.*";
            _ofd.Title = "Models Browser";
            _ofd.Multiselect = true;

            string _path = getAppPath();
            string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\"));

            _ofd.InitialDirectory = _newPath + "main\\_img\\_models";
            if (!Directory.Exists(_ofd.InitialDirectory))
            {
                //Directory.CreateDirectory(_ofd.InitialDirectory);
                throw new Exception("Folder does not exist \n" + _ofd.InitialDirectory);
            }
 
            if (_ofd.ShowDialog() == DialogResult.OK)
            {
                _currModelFile = _ofd.FileName;
                stsLabelModel.Text = "Using model: " + _ofd.SafeFileName;
                //Process.Start(_ofd.FileName);
            }
        }

        private void btnViewScenes_Click(object sender, EventArgs e)
        {
            // Displays an OpenFileDialog so the user can select a Cursor.  
            var _ofd = new OpenFileDialog();
            _ofd.Filter = "Images (*.BMP;*.JPG;*.GIF; *.PNG)|*.BMP;*.JPG;*.GIF;*.PNG|" +
                            "All files (*.*)|*.*";
            _ofd.Title = "Scenes Browser";
            _ofd.Multiselect = true;

            string _path = getAppPath();
            string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\"));

            _ofd.InitialDirectory = _newPath + "main\\_img\\_scenes";
            if (!Directory.Exists(_ofd.InitialDirectory))
            {
                // Directory.CreateDirectory(_ofd.InitialDirectory);
                throw new Exception("Folder does not exist \n" + _ofd.InitialDirectory);
            }

            if (_ofd.ShowDialog() == DialogResult.OK)
            {
                _currSceneFile = _ofd.FileName;
                stsLabelScene.Text = "Using scene: " + _ofd.SafeFileName;
                //Process.Start(_ofd.FileName);
            }
        }

        private void addModelToDB()
        {
            string _path = getAppPath();
            string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\main"));
            Directory.SetCurrentDirectory(_newPath);

            var _currFile = Path.GetFileName(_currModelFile);
            if (_currFile.Trim() == "")
                return;

            string strCmdText;
            strCmdText = String.Format("--filename {0} --imagetype _models ", _currFile);
            run_python_cmd("sift_build_single_descriptor.py", strCmdText, true, false);
        }

        private void addSceneToDB()
        {
            string _path = getAppPath();
            string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\main"));
            Directory.SetCurrentDirectory(_newPath);

            var _currFile = Path.GetFileName(_currSceneFile);
            if (_currFile.Trim() == "")
                return;

            string strCmdText;
            strCmdText = String.Format(" --filename {0} --imagetype _scenes ", _currFile);
            run_python_cmd("sift_build_single_descriptor.py", strCmdText, true, false);
        }
         
        private void siftDetectImage()
        {
            string _path = getAppPath();
            string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\main"));
            Directory.SetCurrentDirectory(_newPath);

            var _currFile = Path.GetFileName(_currSceneFile);
            if (_currFile.Trim() == "")
                return;

            string strCmdText;
            strCmdText = String.Format(" --filename {0} ", _currFile);
            run_python_cmd("perform_sift_matching.py", strCmdText);
        }

        private void siftRebuildDescriptors()
        {
            string _path = getAppPath();
            string _newPath = Path.GetFullPath(Path.Combine(_path, @"..\main"));
            Directory.SetCurrentDirectory(_newPath);

            var strCmdText = "";
            run_python_cmd("build_all_descriptors_main.py", strCmdText, true, false);
        }

        private void run_python_cmd(string cmd, string args="", bool _UseShellExecute=false, bool _RedirectStandardOutput=true)
        {
            try
            {
                var hostName = System.Environment.MachineName;

                ProcessStartInfo start = new ProcessStartInfo();
                if (hostName == "RGEK-LAPTOP-01")
                {
                    string pyExe = System.Configuration.ConfigurationSettings.AppSettings.Get("PythonExe");
                    start.FileName = pyExe;
                }
                else if (hostName == "RGEK-LAPTOP-02")
                {
                    start.FileName =
                        @"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python.exe";
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
                            MessageBox.Show(result, "Informaation ...");
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }


        }

        public void TvMenu_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                // Select the clicked node
                tvMenu.SelectedNode = tvMenu.GetNodeAt(e.X, e.Y);

                if (tvMenu.SelectedNode != null)
                {
                    if (tvMenu.SelectedNode.Name == "StartVideo")
                    {
                        btnStartCapture_Click(null, null);
                    }
                    else if (tvMenu.SelectedNode.Name == "EndVideo")
                    {
                        btnEndCapture_Click(null, null);
                    }
                    else if (tvMenu.SelectedNode.Name == "SaveScene")
                    {
                        btnSaveScene_Click(null, null);
                    }
                    else if (tvMenu.SelectedNode.Name == "SaveModel")
                    {
                        btnSaveModel_Click(null, null);
                    }
                    else if (tvMenu.SelectedNode.Name == "ViewModels")
                    {
                        btnViewModels_Click(null, null);
                    }
                    else if (tvMenu.SelectedNode.Name == "ViewScenes")
                    {
                        btnViewScenes_Click(null, null);
                    }
                    else if (tvMenu.SelectedNode.Name == "addModelToDB")
                    {
                        addModelToDB();
                    }
                    else if (tvMenu.SelectedNode.Name == "addSceneToDB")
                    {
                        addSceneToDB();
                    }
                    else if (tvMenu.SelectedNode.Name == "siftDetectImage")
                    {
                        //MessageBox.Show("Launch a python process that will check for image in the image database.");

                        if (_currSceneFile.Length > 0)
                        {
                            // new CDetect2DObjects().detect2DFeatures(_currModelFile, _currSceneFile);
                            siftDetectImage();
                            //Process.Start()
                        }
                    }
                    else if (tvMenu.SelectedNode.Name == "siftRebuildDescriptors")
                    {
                        siftRebuildDescriptors();
                    }

                    
                }
            }

        }
    }
}
