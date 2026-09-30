import type { Lan } from "../models/Lan"
import type { Month } from "../models/Month"

export const monthsAbbr: Record<Lan, Record<Month, string>> = {
    "ES":{
        "01": "ENE",
        "02": "FEB",
        "03": "MAR",
        "04": "ABR",
        "05": "MAY",
        "06": "JUN",
        "07": "JUL",
        "08": "AGO",
        "09": "SEP",
        "10": "OCT",
        "11": "NOV",
        "12": "DIC"},
    "EN":{
        "01": "JAN",
        "02": "FEB",
        "03": "MAR",
        "04": "APR",
        "05": "MAY",
        "06": "JUN",
        "07": "JUL",
        "08": "AUG",
        "09": "SEP",
        "10": "OCT",
        "11": "NOV",
        "12": "DEC"},
}