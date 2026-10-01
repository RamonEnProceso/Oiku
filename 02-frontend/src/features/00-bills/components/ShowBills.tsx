import type { Bill } from "../../../models/Bill";
import BillCard from "./BillCard";
import styles from "./styles/BillList.module.css"

export const ShowBills = ({ list }: { list: Bill[]}) => {
  return <div className={styles.billList}>
    {list.map((e) => <BillCard billData={e} key={e.id}/>)}
  </div>
}
