import { useEffect, useState } from "react";
import type { Bill } from "../../../models/Bill";
import { dateToString } from "../../../utils/dateToString";
import { getWeekFirstLastDay } from "../../../utils/getWeekFirstLastDay";
import { getBillsByRange } from "../api/read";
import { ShowBills } from "./ShowBills";

const BillsWeek = ({date}:{date:Date}) => {
  const [bills, setBills] = useState<Bill[]>([])

  const [start, end] = getWeekFirstLastDay(date);
  const startString = dateToString(start,"yyyy-mm-dd");
  const endString = dateToString(end,"yyyy-mm-dd");

  useEffect(() => {
    getBillsByRange(startString, endString).then(setBills);
  }, [])

  return <>
    <h2>{dateToString(date,"mmmm")}</h2>
    <ShowBills list={bills}/>
  </>
}

const BillsThisWeek = () => {
  const now = new Date();

  return <BillsWeek date={now}/>
}

export {BillsWeek, BillsThisWeek}