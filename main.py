import numpy as np
import pandas as pd



import xml.etree.ElementTree as et

def make_file(efforts, filename, auth, nm, desc, dur, dur_wc):
    root = et.Element("workout_file")
    #     <author>R.Case</author>
    #     <name>Saturday</name>
    #     <description></description>
    #     <sportType>bike</sportType>
    #     <tags>
    #         <tag name="2019"/>
    #     </tags>
    #     <workout>
    author = et.SubElement(root, "author").text = auth
    name = et.SubElement(root, "name").text = nm
    description = et.SubElement(root, "description").text = desc
    sportType = et.SubElement(root, "sportType").text = "bike"
    tags = et.SubElement(root, "tags")
    workout = et.SubElement(root, "workout")

    #         <Warmup Duration="600" PowerLow="0.2545" PowerHigh="0.75449997" pace="8268"/>
    #         <SteadyState Duration="1200" Power="0.95449996" pace="8268"/>
    #         <SteadyState Duration="600" Power="0.50449997" pace="8268"/>
    #         <SteadyState Duration="1200" Power="0.95449996" pace="8268"/>
    #         <Cooldown Duration="600" PowerLow="0.75449997" PowerHigh="0.2545" pace="8268"/>

    et.SubElement(tags, "tag", name="programmatic")

    et.SubElement(workout, "Warmup", Duration=str(dur_wc), PowerLow="0.2545",
                  PowerHigh="0.75449997", pace="8268")

    for interval in efforts:
        et.SubElement(workout, "SteadyState", Duration=str(dur), Power=str(interval), pace="8268")

    et.SubElement(workout, "Cooldown", Duration=str(dur_wc), PowerLow="0.75449997",
                  PowerHigh="0.2545", pace="8268")

    tree = et.ElementTree(root)
    tree.write(filename)

    make_file(ride_a, "Kinda_Threshold.zwo", "R.Case", "ProcGen Threshold N, mu<-0.9*ftp, sig<-mu*((1-0.9)*2)", "", 60, 300)
make_file(ride_b, "Kinda_VO2.zwo", "R.Case", "ProcGen VO2 N, mu<-0.6*ftp, sig<-mu*((1-0.6)*2)", "", 60, 300)
make_file(ride_c, "Kinda_Steady_State.zwo", "R.Case", "ProcGen SS N, mu<-0.75*ftp, sig<-mu*((1-0.75)*1)", "", 60, 600)
make_file(ride_d, "Kinda_Openers.zwo", "R.Case", "ProcGen Openers? N, mu<-0.7*ftp, sig<-mu*((1-0.7)*1)", "", 30, 600)
