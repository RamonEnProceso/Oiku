import type { Bill } from "../../../models/Bill";
import type { Lan } from "../../../models/Lan";
import { dateToString } from "../../../utils/dateToString";
import { displayDescription } from "../../../utils/displayDescription";
import { displayAmount } from "../../../utils/displayAmount";
import { useCatalog } from "../../shared/data/CategoriesContext";
import styles from "./styles/BillCard.module.css"

const BillCard = ({billData, lan}:{billData:Bill, lan:Lan}) => {
  
  return <>
        <div className={styles.billCard}>
          <div className={styles.billCardDate}>
            <p>{dateToString(new Date(billData.occurred_at),"dd/mmm",lan)}</p>
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
