import os
import shutil
import site
from Utilities.common_utilities import CommonUtilsClass
from AllNavigations.common_bo import CommonBOClass
from AllFolders_location import reportsFolder, cmtSFTPErrorFolder, cmtInputToAPICalls, cmtDataFromAPICalls, cmtEncryptedFilesFolder
import commonVariables
comm = CommonUtilsClass()
commbo = CommonBOClass()

class ExecutionTearDown(object):

    def remove_test_files(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        rd_with_forwardslash = '/'.join(ROOT_DIR.split('\\'))
        comm.write_data_into_file(site.getsitepackages()[1] + r"\CMTModules.pth", rd_with_forwardslash)
        commbo.delete_selected_files_from_filepath()


    def remove_test_reports(self):
        '''
        for deleting all the files created while test execution
        :return:
        '''
        for the_file in os.listdir(reportsFolder):
            file_path = os.path.join(reportsFolder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(file_path)
            except Exception as e:
                print(e)


    def set_masterkey(self):
       commonVariables.master_key = str(input("Please give master key for the framework"))

    def createreadme(self):
        '''
        Creating the readme.txt files
        :return:
        '''
        comm.write_data_into_file(reportsFolder + "ReadMe.txt", "This Folder will hold reports of the framework")
        comm.write_data_into_file(cmtSFTPErrorFolder + "ReadMe.txt", "This Folder will hold SFTP error reports")
        comm.write_data_into_file(cmtInputToAPICalls + "ReadMe.txt", "This Folder will API JSON input calls")
        comm.write_data_into_file(cmtDataFromAPICalls + "ReadMe.txt", "This Folder will API JSON Output")
        comm.write_data_into_file(cmtEncryptedFilesFolder + "ReadMe.txt", "This Folder will hold the csv Encrypted file")

ExecutionTearDown = ExecutionTearDown()
ExecutionTearDown.remove_test_reports()
ExecutionTearDown.remove_test_files()
ExecutionTearDown.createreadme()





