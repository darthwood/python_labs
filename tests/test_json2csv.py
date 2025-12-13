import sys
import os
PROJECT_ROOT = r"C:\\Users\\Andrew\\HiGIT\\python_labs"
sys.path.insert(0, PROJECT_ROOT)
import pytest
import json
import csv
from pathlib import Path
from src.lab05.csv_xlsx import *
from src.lab05.json_csv import *



@pytest.mark.parametrize(  
    "put_in, medved, expected",  
    [
        (
            "././data/samples/people.json",
            "././data/output_stuff/people_rplanes.csv",
            None,
        ), 
        (
            "././data/samples/pisto.json",
            "././data/output_stuff/pisto.csv",
            ValueError,
        ),  
        (
            "././data/samples/shitto.json",
            "././data/output_stuff/shitto11.csv",
            FileNotFoundError,
        ),  
    ],
)
def test_json2csv_fist(put_in, medved, expected):
    if expected is None:  
        assert json_2_csv(put_in, medved) == expected
    else:  
        with pytest.raises(expected):  
            json_2_csv(
                put_in, medved
            )  



@pytest.mark.parametrize(
    "put_in, medved, expected",  
    [
        (
            "././data/samples/people.csv",
            "././data/output_stuff/peoplesnolan.json",
            None,
        ),  
        
        (
            "././data/samples/shitting.csv",
            "././data/output_stuff/shitting11.json",
            FileNotFoundError,
        ),  
    ],
)
def test_csv2json_fist(put_in, medved, expected):
    if expected is None:  
        assert csv_2_json(put_in, medved) == expected
    else:  
        with pytest.raises(expected): 
            csv_2_json(
                put_in, medved
            )  


def test_json2csv_ing(tmp_path: Path):
    src = (
        tmp_path / "people.json"
    )  
    dst = (
        tmp_path / "people.csv"
    )  
    data = [  
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    json_2_csv(
        str(src), str(dst)
    ) 

    with dst.open(
        encoding="utf-8"
    ) as f: 
        rows = list(csv.DictReader(f))

    assert len(rows) == 2  
    assert {"name", "age"} <= set(
        rows[0].keys()
    ) 



def test_csv2json_ing(tmp_path: Path):
    src = (
        tmp_path / "people.csv"
    )  
    dst = (
        tmp_path / "people.json"
    )  
    data = [  
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    x = data[0].keys()  
    with src.open("w", encoding="utf-8") as fc:
        writer = csv.DictWriter(
            fc, fieldnames=x, extrasaction="raise"
        )  
        writer.writeheader()
        writer.writerows(data)
    with src.open("r", encoding="utf-8") as fc:  
        reader = csv.DictReader(fc)  
        data = []  
        for row in reader:  
            data.append(row)  
    with dst.open("w", newline="", encoding="utf-8") as fj:  
        json.dump(
            data, fj, ensure_ascii=False, indent=2
        )  

    assert len(data) == 2  
    assert {"name", "age"} <= set(
        data[0].keys()
    )  



