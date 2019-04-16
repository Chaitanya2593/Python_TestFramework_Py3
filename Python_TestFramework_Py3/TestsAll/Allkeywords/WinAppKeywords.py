'''

Created on March 2018
Framework Conceived by : Venkata
@author: Venkata
Refactoring of method names is finished
class name should be same as the file name
'''
from robot.api.deco import keyword
from AllNavigations.pgptool_bo import WinBusinessObjectsClass


class WinAppKeywords():
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        '''
        this is a class constructor
        '''

    @keyword('Remove Existing Keyring of PGP')
    def win_remove_existing_keyring_of_pgp(self, pgptoolexe_loc, which_btn, file_loc):
        cmt = WinBusinessObjectsClass()
        cmt.win_remove_existing_keyring_of_pgp(pgptoolexe_loc, which_btn, file_loc)

    @keyword('Add a PGP Encryption key')
    def win_add_encryption_key(self, pgptoolexe_loc, which_btn, file_loc):
        cmt = WinBusinessObjectsClass()
        cmt.win_add_encryption_key(pgptoolexe_loc, which_btn, file_loc)

    @keyword('PGP encryption of File')
    def pgp_encryption_of_file(self, pgptoolexe_loc, which_btn, file_loc):
        cmt = WinBusinessObjectsClass()
        cmt.win_pgp_encryption_of_file(pgptoolexe_loc, which_btn, file_loc)

    @keyword('Upload a File to FTP')
    def upload_a_file_to_ftp(self, ftp_server_address, ftp_uname, ftp_pwd, file_loc_icluding_filename, remote_ftp_dir):
        cmt = WinBusinessObjectsClass()
        cmt.win_upload_file_to_sftp(ftp_server_address, ftp_uname, ftp_pwd, file_loc_icluding_filename, remote_ftp_dir)
