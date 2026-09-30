import { request } from "../../shared/api/request"
import type { Bill } from "../../../models/Bill"

export async function getBill(id: number): Promise<Bill> {
  return request<Bill>(`/bills/${id}`)
}

export async function getBills(): Promise<Bill[]> {
  return request<Bill[]>("/bills/")
}