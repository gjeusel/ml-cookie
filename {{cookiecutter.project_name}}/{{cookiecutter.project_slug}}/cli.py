"""Console script for homeserv_inter."""
import fire

from {{ cookiecutter.project_slug }}.raw import convert_csv_to_parquet
from {{ cookiecutter.project_slug }}.datahandler import CleanedDataCookie
from {{ cookiecutter.project_slug }}.boosters import CatBoostCookie, LgbCookie, XgbCookie


def main():
    return fire.Fire({
        "convert-raw": convert_csv_to_parquet,
        "features": CleanedDataCookie,
        "lgb": LgbCookie,
        "xgb": XgbCookie,
        "cgb": CatBoostCookie,
    })
