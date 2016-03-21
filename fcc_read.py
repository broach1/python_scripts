import ROOT as rt
import os
import math
import subprocess
import numpy as np

rt.gSystem.Load("libdatamodel")

f1 = rt.TFile.Open("../output.root") #path to wherever the file is
t1 = f1.Get("events")

c1 = rt.TCanvas("c1","c1",800,600)
#c2 = rt.TCanvas("c2","c2",800,600)
h_rho = rt.TH1F("h_rho","h_rho",160,2700,3500)
h_rho_e = rt.TH1F("h_rho_e","h_rho_e",160,2700,3500)
h_layer = rt.TH1F("h_layer","h_layer",160,2700,3500)
#ensures bins of 5mm in rho - the width of each layer

for i in xrange(t1.GetEntries()):
    #iterate over events
    t1.GetEntry(i)
    
    #cluster posn/energy
    #for j in xrange(t1.clusters.size()):
    #    x = t1.clusters[j].Core.position.X
    #    y = t1.clusters[j].Core.position.Y
    #    z = t1.clusters[j].Core.position.Z
    #    energy = t1.clusters[j].Core.Energy
    #    rho = math.sqrt(x**2 + y**2)
    #    h_rho.Fill(rho)
    #    h_rho_e.Fill(rho,energy)

    for k in xrange(t1.hits.size()):
        #get layers
        #format specification: 19 empty bins + 32 bins (cellid)
        # + 7 bins (layer) + 1 + 1 + 1 + 3
        #currently, only 13 active bins
        cellid = t1.hits[k].Core.Cellid
        energy = t1.hits[k].Core.Energy

        #shift off the trailing bins
        layer = cellid >> 6
        rho = 2705 + 10*layer #mm
        h_layer.Fill(rho,energy)

c1.cd()
h_layer.Draw("E")
c1.SaveAs("h_layer.jpg")

#h_rho.GetXaxis().SetTitle("#rho (mm)")
#h_rho.GetYaxis().SetTitle("hits per bin")
#c1.SaveAs("h_rho.pdf")
        
#c2.cd()
#h_rho_e.Draw("E")
#h_rho_e.GetXaxis().SetTitle("#rho (mm)")
#h_rho_e.GetYaxis().SetTitle("E deposit (MeV)")
#c2.SaveAs("h_rho_e.pdf")
