namespace _2T
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
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.stsLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.txtBoxTableName = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.databaseToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.testLocalDBConnectionToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.checkIfTableExistsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.createTableToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.describeTableToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.deleteTableToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.dataToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.loadDataToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.scanTableToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cmbStates = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.cmbAreas = new System.Windows.Forms.ComboBox();
            this.btnSelectArea = new System.Windows.Forms.Button();
            this.btnSelectByState = new System.Windows.Forms.Button();
            this.btnDataByStateArea = new System.Windows.Forms.Button();
            this.txtOutput = new System.Windows.Forms.TextBox();
            this.btnSelectByStateQry = new System.Windows.Forms.Button();
            this.statusStrip1.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // statusStrip1
            // 
            this.statusStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.stsLabel});
            this.statusStrip1.Location = new System.Drawing.Point(0, 548);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(701, 22);
            this.statusStrip1.TabIndex = 2;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // stsLabel
            // 
            this.stsLabel.Name = "stsLabel";
            this.stsLabel.Size = new System.Drawing.Size(0, 17);
            // 
            // txtBoxTableName
            // 
            this.txtBoxTableName.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtBoxTableName.Location = new System.Drawing.Point(137, 43);
            this.txtBoxTableName.Name = "txtBoxTableName";
            this.txtBoxTableName.Size = new System.Drawing.Size(191, 30);
            this.txtBoxTableName.TabIndex = 4;
            this.txtBoxTableName.Text = "counts";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 43);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(119, 25);
            this.label1.TabIndex = 5;
            this.label1.Text = "Table Name";
            // 
            // menuStrip1
            // 
            this.menuStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.databaseToolStripMenuItem,
            this.toolStripMenuItem1,
            this.dataToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(701, 28);
            this.menuStrip1.TabIndex = 6;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // databaseToolStripMenuItem
            // 
            this.databaseToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.testLocalDBConnectionToolStripMenuItem});
            this.databaseToolStripMenuItem.Name = "databaseToolStripMenuItem";
            this.databaseToolStripMenuItem.Size = new System.Drawing.Size(84, 24);
            this.databaseToolStripMenuItem.Text = "Database";
            // 
            // testLocalDBConnectionToolStripMenuItem
            // 
            this.testLocalDBConnectionToolStripMenuItem.Name = "testLocalDBConnectionToolStripMenuItem";
            this.testLocalDBConnectionToolStripMenuItem.Size = new System.Drawing.Size(247, 26);
            this.testLocalDBConnectionToolStripMenuItem.Text = "Test local DB connection";
            this.testLocalDBConnectionToolStripMenuItem.Click += new System.EventHandler(this.testLocalDBConnectionToolStripMenuItem_Click);
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.checkIfTableExistsToolStripMenuItem,
            this.createTableToolStripMenuItem,
            this.describeTableToolStripMenuItem,
            this.toolStripSeparator1,
            this.deleteTableToolStripMenuItem});
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(56, 24);
            this.toolStripMenuItem1.Text = "Table";
            // 
            // checkIfTableExistsToolStripMenuItem
            // 
            this.checkIfTableExistsToolStripMenuItem.Name = "checkIfTableExistsToolStripMenuItem";
            this.checkIfTableExistsToolStripMenuItem.Size = new System.Drawing.Size(215, 26);
            this.checkIfTableExistsToolStripMenuItem.Text = "Check if Table Exists";
            this.checkIfTableExistsToolStripMenuItem.Click += new System.EventHandler(this.checkIfTableExistsToolStripMenuItem_Click);
            // 
            // createTableToolStripMenuItem
            // 
            this.createTableToolStripMenuItem.Name = "createTableToolStripMenuItem";
            this.createTableToolStripMenuItem.Size = new System.Drawing.Size(215, 26);
            this.createTableToolStripMenuItem.Text = "Create Table";
            this.createTableToolStripMenuItem.Click += new System.EventHandler(this.createTableToolStripMenuItem_Click);
            // 
            // describeTableToolStripMenuItem
            // 
            this.describeTableToolStripMenuItem.Name = "describeTableToolStripMenuItem";
            this.describeTableToolStripMenuItem.Size = new System.Drawing.Size(215, 26);
            this.describeTableToolStripMenuItem.Text = "Describe Table";
            this.describeTableToolStripMenuItem.Click += new System.EventHandler(this.describeTableToolStripMenuItem_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(212, 6);
            // 
            // deleteTableToolStripMenuItem
            // 
            this.deleteTableToolStripMenuItem.Name = "deleteTableToolStripMenuItem";
            this.deleteTableToolStripMenuItem.Size = new System.Drawing.Size(215, 26);
            this.deleteTableToolStripMenuItem.Text = "Delete Table";
            this.deleteTableToolStripMenuItem.Click += new System.EventHandler(this.deleteTableToolStripMenuItem_Click);
            // 
            // dataToolStripMenuItem
            // 
            this.dataToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.loadDataToolStripMenuItem,
            this.scanTableToolStripMenuItem});
            this.dataToolStripMenuItem.Name = "dataToolStripMenuItem";
            this.dataToolStripMenuItem.Size = new System.Drawing.Size(53, 24);
            this.dataToolStripMenuItem.Text = "Data";
            // 
            // loadDataToolStripMenuItem
            // 
            this.loadDataToolStripMenuItem.Name = "loadDataToolStripMenuItem";
            this.loadDataToolStripMenuItem.Size = new System.Drawing.Size(154, 26);
            this.loadDataToolStripMenuItem.Text = "Load Data";
            this.loadDataToolStripMenuItem.Click += new System.EventHandler(this.loadDataToolStripMenuItem_Click);
            // 
            // scanTableToolStripMenuItem
            // 
            this.scanTableToolStripMenuItem.Name = "scanTableToolStripMenuItem";
            this.scanTableToolStripMenuItem.Size = new System.Drawing.Size(154, 26);
            this.scanTableToolStripMenuItem.Text = "Scan Table";
            this.scanTableToolStripMenuItem.Click += new System.EventHandler(this.scanTableToolStripMenuItem_Click);
            // 
            // cmbStates
            // 
            this.cmbStates.FormattingEnabled = true;
            this.cmbStates.Location = new System.Drawing.Point(17, 137);
            this.cmbStates.Name = "cmbStates";
            this.cmbStates.Size = new System.Drawing.Size(152, 24);
            this.cmbStates.TabIndex = 7;
            this.cmbStates.SelectedIndexChanged += new System.EventHandler(this.cmbStates_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(12, 109);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(68, 25);
            this.label2.TabIndex = 8;
            this.label2.Text = "States";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(390, 109);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(64, 25);
            this.label3.TabIndex = 10;
            this.label3.Text = "Areas";
            // 
            // cmbAreas
            // 
            this.cmbAreas.FormattingEnabled = true;
            this.cmbAreas.Location = new System.Drawing.Point(395, 137);
            this.cmbAreas.Name = "cmbAreas";
            this.cmbAreas.Size = new System.Drawing.Size(285, 24);
            this.cmbAreas.TabIndex = 9;
            // 
            // btnSelectArea
            // 
            this.btnSelectArea.Location = new System.Drawing.Point(204, 131);
            this.btnSelectArea.Name = "btnSelectArea";
            this.btnSelectArea.Size = new System.Drawing.Size(152, 30);
            this.btnSelectArea.TabIndex = 11;
            this.btnSelectArea.Text = "Select Area =>";
            this.btnSelectArea.UseVisualStyleBackColor = true;
            this.btnSelectArea.Click += new System.EventHandler(this.btnSelectArea_Click);
            // 
            // btnSelectByState
            // 
            this.btnSelectByState.Location = new System.Drawing.Point(17, 177);
            this.btnSelectByState.Name = "btnSelectByState";
            this.btnSelectByState.Size = new System.Drawing.Size(229, 30);
            this.btnSelectByState.TabIndex = 12;
            this.btnSelectByState.Text = "Select Data by State Linq";
            this.btnSelectByState.UseVisualStyleBackColor = true;
            this.btnSelectByState.Click += new System.EventHandler(this.btnSelectByState_Click);
            // 
            // btnDataByStateArea
            // 
            this.btnDataByStateArea.Location = new System.Drawing.Point(395, 177);
            this.btnDataByStateArea.Name = "btnDataByStateArea";
            this.btnDataByStateArea.Size = new System.Drawing.Size(285, 30);
            this.btnDataByStateArea.TabIndex = 13;
            this.btnDataByStateArea.Text = "Select Data by State and Area Linq";
            this.btnDataByStateArea.UseVisualStyleBackColor = true;
            this.btnDataByStateArea.Click += new System.EventHandler(this.btnDataByStateArea_Click);
            // 
            // txtOutput
            // 
            this.txtOutput.Location = new System.Drawing.Point(17, 261);
            this.txtOutput.Multiline = true;
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtOutput.Size = new System.Drawing.Size(663, 270);
            this.txtOutput.TabIndex = 14;
            // 
            // btnSelectByStateQry
            // 
            this.btnSelectByStateQry.Location = new System.Drawing.Point(17, 210);
            this.btnSelectByStateQry.Name = "btnSelectByStateQry";
            this.btnSelectByStateQry.Size = new System.Drawing.Size(229, 30);
            this.btnSelectByStateQry.TabIndex = 15;
            this.btnSelectByStateQry.Text = "Select Data by State Query";
            this.btnSelectByStateQry.UseVisualStyleBackColor = true;
            this.btnSelectByStateQry.Click += new System.EventHandler(this.btnSelectByStateQry_Click);
            // 
            // main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(701, 570);
            this.Controls.Add(this.btnSelectByStateQry);
            this.Controls.Add(this.txtOutput);
            this.Controls.Add(this.btnDataByStateArea);
            this.Controls.Add(this.btnSelectByState);
            this.Controls.Add(this.btnSelectArea);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.cmbAreas);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.cmbStates);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtBoxTableName);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "main";
            this.Text = "2T";
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel stsLabel;
        private System.Windows.Forms.TextBox txtBoxTableName;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem checkIfTableExistsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem databaseToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem testLocalDBConnectionToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem deleteTableToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem describeTableToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem createTableToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripMenuItem dataToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem loadDataToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem scanTableToolStripMenuItem;
        private System.Windows.Forms.ComboBox cmbStates;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox cmbAreas;
        private System.Windows.Forms.Button btnSelectArea;
        private System.Windows.Forms.Button btnSelectByState;
        private System.Windows.Forms.Button btnDataByStateArea;
        private System.Windows.Forms.TextBox txtOutput;
        private System.Windows.Forms.Button btnSelectByStateQry;
    }
}

