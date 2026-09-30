export interface Subcategory{
    id: number
    name: string
    category_id : number
    mindless_spending: boolean
}

export type SubcategoryCreate = {
  name: string
  category_id: number
  mindless_spending: boolean
}

export type SubcategoryUpdate = {
  name?: string
  category_id?: number
  mindless_spending?: boolean
}