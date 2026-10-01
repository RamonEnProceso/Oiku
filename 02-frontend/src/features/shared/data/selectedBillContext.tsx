import type { ReactNode } from "react";
import { createContext } from "react";
import { useState } from "react";
import type { Bill } from "../../../models/Bill"
import type { SetStateAction, Dispatch } from "react";

type BillContextValue = {
    selectedBill : Bill | null,
    setSelectedBill : Dispatch<SetStateAction<Bill | null>>
}

const BillContext = createContext<BillContextValue>({selectedBill:null,setSelectedBill: () => {}});

const BillProvider = ({ children }: { children: ReactNode }) => {
    const [selectedBill, setSelectedBill] = useState<Bill|null>(null);
    const value : BillContextValue = {selectedBill, setSelectedBill}

    return <BillContext.Provider value={value}>{children}</BillContext.Provider>
}

export {BillProvider, BillContext};