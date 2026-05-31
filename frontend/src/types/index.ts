export interface User { id: string; email: string; full_name: string; }

export interface Company { 
  id: string; 
  name: string; 
  website?: string; 
  industry?: string; 
  notes?: string; 
}

export type ApplicationStatus = 
  'SAVED' | 
  'APPLIED' | 
  'PHONE_SCREEN' | 
  'INTERVIEW' | 
  'OFFER' | 
  'ACCEPTED' | 
  'REJECTED' | 
  'WITHDRAWN'

export interface Application { 
  id: string; 
  company_id: string; 
  role_title: string; 
  current_status: ApplicationStatus; 
  
}

