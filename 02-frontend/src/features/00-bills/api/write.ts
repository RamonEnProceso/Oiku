import { request } from "../../shared/api/request"
import type { Bill, BillCreate, BillUpdate } from "../../../models/Bill"


export async function createBill(data: BillCreate): Promise<Bill> {
  return request<Bill>("/bills/", { method: "POST", body: data })
}

export async function updateBill(id: number, data: BillUpdate): Promise<Bill> {
  return request<Bill>(`/bills/${id}`, { method: "PUT", body: data })
}

export async function deleteBill(id: number): Promise<void> {
  await request(`/bills/${id}`, { method: "DELETE" })
}