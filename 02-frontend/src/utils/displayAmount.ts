type AmountFormat = "k" | "Full"; 

export const displayAmount = (num:number, format: AmountFormat) => {
    switch (format){
        case "k":
            return `${(num/1000).toFixed(1)}k`
        case "Full":
            return num;
    }
}