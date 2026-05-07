from datetime import date, datetime, timedelta
from typing import Any

import pandas as pd
import requests

from src.constants import API_ENDPOINT, PSE_API_V2_FIELDS

__all__ = ["gdat"]


def _validate_fields(
        endpoint: str,
        fields: list[str]
) -> None:
    if len(
            invalid_fields := (
                    set(fields).difference(set(PSE_API_V2_FIELDS[endpoint]))
            )
    ) > 0:
        raise ValueError(
            f"The following fields are not valid for {endpoint=}: "
            f"{', '.join([x for x in invalid_fields])}! "
        )


def gdat(
    endpoint: str,
    day: str | date | datetime,
    fields: list[str],
    *,
    dtime_field: str = "dtime",
    base_url: str = API_ENDPOINT,
    timeout: int = 30,
) -> pd.DataFrame:

    if isinstance(day, str):
        day = date.fromisoformat(day)
    elif isinstance(day, datetime):
        day = day.date()

    _validate_fields(endpoint, fields)

    start = f"{day:%Y-%m-%d} 00:00:00"
    end = f"{day + timedelta(days=1):%Y-%m-%d} 00:00:00"

    selected_fields = list(dict.fromkeys([dtime_field, *fields]))

    params = {
        "$filter": (
            f"{dtime_field} ge '{start}' "
            f"and {dtime_field} lt '{end}'"
        ),
        "$select": ",".join(selected_fields),
    }

    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    response = requests.get(url, params=params, timeout=timeout)

    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        raise requests.HTTPError(
            f"{exc}\nURL: {response.url}\nResponse: {response.text}"
        ) from exc

    data: dict[str, Any] | list[dict[str, Any]] = response.json()
    rows = data.get("value", data) if isinstance(data, dict) else data

    return pd.DataFrame(rows)
