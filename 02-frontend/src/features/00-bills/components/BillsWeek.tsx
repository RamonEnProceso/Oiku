import { useEffect, useState } from "react";
import type { Bill } from "../../../models/Bill";
import type { Lan } from "../../../models/Lan";
import { dateToString } from "../../../utils/dateToString";
import { getWeekFirstLastDay } from "../../../utils/getWeekFirstLastDay";
import { getBillsByRange } from "../api/read";
import { ShowBills } from "./ShowBills";

const BillsWeek = ({date}:{date:Date}) => {
  const [bills, setBills] = useState<Bill[]>([])
  const lan : Lan = "ES";

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

const BillsThisWeek = () => {
  const now = new Date();

  return <BillsWeek date={now}/>
}

export {BillsWeek, BillsThisWeek}