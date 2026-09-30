import type { Bill } from "../../../models/Bill";
import { dateToString } from "../../../utils/dateToString";
import { displayDescription } from "../../../utils/displayDescription";
import { useCatalog } from "../../shared/data/CategoriesContext";

const BillCard = ({billData}:{billData:Bill}) => {
  
  return <>
        <div>
          <div>
            <p>{dateToString(new Date(billData.occurred_at),"dd/mm")}</p>
          </div>
          <div>
            <p>{displayDescription(billData.description)}</p>
            <div>{useCatalog().subcategoryName(billData.subcategory_id)}</div>
          </div>
          <div>
            <p>{billData.amount}</p>
          </div>
        </div>
    </>
}

export default BillCard;
