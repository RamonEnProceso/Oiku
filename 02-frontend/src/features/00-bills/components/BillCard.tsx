import type { Bill } from "../../../models/Bill";
import { dateToString } from "../../../utils/dateToString";
import { displayDescription } from "../../../utils/displayDescription";
import { displayAmount } from "../../../utils/displayAmount";
import { useCatalog } from "../../shared/data/CategoriesContext";
import { useBillContext } from "../../shared/data/selectedBillContext";
import styles from "./styles/BillCard.module.css"

const BillCard = ({billData}:{billData:Bill}) => {
  const { setSelectedBill } = useBillContext();

  return <>
        <div className={styles.billCard} onClick={()=>{setSelectedBill(billData)}}>
          <div className={styles.billCardDate}>
            <p>{dateToString(new Date(billData.occurred_at),"dd/mmm")}</p>
          </div>
          <div className={styles.billCardBody}>
            <p className={styles.description}>{displayDescription(billData.description)}</p>
            <div className={styles.subcategory}>{useCatalog().subcategoryName(billData.subcategory_id)}</div>
          </div>
          <div className={styles.billCardAmount}>
            <p>${displayAmount(billData.amount, "k")}</p>
          </div>
        </div>
    </>
}

export default BillCard;
