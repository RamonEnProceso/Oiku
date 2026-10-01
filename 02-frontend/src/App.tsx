import {BillsThisWeek} from './features/00-bills/components/BillsWeek.tsx'
import { CatalogProvider } from './features/shared/data/CategoriesContext.tsx'
import type { Lan } from './models/Lan.ts'

function App() {
  const lan : Lan = "ES";
  return (
    <>
      <CatalogProvider>
        <section>
          <BillsThisWeek lan={lan}/>
        </section>
      </CatalogProvider>
    </>
  )
}

export default App
