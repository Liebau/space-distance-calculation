# Space Distance Calculation

This project calculates distances in space and scales them down to a specific ratio. It consists of two versions: a **SageMath** version and a **Python** version. Both versions perform the same calculations and can be used to understand the relative sizes and distances of various celestial bodies. 
For more information visit my website: [Cosmic Distances](https://dr-liebau.de/kosmische-entfernungen/)

## Contents

- **`space_distance_calculation.sage`**: The SageMath version of the script, which runs in a SageMath environment.
- **`space_distance_calculation.py`**: The Python version of the script, which runs in a standard Python environment and includes additional functionality for selecting a reference object via command-line arguments.

## Installation

### SageMath Version

1. Install [SageMath](https://www.sagemath.org/).
2. Download or clone the repository:
   ```bash
   git clone https://github.com/username/space-distance-calculation.git
   ```
3. Run the SageMath script:
   ```bash
   sage space_distance_calculation.sage
   ```

### Alternative Execution Option

You can also run the SageMath script directly online at [sagecell.sagemath.org](https://sagecell.sagemath.org/) without needing a local SageMath installation. Simply copy the code from the `.sage` file and paste it into the text field on the website.

### Python Version

1. Ensure that Python 3.6 or higher is installed.
2. Install the required dependencies:
   ```bash
   pip install prettytable
   ```
3. Run the Python script:
   ```bash
   python3 space_distance_calculation.py
   ```

### Command-Line Arguments

The Python script allows you to select the reference object for scaling via a command-line argument:

- **Default**: The script uses a pea (`Erbse`) as the reference object.
- **Custom selection**: You can choose between four different reference objects using the `-v` or `--vergleich` option.

#### Available Reference Objects:

- `0`: Pea 
- `1`: Golf ball 
- `2`: Soccer ball 
- `3`: Dust particle 

#### Example Usage:

- **Default (Pea):**
  ```bash
  python3 space_distance_calculation.py
  ```

- **With Golf Ball:**
  ```bash
  python3 space_distance_calculation.py -v 1
  ```


## Example Output

An example of the script’s output shows the distances of the celestial bodies in kilometers along with the corresponding scaled values:

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

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.

## Contribution

Contributions to the project are welcome! Feel free to open an issue or submit a pull request if you have ideas or improvements.


