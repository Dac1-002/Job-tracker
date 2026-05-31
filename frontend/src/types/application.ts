export type Application = {
  id: string;
  title: string;
  company: string;
  status: "pending" | "accepted" | "rejected";
  createdAt?: string;
};