import { Component, ViewChild, ViewEncapsulation } from '@angular/core';
import { MatSidenavContainer } from '@angular/material/sidenav';
import { NavItem } from 'src/app/components/home/nav-item';

@Component({
  selector: 'order-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class HomeComponent {

  @ViewChild(MatSidenavContainer) sidenavContainer!: MatSidenavContainer;

  menu: NavItem[] = [
    {
      displayName: 'Dashboard',
      iconName: 'order_dashboard',
      route: '/home/dashboard',
    },
    {
      displayName: 'Track Me',
      iconName: 'order_requisitions',
      route: '/home/track-me',
    },
    {
      displayName: 'Orders',
      iconName: 'order_rfx',
      route: '/home/orders/list',
    },
    {
      displayName: 'Reports',
      iconName: 'order_reports',
      route: '/home/reports'
    },
    {
      displayName: 'Configuration',
      iconName: '',
      divider: true
    },
    {
      displayName: 'Client',
      iconName: 'order_masters',
      expanded: false,
      children: [
        {
          displayName: 'List',
          iconName: 'order_list_tenders',
          route: '/home/client/list'
        },
        {
          displayName: 'Create',
          iconName: 'order_create_tender',
          route: '/home/client/create'
        }
      ]
    },
    {
      displayName: 'Integration',
      iconName: 'order_integration',
      route: '/home/integration'
    },
    {
      displayName: 'Market Place',
      iconName: 'order_masters',
      route: '/home/masters'
    },
    {
      displayName: 'Brand Website',
      iconName: 'order_sidenav_settings',
      route: '/setup'
    },
    {
      displayName: 'SMS Templates',
      iconName: 'order_support',
      route: '/support'
    }
  ];

  onActivate() {
    // this.sidenavContainer.scrollable.scrollTo({ left: 0, top: 0 });
  }
}
