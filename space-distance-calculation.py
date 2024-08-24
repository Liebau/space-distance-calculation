
import argparse
from prettytable import PrettyTable


LichtGeschwindigkeit = 299792458  # in [m/s]
ParSec = 3.0856775814913673 * 10**16  # in [m]
Lj = LichJahr = 9460730472580800  # in [m]
AE = AbstandErdeSonne = 149597870700.0  # in [m]
Lj_km = Lj / 1000.0  # in [km]
AE_km = AE / 1000.0  # in [km]

# Funktion zur Umrechnung der Abstände mit angepasstem Maßstab
mm2km = 10**(-6)  # 1 Mio [mm] = 1 [km]
km2mm = 10**6
km2cm = 1000.0 * 100.0
km2m = 1000.0

def umrechnen(abstand_km, faktor, w=5):
    return round(abstand_km * faktor, w)

class Himmelskoerper:
    def __init__(self, name, radius, abstand_km):
        self.name = name
        self.radius_km = radius  # in [km]
        self.abstand_km = abstand_km  # in [km]

    def Durchmesser(self):
        return 2.0 * self.radius_km

    def Vergleichsabstand(self, faktor, w=5):
        w = umrechnen(self.abstand_km, faktor, w)
        if w < 0.00001:
            return str(w * km2mm) + " [mm]"
        elif w < 0.001:
            return str(w * km2cm) + " [cm]"
        elif w < 1.0:
            return str(round(w * km2m,3)) + " [m]"
        elif w > 10**5:
            return str(round(w / 1000000.0,3)) + " [Mio. km]"
        else:
            return str(w) + " [km]"

# Verwendung der Klasse Himmelskoerper
Sonne = Himmelskoerper("Sonne", 696342.0, 0)
Erde = Himmelskoerper("Erde", 6378.1, AE_km)
Mond = Himmelskoerper("Mond", 1737.4, 384400)
Jupiter = Himmelskoerper("Jupiter", 69911.0, 778570000.0)
Saturn = Himmelskoerper("Saturn", 58232.0, 1433530000.0)
Pluto = Himmelskoerper("Pluto", 1188.3, 5906380000.0)
Kuiperguertel = Himmelskoerper("Kuiperguertel", 50 * AE_km, 50 * AE_km)
VoyagerI = Himmelskoerper("Voyager I", 163.299 * AE_km, 163.299 * AE_km)

ProximaCentauri = Himmelskoerper("Proxima Centauri", 0.154 * Sonne.Durchmesser(), 4.2465 * Lj_km)
AlphaCentauri = Himmelskoerper("Alpha Centauri", 1.217 * Sonne.Durchmesser(), 4.344 * Lj_km)
BarnardsPfeilstern = Himmelskoerper("Barnards Pfeilstern", 0.194 * Sonne.Durchmesser(), 5.963 * Lj_km)
Sirius = Himmelskoerper("Sirius", 1.714 * Sonne.Durchmesser(), 8.583 * Lj_km)
GMWolke = Himmelskoerper("Große Magellansche Wolke", 14000 * Lj_km, 158200 * Lj_km)
Andromeda = Himmelskoerper("Andromeda", 200000 * Lj_km, 2.5 * 10**6 * Lj_km)

# Liste von Himmelskörpern
stars = [Erde, Jupiter, Saturn, Pluto, VoyagerI, ProximaCentauri, AlphaCentauri, BarnardsPfeilstern, Sirius, GMWolke]

# Vergleichskörper
Erbse = Himmelskoerper("Erbse", 6.5 / 2.0 * mm2km, 0.0)
Golfball = Himmelskoerper("Golfball", 42.7 / 2.0 * mm2km, 0.0)
Fussball = Himmelskoerper("Fussball", 0.2228 / 2 / 1000.0, 0.0)
Staubkorn = Himmelskoerper("Staubkorn", 0.01 / 2 * mm2km, 0.0)

Vergleiche = [Erbse, Golfball, Fussball, Staubkorn]

# Argument-Parser konfigurieren
parser = argparse.ArgumentParser(description="Berechnung von kosmischen Entfernungen auf einen bestimmten Maßstab.")
parser.add_argument(
    "-v", "--vergleich", 
    type=int, 
    choices=range(0, 4), 
    default=0, 
    help="Wähle den Vergleichskörper: 0: Erbse, 1: Golfball, 2: Fussball, 3: Staubkorn"
)

args = parser.parse_args()

# Auswahl des Vergleichskörpers
Vergleich = Vergleiche[args.vergleich]  # Standardmäßig Erbse (0)

# Maßstab
M = Vergleich.Durchmesser() / Sonne.Durchmesser()

# Ausgabe
# Schöne Ausgabe mit formatierter Ausrichtung

print(f"{'Vergleichskörper ':<25} : {Vergleich.name} mit Durchmesser {umrechnen(Vergleich.Durchmesser(), km2mm, 2)} [mm]")
print(f"{'Maßstab 1':<25} : {round(1 / M, 4)}")
print(f"{'Lichtjahr':<25} : {round(Lj / 1000.0, 4)} [km] im Vergleichsmaßstab {umrechnen(Lj / 1000.0, M, 5)} [km]")
print(f"{'Erde - Mond':<25} : {round(Mond.abstand_km, 0):,.0f} [km]         im Vergleichsmaßstab {Mond.Vergleichsabstand(M, 3)}")
print(f"{'Durchmesser Kuipergürtel':<25} : {round(Kuiperguertel.abstand_km, 0):,.0f} [km]   im Vergleichsmaßstab {Kuiperguertel.Vergleichsabstand(M)}")



# Erstellung der Tabelle
tabelle = [["Himmelskörper", "realer Abstand zur Sonne in Millionen [km]", "Vergleichsabstand"]]
for i in range(len(stars)):
    row = [stars[i].name, round(stars[i].abstand_km * 10**(-6), 3), stars[i].Vergleichsabstand(M)]
    tabelle.append(row)

# Ausgabe der Tabelle

x = PrettyTable()
x.field_names = ["Himmelskörper", "Realer Abstand (Mio. km)", "Vergleichsabstand"]

# Spaltenausrichtung festlegen (erste Spalte linksbündig)
x.align["Himmelskörper"] = "l"
x.align["Realer Abstand (Mio. km)"] = "c"
x.align["Vergleichsabstand"] = "c"

for row in tabelle[1:]:
    x.add_row(row)
print(x)
