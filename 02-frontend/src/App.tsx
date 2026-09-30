import BillsThisMonth from "./features/00-bills/components/BillsList"
import { CatalogProvider } from './features/shared/data/CategoriesContext.tsx'

function App() {
  return (
    <>
      <CatalogProvider>
        <section>
          <BillsThisMonth/>
        </section>
      </CatalogProvider>
    </>
  )
}

export default App
