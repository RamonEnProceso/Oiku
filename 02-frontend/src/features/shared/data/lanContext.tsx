import type { ReactNode } from "react";
import { createContext } from "react";
import { useState } from "react";
import type { Lan } from "../../../models/Lan";
import type { SetStateAction, Dispatch } from "react";

type LanContextValue = {
    lan : Lan;
    setLan : Dispatch<SetStateAction<Lan>>
};

const LanContext = createContext<LanContextValue>({lan:"ES",setLan: () => {}});

const LanProvider = ({children}:{children:ReactNode}) =>{

    const [lan, setLan] = useState<Lan>("ES");

    const value: LanContextValue = {lan, setLan}

    return <LanContext.Provider value={value}>{children}</LanContext.Provider>
}

export {LanContext, LanProvider}