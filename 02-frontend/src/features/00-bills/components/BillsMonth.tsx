import { useEffect, useState } from "react";
import { getBillsByMonth } from "../api/read";
import type { Bill } from "../../../models/Bill";
import { ShowBills } from "./ShowBills";
import { dateToString } from "../../../utils/dateToString";

const BillsMonth = ({date}:{date:Date}) => {
  const [bills, setBills] = useState<Bill[]>([]);

  useEffect(() => {
    getBillsByMonth(date.getFullYear(), date.getMonth() + 1).then(setBills)
  }, [])

  return <>
  <h2>{dateToString(date,"mmmm")}</h2>
  <ShowBills list={bills}/>
  </>
}

const BillsThisMonth = () => {
  const now = new Date()
  return <BillsMonth date={now}/>
}

export {BillsMonth, BillsThisMonth}