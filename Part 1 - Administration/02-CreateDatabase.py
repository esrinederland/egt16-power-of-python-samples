#-------------------------------------------------------------------------------
# Name:        2-CreateDatabase
# Purpose:
#
# Author:      hulzen
#
# Created:     12-11-2015
# Copyright:   (c) esri 2015
#-------------------------------------------------------------------------------
import arcpy
import os

print("Start 2-CreateDatabase")
databasename = "EGT16"
connectionFolderPath = r"D:\EGT16"
connectionFilepath = os.path.join(connectionFolderPath,databasename+".sde")
roleName = None
dbInstance = "ESRIBX0373\SQLEXPRESS"

arcpy.env.overwriteOutput = True
print("Creating database")
#create database
arcpy.CreateEnterpriseGeodatabase_management("SQL_Server", dbInstance, databasename, "OPERATING_SYSTEM_AUTH",
                                             "", "", "SDE_SCHEMA",
                                             "sde", "sde","",r"D:\EGT16\Part 1 - Administration\keycodes")

# Create Connection
print("Creating connection")
arcpy.CreateDatabaseConnection_management(connectionFolderPath,databasename,"SQL_SERVER",
                                          dbInstance,"OPERATING_SYSTEM_AUTH","","","SAVE_USERNAME",databasename)

## Create list of users
print("Creating users")
userList = ['jack', 'linda', 'bill']

## Create users and assign to editor role
for user in userList:
    print("Creating user: {}".format(user))
    arcpy.CreateDatabaseUser_management(connectionFilepath, "DATABASE_USER", user, "SomePassword01") #, roleName)

#import xml workspace document
print("Importing XML Workspace")
arcpy.ImportXMLWorkspaceDocument_management(connectionFilepath,
                                                'D:\EGT16\Part 1 - Administration\WINDMILLS.XML',
                                                'DATA')

print("Script complete")