# Skalierte kosmische Distanzen

Dieses Projekt berechnet die Distanzen im Weltraum und skaliert sie auf einen bestimmten Maßstab herunter. Es besteht aus zwei Versionen: einer SageMath-Version und einer Python-Version. Beide Versionen bieten die gleichen Berechnungen und können verwendet werden, um die Größen und Abstände verschiedener Himmelskörper im Verhältnis zu einem gewählten Vergleichsmaßstab anschaulich darzustellen.
Weitere Informationen findest du auf meiner Webseite: [Kosmische Entfernungen](https://dr-liebau.de/kosmische-entfernungen/)

## Inhalte

- **`space_distance_calculation.sage`**: Die SageMath-Version des Skripts, die in einer SageMath-Umgebung ausgeführt wird.
- **`space_distance_calculation.py`**: Die Python-Version des Skripts, die in einer Standard-Python-Umgebung ausgeführt wird und zusätzliche Funktionalität für die Auswahl eines Vergleichskörpers über Kommandozeilenargumente bietet.

## Installation

### SageMath-Version

1. Installiere [SageMath](https://www.sagemath.org/).
2. Lade das Repository herunter oder klone es:
   ```bash
   git clone https://github.com/username/space-distance-calculation.git
   ```
3. Führe das SageMath-Skript aus:
   ```bash
   sage space_distance_calculation.sage
   ```

### Alternative Ausführungsmöglichkeit

Du kannst das SageMath-Skript auch direkt online auf [sagecell.sagemath.org](https://sagecell.sagemath.org/) ausführen, ohne eine lokale Installation von SageMath. Kopiere dazu einfach den Code aus der `.sage`-Datei und füge ihn in das Textfeld auf der Webseite ein.

### Python-Version

1. Stelle sicher, dass Python 3.6 oder höher installiert ist.
2. Installiere die erforderlichen Abhängigkeiten:
   ```bash
   pip install prettytable
   ```
3. Führe das Python-Skript aus:
   ```bash
   python3 space_distance_calculation.py
   ```

### Kommandozeilenargumente

Das Python-Skript ermöglicht die Auswahl des Vergleichskörpers für die Skalierung über ein Kommandozeilenargument:

- **Standard**: Das Skript verwendet eine Erbse (`Erbse`) als Vergleichskörper.
- **Benutzerdefinierte Auswahl**: Du kannst zwischen vier verschiedenen Vergleichskörpern mit der Option `-v` oder `--vergleich` wählen.

#### Verfügbare Vergleichskörper:

- `0`: Erbse 
- `1`: Golfball 
- `2`: Fußball 
- `3`: Staubkorn 

#### Beispielhafte Verwendung:

- **Standard (Erbse):**
  ```bash
  python3 space_distance_calculation.py
  ```

- **Mit Golfball:**
  ```bash
  python3 space_distance_calculation.py -v 1
  ```



## Beispielausgabe

Ein Beispiel für die Ausgabe des Skripts zeigt die Entfernungen der Himmelskörper in Kilometern sowie die entsprechenden skalierten Werte:

```
Vergleichskörper          : Erbse mit Durchmesser 6.5 [mm]
Maßstab 1                 : 214259076923.0769
Lichtjahr                 : 9460730472580.8 [km] im Vergleichsmaßstab 44.15556 [km]
Erde - Mond               : 384,400 [km]         im Vergleichsmaßstab 0.0 [mm]
Durchmesser Kuipergürtel  : 7,479,893,535 [km]   im Vergleichsmaßstab 34.91 [m]
+--------------------------+--------------------------+-------------------+
| Himmelskörper            | Realer Abstand (Mio. km) | Vergleichsabstand |
+--------------------------+--------------------------+-------------------+
| Erde                     |         149.598          |     70.0 [cm]     |
| Jupiter                  |          778.57          |      3.63 [m]     |
| Saturn                   |         1433.53          |      6.69 [m]     |
| Pluto                    |         5906.38          |     27.57 [m]     |
| Voyager I                |        24429.183         |     114.02 [m]    |
| Proxima Centauri         |       40174991.952       |   187.5066 [km]   |
| Alpha Centauri           |       41097413.173       |   191.81177 [km]  |
| Barnards Pfeilstern      |       56414335.808       |   263.29963 [km]  |
| Sirius                   |       81201449.646       |   378.98721 [km]  |
| Große Magellansche Wolke |    1496687560762.283     |  6.985 [Mio. km]  |
+--------------------------+--------------------------+-------------------+

```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Details findest du in der `LICENSE`-Datei.

## Beitrag

Beiträge zum Projekt sind willkommen! Erstelle gerne ein Issue oder sende einen Pull Request, falls du Ideen oder Verbesserungen hast.

