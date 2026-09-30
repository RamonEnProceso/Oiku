export interface Bill{
    id: number
    subcategory_id: number
    account_id: number
    amount: number
    description: string | null
    occurred_at: Date
    created_at: Date
    updated_at: Date
}


export type BillCreate = {
  subcategory: number
  account: number
  amount: number
  description?: string | null
  occurred_at: Date
  created_at: Date
  updated_at: Date
}

export type BillUpdate = {
  subcategory?: number
  account?: number
  amount?: number
  description?: string | null
  occurred_at?: Date
  updated_at: Date
}