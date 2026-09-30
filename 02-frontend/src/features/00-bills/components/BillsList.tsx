import { useEffect, useState } from "react";
import { getBillsByMonth } from "../api/read";
import type { Bill } from "../../../models/Bill";
import type { Lan } from "../../../models/Lan";
import BillCard from "./BillCard";
import { dateToString } from "../../../utils/dateToString";
import styles from "./styles/BillList.module.css"

const ShowBills = ({ list, lan }: { list: Bill[], lan: Lan }) => {
  return <div className={styles.billList}>
    {list.map((e) => <BillCard billData={e} key={e.id} lan={lan}/>)}
  </div>
}

export default function BillsThisMonth() {
  const [bills, setBills] = useState<Bill[]>([])
  const now = new Date()
  const lan : Lan = "ES";

  useEffect(() => {
    getBillsByMonth(now.getFullYear(), now.getMonth() + 1).then(setBills)
  }, [])

  return <>
  <h2>{dateToString(now,"mmmm", lan)}</h2>
  <ShowBills list={bills} lan={lan}/>
  </>
}