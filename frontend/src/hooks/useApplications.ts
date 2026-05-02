import { useQuery } from "@tanstack/react-query";
import { getApplications } from "../api/applications";
import type { Application } from "../types/application";

export function useApplications() {
  return useQuery<Application[]>({
    queryKey: ["applications"],
    queryFn: getApplications,
  });
}