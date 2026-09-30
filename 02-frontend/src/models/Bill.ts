export interface Bill{
    id: number
    subcategory_id: number
    account_id: number
    amount: number
    description: string | null
    occurred_at: string
    created_at: string
    updated_at: string
}


export type BillCreate = {
  subcategory: number
  account: number
  amount: number
  description?: string | null
  occurred_at: string
  created_at: string
  updated_at: string
}

export type BillUpdate = {
  subcategory?: number
  account?: number
  amount?: number
  description?: string | null
  occurred_at?: string
  updated_at: string
}