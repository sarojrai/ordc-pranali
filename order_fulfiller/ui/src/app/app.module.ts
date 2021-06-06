import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BreadcrumbComponent } from 'src/app/components/breadcrumb/breadcrumb.component';
import { HomeComponent } from 'src/app/components/home/home.component';
import { FooterComponent } from 'src/app/components/footer/footer.component';
import { TopbarComponent } from 'src/app/components/topbar/topbar.component';
import { OrderMaterialModule } from 'src/app/modules/material/material.module';
import { OrderSharedModule } from 'src/app/modules/shared/shared.module';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    TopbarComponent,
    FooterComponent,
    BreadcrumbComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    OrderMaterialModule,
    OrderSharedModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
