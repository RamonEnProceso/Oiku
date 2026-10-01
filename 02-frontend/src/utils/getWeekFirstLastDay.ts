export const getWeekFirstLastDay = (date:Date) =>{
    const day = date.getDay();
    const diff = day === 0 ? -6 : 1 - day;
    const start = new Date(date);
    start.setDate(date.getDate() + diff);
    const end = new Date(start);
    end.setDate(start.getDate() + 7);
    return [start,end]
}