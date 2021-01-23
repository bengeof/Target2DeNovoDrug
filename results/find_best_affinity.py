import os
import numpy as np
import pandas as pd

if __name__ == "__main__":
    files = list(filter(lambda x: x.endswith("log"),list(map(lambda x: os.path.join(".", x), os.listdir(".")))))

    least_affinity = np.inf
    filename_least=""

    for filename in files:
        
        with open(filename, "r") as content:
            in_table = False
            for line in content:
                if line.strip() == "Writing output ... done.":
                    in_table = False
                if in_table:
                    if float(line.split()[1]) < least_affinity:
                        least_affinity = float(line.split()[1])
                        filename_least = filename.split("docking")[0] + "cplx"
                if line.strip() == "-----+------------+----------+----------":
                    in_table = True

    # print("Least Affinity", least_affinity, "\nFilename", filename_least)
    print(filename_least.strip('./'))
    
