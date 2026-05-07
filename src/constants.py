from typing import Final


__all__ = [
    "API_ENDPOINT",
    "API_FIELDS",
    "INVERSE_API_FIELDS"
]


API_ENDPOINT: Final[str] = "https://api.raporty.pse.pl/api/"


API_FIELDS: Final[dict[str, list[str]]] = {
    'KSE-load': [
        'load_fcst', 'load_actual', 'business_date', 'publication_ts',
        'publication_ts_utc', 'dtime', 'dtime_utc', 'period', 'period_utc'
    ],
    'price-fcst': [
        'cen_fcst', 'ckoeb_fcst', 'ceb_sr_fcst', 'cor_fcst', 'imb_energy',
        'dtime', 'dtime_utc', 'period', 'period_utc',
        'contracting', 'business_date', 'publication_ts',
        'publication_ts_utc'
    ]
}

INVERSE_API_FIELDS: Final[dict[str, str]] = {
    fld: edpt
    for edpt, flds in API_FIELDS.items()
    for fld in flds
}

DATETIME_FIELD_BY_ENDPOINT: Final[dict[str, str]] = {
    'KSE-load': 'dtime',
    'price-fcst': 'dtime'
}
