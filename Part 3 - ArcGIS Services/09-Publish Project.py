import arcpy


aprxPath = r"D:\EGT16\Part 3 - ArcGIS Services\Windmills.aprx"
sdDraftFile =  r"D:\EGT16\Windmills.sddraft"
sdFile = r"D:\EGT16\Windmills.sd"
serviceName = "Windmills_EGT16"
serviceSummary = "Windmills Summary"
serviceTags = "Windmills_Tag"

print("Start 09-Publish MXD")
arcpy.env.overwriteOutput = True

print("Opening arpx")
aprx = arcpy.mp.ArcGISProject(aprxPath)

print("Getting Map")
m = aprx.listMaps('Map')[0]

print("Creating SDDraft")
arcpy.mp.CreateWebLayerSDDraft(m, sdDraftFile, 'Windmills_EGT16', 'MY_HOSTED_SERVICES', 'FEATURE_ACCESS')

print("Stage Sevice")
arcpy.StageService_server(sdDraftFile, sdFile)

print("Upload Service")
arcpy.UploadServiceDefinition_server(sdFile, 'My Hosted Services',in_override=True)

print("Script complete")