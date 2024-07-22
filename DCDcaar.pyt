# -*- coding: utf-8 -*-
##Potentially sensitive pathways replaced with "PATHWAY_TO_TARGET_OBJECT"

import arcpy
arcpy.env.overwriteOutput=True
testM=[]

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [CAAR0]


class CAAR0(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "CAAR- Critical Area & Archaeology Review"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        pp=arcpy.Parameter(
            displayName="Identify Folder zzz",
            name="ServerFolder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )
        #0
        p0=arcpy.Parameter(
            displayName="Enter TPN's to search for:",
            name="ListTPN",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p0.values=[362833002000,272141003000,350621001000,461313008000]
        #1 parcels
        p1=arcpy.Parameter(
            displayName="Parcel source to search in:",
            name="StringParcelSource",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        p1.value=r"PATHWAY_TO_TARGET_OBJECT"
        #2a shoreline des
        p2=arcpy.Parameter(
            displayName="Land Use- Shoreline (SMP Designation(s))",
            name="carrLUsmp",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p2.category="1. Shoreline, Land Use, Subarea/Overlay, Plat"
        p2.values=[r"PATHWAY_TO_TARGET_OBJECT"]
        #2b1 lu des
        p3=arcpy.Parameter(
            displayName="Land Use- Comp Plan: Designation",
            name="carrLUcompplan",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p3.category="1. Shoreline, Land Use, Subarea/Overlay, Plat"
        p3.values=[r"PATHWAY_TO_TARGET_OBJECT"]
        #2b2
        p4=arcpy.Parameter(
            displayName="Land Use- Comp Plan: Density",
            name="carrLUcompdensity",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p4.category="1. Shoreline, Land Use, Subarea/Overlay, Plat"
        p4.values=[r"PATHWAY_TO_TARGET_OBJECT"]
        #2c subarea/overlay
        p5=arcpy.Parameter(
            displayName="Land Use- Comp Plan: Subarea/Overlay",
            name="carrLUcompoverlay",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p5.category="1. Shoreline, Land Use, Subarea/Overlay, Plat"
        p5.values=[r"PATHWAY_TO_TARGET_OBJECT",r"PATHWAY_TO_TARGET_OBJECT"]
        #2d plat
        p6=arcpy.Parameter(
            displayName="UPDATE--Land Use- Plat polygons Layer",
            name="carrLUplat",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p6.category="1. Shoreline, Land Use, Subarea/Overlay, Plat"
        p6.values=[r"PATHWAY_TO_TARGET_OBJECT"]
        #3 wetlands
        p7=arcpy.Parameter(
            displayName="Wetland Layer(s)",
            name="carrWetlands",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p7.category="2. Wetlands"
        p7.values=[r"PATHWAY_TO_TARGET_OBJECT",r"PATHWAY_TO_TARGET_OBJECT",r"PATHWAY_TO_TARGET_OBJECT"]
        #4 geology
        p8=arcpy.Parameter(
            displayName="UPDATE--Geological Hazards",
            name="carrLUgeohaz",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p8.category="3. Geological Hazards"
        p8.values=[r"PATHWAY_TO_TARGET_OBJECT", r"PATHWAY_TO_TARGET_OBJECT", r"PATHWAY_TO_TARGET_OBJECT", r"PATHWAY_TO_TARGET_OBJECT", r"PATHWAY_TO_TARGET_OBJECT"]
        #5 fema flodzone
        p9=arcpy.Parameter(
            displayName="Flood Hazard Layer(s)",
            name="carrFloodHazard",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p9.category="4. Special Flood Hazard"
        p9.values=[r"PATHWAY_TO_TARGET_OBJECT"]
        #6 fwhca
        p10=arcpy.Parameter(
            displayName="UPDATE--FWHCA",
            name="carrLUfwhca",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p10.category="5. FWHCA Data"
        p10.values=[r"PATHWAY_TO_TARGET_OBJECT"]
        #7 archaeology
        p11=arcpy.Parameter(
            displayName="Archaeology Layer(s); requires Archaeology2021 feature layer to be open in current map",
            name="caarArchaeology",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p11.category="6. Archaeology"
        p11.values=["6. Archaeology\\Archaeological_Polys"]
        p12=arcpy.Parameter(
            displayName="Plats and Surveys Point Data- used to point to attachments",
            name="caarPlatPoint",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )
        p12.category="7. Additional Data Inputs"
        p12.values=[r"PATHWAY_TO_TARGET_OBJECT"]##2022-08-09 ADDED- need to create this dataset
        ##
        params = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        tpn=[i for i in parameters[0].values]
        dResults={}
        where_clause =""
        for i in tpn:
            if len(where_clause)==0:
                where_clause="PIN = '{}'".format(i)
            else:
                newClause = " OR PIN = '{}'".format(i)
                where_clause=where_clause+newClause
        parcels=parameters[1].valueAsText
        luShoreLayers=parameters[2].values
        luCompLayers=parameters[3].values
        luDensityLayers=parameters[4].values
        luOverlayLayers=parameters[5].values
        luPlatLayers=parameters[6].values
        wetlandLayers=parameters[7].values
        geoHazLayers=parameters[8].values
        #lGeo=["Nonbedrock_Shoreline","SlopeO15","SlopeO50","Soils_With_Subclass_e","unsbluf","WADOEczAtlas"]
        floodLayers=parameters[9].values
        fwhcaLayers=parameters[10].values
        archaeologyLayers=parameters[11].values
        caarPlatPoint=parameters[12].values##2022-08-09 ADDED need to add logic for looking up data, finding fid, and using rest endpoint online to retrieve url's
        l_kSection=["Parcel Overview","Shoreline Designation","Land Use Designation","Land Use Density","Subarea/Overlay Area","Plat Information","Wetlands","Geological Hazards","Special Flood Hazard Area","FWHCA Area","Archaeology"]
        ##2022-08-09 ADDED 'Short_Lega' to search cursor:
        dPlatsPlus={"BS":"Binding Site Plan", "CO":"Condominium", "LP":"Long Plats", "PU":"Planned Unit Development", "SP":"Short Plats"}##key = PlatBoundaries[File_Type]: value = PlatsandSurveys[File_Type]
        with arcpy.da.SearchCursor(parcels,['PIN','SHAPE@','Acres','SitusAddr','Short_Lega'],where_clause) as sc1:
            for row in sc1:
                dResults[row[0]]={}
                dResults[row[0]]["geom"]=row[1]
                dResults[row[0]]["acres"]=round(row[2],2)
                dResults[row[0]]["addr"]=row[3]
                dResults[row[0]]["shortLegal"]=row[4]
        for PIN in dResults.keys():
            PINpoly=dResults[PIN]["geom"]
            ##1 TPN Base Results
            kSection="Parcel Overview"
            addr=""
            for i in "a":
                if len(dResults[PIN]["addr"])<1:
                    addr=""
                else:
                    addr=" ({})".format(dResults[PIN]["addr"])
            dResults[PIN][kSection]="TPN-{0}{1}; Acres={2}; \nShort Legal Description={3}".format(PIN,addr,str(dResults[PIN]["acres"]),dResults[PIN]["shortLegal"])
            ##2a LANDUSE-SHORE
            kSection="Shoreline Designation"
            tCheck=False
            for i in luShoreLayers:
                with arcpy.da.SearchCursor(i,['SHAPE@','Designatio']) as scLUshore:
                    for row in scLUshore:
                        TESTpoly = row[0]
                        desig=row[1]
                        if TESTpoly.disjoint(PINpoly)==False:
                            if kSection in dResults[PIN].keys():
                                dResults[PIN][kSection]="{}, {}".format(dResults[PIN][kSection],desig)
                            else:
                                dResults[PIN][kSection]=desig
                            tCheck=True
                        else:
                            continue
            for i in "r":
                if tCheck==False:
                    dResults[PIN][kSection]="N/A"
                else:
                    continue
            ##2b1 LANDUSE-CompPlan
            kSection="Land Use Designation"
            tCheck=False
            for i in luCompLayers:
                with arcpy.da.SearchCursor(i,['SHAPE@','Landuse']) as scLUcomp:
                    for row in scLUcomp:
                        TESTpoly = row[0]
                        desig=row[1]
                        if PINpoly.trueCentroid.within(TESTpoly)==True:
                            dResults[PIN][kSection]=desig
                            tCheck=True
                            break
                        else:
                            continue
            for i in "r":
                if tCheck==False:
                    dResults[PIN][kSection]="ERROR- no Comp Plan designation found".format(PIN)
                else:
                    continue
            ##2b2 LANDUSE-Density
            kSection="Land Use Density"#adds density
            tCheck=False
            for i in luDensityLayers:
                with arcpy.da.SearchCursor(i,['SHAPE@','Density']) as scLUdens:
                    for row in scLUdens:
                        TESTpoly = row[0]
                        desig=row[1]
                        if PINpoly.trueCentroid.within(TESTpoly)==True:
                            if dResults[PIN]["acres"]<5:
                                dResults[PIN][kSection]=dResults[PIN][kSection]+"-{}".format(desig)
                            else:
                                dResults[PIN][kSection]=dResults[PIN][kSection]+"-{}; Should doublecheck large parcels for multiple densities".format(desig)
                            tCheck=True
                            break
                        else:
                            continue
            for i in "r":
                if tCheck==False:
                    #testM.append("{}: ERROR- no Comp Plan density designation found".format(PIN))
                    dResults[PIN][kSection]="ERROR- no Comp Plan density designation found"
                else:
                    continue
            ##2c1 LANDUSE-OVERLAY####
            kSection="Subarea/Overlay Area"
            tCheck=False
            for i in luOverlayLayers:
                desc=['SHAPE@']
                lFields=[f.name for f in arcpy.ListFields(i)]
                for f in "t":
                    if 'ZONECLASS' in lFields:
                        desc.append('ZONECLASS')
                    else:
                        desc.append('Subarea')
                with arcpy.da.SearchCursor(i,desc) as scLUoverlay:
                    for row in scLUoverlay:
                        TESTpoly = row[0]
                        desig=row[1]
                        if PINpoly.trueCentroid.within(TESTpoly)==True:
                            if kSection in dResults[PIN].keys():
                                dResults[PIN][kSection]="{}, {}".format(dResults[PIN][kSection],desig)
                            else:
                                dResults[PIN][kSection]=desig
                            tCheck=True
                        else:
                            continue
            for i in "r":
                if tCheck==False:
                    dResults[PIN][kSection]="N/A"
                else:
                    continue
            ##2d plat 
            kSection="Plat Information"#luPlatLayers
            tCheck=False
            for i in luPlatLayers:
                with arcpy.da.SearchCursor(i,['SHAPE@','Name','File_Type']) as scLUplat:
                    for row in scLUplat:
                        TESTpoly = row[0]
                        fileType=dPlatsPlus[row[2]]
                        if PINpoly.trueCentroid.within(TESTpoly)==True:
                            dResults[PIN][kSection]=row[1]
                            tCheck=True
                            break
                        else:
                            continue
            for i in "r":
                if tCheck==False:
                    #testM.append("{}: ERROR- no Comp Plan density designation found".format(PIN))
                    dResults[PIN][kSection]="N/A".format(PIN)
                else:
                    continue
            ##3 WETLANDS TEST
            kSection="Wetlands"
            tCheck=False
            for i in wetlandLayers:
                if tCheck==False:
                    with arcpy.da.SearchCursor(i,['SHAPE@']) as scW:
                        for row in scW:
                            TESTpoly = row[0]
                            if TESTpoly.disjoint(PINpoly)==False:
                                dResults[PIN][kSection]="Possible wetlands within 300' of TPN"
                                tCheck=True
                                break
                            else:
                                continue
                else:
                    continue
            for i in "r":
                if tCheck==False:
                    dResults[PIN][kSection]="None in GIS Data"
                else:
                    continue
            ##4 Geological Hazards#geoHazLayers
            kSection="Geological Hazards"
            tCheck=False
            for i in geoHazLayers:
                with arcpy.da.SearchCursor(i,['SHAPE@']) as scGeoHaz:
                    for row in scGeoHaz:
                            TESTpoly = row[0]
                            if TESTpoly.disjoint(PINpoly)==False:
                                dResults[PIN][kSection]="Possible Geological Hazard"
                                tCheck=True
                                break
                            else:
                                continue
            for i in "r":
                if tCheck==False:
                    dResults[PIN][kSection]="None in GIS Data"
                else:
                    continue
            ##5 FLOODZONE TEST
            kSection="Special Flood Hazard Area"
            tCheck=False
            for i in floodLayers:
                if tCheck==False:
                    with arcpy.da.SearchCursor(i,['SHAPE@','SFHA_TF','DFIRM_ID','STATIC_BFE','FLD_AR_ID','FLD_ZONE'],"FLD_ZONE = 'A' OR FLD_ZONE = 'AE' OR FLD_ZONE = 'VE'") as scA:
                        for row in scA:
                            TESTpoly = row[0]
                            if TESTpoly.disjoint(PINpoly)==False:
                                dResults[PIN][kSection]="Special Flood Hazard Area= {0} | DFIRM: {1} | BFE= {2} | Elevation Certificate= {3} (if available) | Zone= {4}".format(row[1],row[2],row[3],row[4],row[5])
                                tCheck=True
                                break
                            else:
                                continue
                else:
                    continue
            for i in "r":
                if tCheck==False:
                    dResults[PIN][kSection]="N/A"
                else:
                    continue
            #5 fwhcaLayers##needs work
            kSection="FWHCA Area"
            tCheck=False
            dResults[PIN][kSection]="Not yet incorporated into model"
            for i in fwhcaLayers:
                desc=arcpy.da.Describe(i)
                with arcpy.da.SearchCursor(i,['SHAPE@']) as scFWHCA:
                    for row in scFWHCA:
                        TESTpoly = row[0]
                        if TESTpoly.disjoint(PINpoly)==False:
                            if kSection in dResults[PIN].keys():
                                dResults[PIN][kSection]="{}, {}".format(dResults[PIN][kSection],desc["name"])
                            else:
                                dResults[PIN][kSection]=desc["name"]
                            tCheck=True
                        else:
                            continue
            for i in "r":
                if tCheck==False:
                    dResults[PIN][kSection]="N/A"
                else:
                    continue
            #6 ARCHAEOLOGY TEST
            kSection="Archaeology"
            tCheck=False
            for i in archaeologyLayers:
                if tCheck==False:
                    with arcpy.da.SearchCursor(i,['SHAPE@']) as scA:
                        for row in scA:
                            TESTpoly = row[0]
                            if TESTpoly.disjoint(PINpoly)==False:
                                dResults[PIN][kSection]="TPN overlaps with Archaeology buffer"
                                tCheck=True
                                break
                            else:
                                continue
                else:
                    continue
            for i in "r":
                if tCheck==False:
                    dResults[PIN][kSection]="N/A"
                else:
                    continue
        for PIN in tpn:
            arcpy.AddMessage("CAAR Script Tool results for TPN- {}".format(PIN))
            for item in l_kSection:
                arcpy.AddMessage("{}: {}".format(item,dResults[iM][item]))
            arcpy.AddMessage("\n---\n")
        del desc, tpn, parcels, row, PIN, PINpoly, wetlandLayers, archaeologyLayers, floodLayers, TESTpoly, luShoreLayers, tCheck, desig, i, luCompLayers, luOverlayLayers, luDensityLayers, kSection, l_kSection, item
        return
