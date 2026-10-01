import type { Month } from "../models/Month";
import { monthsAbbr } from "./monthsAbbr";
import { monthsFull } from "./monthsFull";
import { useLanContext } from "../features/shared/data/lanContext";

type dateFormat = "dd/mm" | "dd/mm/yy" | "dd/mmm" | "mmmm" | "yyyy-mm-dd";

export const dateToString = (date: Date, format : dateFormat) => {
    const day = date.getDate();
    const dayString = day >= 10? `${day}`:`0${day}`;
    const month = date.getMonth()+1;
    const monthString = (month >= 10 ? `${month}` : `0${month}`) as Month;
    const year = date.getFullYear();

    const {lan} = useLanContext();

    switch(format){
        case "dd/mm":
            return `${dayString}/${monthString}`
        case "dd/mm/yy":
            return `${dayString}/${monthString}/${year}`
        case "dd/mmm":
            return `${dayString} ${monthsAbbr[lan][monthString]}`
        case "mmmm":
            return `${monthsFull[lan][monthString]}`
        case "yyyy-mm-dd":
            return `${year}-${month}-${dayString}`
    }
}