import { Component, OnDestroy, OnInit, ViewEncapsulation } from "@angular/core";
import { AbstractControl, FormArray, FormBuilder, FormControl, FormGroup, Validators } from "@angular/forms";
import { MatSnackBar } from "@angular/material/snack-bar";
import { ActivatedRoute, Router } from "@angular/router";
import { BrandWebsite, WarehouseManagementSystem, CourierPartner, ModeOfNotification, NotificationMethod, OrderType } from "src/app/modules/models";
import { formatDateYYYYMMDDD, markFormGroupTouched } from "../../shared/helper";
import { ClientDataService } from "../services/ClientDataService";
import { generateBankDetailFG, generateContactDetailFG } from "./utils";


@Component({
    selector: 'order-create-client',
    templateUrl: './create-client.component.html',
    styleUrls: ['./create-client.component.scss'],
    encapsulation: ViewEncapsulation.None,
    providers: [
    ],
})
export class CreateClientComponent implements OnInit, OnDestroy {
    createClientFormGroup!: FormGroup;
    brandWebsites: Array<BrandWebsite> = [
        {
            value: "SHOPIFY",
            label: "SHOPIFY"
        },
        {
            value: "MAGANTO",
            label: "MAGANTO"
        },
        {
            value: "NOOCOMMERCE",
            label: "NOO-COMMERCE"
        },
        {
            value: "INHOUSE",
            label: "IN-HOUSE"
        }
    ];

    marketPlaceWebsites: Array<BrandWebsite> = [
        {
            label: 'Amazon',
            value: 'AMAZON'
        },
        {
            label: 'Flipkart',
            value: 'FLIPKART'
        },
        {
            label: 'Snapdeal',
            value: 'SNAPDEAL'
        },
        {
            label: 'Myntra',
            value: 'MYNTRA'
        },
        {
            label: 'Any Other (Specify)',
            value: 'other'
        }
    ];

    warehouseMgmts: Array<WarehouseManagementSystem> = [
        {
            label: 'UNI-COMMERCE',
            value: 'UNI-COMMERCE'
        },
        {
            label: 'PURPLEDRONE',
            value: 'PURPLEDRONE'
        },
        {
            label: 'VINCULLUM',
            value: 'VINCULLUM'
        },
        {
            label: 'Any Other',
            value: 'other'
        }
    ];

    courierPartners: Array<CourierPartner> = [
        {
            label: 'Pickrr',
            value: 'PICKRR'
        },
    ];

    modeOfNotifications: Array<ModeOfNotification> = [
        {
            label: 'WHATSAPP',
            value: 'WHATSAPP'
        },
        {
            label: 'SMS',
            value: 'SMS'
        },
        {
            label: 'EMAIL',
            value: 'EMAIL'
        },
        {
            label: 'IVR',
            value: 'IVR'
        },
        {
            label: 'Manual Calling',
            value: 'MANUAL-CALLING'
        }
    ];

    orderTypes: Array<OrderType> = [
        {
            label: "COD",
            value: "COD"
        },
        {
            label: "Pre-Paid",
            value: "PRE-PAID"
        }
    ];

    notificationMethods: Array<NotificationMethod> = [
        {
            label: "ALL w/o Logic",
            value: "ALL-WO-LOGIC"
        },
        {
            label: "AUTO with Logic",
            value: "AUTO-WITH-LOGIC"
        }
    ]

    constructor(
        private router: Router,
        private activatedRoute: ActivatedRoute,
        private _snackBar: MatSnackBar,
        private _formBuilder: FormBuilder,
        private _dataService: ClientDataService
    ) { }

    ngOnDestroy(): void {
    }

    ngOnInit(): void {
        this.createClientGroup();

        console.log(this.generateCreateClientModel());
    }

    get clientSection(): AbstractControl | null { return this.createClientFormGroup.get('clientSection'); }

    getStepperFormGroup(index: number) {
        return <FormGroup>this.createClientFormGroup.get('clientSection')?.get([index])
    }

    getStepperFormArray(index: number) {
        return <FormArray>this.createClientFormGroup.get('clientSection')?.get([index])
    }

    createClientGroup() {
        this.createClientFormGroup = this._formBuilder.group({
            clientSection: this._formBuilder.array([
                this._formBuilder.group({
                    name: this._formBuilder.control('', [Validators.required]),
                    source: this._formBuilder.control('', [Validators.required]),
                    address1: this._formBuilder.control('', [Validators.required]),
                    address2: this._formBuilder.control('', []),
                    address3: this._formBuilder.control('', []),
                    state: this._formBuilder.control('', [Validators.required]),
                    city: this._formBuilder.control('', [Validators.required]),
                    pincode: this._formBuilder.control('', [Validators.required]),
                    productCategory: this._formBuilder.control('', [Validators.required]),
                    salesValue: this._formBuilder.control('', [Validators.required]),
                    bankDetails: this._formBuilder.array([generateBankDetailFG(this._formBuilder)], [Validators.required]),
                    contactDetails: this._formBuilder.array([generateContactDetailFG(this._formBuilder)], [Validators.required])
                }),
                this._formBuilder.group({
                    brandWebsite: this._formBuilder.control('', [Validators.required]),
                    mktPlaceWebsites: this.generateMarketPlaceFormArray(this._formBuilder),
                    warehouseMgmt: this._formBuilder.control('', [Validators.required]),
                    courierPartner: this._formBuilder.control('', [Validators.required]),
                }),
                this._formBuilder.group({
                    modeOfNotification: this.generateModeOfNotificationFormArray(this._formBuilder),
                    orderTypes: this.generateOrderTypesFormArray(this._formBuilder),
                    notificationMethod: this._formBuilder.control('', [Validators.required]),
                    firstModeOfNotification: this._formBuilder.control('', [Validators.required]),
                    eddCalaculationFeature: this._formBuilder.control(false, [Validators.required]),
                    noOfReminders: this.generateNoOfNotificationsFormArray(),
                    notificationModePriority: this._formBuilder.array([], [Validators.required]),
                    sequenceNdrShipmentOrders: this._formBuilder.array([], [Validators.required])
                }),
                this._formBuilder.group({})
            ])
        });
    }

    generateMarketPlaceFormArray(_formBuilder: FormBuilder) {
        let marketPlacesFA = this._formBuilder.array([], [Validators.required]);
        this.marketPlaceWebsites.forEach(_ => marketPlacesFA.push(this._formBuilder.control(false)));
        return marketPlacesFA;
    }

    generateOrderTypesFormArray(_formBuilder: FormBuilder) {
        let orderTypesFA = _formBuilder.array([], [Validators.required]);
        this.orderTypes.forEach(_ => orderTypesFA.push(_formBuilder.control(false)));
        return orderTypesFA;
    }

    generateModeOfNotificationFormArray(_formBuilder: FormBuilder) {
        let modeOfNotificationsFA = _formBuilder.array([], [Validators.required]);
        this.modeOfNotifications.forEach(_ => modeOfNotificationsFA.push(_formBuilder.control(false)));
        return modeOfNotificationsFA;
    }

    generateNoOfNotificationsFormArray() {
        let noOfNotifications = this._formBuilder.array([], [Validators.required]);
        this.modeOfNotifications.map(_ => {
            let group = this._formBuilder.group({
                duration: this._formBuilder.control(0),
                priority: this._formBuilder.control(0),
                number: this._formBuilder.control(0)
            });
            noOfNotifications.push(group);
        });
        return noOfNotifications;
    }

    checkGroupValidation() {
        markFormGroupTouched(this.createClientFormGroup);
    }

    generateCreateClientModel() {
        if (!this.createClientFormGroup.valid) {
            return {};
        }

        let clientFormGroup = this.createClientFormGroup.value.clientSection;
        // let clientFormGroup = this.tempClientFormGroup();
        console.log(clientFormGroup);
        let basicDetailFG = clientFormGroup[0];
        let integrationFG = clientFormGroup[1];
        let communicationFG = clientFormGroup[2];

        var currentDate = new Date();
        var nextYear = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDay())
        // let bankDetails = 
        let clientModel = {
            basic_detail: {
                name: basicDetailFG.name,
                client_type: basicDetailFG.source,
                contract_from: formatDateYYYYMMDDD(currentDate),
                contract_to: formatDateYYYYMMDDD(nextYear),
                deactivation_date: formatDateYYYYMMDDD(nextYear)
            },
            basic_detail_additional: {
                address1: basicDetailFG.address1,
                address2: basicDetailFG.address2,
                address3: basicDetailFG.address3,
                state: basicDetailFG.state,
                city: basicDetailFG.city,
                pincode: basicDetailFG.pincode,
                product_category: basicDetailFG.productCategory,
                sales_value: basicDetailFG.salesValue,
                bank_details: basicDetailFG.bankDetails?.map((bankDetail: { bankName: any; accountNo: any; ifscCode: any; }) => {
                    return {
                        bank_name: bankDetail.bankName,
                        account_no: bankDetail.accountNo,
                        ifsc_code: bankDetail.ifscCode
                    };
                }),
                contact_details: basicDetailFG.contactDetails?.map((contact: { name: any; email: any; contactNo: any; }) => {
                    return {
                        name: contact.name,
                        email: contact.email,
                        contact_no: contact.contactNo
                    };
                })
            },
            integration: {
                brand_website: integrationFG.brandWebsite,
                mkt_place_websites: this.mapMktPlaceWebsites(integrationFG.mktPlaceWebsites),
                warehouse_mgmt: integrationFG.warehouseMgmt,
                courier_partner: integrationFG.courierPartner,
            },
            communication: {
                notification_method: communicationFG.notificationMethod,
                first_mode_of_notification: communicationFG.firstModeOfNotification,
                edd_calaculation_deature: communicationFG.eddCalaculationFeature,
                no_of_reminders: communicationFG.noOfReminders,
                notification_mode_priority: communicationFG.notificationModePriority,
                sequence_ndr_shipment_orders: communicationFG.sequenceNdrShipmentOrders,
                mode_of_notification: this.mapModeOfNotifications(communicationFG.modeOfNotification),
                order_types: this.mapOrderTypes(communicationFG.orderTypes)
            }
        }
        return clientModel;
    }

    onSubmit(event: Event) {
        var clientRequest = this.generateCreateClientModel();
        console.log(clientRequest);
        this._dataService.createClient(clientRequest)
            .subscribe(result => {
                if (!result['is_error']) {
                    // let message = (this.editTender ? 'Tender Edited SuccessFully' : 'Tender Created SuccessFully');
                    let message = 'Client Created SuccessFully';
                    this._snackBar.open(message, 'Ok', {
                        duration: 2000,
                        panelClass: ['success-snackbar']
                    });
                    this.createClientFormGroup.reset();
                    this.router.navigate(['/home/client/list']);

                } else {
                    // let message = (this.editTender ? 'Tender Edited Failed' : 'Tender Created Failed');
                    let message = 'Tender Created Failed';
                    this._snackBar.open(message, 'Ok', {
                        duration: 2000,
                        panelClass: ['error-snackbar']
                    });
                }
            }, err => {
                let message = 'Tender Created Failed';
                this._snackBar.open(message, 'Ok', {
                    duration: 2000,
                    panelClass: ['error-snackbar']
                });
            })
    }


    mapMktPlaceWebsites(mktPlaceWebsitesSelected: Array<boolean> | undefined) {
        let websites = [...this.marketPlaceWebsites];
        if (mktPlaceWebsitesSelected !== undefined) {
            for (let i = 0; i < websites.length; i++) {
                websites[i].selected = mktPlaceWebsitesSelected[i];
            }
        }
        return websites;
    }


    mapModeOfNotifications(modeofNotificationsSelected: Array<boolean> | undefined) {
        let modes = [...this.modeOfNotifications];
        if (modeofNotificationsSelected !== undefined) {
            for (let i = 0; i < modes.length; i++) {
                modes[i].selected = modeofNotificationsSelected[i];
            }
        }
        return modes;
    }

    mapOrderTypes(orderTypesSelected: Array<boolean> | undefined) {
        let orders = [...this.orderTypes];
        if (orderTypesSelected !== undefined) {
            for (let i = 0; i < orders.length; i++) {
                orders[i].selected = orderTypesSelected[i];
            }
        }
        return orders;
    }

    // tempClientFormGroup() {
    //     return [
    //         {
    //             "name": "Nitishkumar kamlesh singh",
    //             "source": "MARKETPLACE",
    //             "address1": "A-604 SHEETAL COMPLEX",
    //             "address2": "Mira-Bhayander",
    //             "address3": "Mira Road",
    //             "state": "maharashtra",
    //             "city": "MIRA BHAYANDER ROAD",
    //             "pincode": "401107",
    //             "productCategory": "category1",
    //             "salesValue": "10000",
    //             "bankDetails": [
    //                 {
    //                     "bankName": "SBI",
    //                     "ifscCode": "SBIN000112",
    //                     "accountNo": "01279312963"
    //                 }
    //             ],
    //             "contactDetails": [
    //                 {
    //                     "name": "Nitishkumar kamlesh singh",
    //                     "contactNo": "9768719444",
    //                     "email": "nitishkumarsingh71@gmail.com"
    //                 }
    //             ]
    //         },
    //         {
    //             "brandWebsite": "SHOPIFY",
    //             "mktPlaceWebsites": [
    //                 false,
    //                 false,
    //                 false,
    //                 false,
    //                 false
    //             ],
    //             "warehouseMgmt": "UNI-COMMERCE",
    //             "courierPartner": "PICKRR"
    //         },
    //         {
    //             "modeOfNotification": [
    //                 true,
    //                 true,
    //                 false,
    //                 false,
    //                 false
    //             ],
    //             "orderTypes": [
    //                 true,
    //                 true
    //             ],
    //             "notificationMethod": "ALL-WO-LOGIC",
    //             "firstModeOfNotification": "WHATSAPP",
    //             "eddCalaculationFeature": true,
    //             "noOfReminders": [
    //                 {
    //                     "duration": 0,
    //                     "priority": 0,
    //                     "number": 0
    //                 },
    //                 {
    //                     "duration": 0,
    //                     "priority": 0,
    //                     "number": 0
    //                 },
    //                 {
    //                     "duration": 0,
    //                     "priority": 0,
    //                     "number": 0
    //                 },
    //                 {
    //                     "duration": 0,
    //                     "priority": 0,
    //                     "number": 0
    //                 },
    //                 {
    //                     "duration": 0,
    //                     "priority": 0,
    //                     "number": 0
    //                 }
    //             ],
    //             "notificationModePriority": [
    //                 "SMS",
    //                 "EMAIL",
    //                 "MANUAL-CALLING"
    //             ],
    //             "sequenceNdrShipmentOrders": [
    //                 "SMS",
    //                 "EMAIL",
    //                 "WHATSAPP"
    //             ]
    //         },
    //         {}
    //     ];
    // }
}