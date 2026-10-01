import {BillsThisWeek} from './features/00-bills/components/BillsWeek.tsx'
import { CatalogProvider } from './features/shared/data/CategoriesContext.tsx'
import { BillProvider } from './features/shared/data/selectedBillContext.tsx';
import { LanProvider } from './features/shared/data/lanContext.tsx';

function App() {
  return (
    <>
      <LanProvider>
      <CatalogProvider>
      <BillProvider>
        <section>
          
            <BillsThisWeek/>

        </section>
      </BillProvider>
      </CatalogProvider>
      </LanProvider>
    </>
  )
}

export default App
