namespace Client
{
    partial class main
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(main));
            System.Windows.Forms.TreeNode treeNode1 = new System.Windows.Forms.TreeNode("Start");
            System.Windows.Forms.TreeNode treeNode2 = new System.Windows.Forms.TreeNode("End");
            System.Windows.Forms.TreeNode treeNode3 = new System.Windows.Forms.TreeNode("Video", new System.Windows.Forms.TreeNode[] {
            treeNode1,
            treeNode2});
            System.Windows.Forms.TreeNode treeNode4 = new System.Windows.Forms.TreeNode("Save");
            System.Windows.Forms.TreeNode treeNode5 = new System.Windows.Forms.TreeNode("View");
            System.Windows.Forms.TreeNode treeNode6 = new System.Windows.Forms.TreeNode("Add To DB");
            System.Windows.Forms.TreeNode treeNode7 = new System.Windows.Forms.TreeNode("Models", new System.Windows.Forms.TreeNode[] {
            treeNode4,
            treeNode5,
            treeNode6});
            System.Windows.Forms.TreeNode treeNode8 = new System.Windows.Forms.TreeNode("Save");
            System.Windows.Forms.TreeNode treeNode9 = new System.Windows.Forms.TreeNode("View");
            System.Windows.Forms.TreeNode treeNode10 = new System.Windows.Forms.TreeNode("Add To DB");
            System.Windows.Forms.TreeNode treeNode11 = new System.Windows.Forms.TreeNode("Scenes", new System.Windows.Forms.TreeNode[] {
            treeNode8,
            treeNode9,
            treeNode10});
            System.Windows.Forms.TreeNode treeNode12 = new System.Windows.Forms.TreeNode("Images", new System.Windows.Forms.TreeNode[] {
            treeNode7,
            treeNode11});
            System.Windows.Forms.TreeNode treeNode13 = new System.Windows.Forms.TreeNode("Rebuild Descriptors");
            System.Windows.Forms.TreeNode treeNode14 = new System.Windows.Forms.TreeNode("Detect Image");
            System.Windows.Forms.TreeNode treeNode15 = new System.Windows.Forms.TreeNode("SIFT", new System.Windows.Forms.TreeNode[] {
            treeNode13,
            treeNode14});
            System.Windows.Forms.TreeNode treeNode16 = new System.Windows.Forms.TreeNode("SURF");
            System.Windows.Forms.TreeNode treeNode17 = new System.Windows.Forms.TreeNode("Methods", new System.Windows.Forms.TreeNode[] {
            treeNode15,
            treeNode16});
            System.Windows.Forms.TreeNode treeNode18 = new System.Windows.Forms.TreeNode("Menu", new System.Windows.Forms.TreeNode[] {
            treeNode3,
            treeNode12,
            treeNode17});
            this.label1 = new System.Windows.Forms.Label();
            this.cmbImagingDevices = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.pctBoxCapture = new System.Windows.Forms.PictureBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.tvMenu = new System.Windows.Forms.TreeView();
            this.stsStrip = new System.Windows.Forms.StatusStrip();
            this.stsLabelModel = new System.Windows.Forms.ToolStripStatusLabel();
            this.stsLabelScene = new System.Windows.Forms.ToolStripStatusLabel();
            ((System.ComponentModel.ISupportInitialize)(this.pctBoxCapture)).BeginInit();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            this.stsStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(21, 24);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(0, 17);
            this.label1.TabIndex = 0;
            // 
            // cmbImagingDevices
            // 
            this.cmbImagingDevices.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.125F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.cmbImagingDevices.FormattingEnabled = true;
            this.cmbImagingDevices.Location = new System.Drawing.Point(7, 36);
            this.cmbImagingDevices.Margin = new System.Windows.Forms.Padding(2);
            this.cmbImagingDevices.Name = "cmbImagingDevices";
            this.cmbImagingDevices.Size = new System.Drawing.Size(722, 28);
            this.cmbImagingDevices.TabIndex = 1;
            this.cmbImagingDevices.SelectedIndexChanged += new System.EventHandler(this.cmbImagingDevices_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.125F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.Location = new System.Drawing.Point(2, 9);
            this.label2.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(154, 20);
            this.label2.TabIndex = 2;
            this.label2.Text = "Select Input Device";
            // 
            // pctBoxCapture
            // 
            this.pctBoxCapture.InitialImage = ((System.Drawing.Image)(resources.GetObject("pctBoxCapture.InitialImage")));
            this.pctBoxCapture.Location = new System.Drawing.Point(7, 70);
            this.pctBoxCapture.Name = "pctBoxCapture";
            this.pctBoxCapture.Size = new System.Drawing.Size(722, 584);
            this.pctBoxCapture.TabIndex = 5;
            this.pctBoxCapture.TabStop = false;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.splitContainer1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(1044, 787);
            this.panel1.TabIndex = 7;
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.tvMenu);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.stsStrip);
            this.splitContainer1.Panel2.Controls.Add(this.label2);
            this.splitContainer1.Panel2.Controls.Add(this.cmbImagingDevices);
            this.splitContainer1.Panel2.Controls.Add(this.pctBoxCapture);
            this.splitContainer1.Panel2.Cursor = System.Windows.Forms.Cursors.Default;
            this.splitContainer1.Size = new System.Drawing.Size(1044, 787);
            this.splitContainer1.SplitterDistance = 212;
            this.splitContainer1.TabIndex = 7;
            // 
            // tvMenu
            // 
            this.tvMenu.Cursor = System.Windows.Forms.Cursors.Default;
            this.tvMenu.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tvMenu.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.tvMenu.Location = new System.Drawing.Point(0, 0);
            this.tvMenu.Margin = new System.Windows.Forms.Padding(2);
            this.tvMenu.Name = "tvMenu";
            this.tvMenu.MouseUp += TvMenu_MouseUp;
            treeNode1.Name = "StartVideo";
            treeNode1.Text = "Start";
            treeNode2.Name = "EndVideo";
            treeNode2.Text = "End";
            treeNode3.Name = "Video";
            treeNode3.Text = "Video";
            treeNode4.Name = "SaveModel";
            treeNode4.Text = "Save";
            treeNode5.Name = "ViewModels";
            treeNode5.Text = "View";
            treeNode6.Name = "addModelToDB";
            treeNode6.Text = "Add To DB";
            treeNode7.Name = "Models";
            treeNode7.Text = "Models";
            treeNode8.Name = "SaveScene";
            treeNode8.Text = "Save";
            treeNode9.Name = "ViewScenes";
            treeNode9.Text = "View";
            treeNode10.Name = "addSceneToDB";
            treeNode10.Text = "Add To DB";
            treeNode11.Name = "Scenes";
            treeNode11.Text = "Scenes";
            treeNode12.Name = "Images";
            treeNode12.Text = "Images";
            treeNode13.Name = "siftRebuildDescriptors";
            treeNode13.Text = "Rebuild Descriptors";
            treeNode14.Name = "siftDetectImage";
            treeNode14.Text = "Detect Image";
            treeNode15.Name = "methodSIFT";
            treeNode15.Text = "SIFT";
            treeNode16.Name = "SURF";
            treeNode16.Text = "SURF";
            treeNode17.Name = "Node0";
            treeNode17.Text = "Methods";
            treeNode18.Name = "Menu";
            treeNode18.Text = "Menu";
            this.tvMenu.Nodes.AddRange(new System.Windows.Forms.TreeNode[] {
            treeNode18});
            this.tvMenu.Size = new System.Drawing.Size(212, 787);
            this.tvMenu.TabIndex = 0;
            // 
            // stsStrip
            // 
            this.stsStrip.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.stsStrip.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.stsStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.stsLabelModel,
            this.stsLabelScene});
            this.stsStrip.Location = new System.Drawing.Point(0, 765);
            this.stsStrip.Name = "stsStrip";
            this.stsStrip.Size = new System.Drawing.Size(828, 22);
            this.stsStrip.TabIndex = 6;
            this.stsStrip.Text = "Hello !";
            // 
            // stsLabelModel
            // 
            this.stsLabelModel.Name = "stsLabelModel";
            this.stsLabelModel.Size = new System.Drawing.Size(0, 17);
            // 
            // stsLabelScene
            // 
            this.stsLabelScene.Name = "stsLabelScene";
            this.stsLabelScene.Size = new System.Drawing.Size(0, 17);
            // 
            // main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1044, 787);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.label1);
            this.Cursor = System.Windows.Forms.Cursors.No;
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "main";
            this.Text = "Computer Vision";
            ((System.ComponentModel.ISupportInitialize)(this.pctBoxCapture)).EndInit();
            this.panel1.ResumeLayout(false);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            this.splitContainer1.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            this.stsStrip.ResumeLayout(false);
            this.stsStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        private void TvMenu_MouseUp3(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            throw new System.NotImplementedException();
        }

        private void TvMenu_MouseUp2(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            throw new System.NotImplementedException();
        }

        private void TvMenu_MouseUp1(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            throw new System.NotImplementedException();
        }


        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox cmbImagingDevices;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.PictureBox pctBoxCapture;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.SplitContainer splitContainer1;
        public System.Windows.Forms.TreeView tvMenu;
        private System.Windows.Forms.StatusStrip stsStrip;
        private System.Windows.Forms.ToolStripStatusLabel stsLabelModel;
        private System.Windows.Forms.ToolStripStatusLabel stsLabelScene;
    }
}

