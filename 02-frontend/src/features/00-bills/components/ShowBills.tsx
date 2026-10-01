import type { Bill } from "../../../models/Bill";
import type { Lan } from "../../../models/Lan";
import BillCard from "./BillCard";
import styles from "./styles/BillList.module.css"

export const ShowBills = ({ list, lan }: { list: Bill[], lan: Lan }) => {
  return <div className={styles.billList}>
    {list.map((e) => <BillCard billData={e} key={e.id} lan={lan}/>)}
  </div>
}
