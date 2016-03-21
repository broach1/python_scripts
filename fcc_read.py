import ROOT as rt
import os
import math
import subprocess

#source the environment from global
#NOTE - this functionality currently doesn't work -
#you need to source from the command line before running this script

rt.gSystem.Load("libdatamodel")

f1 = rt.TFile.Open("../output.root") #path to wherever the file is
t1 = f1.Get("events")

c1 = rt.TCanvas("c1","c1",800,600)
c2 = rt.TCanvas("c2","c2",800,600)
h_rho = rt.TH1F("h_rho","h_rho",160,2700,3500)
h_rho_e = rt.TH1F("h_rho_e","h_rho_e",160,2700,3500)
#ensures bins of 5mm in rho - the width of each layer

for i in xrange(t1.GetEntries()):
    #iterate over events?
    t1.GetEntry(i)
    for j in xrange(t1.clusters.size()):
        x = t1.clusters[j].Core.position.X
        y = t1.clusters[j].Core.position.Y
        z = t1.clusters[j].Core.position.Z
        energy = t1.clusters[j].Core.Energy
        rho = math.sqrt(x**2 + y**2)
        h_rho.Fill(rho)
        h_rho_e.Fill(rho,energy)

c1.cd()
h_rho.Draw("E")
h_rho.GetXaxis().SetTitle("#rho (mm)")
h_rho.GetYaxis().SetTitle("hits per bin")
c1.SaveAs("h_rho.pdf")
        
c2.cd()
h_rho_e.Draw("E")
h_rho_e.GetXaxis().SetTitle("#rho (mm)")
h_rho_e.GetYaxis().SetTitle("E deposit (MeV)")
c2.SaveAs("h_rho_e.pdf")
