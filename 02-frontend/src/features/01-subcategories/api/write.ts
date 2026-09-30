import { request } from "../../shared/api/request"
import type { Subcategory, SubcategoryCreate, SubcategoryUpdate } from "../../../models/Subcategory"

export async function createSubcategory(data: SubcategoryCreate): Promise<Subcategory> {
  return request<Subcategory>("/subcategory/", { method: "POST", body: data })
}

export async function updateSubcategory(id: number, data: SubcategoryUpdate): Promise<Subcategory> {
  return request<Subcategory>(`/subcategory/${id}`, { method: "PUT", body: data })
}

export async function deleteSubcategory(id: number): Promise<void> {
  await request(`/subcategory/${id}`, { method: "DELETE" })
}