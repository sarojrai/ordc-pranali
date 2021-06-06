import { Component } from '@angular/core';
import { OrderIconServices } from './modules/material/services/order.icon.services';

@Component({
  selector: 'of-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor(private iconService: OrderIconServices) {
    this.iconService.loadIcons();
  }
}
