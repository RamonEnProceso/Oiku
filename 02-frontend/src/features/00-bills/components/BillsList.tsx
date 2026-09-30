import { useEffect, useState } from "react";
import { getBillsByMonth } from "../api/read";
import type { Bill } from "../../../models/Bill";
import BillCard from "./BillCard";

const ShowBills = ({ list }: { list: Bill[] }) => {
  return <>
    {list.map((e) => <BillCard billData={e} key={e.id} />)}
  </>
}

export default function BillsThisMonth() {
  const [bills, setBills] = useState<Bill[]>([])

  useEffect(() => {
    const now = new Date()
    getBillsByMonth(now.getFullYear(), now.getMonth() + 1).then(setBills)
  }, [])

  return <ShowBills list={bills} />
}