import { useEffect, useState } from "react";
import type { Bill } from "../../../models/Bill";
import type { Lan } from "../../../models/Lan";
import { dateToString } from "../../../utils/dateToString";
import { getWeekFirstLastDay } from "../../../utils/getWeekFirstLastDay";
import { getBillsByRange } from "../api/read";
import { ShowBills } from "./ShowBills";

const BillsWeek = ({date, lan}:{date:Date, lan:Lan}) => {
  const [bills, setBills] = useState<Bill[]>([])

  const [start, end] = getWeekFirstLastDay(date);
  const startString = dateToString(start,"yyyy-mm-dd",lan);
  const endString = dateToString(end,"yyyy-mm-dd",lan);

  useEffect(() => {
    getBillsByRange(startString, endString).then(setBills);
  }, [])

  return <>
    <h2>{dateToString(date,"mmmm", lan)}</h2>
    <ShowBills list={bills} lan={lan}/>
  </>
}

const BillsThisWeek = ({lan}:{lan:Lan}) => {
  const now = new Date();

  return <BillsWeek date={now} lan={lan}/>
}

export {BillsWeek, BillsThisWeek}