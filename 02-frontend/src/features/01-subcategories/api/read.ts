import { request } from "../../shared/api/request"
import type { Subcategory } from "../../../models/Subcategory"

export async function getSubcategory(id: number): Promise<Subcategory> {
  return request<Subcategory>(`/subcategory/${id}`)
}

export async function getSubcategories(): Promise<Subcategory[]> {
  return request<Subcategory[]>("/subcategory/")
}