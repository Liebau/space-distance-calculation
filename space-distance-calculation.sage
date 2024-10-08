#
# alle Werte aus Wikipedia
#
LichtGeschwindigkeit=299792458      # in [m/s]
ParSec=3.0856775814913673*10**(16)   # in [m]   
Lj=LichJahr=9460730472580800        # in [m]
AE=AbstandErdeSonne=149597870700.0  # in [m]
Lj_km = Lj/1000.0                   # in [km]
AE_km =AE/1000.0                    # in [km]
#
# Funktion zur Umrechnung der Abstände mit angepasstem Maßstab
#
mm2km =10**(-6);                    # 1 Mio [mm] = 1 [km]
km2mm =10**6
km2cm =1000.0*100.0; 
km2m  =1000.0; 
#
def umrechnen(abstand_km, faktor, w=5):
    return n(abstand_km * faktor,digits=w)
#
class Himmelskoerper:
    def __init__(self, name, radius, abstand_km):
        self.name = name
        self.radius_km = radius           # in [km]
        self.abstand_km = abstand_km      # in [km]
#
    def Duchmesser(self):
        return 2.0*self.radius_km; 
#
    def Vergleichsabstand(self, faktor, w=5):
        w=umrechnen(self.abstand_km, faktor,w)
        if w < 0.00001:
            return str(w*km2mm)+ " [mm]"; 
        elif w < 0.001:
            return str(w*km2cm)+ " [cm]"; 
        elif w < 1.0: 
            return str(w*km2m)+ " [m]"; 
        elif w > 10**5:
            return str(w/1000000.0)+ " Mio. [km]"; 
        else:
            return str(w)+ " [km]"; 
#
#        
# Verwendung der Klasse Himmelskoerper
# alle Entfernungen und Radien in [km]
#   Argumente für die Klasse Himmelskoerper : Name, Radius, Abstand zur Sonne 
Sonne           = Himmelskoerper(   "Sonne", 696342.0, 0); 
Erde            = Himmelskoerper(    "Erde",   6378.1, AE_km); 
Mond            = Himmelskoerper(    "Mond",   1737.4, 384400); 
Jupiter         = Himmelskoerper( "Jupiter",  69911.0, 778570000.0); 
Saturn          = Himmelskoerper(  "Saturn",  58232.0, 1433530000.0); 
Pluto           = Himmelskoerper(   "Pluto",   1188.3, 5906380000.0); 
Kuiperguertel   = Himmelskoerper(   "Kuipergürtel", 50*AE_km, 50*AE_km); 
VoyagerI        = Himmelskoerper(   "Voyager I", 163.299*AE_km, 163.299*AE_km); 
#
ProximaCentauri     = Himmelskoerper("Proxima Centauri   "    , 0.154 * Sonne.radius_km, 4.2465 *Lj_km); 
AlphaCentauri       = Himmelskoerper("Alpha Centauri   "      , 1.217 * Sonne.radius_km, 4.344  *Lj_km); 
BarnardsPfeilstern = Himmelskoerper("Barnards Pfeilstern"     , 0.194 * Sonne.radius_km, 5.963  *Lj_km); 
Sirius             = Himmelskoerper("Sirius"                  , 1.714 * Sonne.radius_km, 8.583  *Lj_km); 
GMWolke            = Himmelskoerper("Große Magellansche Wolke", 14000*Lj_km    , 158200   *Lj_km); 
Andromeda          = Himmelskoerper("Andromeda"               , 200000*Lj_km   , 2.5*10**6 *Lj_km); 
#
# Liste von Himmelskörpern 
stars = [ Erde, Jupiter, Saturn, Pluto, VoyagerI, ProximaCentauri, AlphaCentauri, BarnardsPfeilstern, Sirius, GMWolke]
#
# Vergleichskörper
#
Erbse     = Himmelskoerper( "Erbse"     ,6.5/2.0*mm2km  , 0.0);
Golfball  = Himmelskoerper( "Golfball"  ,42.7/2.0*mm2km , 0.0);
Fussball  = Himmelskoerper( "Fußball"   ,0.2228/2/1000.0, 0.0);
Staubkorn = Himmelskoerper( "Staubkorn" ,0.01/2*mm2km   , 0.0);
# 
Vergleiche=[Erbse, Golfball, Fussball, Staubkorn]
#
# Maßstab 
#  
Vergleich = Vergleiche[0];    # 0: Erbse, 1 : Golfball, 2: fussball, 3: Staubkorn
M=(Vergleich.Duchmesser())/Sonne.Duchmesser();
#
show(" Vergleichskörper         : \t", Vergleich.name, "\t mit Durchmesser \t",  umrechnen(Vergleich.Duchmesser(),km2mm,2), " [mm]"); 
show(" Maßstab        1         : \t", n(M**(-1),digits=4))
show(" Lichtjahr                : \t", n(Lj/1000.0,digits=4), " [km]     im Vergleichmaßstab : \t"             , umrechnen(Lj/1000.0, M,5), " [km]"); 
show(" Erde - Mond              : \t", n(Mond.abstand_km,digits=7), " [km]        im Vergleichmaßstab :  \t"   , Mond.Vergleichsabstand(M,3)); 
show(" Durchmesser Kuipergürtel : \t", n(Kuiperguertel.abstand_km,digits=7), " [km]   im Vergleichmaßstab : \t", Kuiperguertel.Vergleichsabstand(M)); 
#
# Erstellung der Tabelle
#
tabelle = [["Himmelskörper", "realer Abstand zur Sonne in Millionen[km]", "Vergleichsabstand"]];  
#
for i in range(len(stars)):
    row = [stars[i].name, n(stars[i].abstand_km*10**(-6),digits=4), stars[i].Vergleichsabstand(M)]
    tabelle.append(row)
#
# Ausgabe der Tabelle
pretty_print(table(tabelle,frame=True, align='center'))
#
