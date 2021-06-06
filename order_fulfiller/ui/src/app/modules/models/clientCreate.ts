
export interface Bankdetails {
    bank_name: string;
    ifsc_code: string;
    account_no: string;

}

export interface ContactDetails {
    name: string;
    contact_no: string;
    email: string;

}



export interface Client {
    isSelected?: boolean;
    id: number,
    name: string,
    code: string,
    website?: string | null,
    email?: string | null,
    client_type?: string,
    contract_from?: string,
    contract_to?: string,
    activation_status?: boolean,
    // billing_schedule": 7,
    // day_of_billing": 7,
    // remittance_cycle": 7,
    // credit_limit": 10000,
}