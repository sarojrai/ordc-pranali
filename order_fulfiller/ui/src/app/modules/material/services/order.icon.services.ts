import { Injectable } from '@angular/core'
import { MatIconRegistry } from '@angular/material/icon';
import { DomSanitizer } from '@angular/platform-browser';


@Injectable({
    providedIn: 'root'
})
export class OrderIconServices {
    constructor(
        private matIconRegistry: MatIconRegistry,
        private domSanitizer: DomSanitizer
    ) {
        this.loadIcons()
    }

    loadIcons() {
        // topbar
        this.matIconRegistry.addSvgIcon('order_menu', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/topbar/order-menu.svg`));
        this.matIconRegistry.addSvgIcon('order_notifications', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/topbar/order-notifications.svg`));
        this.matIconRegistry.addSvgIcon('order_arrow_drop_down_circle', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/topbar/order-arrow-drop-down-circle.svg`));

        // sidenav
        this.matIconRegistry.addSvgIcon('order_dashboard', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-dashboard.svg`));
        this.matIconRegistry.addSvgIcon('order_create_tender', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-create-tender.svg`));
        this.matIconRegistry.addSvgIcon('order_integration', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-integration.svg`));
        this.matIconRegistry.addSvgIcon('order_invite_bidders', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-invite-bidders.svg`));
        this.matIconRegistry.addSvgIcon('order_list_tenders', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-list-tenders.svg`));
        this.matIconRegistry.addSvgIcon('order_masters', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-masters.svg`));
        this.matIconRegistry.addSvgIcon('order_reports', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-reports.svg`));
        this.matIconRegistry.addSvgIcon('order_tenders', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-tenders.svg`));
        this.matIconRegistry.addSvgIcon('order_sidenav_truck', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-sidenav-truck.svg`));
        this.matIconRegistry.addSvgIcon('order-auction', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-auction.svg`));
        this.matIconRegistry.addSvgIcon('order_requisitions', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-requisitions.svg`));
        this.matIconRegistry.addSvgIcon('order_support', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-support.svg`));
        this.matIconRegistry.addSvgIcon('order_rfx', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-rfx.svg`));
        this.matIconRegistry.addSvgIcon('order_sidenav_settings', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-sidenav-settings.svg`));
        this.matIconRegistry.addSvgIcon('order_sidenav_chevron_down', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/sidenav/order-sidenav-chevron-down.svg`));

        // login
        this.matIconRegistry.addSvgIcon('icon_feather_eye_off', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/login/icon-feather-eye-off.svg`));
        this.matIconRegistry.addSvgIcon('facebook', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/login/facebook.svg`));
        this.matIconRegistry.addSvgIcon('twitter', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/login/twitter.svg`));
        this.matIconRegistry.addSvgIcon('linkedin', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/login/linkedin.svg`));

        // common
        this.matIconRegistry.addSvgIcon('order_settings', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-settings.svg`));
        this.matIconRegistry.addSvgIcon('order_search', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-search.svg`));
        this.matIconRegistry.addSvgIcon('order_date_picker', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-date-picker.svg`));
        this.matIconRegistry.addSvgIcon('order_time_picker', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-time-picker.svg`));
        this.matIconRegistry.addSvgIcon('order_chevron_next', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-chevron-next.svg`));
        this.matIconRegistry.addSvgIcon('order_reset', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-reset.svg`));
        this.matIconRegistry.addSvgIcon('order_more', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-more.svg`));
        this.matIconRegistry.addSvgIcon('order_arrow_forward', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-arrow-forward.svg`));
        this.matIconRegistry.addSvgIcon('order_chevron_down', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-chevron-down.svg`));
        this.matIconRegistry.addSvgIcon('order_delete', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-delete.svg`));
        this.matIconRegistry.addSvgIcon('order_active_info', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-active-info.svg`));
        this.matIconRegistry.addSvgIcon('order_edit', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-edit.svg`));
        this.matIconRegistry.addSvgIcon('order_cancel', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-cancel.svg`));
        this.matIconRegistry.addSvgIcon('order_add', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-add.svg`));
        this.matIconRegistry.addSvgIcon('order_sub', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-sub.svg`));
        this.matIconRegistry.addSvgIcon('order_reply', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-reply.svg`));
        this.matIconRegistry.addSvgIcon('order_whatsapp', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-whatsapp.svg`));
        this.matIconRegistry.addSvgIcon('order_email', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-email.svg`));
        this.matIconRegistry.addSvgIcon('order_sms', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/common/order-sms.svg`));

        // Client Onboarding
        this.matIconRegistry.addSvgIcon('order_item_details', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-item-details.svg`));
        this.matIconRegistry.addSvgIcon('order_general_info', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-general-info.svg`));
        this.matIconRegistry.addSvgIcon('order_bidding_rules', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-bidding-rules.svg`));
        this.matIconRegistry.addSvgIcon('order_item_details_white', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-item-details-white.svg`));
        this.matIconRegistry.addSvgIcon('order_general_info_white', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-general-info-white.svg`));
        this.matIconRegistry.addSvgIcon('order_bidding_rules_white', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-bidding-rules-white.svg`));
        this.matIconRegistry.addSvgIcon('order_item_details_active', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-item-details-active.svg`));
        this.matIconRegistry.addSvgIcon('order_general_info_active', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-general-info-active.svg`));
        this.matIconRegistry.addSvgIcon('order_bidding_rules_active', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-bidding-rules-active.svg`));
        this.matIconRegistry.addSvgIcon('order_email', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-email.svg`));
        this.matIconRegistry.addSvgIcon('order_phone', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-phone.svg`));
        this.matIconRegistry.addSvgIcon('order_web', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-web.svg`));
        this.matIconRegistry.addSvgIcon('order_rupees', this.domSanitizer.bypassSecurityTrustResourceUrl(`./assets/icons/client-onboarding/order-rupees.svg`));
    }
}