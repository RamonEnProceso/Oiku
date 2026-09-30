type format = "dd/mm" | "dd/mm/yy";

export const dateToString = (date: Date, format : format) => {
    const day = date.getDate();
    const dayString = day >= 10? `${day}`:`0${day}`;
    const month = date.getMonth()+1;
    const monthString = month >= 10? `${month}`:`0${month}`;
    const year = date.getFullYear();
    switch(format){
        case "dd/mm":
            return `${dayString}/${monthString}`
        case "dd/mm/yy":
            return `${dayString}/${monthString}/${year}`
    }
}