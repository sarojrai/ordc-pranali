export interface Order {
  id?: number;
  order_number: string | number;
  client_id?: string;
  source: string;
  payment_type: string;
  currency: string;
  gross_amount: string | number;
  source_status: string;
  is_blacklisted: boolean;
  created_at: string;
  updated_at: string;
}
