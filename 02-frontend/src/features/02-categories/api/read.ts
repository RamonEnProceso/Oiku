import { request } from "../../shared/api/request"
import type { Category } from "../../../models/Category"

export async function getCategory(id: number): Promise<Category> {
  return request<Category>(`/category/${id}`)
}

export async function getCategories(): Promise<Category[]> {
  return request<Category[]>("/category/")
}
