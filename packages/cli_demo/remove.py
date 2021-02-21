import argparse

import sdk_demo as sdk
import dacite


def remove(args: argparse.Namespace):
    datum: sdk.Datum = dacite.from_dict(data_class=sdk.Datum, data=args.__dict__)
    sdk.remove_datum(database_path=args.database, record_no=datum.record_no)
