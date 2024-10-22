# **********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************
import os
from pathlib import Path

class PackageManager(object):

    def __init__(self, name='PackageManager',description='Build-in package manager',verbose=False):
        """Initialize a Package Manager component.

                Parameters
                ----------
                name : string
                    name of the property components

                description : string
                    description of the property components

                verbose : bool
                    component verbose execution

        See Also
        --------
        ..

        Examples
        --------
        >> pm = PackageManager(name="PM1",description="Default package manager",verbose=False)

        """

        self._name = name
        self._description = description
        self._verbose = verbose

        #package info
        self._packageName = "rpio_pkg"
        self.standalonePath = ""
        # get current directory
        self._directory = os.getcwd()


    @property
    def name(self):
        """The name property (read-only)."""
        return self._name

    @property
    def description(self):
        """The description property (read-only)."""
        return self._description

    def create(self,name,force=False,standalone=False,path=None):
        """Create rpIO package.

                Parameters
                ----------
                name : string
                    name of the rpIO package

                force : bool
                    force the creation of a rpIO package

                standalone : bool
                    create rpIO package in standalone mode, not in current directory

                path : string
                    path where the new hybridIO package needs to be generated

                See Also
                --------
                ..

                Examples
                --------
                >> pm.create(force=False,standalone=True)

                """
        isEmpty=self._checkEmptyDir()

        if not standalone:
            if isEmpty or (not isEmpty and force):
                if self._verbose:print("DEBUG: directory is empty, creating "+self._packageName+" package...")
                # --- rpio package creation ---
                try:
                    self._populatePackage(name=name, standalone=standalone)
                except:
                    raise Exception("ERROR: "+self._packageName+" package could not be created!")

                if self._verbose: print("DEBUG: "+self._packageName+" package created...")
            else:
                if self._verbose: print("DEBUG: directory is not empty, no "+self._packageName+" package created!")
        else:
            if path is not None:
                self.standalonePath = path
                try:
                    self._populatePackage(name=name, standalone=standalone)
                except:
                    raise Exception("ERROR: "+self._packageName+" package could not be created!")

                if self._verbose: print("DEBUG: " + self._packageName + " package created...")
            else:
                if self._verbose: print("DEBUG: directory is not provided for standalone creation, no " + self._packageName + " package created!")

    def check(self,path=None):
        """Check rpIO package.

            Parameters
            ----------
            path : string
                path to the standalone hybridIO package


            See Also
            --------
            ..

            Examples
            --------
            >> isHybridIOPackage = pm.check(path="path/to/rpio/package")

        """
        validPackage = True
        if path is None:
            if self._verbose: print("DEBUG: checking "+self._packageName+" package...")
            validPackage = os.path.isfile("robosapiensIO.ini")
            #TODO: add other checks
        else:
            if self._verbose: print("DEBUG: checking "+self._packageName+" package in "+self._directory+"/"+path+"...")
            validPackage = os.path.isfile(path+"/robosapiensIO.ini")
            # TODO: add other checks

        return validPackage

    def _checkEmptyDir(self):
        """Function to determine if directory is empty."""
        if self._verbose: print("DEBUG: Checking if directory is empty...")
        dir = os.listdir(self._directory)
        return len(dir) == 0

    def _populatePackage(self, name="rpio_pkg", standalone=False):
        """Function to populate the empty package."""
        self._packageName = name
        if standalone:
            # generate in standalone package instead of in current directory
            Path(self.standalonePath+"/"+self._packageName).mkdir(parents=True, exist_ok=True)
            prefix = self.standalonePath+"/"+self._packageName+'/'
            self._addFile(file="robosapiensIO.ini",name=self._packageName, path=self._directory + "/" + prefix)
            logfilepath = self._directory + "/" + prefix+"/Resources"
        else:
            prefix=""
            self._addFile(file="robosapiensIO.ini",name=self._packageName)
            logfilepath = self._directory + "/Resources"

        self._mkdir_custom(prefix + "00_Documentation")
        self._mkdir_custom(prefix + "01_Concept")
        self._mkdir_custom(prefix + "02_Design")
        self._mkdir_custom(prefix + "02_Realization")
        #managing system
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/00_Documentation")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/01_Binaries")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/02_Nodes/00_Monitor")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/02_Nodes/01_Analysis")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/02_Nodes/02_Plan")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/02_Nodes/03_Legitimize")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/02_Nodes/04_Execute")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/02_Nodes/05_AdaptationOrchestration")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/03_Messages")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/04_Platform")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/05_Actions")
        self._mkdir_custom(prefix + "02_Realization/00_ManagingSystem/06_Workflows")
        #managed system
        self._mkdir_custom(prefix + "02_Realization/01_ManagedSystem/00_Documentation")
        self._mkdir_custom(prefix + "02_Realization/01_ManagedSystem/01_Binaries")
        self._mkdir_custom(prefix + "02_Realization/01_ManagedSystem/02_Nodes/01_Probes")
        self._mkdir_custom(prefix + "02_Realization/01_ManagedSystem/02_Nodes/02_Effector")
        self._mkdir_custom(prefix + "02_Realization/01_ManagedSystem/03_Messages")
        self._mkdir_custom(prefix + "02_Realization/01_ManagedSystem/04_Platform")
        self._mkdir_custom(prefix + "02_Realization/01_ManagedSystem/05_Actions")
        self._mkdir_custom(prefix + "02_Realization/01_ManagedSystem/06_Workflows")
        self._mkdir_custom(prefix + "Resources")

        # add system log file
        self._addFile(file="sys.log", path=logfilepath)

    def _mkdir_custom(self, folder="empty", file='readme.md'):
        """CUSTOM mkdir function to initialize git-pushable directories"""
        #create directory
        Path(folder).mkdir(parents=True, exist_ok=True)
        #add file
        self._addFile(file=file, path=folder)

    def _addFile(self, file="requirements.txt",name="",description="", path=None):
        """Function to add a file to the provided path."""

        if path==None:
            path = self._directory

        # --- open file ---
        f = open(path + "/" + file, "a")

        # --- custom file content ---


        if "readme" in file:
            f.write("Placeholder")

        if "sys.log" in file:
            f.write("---------------------- RoboSAPIENS Adaptive Platform system logs ----------------------\n")

        if "robosapiensIO.ini" in file:
            f.write("[RoboSAPIENSIO]\n")
            f.write('name = '+name+'\n')
            f.write('description = " Add project description"\n')




        # --- close file ---
        f.close()

