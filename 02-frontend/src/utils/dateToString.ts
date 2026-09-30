import type { Lan } from "../models/Lan";
import type { Month } from "../models/Month";
import { monthsAbbr } from "./monthsAbbr";
import { monthsFull } from "./monthsFull";

type dateFormat = "dd/mm" | "dd/mm/yy" | "dd/mmm" | "mmmm";

export const dateToString = (date: Date, format : dateFormat, lan : Lan) => {
    const day = date.getDate();
    const dayString = day >= 10? `${day}`:`0${day}`;
    const month = date.getMonth()+1;
    const monthString = (month >= 10 ? `${month}` : `0${month}`) as Month;
    const year = date.getFullYear();
    switch(format){
        case "dd/mm":
            return `${dayString}/${monthString}`
        case "dd/mm/yy":
            return `${dayString}/${monthString}/${year}`
        case "dd/mmm":
            return `${dayString} ${monthsAbbr[lan][monthString]}`
        case "mmmm":
            return `${monthsFull[lan][monthString]}`
    }
}