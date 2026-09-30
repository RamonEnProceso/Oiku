import { createContext, useContext, useEffect, useState, type ReactNode } from "react"
import { getCategories } from "../../02-categories/api/read"
import { getSubcategories } from "../../01-subcategories/api/read"
import type { Category } from "../../../models/Category"
import type { Subcategory } from "../../../models/Subcategory"

type Catalog = {
  categories: Category[]
  subcategories: Subcategory[]
  loading: boolean
  error: string | null
  categoryName: (id: number) => string | undefined
  subcategoryName: (id: number) => string | undefined
}

const CatalogContext = createContext<Catalog | null>(null)

export function CatalogProvider({ children }: { children: ReactNode }) {
  const [categories, setCategories] = useState<Category[]>([])
  const [subcategories, setSubcategories] = useState<Subcategory[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    async function load() {
      try {
        const [cats, subs] = await Promise.all([getCategories(), getSubcategories()])
        setCategories(cats)
        setSubcategories(subs)
      } catch (e) {
        setError(e instanceof Error ? e.message : "Unknown error")
      } finally {
        setLoading(false)
      }
    }

    load()
  }, [])

  const categoryName = (id: number) => categories.find((c) => c.id === id)?.name
  const subcategoryName = (id: number) => subcategories.find((s) => s.id === id)?.name

  const value: Catalog = {
    categories,
    subcategories,
    loading,
    error,
    categoryName,
    subcategoryName,
  }

  return <CatalogContext.Provider value={value}>{children}</CatalogContext.Provider>
}

export function useCatalog(): Catalog {
  const ctx = useContext(CatalogContext)
  if (!ctx) {
    throw new Error("useCatalog must be used inside <CatalogProvider>")
  }
  return ctx
}