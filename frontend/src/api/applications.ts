import api from "./client";
import type { Application } from "../types/application";

// Get all applications
export const getApplications = async (): Promise<Application[]> => {
  const res = await api.get<Application[]>("/applications");
  return res.data;
};

// Get single application by ID
export const getApplication = async (id: string): Promise<Application> => {
  const res = await api.get<Application>(`/applications/${id}`);
  return res.data;
};

// Create new application
export const createApplication = async (
  data: Omit<Application, "id">
): Promise<Application> => {
  const res = await api.post<Application>("/applications", data);
  return res.data;
};

// Update existing application
export const updateApplication = async (
  id: string,
  data: Partial<Application>
): Promise<Application> => {
  const res = await api.put<Application>(`/applications/${id}`, data);
  return res.data;
};

// Delete application
export const deleteApplication = async (id: string): Promise<void> => {
  await api.delete(`/applications/${id}`);
};