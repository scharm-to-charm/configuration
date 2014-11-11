// NOTE: this should be pasted into the bottom of some root macro
// replace XXXX with the histogram to dump points
   TCanvas* can = new TCanvas();
   XXXX->Draw("cont z list");
   can->Update();
   TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
   if (conts == NULL){
      printf("*** No Contours Were Extracted!\n");
      TotalConts = 0;
      return;
   } else {
     // printf("nconts: %i\n", conts->GetSize());
   }
   TList* curves = conts->At(0);
   TGraph* curve = curves->First();
   int npts = curve->GetN();
   // printf("number of points: %i\n", npts);
   for (int iii = 0; iii < npts; iii++) {
     double x, y;
     curve->GetPoint(iii, x, y);
     printf("%f, %f\n", x, y);
   }
   curve->SetLineColor(kRed);
   curve->Draw("l");
