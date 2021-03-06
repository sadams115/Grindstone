# Grindstone gs_NonDefHistCheck_class.py
# Authors: Sam Carnes and Sean Adams

# This file scans every DAG object in the scene and checks for any non-deformer history.
# The script returns a true or false depending on the results

import pymel.core as pm
import maya.cmds as cmds

class NonDefHistCheck:
    
    
    #********** INIT **********#
    
    def __init__(self):
        
        # identify whether or not the script has an auto-fix function
        self.hasFix = True

        # identify what this check is called
        self.scriptName = "Non-deformer history"
        
        # provides a label for the button that executes the auto-fix
        # NO MORE THAN 20 CHARACTERS
        self.fixLabel = "Delete history"
    
    
    
    #********** DO CHECK **********#
    
    def doCheck(self):
        
        # Select all DAG objects in the scene and set them to an array
        sceneSel = pm.ls(dagObjects = True)
        
        # Set up elements for iterating through the selection
        objInd = 0
        nonDefTag = ''
        
        for someObj in sceneSel:
            nonDefChk = [n for n in sceneSel[objInd].history(il=1,pdo=True) if not isinstance(n, pm.nodetypes.GeometryFilter)] #and not cmds.referenceQuery(n, isNodeReferenced=True)
            objInd += 1
            
            if nonDefChk:
                nonDefTag = 'Non-Deformer history detected.'
                break
        
        return nonDefTag
        
        
        
    #********** RUN FIX **********#
    
    # deletes non-deformer history
    def runFix(self):
        
        try:
            
            # delete non-deformer history
            cmds.bakePartialHistory(allShapes=True, prePostDeformers=True)
            
            return "Non-deformer history deleted."
            
        except:
            
            return "There was a problem deleteing non-deformer history."
            


#********** RETURN INSTANCE OF SCRIPT CLASS **********#

def getObject():
    return NonDefHistCheck()