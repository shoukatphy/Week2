#include<iostream>
#include"Random.cc"

using namespace std;

int randm2(){
int mx=10000;
Random rnd;
rnd.int64();

double x=0;
double numb=0;


auto *hist = new TH1D("hist","CoinToss Probability Distribution", 10000, 0, 7);
for(int i=0; i<mx; i++){

numb = 3.11*TMath::Power(10, -19)*rnd.int64();

//cout<<numb<<endl;

x = Distribution(numb);
hist->Fill(x);
cout<<x<<endl;

}

auto *c = new TCanvas();
hist->SetMarkerStyle(21);
hist->SetLineColor(2);
hist->Draw();


c->SaveAs("TossDis.pdf");
return 0;
}
