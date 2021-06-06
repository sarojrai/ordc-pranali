import { Component, ViewEncapsulation } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'order-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class LoginComponent {

  showPassword: boolean = false;
  loginForm = new FormGroup({
    userName: new FormControl('', [
      Validators.required,
      Validators.email
    ]),
    password: new FormControl('', [
      Validators.required
    ]),
  });
  constructor(private router: Router) { }

  signIn() {
    if(this.loginForm.valid){
      this.router.navigate(['/home']);
    }
  }
}
