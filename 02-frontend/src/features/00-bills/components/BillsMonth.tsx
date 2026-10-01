import { useEffect, useState } from "react";
import { getBillsByMonth } from "../api/read";
import type { Bill } from "../../../models/Bill";
import type { Lan } from "../../../models/Lan";
import { ShowBills } from "./ShowBills";
import { dateToString } from "../../../utils/dateToString";

const BillsMonth = ({date, lan}:{date:Date, lan:Lan}) => {
  const [bills, setBills] = useState<Bill[]>([])

  useEffect(() => {
    getBillsByMonth(date.getFullYear(), date.getMonth() + 1).then(setBills)
  }, [])

  return <>
  <h2>{dateToString(date,"mmmm", lan)}</h2>
  <ShowBills list={bills} lan={lan}/>
  </>
}

const BillsThisMonth = ({lan}:{lan:Lan}) => {
  const now = new Date()
  return <BillsMonth date={now} lan={lan}/>
}

export {BillsMonth, BillsThisMonth}