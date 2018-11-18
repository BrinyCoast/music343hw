#######################################################################
# This uses all of the Expection classes created and declares them 
# under CLI_Audio_Exception class to take care all of the errors 
# that can occur in the program cli-audio.
#
# @author Hai Duong, Theodore Lang, Trung-Vuong Pham
# @date November 18, 2018
#######################################################################
class CLI_Audio_Exception(Exception):
    pass

class CLI_Audio_File_Exception(CLI_Audio_Exception):
    pass

class CLI_Audio_Screen_Size_Exception(CLI_Audio_Exception):
    pass
